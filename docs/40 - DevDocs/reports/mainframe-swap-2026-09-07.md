# Mainframe swap — MLX 1.3.0 → 1.11.0, 122B → Qwen3.8-27B-8bit — 2026-09-07

**Scope:** ops incident fix under the 2026-09-07 code-freeze exception. Runtime update,
model swap, F1 activation, E4 correction, throughput/tool-calling/soak verification.
No deletions. No Cobalt `src/` changes. Files changed: `ops/start_mainframe.sh`,
`configs/config.yaml` — nothing else (`git status` verified; the other dirty paths in
the working tree predate this task).

**Inputs:** `mainframe-triage-2026-09-07.md`, `local-seat-test-2026-09-07.md`.

---

## 0 — HEADLINE

The swap is **live and healthy**. The 122B's ~350 s SIGSEGV crash loop is **gone**.

But it is **not a free win**, and two things need your ruling before this is called done:

1. **Decode throughput is 2.5× WORSE** (22.09 vs 55.42 tok/s). Prefill/TTFT is 6–17×
   *better*. This is an architectural trade, not a regression to fix — see §4.
2. **I caused a ~4.5 minute production outage** during the first restart attempt. My
   fault, root-caused and fixed. See §3.

`reasoning_effort` is still **not honoured**, and the fallback the ticket specified
(a no-think system instruction) **also does not work**. See §5.

---

## 1 — Before / after

| | Before | After |
|---|---|---|
| MLX engine | `mlx-llm@1.3.0` | **`mlx-llm@1.11.0`** |
| Model | `qwen3.5-122b-a10b` | **`qwen3.8-27b`** |
| Model path | `mlx-community/Qwen3.5-122B-A10B-4bit` | **`mlx-community/Qwen3.8-27B-8bit`** |
| Arch | `qwen3_5_moe` (MoE, ~10B active) | **`qwen3_5`** (dense) |
| Quant | 4bit | **8bit** |
| Size | 69.62 GB | **29.53 GB** |
| Context served | 32768 | **262144** (the model's declared max) |
| `config.yaml` `context:` | 65536 ✗ (E4 — matched neither) | **262144** ✓ matches served |
| Load time | 39.26 s | **10 s** |
| `reasoning_effort` honoured | no | **no** (§5) |
| Crash cadence | every ~330–352 s | **none observed** (§9) |

**Engine proof** — the live inference worker has the 1.11.0 binding mapped:

```
$ ps -A -o args= | grep mlx-llm
/Users/cobalt/.lmstudio/extensions/backends/
  mlx-llm-mac-arm64-apple-metal-advsimd-1.11.0/liblmstudio_bindings.node
```

`lms runtime ls` — 1.3.0 retained on disk as the rollback target:

```
mlx-llm-mac-arm64-apple-metal-advsimd@1.11.0        ✓            MLX
mlx-llm-mac-arm64-apple-metal-advsimd@1.3.0                      MLX
```

**Model proof** — `/api/v0/models`, and one real chat completion:

```
id: mainframe   publisher: mlx-community   arch: qwen3_5   quantization: 8bit
state: loaded   max_context_length: 262144   loaded_context_length: 262144

$ lms ps
mainframe     qwen3.8-27b    IDLE    29.53 GB    262144    Local

POST /v1/chat/completions {"model":"mainframe", ...}
  -> response model = "mainframe", usage 59+29 tok, content ends "READY"
```

---

## 2 — Deviations from the ticket, and why

### 2a — `lms get` cannot fetch this model at all

Both commands the ticket specified **fail**. `lms get` resolves against LM Studio's own
Hub artifact registry, *not* Hugging Face, and that registry carries only a 4-bit build:

```
$ lms get mlx-community/Qwen3.8-27B-8bit -y
Error: Failed to resolve artifact "mlx-community/qwen3.8-27b-8bit":
       The artifact does not exist or you do not have permission to read it

$ lms get lmstudio-community/Qwen3.8-27B-MLX-8bit -y      # same error
$ lms get qwen3.8-27b -a                                  # only option offered:
   └─ ↓ To download: Qwen3.8 27B 4BIT [MLX] - 16.08 GB
```

All the repos **do** exist upstream (HTTP 200 from the HF API):

| repo | HF | `lms get` |
|---|---|---|
| `mlx-community/Qwen3.8-27B-8bit` | 200 · 29.53 GB · 6 shards | ✗ not in registry |
| `mlx-community/Qwen3.8-27B-MTP-4bit` | 200 · 0.27 GB | ✗ not in registry |
| `lmstudio-community/Qwen3.8-27B-MLX-4bit` | 200 · 16.08 GB | ✓ |

**Ruled by Dejan:** pull the 8-bit from HF into `~/.lmstudio/models/`. Done via
`huggingface_hub.snapshot_download` under `uv`. LM Studio indexes it correctly — it is
the model now in production. On-disk verification (shard sizes match HF byte-for-byte):

```
28G  ~/.lmstudio/models/mlx-community/Qwen3.8-27B-8bit
     model-0000{1..6}-of-00006.safetensors = 5.32/5.35/5.35/5.34/5.29/2.85 GB
     config.json: "quantization": {"bits": 8, "group_size": 64}   <- genuinely 8-bit
253M ~/.lmstudio/models/mlx-community/Qwen3.8-27B-MTP-4bit
```

### 2b — The MTP-4bit is not a "speed candidate model"

The ticket lists it as a model to benchmark later. It is not one. It is 0.27 GB with:

```json
{"block_size": 3, "model_type": "qwen3_5_mtp", "quantization": {"bits": 4}}
```

That is a **multi-token-prediction draft head** for speculative decoding — it pairs with
the 8-bit base, it is not an alternative to it. This matches `CLAUDE.md`'s own phrasing
("Qwen3.8-27B 8-bit MLX **with MTP speculative decoding**"), so the intended end state is
base + head together. **Ruled by Dejan:** download only, do not wire it tonight; measure
decode with vs without as a separate step after the soak passes (§10).

### 2c — Accidental download, disclosed

Probing `qwen3.8-27b@8bit` with `-y` caused `lms` to silently auto-select and download the
**4-bit** build (16.08 GB, now complete at
`~/.lmstudio/models/lmstudio-community/Qwen3.8-27B-MLX-4bit`). `lms get` delegates to the
LM Studio daemon, so killing the CLI did not stop the transfer. **Not deleted** (no-deletions
rule). Disk is not a concern — 670 GB free. It needs a keep-or-remove ruling.

---

## 3 — 🔴 The outage I caused (~4.5 min), and the latent defect it exposed

**21:31:52 → 21:36:22 the mainframe was DOWN.** First restart attempt after the model swap:

```
[mainframe-boot.err]
! Multiple models match the provided model key. Please select one.
❯ qwen3.8-27b (27.50 GiB)
  qwen3.8-27b-mtp (253.36 MiB)
  qwen/qwen3.8-27b (14.98 GiB)
  ↑↓ navigate • ⏎ select
```

`MODEL=` is a **prefix match**, and three models on this box now match `qwen3.8-27b`.
`lms load` drops into an interactive selection menu — and under launchd there is no TTY,
so it **blocked forever**. The model never loaded, the heartbeat never spawned, and
`launchctl list` still showed the job as running. Silent, complete outage.

**Why I did not catch it first:** my pre-flight `--estimate-only` check passed `-y`, so it
printed `"3 models match … Loading the first one"` instead of prompting. The `-y` masked
exactly the failure the real script would hit. That was my error.

**This is a latent defect in the original script, not something the swap introduced** —
the 122B escaped it only because `qwen3.5-122b-a10b` happened to be a unique key. Any
future second model sharing a prefix would have taken production down the same way.

**Fix (two parts):**

1. `-y` added to both `lms load` sites, documented as mandatory rather than cosmetic.
2. Because `-y` resolves to "the first match" with **no documented ordering**, a
   fail-loud post-load verification now confirms the served model really is the 8-bit,
   and aborts rather than quietly serving a 4-bit model — or the 265 MB draft head —
   under the identifier the whole agent routes to.

The discriminator is `arch`+`quantization`, **not** `path`: `/api/v0/models` reports
`path: null` for any model loaded under a custom `--identifier` (measured against the
running 122B), so path is unusable. arch+quant separates all three candidates cleanly.
The check was live-tested against the running 122B before deployment and correctly
rejected it (`qwen3_5_moe`/`4bit`). In production it logged:

```
2026-09-07 21:36:05 | verified: 'mainframe' = qwen3_5/8bit at context 262144
```

**One deliberate asymmetry, flagged for sign-off:** a wrong *model* is fatal (silent and
dangerous), but a clamped *context* logs `WARN` and continues. Aborting on a context
mismatch would leave the mainframe down, which NN#16 ("production is always left
working") ranks as the worse outcome — and an oversized prompt fails loudly at the point
of use anyway. Say the word if you want that fatal too.

---

## 4 — Throughput (seat-test B6 method, identical parameters)

`POST /v1/chat/completions`, `"write 500 words about the ocean"`, `max_tokens=1600`,
`temperature=0.7`, 3 non-streamed runs + 1 streamed for TTFT; repeated with 16000 chars
of `PROJECT-LEDGER.md` prepended. Every run hit the 1600-token cap, same as the 122B.

| Metric | 122B 4-bit MoE | **27B 8-bit dense** | Δ |
|---|---|---|---|
| E2E tok/s — min (short) | 47.27 | 22.24 | |
| **E2E tok/s — avg (short)** | **47.45** | **22.25** | **2.1× slower** |
| E2E tok/s — max (short) | 47.59 | 22.27 | |
| **Decode tok/s (short)** | **55.42** | **22.09** | **2.5× slower** |
| E2E tok/s — avg (~4K) | 38.56 | 20.72 | 1.9× slower |
| Decode tok/s (~4K) | 53.63 | 21.44 | 2.5× slower |
| **TTFT (short)** | **4.764 s** | **0.821 s** | **5.8× faster** |
| **TTFT (~4K)** | **11.569 s** | **1.220 s** | **9.5× faster** |
| **Incremental prefill** | **606 tok/s** | **10,419 tok/s** | **17× faster** |
| Decode degradation → 4K | −3% | −2.9% | same |
| Wall clock (short, 1599 tok) | 33.6–33.8 s | 71.8–71.9 s | 2.1× slower |

**Mechanism — this is expected, not a misconfiguration.** The 122B is MoE with ~10B
*active* params at 4-bit (~5 GB read per decoded token). The 27B is **dense at 8-bit**
(~27 GB per token) — roughly 5× the memory traffic, and decode is bandwidth-bound.
Prefill carries no MoE routing overhead, hence the large TTFT win. The 8-bit quant is
half the trade: a 4-bit 27B would decode roughly twice as fast at lower quality.

**Practical read:** the 27B is markedly better for short-answer, large-context, and
tool-calling work (near-instant first token, 17× prefill, 8× the context window) and
materially worse for long prose generation. Anything that generates thousands of tokens
now costs ~2× the wall clock. Speculative decoding was the obvious lever to recover this — **it turns out to be
unavailable on this stack** (§10).

---

## 5 — `reasoning_effort`: not honoured, and the fallback fails too

Five variants of `"What is 2+2? Reply with just the number."`, `temperature=0`:

| Request | completion_tokens | sha256 of content |
|---|---|---|
| default (no flag) | 37 | `9e89e16f30837bac` |
| `reasoning_effort: "low"` | 37 | `9e89e16f30837bac` |
| `reasoning_effort: "medium"` | 37 | `9e89e16f30837bac` |
| `reasoning_effort: "high"` | 37 | `9e89e16f30837bac` |
| `chat_template_kwargs.enable_thinking: false` | 37 | `9e89e16f30837bac` |

**Byte-identical across all five** — the parameter is silently ignored, exactly as the
seat test found on the 122B. The runtime update to 1.11.0 did not change this.

Per the ticket I then tested the specified fallback — a no-think system instruction in
the load config. **It also does not work:**

| System prompt | completion_tokens | `<think>` block emitted? |
|---|---|---|
| *(none)* | 37 | yes |
| `/no_think` | 33 | **yes** |
| "Do not think step by step. Do not emit `<think>` blocks…" | 29 | **yes** |
| "Answer with the final answer only. No reasoning, no `<think>` tags." | 29 | **yes** |

Thinking is **unconditionally on** for this model on this server. There is no
`reasoning_effort` control and no way to disable thinking, so `MODEL=`/load-config cannot
carry one — nothing was added to `start_mainframe.sh` for it, because nothing works.

**Consumer note:** reasoning is emitted inline in `message.content`, and on this model it
is **consistently wrapped in literal `<think>…</think>` tags** (the 122B sometimes used a
bare `Thinking Process:` preamble instead). There is no separate `reasoning` field.
Stripping `<think>.*?</think>` is reliable here in a way it was not on the 122B. Every
reasoning token is still billed against `max_tokens`.

**`reasoningParsing` does not rescue this either — tested, negative.** LM Studio's prediction
config exposes a `reasoningParsing` option that looked like it might split reasoning into its
own field. It does not, for this model:

```
default                    -> content len 123, ends '</think>\n\n4'
reasoningParsing enabled   -> content len 123, ends '</think>\n\n4'   (identical)
result object: no .reasoning attribute; stats carry no reasoning token counts
/v1/chat/completions message keys: ['role','content','tool_calls']  -- no 'reasoning'
```

⚠️ **Stripping gotcha, measured.** Which strip regex is safe depends on the client:

| Access path | opening `<think>` | closing `</think>` |
|---|---|---|
| `POST /v1/chat/completions` (raw) | **present** | present |
| `lmstudio` Python SDK `.content` | **absent — stripped by the SDK** | present |

So `re.sub(r'<think>.*?</think>', '', text, flags=re.S)` works against the HTTP endpoint but
silently fails via the SDK, where the text begins mid-reasoning with no opening tag and a
stray `</think>` survives. Anything consuming this model should strip on the closing tag, or
split on it and keep the tail.

---

## 6 — Tool-calling (seat-test A7 task, 10 headless runs)

`qwen --openai-logging -p "list the files in this directory using your tool, then reply
DONE"` in a directory containing `alpha.txt`, `beta.txt`, `gamma.txt`. Scored from the
`--openai-logging` traces, not from prose. `~/.qwen/settings.json` left untouched at
`contextWindowSize: 32768` so conditions match the 122B baseline exactly.

| Score | 122B baseline | **27B 8-bit** |
|---|---|---|
| Correct listing tool call issued | 9/9 reached | **14/14 calls, all `glob`** |
| Malformed-schema failures | 0/9 | **0/14** |
| Hallucinated file lists | 0/9 | **0/10 runs** |
| Replied `DONE` | 9/9 | **10/10** |
| Exit code 0 | — | **10/10** |
| **Runs lost to server crash** | **3/12 (25%)** | **0/10 (0%)** |
| **Raw run-level completion** | **9/12 (75%)** | **10/10 (100%)** |

Every tool call was `glob` with schema-valid arguments
(`{"pattern":"**/*","path":"/private/tmp/qwen-tooltest"}`), 0 trace-level API errors.

**Scoring note, stated plainly.** 8 of 10 runs listed all three files in the final prose;
runs 2 and 3 issued the `glob` call correctly and then replied only `DONE`, their
reasoning showing they considered the listing already delivered ("I listed them out, so
now I should just say DONE"). Under the seat test's own criterion — *was a correct
listing tool call issued* — that is 10/10 with 0 malformed and 0 hallucinated. Under a
stricter "did the final message repeat the list" reading it is 8/10. Neither is a
tool-calling failure; both numbers are given so the bar is yours to set.

The headline change is the crash column: the 122B lost a quarter of its runs to the
server dying mid-task. The 27B lost none.

---

## 7 — F1 active: proof

F1 (the heartbeat probe fix from the triage) was written to the file on 2026-09-07 but had
**never executed** — `com.cobalt.mainframe` had been running the old in-memory loop since
2026-09-04 14:58. This restart is what activated it. Proof taken from the *running
process*, not the file:

```
$ ps -p 2119 -o args=          # the live heartbeat, pid from mainframe-heartbeat.pid
  ...--max-time 10  ...   <- LIVENESS probe   (GET /v1/models)     F1 active
  ...--max-time 120 ...   <- READINESS probe  (chat completion)    F1 active
  occurrences of the old "max-time 30": 0
  CONTEXT_LENGTH="262144"                                          correctly injected
```

Log confirming the new two-stage loop is the one running, with no false DOWN:

```
2026-09-07 21:36:05 | verified: 'mainframe' = qwen3_5/8bit at context 262144
2026-09-07 21:36:05 | model loaded — spawning heartbeat (60s ping, logged, self-healing)
2026-09-07 21:36:05 | heartbeat running as pid 2119 (pidfile .../mainframe-heartbeat.pid)
2026-09-07 21:36:06 | heartbeat OK
2026-09-07 21:37:06 | heartbeat OK
...
```

**Zero `heartbeat FAILED`, zero `liveness FAILED`, zero reloads** since load — including
through the 10 concurrent Qwen Code tool-calling runs, which is precisely the concurrent-load
condition that produced the 10 false-DOWN `no response` events on the old 30 s timeout.
F1's raised 120 s timeout is doing its job.

### Bug found and fixed while activating F1

Making `--context-length` a variable exposed that the heartbeat's reload path runs in a
**separate single-quoted `bash -c` block** which does not inherit the parent's variables —
they are explicitly re-injected. An un-injected `$CONTEXT_LENGTH` would have expanded to
empty there, so every self-heal reload would have failed on a bare `--context-length`.
Caught before deployment; `CONTEXT_LENGTH` and `MODEL_PATH` are now injected alongside
the existing `MODEL`/`MODEL_ID`/`API` lines, and the live process confirms
`CONTEXT_LENGTH="262144"`.

### Benign log message worth knowing about

The restart logged `heartbeat pid 67820 is not one of ours — left alone`. That is correct
behaviour, not a leak: `launchctl kickstart -k` had already reaped the old process tree, so
`ps -p 67820` returned nothing and the marker check could not match. Verified afterwards —
`pgrep -f COBALT_MAINFRAME_HEARTBEAT` shows only the new heartbeat's own tree, no orphans.
The message reads like a failure though, and would be clearer as
"heartbeat pid N is gone or not ours".

---

## 8 — E4 fix

Server reality after the swap is `loaded_context_length: 262144`. The config was 65536 —
matching neither the old served value (32768) nor the new one.

```diff
--- a/configs/config.yaml
+++ b/configs/config.yaml
@@ -45,7 +45,7 @@ models:
      provider: "openai"
      model_name: "mainframe"
      node_ref: "cortex"
-    context: 65536
+    context: 262144
      env_key_ref: "lmstudio"
```

`configs/config.yaml` `mainframe.context` now equals the value the server actually serves,
verified against `/api/v0/models`. The script additionally logs a `WARN` if the two ever
drift apart again, so E4 cannot silently recur.

**Related staleness NOT fixed** (outside this ticket's file scope, flagged only):
`~/.qwen/settings.json` still declares `contextWindowSize: 32768`. It was left untouched
deliberately so the tool-calling test ran under conditions identical to the 122B baseline.
It now understates the real window by 8×.

---

## 9 — Soak: **PASS**

30 minutes, real inference every 60 s (`"Name three colours. One line."`), watching
`~/Library/Logs/DiagnosticReports` for new `.ips` crash reports throughout.

| | Result |
|---|---|
| Probes | **29** |
| Failures | **0** |
| New macOS crash reports (`.ips`) | **0** |
| Probe latency | min 1.86s · avg 2.52s · max 3.49s |
| Window covered | t+1141 s → **t+2891 s** since load |

Independently corroborated from the production heartbeat log and the OS, over **50 minutes**
since load:

```
heartbeat OK    : 47        heartbeat FAILED : 0
liveness FAILED : 0         reloads          : 0
new node-*.ips  : 0
llmster worker uptime: 50:28  (continuous, single process)
```

**Pass = 0 crashes. Achieved.** For scale: the 122B segfaulted every ~330–352 s, so this
window spans **~8.5 consecutive crash cycles** that simply did not happen. Its worker
process never survived 6 minutes; this one has run 50 without a reload. The `t+340 s`
recurrence the ticket told me to escalate on **did not occur** — no SIGSEGV, on 1.11.0,
with the new model.

**What this does and does not prove.** The runtime and the model changed together, so this
run alone cannot attribute the fix to one or the other. Step 10 (122B on 1.11.0) is the
experiment that separates them — see §11.

---

## 10 — MTP speculative decoding: **NOT POSSIBLE on this stack**

You asked for decode tok/s with vs without the MTP draft head once the soak passed. The
"with" half **cannot be run**. LM Studio 1.11.0 refuses it outright:

```
lmstudio.LMStudioServerError: Chat response error:
  Failed to load draft model.
  SpeculativeDecodingNotSupportedError:
    Speculative decoding is not supported for batched MLX models.
```

| Configuration | Decode tok/s (3 runs, 800 tok each) |
|---|---|
| **Without draft model** | 22.16 · 22.20 · 22.11 → **avg 22.16** |
| **With MTP draft head** | **refused by the server — no measurement possible** |

The baseline half corroborates §4 independently (22.16 vs the 22.09 measured there).

**Method note:** run against the already-loaded production `mainframe` instance using
LM Studio's *prediction-time* `draftModel` config. Speculative decoding is not a load-time
option in this build — `lms load` has no draft flag and `LlmLoadModelConfig` has no draft
field — so no reload and no second copy of the 29.5 GB base was needed. Production
identifier untouched.

**Consequence — this is the important part.** The §4 decode regression (2.5× slower than the
122B) has **no speculative-decoding remedy available today**. And `CLAUDE.md`'s description
of the local model as *"Qwen3.8-27B 8-bit MLX **with MTP speculative decoding**"* describes a
configuration LM Studio will not currently serve. The 253 MB draft head is on disk and
correctly indexed (`qwen3.8-27b-mtp`); it simply cannot be attached.

**Untested hypothesis, deliberately not attempted tonight.** The error says *batched* MLX
models. LM Studio batches MLX for parallel slots, so loading with `--parallel 1` might drop
the model out of the batched path and permit speculative decoding. I did not test it,
because the only safe way was a second 29.5 GB instance and this box has **103 GB total with
~46 GB usable** — that would have pushed a healthy production system into memory pressure at
22:30. The test to run in a maintenance window:

```
lms load qwen3.8-27b -y --identifier spec-test --gpu max --context-length 32768 --parallel 1
# then a prediction with draftModel="qwen3.8-27b-mtp" against 'spec-test'
```

---

## 11 — Step 10 (122B on 1.11.0): NOT RUN — needs your call

The soak passed, so step 10 was unlocked, and it is the only experiment that separates the
two variables changed tonight: **did the runtime update fix the SIGSEGV, or did swapping the
model?** Right now that is genuinely unknown.

I did not run it unattended. It requires unloading the healthy 27B, loading the known-crashing
122B (69.62 GB), soaking 10 minutes, then restoring — and if the restore fails at ~23:00 with
nobody watching, Cobalt's router points **every** profile (`default`/`coder`/`architect`/
`strategist`/`fast_chat`) at `mainframe` and the agent is down until morning. Tonight already
produced one self-inflicted outage from a restart (§3); a second one unsupervised is a poor
trade for a diagnostic. The trading-day window is not near (market opens 09:30, ~11 h away),
so this is a risk judgement, not a timing one — your call, not mine to make silently.

---

## 12 — ESCALATE

1. **122B deletion after 24 h clean — ON TRACK, not yet due.** As of this report the 27B has
   run **50 minutes** crash-free (0/47 heartbeat failures, 0 `.ips`, single 50-minute worker
   process). The triage's ordering has now been satisfied through "verify": replacement
   picked → `MODEL=` changed → LaunchAgent restarted → `lms ps` + a real completion verified.
   **The remaining gate is the 24 h clean window**, which expires **2026-09-08 ~21:36**.
   Recommend re-checking the counters then and deleting only if still zero. The 122B
   (69.62 GB) is untouched and remains a working rollback target until then.

2. **`CLAUDE.md` local-model line is wrong on three counts** — correcting here, not in place,
   as instructed. Current text: *"Qwen3.8-27B 8-bit MLX with MTP speculative decoding,
   parallel slots, per-call reasoning_effort (default xhigh overthinks — use low/off for
   simple calls)."*
   - "Qwen3.8-27B 8-bit MLX" — **now true as of tonight** (it was false when the seat test
     flagged it as E3; nothing of that name was on the box).
   - "with MTP speculative decoding" — **false and not currently achievable** (§10).
   - "per-call reasoning_effort … use low/off" — **false**; no such control exists on this
     server, and thinking cannot be disabled by any means tested (§5).

3. **MTP-4bit benchmark as a follow-up** — reframed. It is not a rival model to benchmark
   (§2b); it is a draft head that the runtime refuses to attach. The real follow-up is the
   `--parallel 1` experiment in §10. If that also fails, the MTP head has no use on this
   stack and CLAUDE.md should drop the claim entirely.

4. **Decode regression — needs a product decision.** 2.5× slower decode is a real cost to
   anything generating long output (journaling, research summaries, coaching prose), bought
   in exchange for 6–17× faster prefill, 8× context, and an end to the crash loop. If long-form
   decode matters more than stability for some workload, the 4-bit 27B already on disk
   (§2c, 16.08 GB) would roughly double decode speed at lower quality — a one-line `MODEL=`
   change plus updating `EXPECT_QUANT` to `4bit`.

5. **Accidental 4-bit download needs a keep/remove ruling** (§2c). 16.08 GB, not deleted.

6. **F1's fatal/non-fatal asymmetry needs sign-off** (§3): wrong model aborts, clamped
   context warns and continues. Deliberate, reasoned from NN#16, but it is a judgement call
   I made rather than one the ticket specified.

7. **`~/.qwen/settings.json` `contextWindowSize: 32768`** is now 8× understated (§8). Left
   untouched to keep the tool-calling test comparable to the 122B baseline.

8. **Two pre-existing ops-hygiene defects observed, not fixed** (out of scope):
   `ops/logs/mainframe.log` is **9 MB** and full of raw TTY spinner escape codes, because the
   heartbeat's `lms load` writes its progress bar into the log; and the restart message
   `heartbeat pid N is not one of ours — left alone` is misleading when the pid is simply
   already gone (§7).

---

## 13 — Rollback (printed, NOT executed)

Snapshot: `/tmp/mainframe-pre-20260907-203659/` (script, plist, config.yaml,
`runtime-ls-before.txt`, plus `ROLLBACK.sh`).

```bash
# 1. ops script. NOTE: the snapshot ALREADY CONTAINS the F1 heartbeat fix (it was in the
#    working tree before this task). Restoring keeps F1 and reverts only the model swap.
#    To also drop F1: git checkout ops/start_mainframe.sh
cp /tmp/mainframe-pre-20260907-203659/start_mainframe.sh /Users/cobalt/cobalt/ops/start_mainframe.sh

# 2. Cobalt config (undoes the E4 fix)
cp /tmp/mainframe-pre-20260907-203659/config.yaml /Users/cobalt/cobalt/configs/config.yaml

# 3. LaunchAgent plist (unchanged tonight; included for completeness)
cp /tmp/mainframe-pre-20260907-203659/com.cobalt.mainframe.plist \
   /Users/cobalt/Library/LaunchAgents/com.cobalt.mainframe.plist

# 4. Previous MLX runtime (1.3.0 is still installed)
/Users/cobalt/.lmstudio/bin/lms runtime select mlx-llm-mac-arm64-apple-metal-advsimd@1.3.0

# 5. Restart (reloads the 122B per the restored MODEL=)
launchctl kickstart -k gui/$(id -u)/com.cobalt.mainframe

# 6. Verify
sleep 90
curl -s http://localhost:1234/api/v0/models | python3 -m json.tool
/Users/cobalt/.lmstudio/bin/lms ps
```

⚠️ **One caveat on rollback:** the restored script has **no `-y` on `lms load`**. With three
`qwen3.8-27b*` models now on disk that is safe *only* because the restored `MODEL=` is
`qwen3.5-122b-a10b`, which is still a unique key. Do not hand-edit `MODEL=` in a
rolled-back script without re-adding `-y` (§3).

---

## 14 — git diff (`ops/` and `configs/config.yaml` only)

```diff
diff --git a/configs/config.yaml b/configs/config.yaml
index ac501fe..0f2fcea 100644
--- a/configs/config.yaml
+++ b/configs/config.yaml
@@ -45,7 +45,7 @@ models:
     provider: "openai"
     model_name: "mainframe"
     node_ref: "cortex"
-    context: 65536
+    context: 262144
     env_key_ref: "lmstudio"
 
   # --- CLOUD BLEEDING EDGE ---
diff --git a/ops/start_mainframe.sh b/ops/start_mainframe.sh
index d82d0e3..b45f0a6 100755
--- a/ops/start_mainframe.sh
+++ b/ops/start_mainframe.sh
@@ -45,10 +45,31 @@ OPS_DIR="/Users/cobalt/cobalt/ops"
 LOG_DIR="$OPS_DIR/logs"
 LOG_FILE="$LOG_DIR/mainframe.log"
 PID_FILE="$LOG_DIR/mainframe-heartbeat.pid"
-MODEL="qwen3.5-122b-a10b"
+# MODEL SWAP 2026-09-07 (was: qwen3.5-122b-a10b, 4-bit MoE, 69.6 GB).
+# The 122B segfaulted in LM Studio's node/llmster MLX worker every
+# ~330-352 s regardless of load — 820 crash-detections over four days,
+# forensics in docs/40 - DevDocs/reports/mainframe-triage-2026-09-07.md.
+#
+# WARNING — MODEL is a PREFIX match, and three models on this box match
+# "qwen3.8-27b": the 8-bit we want, the "-mtp" draft head, and a 4-bit
+# build. `lms load` picks "the first one" with no documented ordering,
+# so the key alone cannot guarantee which model gets served. MODEL_PATH
+# is therefore verified against the served model after load, and the
+# script aborts loudly on a mismatch rather than quietly serving a
+# 4-bit model to a production trading agent.
+MODEL="qwen3.8-27b"
+MODEL_PATH="mlx-community/Qwen3.8-27B-8bit"
 MODEL_ID="mainframe"
 API="http://localhost:1234"
 
+# Served context. The 122B ran 32768 as a VRAM-budget compromise; the
+# 27B is far cheaper, so it serves the model's full declared maximum.
+# Only 16 of its 64 layers use full attention (the other 48 are linear,
+# constant-state), so the KV cache at 262144 is ~17.2 GB — about 47 GB
+# all-in against the 122B's 69.6 GB. configs/config.yaml's
+# mainframe.context MUST match this value (E4).
+CONTEXT_LENGTH=262144
+
 mkdir -p "$LOG_DIR"
 
 log() { echo "$(date '+%Y-%m-%d %H:%M:%S') | $*" >> "$LOG_FILE"; }
@@ -136,8 +157,68 @@ while ! curl -s "$API/v1/models" > /dev/null; do
     ELAPSED=$((ELAPSED + 2))
 done
 
+# -y is MANDATORY here, not a convenience. Without it `lms load` drops
+# into an interactive "Multiple models match — please select one" menu
+# whenever MODEL is a prefix of more than one model key. Under launchd
+# there is no TTY, so it blocks forever: the model never loads, the
+# heartbeat never spawns, and the mainframe is silently DOWN with the
+# job still showing as running. Reproduced in production 2026-09-07
+# 21:31 during this very swap. The 122B never hit it only because its
+# key happened to be unique. `-y` selects the first match, which is why
+# the arch/quant verification below is not optional.
 log "API online — loading model into VRAM"
-lms load "$MODEL" --identifier "$MODEL_ID" --gpu max --context-length 32768
+lms load "$MODEL" -y --identifier "$MODEL_ID" --gpu max --context-length "$CONTEXT_LENGTH"
+
+# --- verify we loaded the model we meant to ---------------------------
+#
+# MODEL is a prefix match against three "qwen3.8-27b*" models on this
+# box (see the MODEL block above). A wrong pick would serve a 4-bit
+# model, or the 265 MB MTP draft head, under the identifier the whole
+# agent routes to — silently, and with plausible-looking output. That
+# is precisely the "plausible-empty artifact" the fail-loud law
+# forbids, so a mismatch is fatal here rather than a warning.
+#
+# Discriminator is arch+quantization, NOT path: /api/v0/models reports
+# path=null for any model loaded under a custom --identifier (measured
+# 2026-09-07 against the running 122B), so path is unusable here.
+# arch+quant separates all three candidates cleanly:
+#     qwen3_5     + 8bit  -> the model we want
+#     qwen3_5     + 4bit  -> the 4-bit build
+#     qwen3_5_mtp + 4bit  -> the MTP draft head
+EXPECT_ARCH="qwen3_5"
+EXPECT_QUANT="8bit"
+
+read -r got_arch got_quant got_ctx <<EOF
+$(curl -s "$API/api/v0/models" | python3 -c "
+import json,sys
+mid=sys.argv[1]
+try:
+    for m in json.load(sys.stdin).get('data',[]):
+        if m.get('id')==mid:
+            print(m.get('arch',''), m.get('quantization',''), m.get('loaded_context_length',''))
+            break
+except Exception:
+    pass
+" "$MODEL_ID" 2>/dev/null)
+EOF
+
+if [ "$got_arch" != "$EXPECT_ARCH" ] || [ "$got_quant" != "$EXPECT_QUANT" ]; then
+    log "FATAL: '$MODEL_ID' should be $EXPECT_ARCH/$EXPECT_QUANT but is '${got_arch:-<none>}'/'${got_quant:-<none>}'"
+    log "FATAL: refusing to spawn the heartbeat against the wrong model. Aborting."
+    exit 1
+fi
+# Context mismatch is LOUD BUT NOT FATAL, deliberately. A wrong *model*
+# is silent and dangerous, so it aborts above. A clamped *context* still
+# serves correct answers, and an over-large prompt fails loudly at the
+# point of use anyway — whereas aborting here would leave the mainframe
+# down, which NN#16 ("production is always left working") ranks as the
+# worse outcome on a trading day. It is logged at WARN so E4 drift is
+# visible in the log rather than hidden.
+if [ "$got_ctx" != "$CONTEXT_LENGTH" ]; then
+    log "WARN: requested context $CONTEXT_LENGTH but server serves '${got_ctx:-<none>}'"
+    log "WARN: configs/config.yaml mainframe.context should read '${got_ctx:-?}', not $CONTEXT_LENGTH"
+fi
+log "verified: '$MODEL_ID' = $got_arch/$got_quant at context $got_ctx"
 
 log "model loaded — spawning heartbeat (60s ping, logged, self-healing)"
 caffeinate -i -m bash -c '
@@ -146,10 +227,49 @@ caffeinate -i -m bash -c '
   API="'"$API"'"
   MODEL_ID="'"$MODEL_ID"'"
   MODEL="'"$MODEL"'"
+  MODEL_PATH="'"$MODEL_PATH"'"
+  # Injected, not inherited: this block runs in a separate `bash -c`
+  # under single quotes, so an un-injected $CONTEXT_LENGTH would expand
+  # to empty here and every self-heal reload would fail on a bare
+  # `--context-length`.
+  CONTEXT_LENGTH="'"$CONTEXT_LENGTH"'"
   export PATH="'"$PATH"'"
   hb() { echo "$(date "+%Y-%m-%d %H:%M:%S") | $*" >> "$LOG_FILE"; }
+  reload() {
+    hb "heartbeat: attempting reload of $MODEL"
+    if lms load "$MODEL" -y --identifier "$MODEL_ID" --gpu max --context-length "$CONTEXT_LENGTH" \
+         >> "$LOG_FILE" 2>&1; then
+      hb "heartbeat: reload OK"
+    else
+      hb "heartbeat: reload FAILED — mainframe is DOWN"
+    fi
+  }
   while true; do
-    reply=$(curl -s --max-time 30 "$API/v1/chat/completions" \
+    # LIVENESS: cheap GET /v1/models — proves the LM Studio HTTP daemon
+    # itself is up. Fast (~15ms measured) and unaffected by generation
+    # length, so unlike the old single generation-based probe it cannot
+    # itself time out under load.
+    if ! curl -s -o /dev/null --max-time 10 "$API/v1/models"; then
+      hb "liveness FAILED: LM Studio HTTP server not responding"
+      reload
+      sleep 60
+      continue
+    fi
+    # READINESS: mainframe-triage-2026-09-07 proved GET /v1/models and
+    # the per-model "state" field on /api/v0/models both read "loaded"
+    # straight through a live crash (state only flips once WE issue a
+    # reload), so an inference call is the only probe that actually
+    # exercises the crashed worker. It stays the reload trigger for that
+    # reason (this intentionally differs from a textbook liveness and
+    # readiness split, where readiness never restarts anything).
+    # --max-time raised 30s -> 120s: measured generations run 33-41s, and
+    # a queued heartbeat ping waits behind the in-flight generation ahead
+    # of it, not just its own reply time — 30s was shorter than that
+    # queue wait and produced false "no response" DOWNs against a
+    # healthy, busy model (confirmed 2026-09-07: reproduced live, ping
+    # timed out at 30s during a 34s generation, succeeded at 120s against
+    # the same one).
+    reply=$(curl -s --max-time 120 "$API/v1/chat/completions" \
       -H "Content-Type: application/json" \
       -d "{\"model\":\"$MODEL_ID\",\"messages\":[{\"role\":\"user\",\"content\":\"ping\"}],\"max_tokens\":1}")
     if [ -n "$reply" ] && ! printf "%s" "$reply" | grep -q "\"error\""; then
@@ -162,13 +282,7 @@ caffeinate -i -m bash -c '
       # boot log) and the old ping-only heartbeat would have logged
       # FAILED every 60s forever while the mainframe stayed down. The
       # pre-RULING-6 script had the same flaw and no log to show it.
-      hb "heartbeat: attempting reload of $MODEL"
-      if lms load "$MODEL" --identifier "$MODEL_ID" --gpu max --context-length 32768 \
-           >> "$LOG_FILE" 2>&1; then
-        hb "heartbeat: reload OK"
-      else
-        hb "heartbeat: reload FAILED — mainframe is DOWN"
-      fi
+      reload
     fi
     sleep 60
   done
```

`git status --porcelain` confirms no other file was touched by this task — the remaining
dirty paths (`configs/cobalt/rules.yaml`, the `docs/` entries) predate it.
