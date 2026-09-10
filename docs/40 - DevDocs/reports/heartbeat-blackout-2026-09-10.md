# Heartbeat blackout — 2026-09-08 & 09-09, 20:00–21:00 ET

*Read-only diagnosis. No fix applied, nothing committed. Hub: Opus 5. Worker: Codex `gpt-5.6-terra`, `-s read-only`.*

## §0 Headline

Both blackouts are **one cause, fully in the log**: every "missing" beat ran, and
died at the F1 `market_reset` gate on its own daily-note write. `write_note_block()`
is called unguarded at `runner.py:249`, and the heartbeat's own DB row is not stamped
until `runner.py:291-292` — so the refusal kills the beat before it records itself,
alerts, or DMs. **H1 SUPPORTED · H2 REFUTED · H3 REFUTED.** ESCALATE: 4.

## The two windows, side by side

| | 2026-09-08 | 2026-09-09 |
|---|---|---|
| Last beat before gap | 19:52:20 ET (`vault_writes` id 2103) | 19:59:01 ET (id 2216) |
| Beats attempted in gap | 20:07:23, 20:22:26, 20:37:28, 20:52:31 | 20:14:04, 20:29:07, 20:44:10, 20:59:13 |
| Each attempt's outcome | `SessionBlocked` → process exit non-zero | `SessionBlocked` → process exit non-zero |
| First beat back | 21:07:31 ET, **RED — 1 job(s)** (id 2106) | 21:14:16 ET, **RED — 1 job(s)** (id 2219) |
| Gap length | 75 min 13 s | 75 min 15 s |
| Archiver 20:30 run | 20:30:05 → 20:53:26, 3,166,696 rows, exit 0, 23m20s | 20:30:05 → 20:53:25, 3,167,272 rows, exit 0, 23m19s |

The gap is not approximately the block window — it **is** the block window, snapped to
the 15-min phase: every scheduled tick whose clock fell inside 20:00–21:00 ET died,
and the phase is unbroken across the gap (19:52→21:07, 19:59→21:14). launchd never
missed a beat; the beat missed itself.

## Verdicts

| H | Verdict | Evidence |
|---|---|---|
| **H1** write-block collision | **SUPPORTED** | `system.session_blocks` ids 1–8, actor `vaultwrite:heartbeat:upsert_unit`, one row per missing tick, target = that day's daily note. Each is paired in `logs/heartbeat.err` with `FAILED: SessionBlocked: …` — the CLI's top-level fail-loud exit. 8 rows, 8 `FAILED` lines, whole-file totals, no other cause anywhere. |
| **H2** job never launched | **REFUTED** | The job launched at all four ticks each night — the refusal rows carry its own wall clock (20:07:23, 20:22:26, …). `launchctl print gui/501/com.cobalt.heartbeat`: `run interval = 900 seconds`, `runs = 518`, `last exit code = 0`, no throttle field, `runatload`. `pmset -g log` shows `caffeinate PreventUserIdleSystemSleep` held through both windows and no sleep/wake transition. |
| **H3** launched, hung or killed | **REFUTED** | Every attempt died **fast** and by name: `SessionBlocked`, ~3 s after launch, after all 12 probes had already run. The archiver completed cleanly both nights (exit 0, 0 failures, 23m). No hang, no SIGKILL, no timeout. |

## The code path (item 1.6)

`src/cobalt/heartbeat/runner.py:243-292` — the order is the defect:

```python
243  def run_beat(*, now=None, dry_run=False, probe=True) -> Beat:
247      beat = take_beat(now=now, probe=probe)      # all 12 probes + job sweep — succeeded every time
249      write = write_note_block(beat, dry_run=dry_run)   # ← raises here, unguarded
250      if write is None:                                  # only handles "note does not exist"
...
291      store.mark_running(JOB_LABEL,  now=...)     # ← never reached
292      store.mark_finished(JOB_LABEL, exit_code=0, result=result, now=...)
```

`write_note_block` → `runner.py:147` `writer.upsert_unit(...)` → `vaultwrite/writer.py:664`
`self._session_gate("upsert_unit", path)` → `writer.py:411` `assert_writable(...)` →
`session/guard.py:150` **raises `SessionBlocked`** (a `RuntimeError`; the ERROR line is `guard.py:146`).

Nothing catches it. `write_note_block` guards only "the note does not exist"
(`runner.py:136-142`); `cmd_beat` (`heartbeat/cli.py:27`) has no handler either. The
exception unwinds to the CLI's fail-loud top level, which prints `FAILED: SessionBlocked: …`
to stderr and exits non-zero.

Consequences of dying at :249, all four of them:
1. **No DB row** — `system.cobalt_jobs` is a single upsert row per label, so the heartbeat's
   row simply stays at 19:52 and goes stale. There is no beat history to lose; there is no
   beat history at all.
2. **No alert** — `out_of_band()` (email) and `send_dm()` are at `runner.py:269-270`, after
   the write. A beat that has something to say is silenced by the fact that it cannot write
   the note.
3. **No F17 wrapper to catch it** — the plist runs `uv run cobalt heartbeat beat` directly.
   Unlike the archiver (`jobs.wrapper` logs `F17: … RUNNING` / `DONE`), the heartbeat
   self-records inside `run_beat`, so a crash before :291 leaves no `failed` row — just silence.
4. **Nothing degrades** — probes, sweep, and rendered beat were all in hand at :249 and were
   thrown away with the exception.

## Why it self-detects, and why that took 75 minutes

The 21:07 / 21:14 beat is the first one whose clock is outside the block. Its own watchdog
sweep reads its own stale `cobalt_jobs` row and reports:

```
RED  com.cobalt.heartbeat  done (MISSED) every 15 min; last finish 2026-09-08 19:52 ET,
     measured from 2026-09-08 19:52 ET — more than two intervals (30 min) ago.
```

Correct, and it names the symptom without the cause. The cause was in `heartbeat.err` the
whole time — Dejan's "not in the log" is `heartbeat.log` (stdout, the rendered beat), which
by construction contains only beats that survived to be rendered.

## The probe that watched it happen and called it green

`probes.py:320-348` `vaultwrite_blocks` reported, in the very RED beat that noticed the gap:

```
OK   vault blocks   4 refused, 0 ungated repair run(s) in the counter window
```

Four refusals — the exact four dead beats — rated **OK by design**: *"NOT RED ON ITS OWN. A
refusal is the guard WORKING"* (`probes.py:321-324`). True of every other actor; false when
the refused writer is the heartbeat itself. `system.session_blocks` has **8 rows total,
all 8 `vaultwrite:heartbeat:upsert_unit`** — to date, the only thing F1 has ever turned away
is the heartbeat.

## The control case: 2026-09-07 proves causation

| Date | Trading day? | Heartbeat writes inside 20:00–21:00 |
|---|---|---|
| 2026-09-07 | **No — Labor Day** (`configs/cobalt/calendar/nyse-2026.yaml:45`) | **4** (20:02, 20:17, 20:32, 20:47) — no gap |
| 2026-09-08 | Yes | 0 |
| 2026-09-09 | Yes | 0 |

On a market holiday the whole day is `overnight` (`clock.py:196-198`), no `market_reset`
window exists, the gate never fires, and the beats went through — same code, same archiver
run at 20:30 (also exit 0, 23m21s), same machine. This also dates the defect: the gate landed
2026-09-04 19:03 (`e2acd20`), and **09-08 was the first trading-day 20:00–21:00 window with
both the gate and the heartbeat live**. It is not a regression from 09-08's deploy; it is the
first night the two met. It will recur tonight and every trading night until fixed.

## ESCALATE

- **Fix class (not applied):** *persistence ordering + vault-write degradation.* The beat must
  persist itself (DB row) and run its alert channels **before**, or independently of, the vault
  write; the `market_reset` refusal of the heartbeat's own status unit must be a caught,
  degraded, reported condition — not an exception that ends the beat. Whether the correct shape
  is (a) reorder + `try/except SessionBlocked` around `write_note_block`, (b) a repo-owned-style
  carve-out for the heartbeat's status unit, or (c) writing the block at 21:00 as a catch-up, is
  a **trading-logic-adjacent design call** — F1's window is a Charter rule and any carve-out in it
  needs its own ruling. Not decided here.
- **`log show` unavailable.** Terra's Unified Log queries returned `log: Cannot run while sandboxed`;
  launchd's own spawn/throttle/kill messages are unread. Moot for these verdicts — the refusal rows
  timestamp the launches directly — but it means no independent launchd-side confirmation exists,
  and this tool will be unavailable to the next sandboxed forensics run too.
- **Per-run exit codes are not retained.** `heartbeat.err` carries no per-run exit code or duration,
  and `launchctl` keeps only the most recent (`last exit code = 0`). Eight non-zero exits left no
  durable trace outside the log text. The heartbeat is the one job with no F17 wrapper.
- **Second failure mode, unrelated to the gap:** `vaultwrite_blocks` cannot distinguish "F1 turned
  away someone else" from "F1 killed the watcher". As written it will stay green through every
  future recurrence of this exact outage.
- **Also observed, not investigated:** an off-phase beat at 2026-09-08 19:22:14, 62 s after the
  19:21:12 beat. Out of scope here; flagging it rather than dropping it.
