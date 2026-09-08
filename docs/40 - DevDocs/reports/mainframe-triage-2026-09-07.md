# Mainframe triage — crash loop (E1) + heartbeat false-DOWN (E3) — 2026-09-07

**Scope:** read-only diagnosis of the 122B crash loop and the heartbeat probe defect
surfaced by `local-seat-test-2026-09-07.md` (E1, E3, E4), plus the two bounded fixes
(F1, F2) authorized under the 2026-09-07 ops-incident code-freeze exception. No model
unloaded, reloaded, or deleted. No Cobalt `src/` or `configs/` touched. The only file
changed is `ops/start_mainframe.sh`'s heartbeat loop (F1) — `MODEL=` untouched.

---

## 1 — Aligned timeline (first 20 events, last 24h)

Sources: `ops/logs/mainframe.log` (heartbeat FAILED / reload lines), macOS crash
reporter (`~/Library/Logs/DiagnosticReports/node-*.ips`, the actual SIGSEGV proof —
see §2), `launchctl list` (job restarts). Window: 2026-09-06 20:05 → 2026-09-07 20:05.

```
2026-09-06 20:05:14 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:05:38 | heartbeat: reload OK
2026-09-06 20:11:03 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:11:27 | heartbeat: reload OK
2026-09-06 20:16:51 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:17:16 | heartbeat: reload OK
2026-09-06 20:22:40 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:23:05 | heartbeat: reload OK
2026-09-06 20:28:29 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:28:54 | heartbeat: reload OK
2026-09-06 20:34:19 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:34:43 | heartbeat: reload OK
2026-09-06 20:40:08 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:40:32 | heartbeat: reload OK
2026-09-06 20:45:56 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:46:21 | heartbeat: reload OK
2026-09-06 20:51:45 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:52:10 | heartbeat: reload OK
2026-09-06 20:57:34 | heartbeat FAILED: {"error":"The model has crashed..."}
2026-09-06 20:57:59 | heartbeat: reload OK
```
(532 aligned events total in the 24h window; pattern repeats identically — crash,
reload ~24-25s later, ~349-352s of healthy runtime, crash again.)

**No `start_mainframe.sh` invocation occurred anywhere in this 24h window.** The job's
last (re)start was `2026-09-04 14:58:17` (pid 67727), confirmed still running today
(`launchctl list`: `67727  -15  com.cobalt.mainframe`). Every crash/reload cycle above
happened *inside that one long-lived heartbeat loop* — no launchd restart, no boot-log
entry, nothing external kicked it.

**Does every crash follow a reload, or precede it?** Every crash **precedes**
detection and reload. The heartbeat is purely reactive: the model dies silently
(§2 — SIGSEGV in the inference worker), and the *next* 60s-cadence ping is simply the
first thing to notice, logging `heartbeat FAILED` before the script's own `reload()`
call fires ~0-25s later. Nothing in the reload path causes the *next* crash on a short
delay tied to the reload itself — the ~350s gap holds steady in both directions
(idle periods and busy periods, per the original seat-test) and does not shift when a
reload happens to land early or late in that window.

**Cumulative totals (2026-09-04 14:45 → 2026-09-07 20:04, as of this triage):**

| | |
|---|---|
| Total crash detections (`heartbeat FAILED`) | **820** |
| `reload OK` | 796 |
| `reload FAILED` | 10 |
| Per-day | 09-04: 106 · 09-05: 247 · 09-06: 248 · 09-07: 219 (partial day) |
| Interval (all days) | min 60s / median 349s / max 353s |

---

## 2 — H1–H4 verdicts

### H1 — heartbeat `--max-time 30` shorter than generation time → false DOWN → the reload IS the "crash" — **CONFIRMED, narrow scope**

Breaking down all 820 `heartbeat FAILED` lines by cause:

| Cause | Count |
|---|---|
| `{"error":"The model has crashed..."}` (genuine crash, instant response) | 790 |
| `no response` (curl timed out — this is H1) | **10** |
| Other transient JSON errors (no-model-loaded during a reload race, etc.) | 20 |

All 10 `no response` events are timestamped **2026-09-07 17:07:52 → 18:10:53** — the
exact window of the seat-test's Qwen Code throughput runs (long, concurrent
generations). **Reproduced live during this triage:** fired a real ~34s background
generation, then raced the old-style ping against it —

```
OLD ping (max-time 30), during a live 34s generation: timed out after 30s, empty reply
  → would log "heartbeat FAILED: no response" against a healthy, busy model
NEW ping (max-time 120), fired right after, same generation: real 200 response
  after 7s (queue cleared at 33.9s total) — no false DOWN
```

**Verdict: CONFIRMED as a real, distinct defect, but it accounts for only 10 of 820
crash-detections (1.2%) and only fires under concurrent load.** It does not explain
the dominant pattern — a quiet-system check just now (19:35–20:05, zero concurrent
traffic) still logged 6 crashes, all the instant "model has crashed" JSON kind, zero
timeouts.

### H2 — LM Studio idle-TTL / JIT auto-unload (~5-6 min) — **RULED OUT**

`~/.lmstudio/settings.json`:
```json
"jitModelTTL": { "enabled": true, "ttlSeconds": 3600 }
```
3600s = 1 hour, not 5-6 minutes — off by ~10x from the observed 349s cadence. It also
applies to models loaded via JIT auto-load; `mainframe` is loaded explicitly by
`ops/start_mainframe.sh`'s `lms load … --identifier mainframe`, not JIT. And the
failure signature is wrong for a timer-based unload: every event logs `"The model has
crashed without additional information"` (an *error*), never a graceful "unloaded —
idle" message.

### H3 — memory pressure (69.6 GB resident + 88 GB wired limit) — **RULED OUT**

```
$ log show --last 24h --predicate 'eventMessage contains "jetsam"'
→ 0 events
```
Zero jetsam kills in the 24h window that contains 216 of the 820 crashes. `vm_stat`
right now shows no pressure signature (large free/inactive pool, ~4 GB wired). More
directly: the macOS crash reporter caught the failure mode outright (see below) and it
is **`EXC_BAD_ACCESS` / `SIGSEGV`**, not the `SIGKILL` a jetsam-triggered kill would
produce.

### H4 — another launchd job on a ~350s cadence — **RULED OUT**

Full scan of every `StartInterval` in `~/Library/LaunchAgents/*.plist`:

```
com.cobalt.heartbeat.plist        StartInterval=900
com.google.GoogleUpdater.wake.plist  StartInterval=3600
```

Nothing else carries a `StartInterval` at all — no 350s-cadence job exists anywhere in
the user LaunchAgents that could be touching the model.

### The actual mechanism (new finding — not H1-H4 as posed)

macOS's own crash reporter caught it. 47 `.ips` reports across the 4 days, e.g.
`~/Library/Logs/DiagnosticReports/node-2026-09-07-154644.ips`:

```json
"procName": "node", "parentProc": "llmster", "parentPid": 67749,
"coalitionName": "com.cobalt.mainframe",
"uptime": 330000,   // 330s process uptime at crash — matches the 349s cadence
"exception": {
  "type": "EXC_BAD_ACCESS", "signal": "SIGSEGV",
  "subtype": "KERN_INVALID_ADDRESS at 0x0000000000000028"
}
```

This is a **reproducible segmentation fault inside LM Studio's `node`/`llmster`
inference worker**, consistently ~330-352 seconds after each load, independent of
whether the model is idle or serving traffic (confirmed both in the original seat
test and again just now under a fully idle system). It is not caused by Cobalt's ops
layer, an idle timer, system memory pressure, or a competing scheduled job — H1-H4 are
all ruled out or narrow. It is internal to the LM Studio/MLX runtime as applied to
**this specific model build** (`qwen3.5-122b-a10b`, MoE, 4-bit, `--gpu max
--context-length 32768`) on this host. Only 47 of 820 crashes produced a `.ips` (the
crash reporter appears to only catch a fraction of them), but every one that was
caught shows the identical signature.

**Practical read:** this is not fixable from the ops/heartbeat layer — it is a bug in
a closed-source LM Studio component tied to this model. See ESCALATE §5.

---

## 3 — E4: context declaration mismatch

`configs/config.yaml`:
```yaml
mainframe:
  ...
  context: 65536
```
Server reality: `ops/start_mainframe.sh` loads with `--context-length 32768`;
`/api/v0/models` confirms `loaded_context_length: 32768` right now. **The config side
is wrong.** 32768 is the deliberate VRAM-budget choice baked into the ops script (the
model supports up to 262144); the config simply never got updated to match. Any Cobalt
code that trusts `config.context` believes it has 2x the real window. Fix =
`configs/config.yaml` → `context: 32768`. This is a `configs/` change, outside F1's
bounded scope — escalated, not applied here.

---

## 4 — F1: heartbeat probe fix

**Diff** (`ops/start_mainframe.sh`, heartbeat loop only — `MODEL=` untouched):

```diff
@@ -148,8 +148,41 @@ caffeinate -i -m bash -c '
   MODEL="'"$MODEL"'"
   export PATH="'"$PATH"'"
   hb() { echo "$(date "+%Y-%m-%d %H:%M:%S") | $*" >> "$LOG_FILE"; }
+  reload() {
+    hb "heartbeat: attempting reload of $MODEL"
+    if lms load "$MODEL" --identifier "$MODEL_ID" --gpu max --context-length 32768 \
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
@@ -162,13 +195,7 @@ caffeinate -i -m bash -c '
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

**Rollback:** `git checkout ops/start_mainframe.sh` (single file, no dependents).

### ⚠️ Deviation from the literal F1 spec — evidence-based, needs sign-off

The ticket asked for the generation check to become a "readiness" probe that "never
triggers a reload on its own." **Testing during this triage proved that would leave
the mainframe permanently dead after the very next crash.** Passively polled
`GET /v1/models` and `/api/v0/models`'s per-model `state` field every 3s through one
full natural crash-and-heal cycle (19:53:43 → 20:01:41, no intervention):

```
19:53:49  v1_models=200  mainframe_state=loaded      <- last sample before the crash
19:54:24  [mainframe.log] heartbeat FAILED: model has crashed   <- crash detected
19:54:26  v1_models=200  mainframe_state=loading      <- state changed only because
19:54:29  v1_models=200  mainframe_state=loading         the EXISTING heartbeat's own
  ...                                                     reload command started
19:54:50  [mainframe.log] heartbeat: reload OK
20:00:15  [mainframe.log] heartbeat FAILED (next crash)
20:00:18  v1_models=200  mainframe_state=loading      <- again, only once WE reloaded
```

**`v1_models` returned HTTP 200 continuously — it never failed, not once, through the
whole cycle.** `state` never moved off `"loaded"` at the moment of the crash itself;
it only flipped to `"loading"` a beat later, driven by the pre-existing heartbeat's
own reload call. Neither endpoint reflects the crash on its own. Only an actual
inference call (the generation probe) exercises the dead worker and gets the error
back. **I therefore kept the generation probe as the reload trigger** (with the raised
120s timeout) and added the new `/v1/models` check only as a faster, cheaper
*additional* trigger for the case the ticket's liveness/readiness split was actually
aimed at — a fully dead HTTP daemon (e.g. the "API failed to start" boot-time case),
which `/v1/models` does correctly detect. This is a correction made from evidence
gathered in this same incident, not scope creep — flagging for explicit approval
rather than silently deviating.

### Live validation performed

1. **False-DOWN reproduction** (§2, H1): old 30s timeout → empty reply against a real
   34s generation (false DOWN); new 120s timeout → real reply, no false DOWN. Same
   curl invocations the script uses.
2. **New-logic dry run** (isolated copy, separate log file, reload stubbed so nothing
   was actually reloaded): two clean cycles against the live server —
   ```
   20:04:53 | liveness OK
   20:04:59 | heartbeat OK
   20:05:04 | liveness OK
   20:05:09 | heartbeat OK
   ```
3. **Crash count, 30 min immediately before this edit** (19:35–20:05, live production
   log, **old** code still running): **6 crashes**, all genuine `model has crashed`
   (zero `no response` — consistent with H1 only firing under concurrent load).

### NOT YET ACTIVE — deployment requires a decision outside this incident's scope

`com.cobalt.mainframe` (pid 67727) has been running continuously since
**2026-09-04 14:58** and has not restarted since — it is still executing the *old*
heartbeat loop from memory; editing the script file does not change an already-running
process. Activating F1 requires restarting the job, and `start_mainframe.sh` opens
with `lms unload --all` + `lms load …` — **that is an unload/reload of the model**,
explicitly forbidden under this incident's scope ("DO NOT: unload/reload/delete any
model"). **F1 is committed to the file only.** A "30 min after" crash count is
therefore not obtainable without violating that constraint — any count taken now would
still reflect the old, unfixed code. Activation is a deliberate, Dejan-approved
restart, ideally outside market hours per the standing deploy law, and is called out
in the ESCALATE section.

### F2 — LM Studio setting, if H2 confirmed

**N/A — H2 was RULED OUT** (§2). For completeness, the only TTL-shaped setting found
is `jitModelTTL.ttlSeconds = 3600` in `~/.lmstudio/settings.json`; it does not match
the observed cadence and was not touched.

---

## 5 — ESCALATE

**ESCALATE: higher-tier / human decision needed on the following:**

1. **Replacement-model decision (blocking E1's real fix).** The crash is now
   forensically tied to a SIGSEGV in the `node`/`llmster` MLX worker specific to
   running `qwen3.5-122b-a10b` (4-bit MoE) on this host's LM Studio build — not to
   load, memory, or timer conditions this triage can change. Replacing the served
   model is the most direct lever left. Everything already on disk, no download
   (`~/.lmstudio/models/`, from the 2026-09-07 seat test's B1/B4 inventory):

   | id | arch | quant | size | max ctx | state |
   |---|---|---|---|---|---|
   | `qwen3.5-122b-a10b` (current, crash-looping) | qwen3_5_moe | 4-bit | 65 GB | 262144 | loaded |
   | `qwen3.5-35b-a3b` | qwen3_5_moe | **8-bit** | 35 GB | 262144 | not-loaded |
   | `qwen3.5-27b` | qwen3_5 | 4-bit | 15 GB | 262144 | not-loaded |
   | `qwen3.5-27b-claude-4.6-opus-distilled-mlx` | qwen3_5 | 4-bit | 14 GB | 262144 | not-loaded |
   | `qwen3.5-4b-mlx` | qwen3_5 | 4-bit | 2.9 GB | 262144 | not-loaded |

   **There is no "3.8" build in the catalog at all** — `CLAUDE.md`'s "Qwen3.8-27B
   8-bit MLX" describes nothing present on this host on any layer (confirmed E3); the
   only 27B builds on disk are 4-bit, and the only 8-bit build is the 35B-A3B. Picking
   a replacement is a real trade-off (throughput/quality vs. this MoE crash risk) that
   needs a human or a higher-tier call, not this triage.

2. **The 122B deletion (E2, restated with new evidence).** Still **DO NOT DELETE
   YET** — it is the only model the ops job loads and the only one Cobalt's router can
   reach (`active_profile`: `default`/`coder`/`architect`/`strategist`/`fast_chat` all
   → `mainframe`). Order stands: pick replacement (#1) → change `MODEL=` in
   `ops/start_mainframe.sh` (a change explicitly out of my bounds here) → restart the
   LaunchAgent (unload/reload — also out of my bounds here) → verify `lms ps` + one
   router call → *then* delete. Given the SIGSEGV is now shown to be reproducible and
   model-specific rather than load-driven, replacing the model is a stronger candidate
   than before to independently resolve E1.

3. **E4's fix touches Cobalt config** — `configs/config.yaml` `mainframe.context`
   should change from `65536` to `32768` to match what is actually served. Out of
   scope for F1 (config change, not the heartbeat unit) — needs a deliberate edit
   plus `cobalt validate` per the repo's own config-boundary law.

4. **F1's design deviation (§4)** needs explicit sign-off: I kept the generation probe
   as the reload trigger against the ticket's literal wording, based on live evidence
   gathered in this same triage that the alternative leaves the mainframe unrecoverable
   after the next crash. If that read is wrong, the readiness/liveness split can be
   changed — but not back to the literal spec without also solving how a genuinely
   crashed model gets detected some other way.

5. **F1 activation.** The fix is written, syntax-checked, and validated against the
   live API, but is not running — it requires restarting `com.cobalt.mainframe`
   (which unloads/reloads the model), which this incident's scope forbids me from
   doing. Needs a deliberate restart, ideally outside market hours.
