# draft-f5-x3-values — drafter report 2026-10-20

## §0 Headline
Card written: `prompts/2026-10-20/958-f5-x3-values-card.md` (JOB `f5-x3-values`, BASE `20dd871d`, BAND LOW, RESTARTS `com.cobalt.aset`), uncommitted.
T1 `timeout_s: 10`, T2 `max_output_tokens: 256`, each `# source: X3 reports/f5-x3-measure-2026-10-20.md (warm model)`; one invariant test beside `test_route_is_loaded_and_local`.
COLD is `ASK DESK`: no admitted command unloads `mainframe`. Default: a read-only proxy from `ops/logs/mainframe.log`: load 8.67 s + X3 max 4.97 s = 13.64 s, which gives 25 under the ×1.5 rule. It is reported, not applied.
The heartbeat holds `mainframe` loaded (60 s pings, no `--ttl`). At 07:15 the risk the log shows is a busy server (today 07:14→07:18, no response to a 120 s ping), not a cold one.
GATE: the build launches after the 945 check reads `CHECK DONE · … ready: YES`. At 21:12 it was still running.

## DECISIONS
1. ASK DESK: COLD leg. Pick one: apply the proxy (T1 = 25, with the comment saying so), name an admitted unload (then one live call in the 20:35–07:00 window, BAND to HIGH), or keep it at 10. Default: keep 10 and report the proxy (card `## DECISIONS` 1, 2).
2. BASE `20dd871d` (the `ops/f5-x3-measure` tip), not main. The source comments cite the X3 report, which exists only on that branch. `git diff --stat de976722 main -- src configs tests ops` prints nothing. If the check moves the tip, the desk resets BASE.
3. Header keys beyond the prompt, taken from 945/933: `CLASS: K2`, `INSTALL: none`, `RESTARTS: com.cobalt.aset`. `BASE` is a real hash, because CARD.md does not mark BASE as the desk's. No `DB:` key, because the rows touch `configs/` and `tests/cobalt/`.
4. T1 keeps the existing `Never the voice route's 15 s.` after the source text. The marker string `(warm model)` still counts 2.
5. Card body adds `## GATE` (asked by the prompt; not a CARD.md section). The desk confirms `desk-launch.sh` accepts it.

## RECORDS
- `date`: 21:11:17 EDT (start), 21:13:56 (card write), 21:14:53 (report).
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `f185458c`; `… ops/f5-x3-measure` → `20dd871d`; `git log --oneline de976722..ops/f5-x3-measure` → `20dd871d docs(f5-x3-measure): build report — de976722`.
- Read whole: the prompt 957; `prompts/CARD.md`; cards 945 and 933; the X3 report (`cobalt-wt/f5-x3-measure/…/f5-x3-measure-2026-10-20.md`); `writing-rules.md`; `areas/cobalt.md` `## What Cobalt is`, `## Build rules` down.
- `git show main:`: `configs/cobalt/modelaccess.yaml` (`:70-82`; comments `:77`, `:79`), `configs/cobalt/jobs.yaml` (`:86`, `:102-112`, checkpoint rows), `docs/30 - Design/F5-FINAL-2026-10-11.md` (`:88`, `:138`, `:177`, `:235`), `prompts/BUILD-HUB.md` (`:14`, `:16`, `## W`, `## RESTARTS`), `ops/desk/deploy-smoke.sh`, `ops/start_mainframe.sh`, `tests/cobalt/test_modelaccess_config.py`.
- `git grep` on main: `-i "unload\|keep_alive" -- src ops` → only `ops/start_mainframe.sh:242` `lms unload --all` for the model; `-F "lms "` → start_mainframe.sh only; `"source: UNMEASURED"` → `modelaccess.yaml:77`, `:79`; `"source: X3"` in configs → none; tests on the route → `test_checkpoints_offline.py:553-558`, `test_checkpoints_registry.py:23`; `src/cobalt/jobs/config.py:453` `spec`, `:463` `load_job_registry`; `src/cobalt/modelaccess/config.py:31`, `:150`; `docs/40 - DevDocs/cobalt/prefill/checkpoints.md:19`; `cto-2026-10-20.md` R2217 `:52`, R2248 `:21`, R2249 `:20`.
- `grep` of `ops/logs/mainframe.log`: `Model loaded successfully` → `:12` 8.67 s, `:31` 5.47 s (2026-09-09); `heartbeat: reload` → 32 failures, the latest `:58013` 2026-10-20 07:17:00; Read `:1-35`, `:58000-58024`.
- `tail -n 5` of `reports/f5-x3-measure-check-2026-10-20.md` → `(run in progress — next step under ## CONTINUE)`.
- Nothing run beyond reads; no model call; no git write.

DRAFTED · decisions: 5
