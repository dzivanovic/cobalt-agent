JOB: f5-x3-values
LADDER: OFF-LADDER — reports/cto-2026-10-20.md R2217
CLASS: K2
INSTALL: none
BRANCH: ops/f5-x3-values
WORKTREE: f5-x3-values
BASE: 20dd871d
TIP:
REPORT: /Users/cobalt/cobalt-wt/f5-x3-values/docs/40 - DevDocs/reports/f5-x3-values-build-2026-10-20.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x3-values-check-2026-10-20.md
HOUSE B: as needed
BAND: LOW
RESTARTS: com.cobalt.aset
RULINGS: 2026-10-18 R1863

## GATE
- The build launches only after the last line of `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x3-measure-check-2026-10-20.md` (the card 945 check) is `CHECK DONE · … ready: YES`. Any other last line → no launch; the desk takes it to the brain.
- BASE `20dd871d` is the `ops/f5-x3-measure` tip (the X3 report commit on `de976722`), so this branch carries the report its `# source:` comments cite. If the 945 check moves that tip, the desk sets BASE to the checked tip before the launch.
- `## DECISIONS` 1 (the COLD row) is answered by the desk before the launch.

## ROWS

WHY: F5 is on main with the `checkpoint.narrative` route at UNMEASURED provisional values (`configs/cobalt/modelaccess.yaml:70-82`: `timeout_s: 60` `:78`, `max_output_tokens: 512` `:80`, comments `:77`, `:79`). X3 (`docs/30 - Design/F5-FINAL-2026-10-11.md:177`; FINAL `:88`: each value carries its `source:` comment, never the voice route's 15 s) measured 30 of 30 warm calls: p95 3.53 s, max 4.97 s, max output tokens 59, think_leak 0, empty 0 (`reports/f5-x3-measure-2026-10-20.md` on `ops/f5-x3-measure`, `### V1`). Values rule (R2217, R2248): `timeout_s` = max(2 × p95, max), up to a multiple of 5 s (7.06 → 10); `max_output_tokens` = 2 × max tokens, up to a multiple of 64, floor 256 (118 → 256). Every `file:line` is `main` at drafting; re-find each by content (BUILD-HUB E3). No `src/` change, no plist, no migration, no database.

| row | what | red first | files |
|---|---|---|---|
| T1 | `configs/cobalt/modelaccess.yaml`, route `checkpoint.narrative` (`:70`): `timeout_s: 60` (`:78`) → `timeout_s: 10`; its comment line `:77` (`# source: UNMEASURED, provisional — X3 owed before load (card 731 DECISION 2). Never the voice route's 15 s.`) → `# source: X3 reports/f5-x3-measure-2026-10-20.md (warm model). Never the voice route's 15 s.` Find the line by content, not by number. If `## DECISIONS` 1 is answered with a cold figure over 10 s, the value is cold × 1.5 rounded up to a multiple of 5 s and the comment ends `(warm model); cold <s> s × 1.5 → <n>` in place of `(warm model).`; otherwise it stays 10 | NEW test in `tests/cobalt/test_checkpoints_offline.py`, beside `test_route_is_loaded_and_local` (`:553-558`), in its style: `test_route_budgets_are_measured`. Reads `load_routes().routes["checkpoint.narrative"]` and `load_routes().routes["local.plan"]` through the loader and asserts invariants only (L69): `timeout_s` is an `int`, `> 0`, a multiple of 5, and not `local.plan`'s `timeout_s` (FINAL `:88`); for each of the four `com.cobalt.checkpoint-*` labels, `load_job_registry().spec(label).timeout_s` (`src/cobalt/jobs/config.py:453`, `:463`) is greater than the route's `timeout_s` + 60 (the two 30 s fetches, `configs/cobalt/jobs.yaml` checkpoint comment above `com.cobalt.checkpoint-0715`); the route's block in the file text (from the line `  checkpoint.narrative:` to the end of `routes:`) holds no `UNMEASURED` and exactly two lines holding `# source: X3 reports/f5-x3-measure-2026-10-20.md`. It never spells 10 or 256. RED on BASE: the block holds `UNMEASURED` | `configs/cobalt/modelaccess.yaml` (`:77-78`), `tests/cobalt/test_checkpoints_offline.py` (the NEW test), `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` (ONE dated line `## <date> — f5-x3-values` saying the two values are measured by X3, superseding the UNMEASURED sentence at `:19`) |
| T2 | Same route: `max_output_tokens: 512` (`:80`) → `max_output_tokens: 256`; its comment line `:79` (`# source: UNMEASURED, provisional — X3 owed before load (card 731 DECISION 2).`) → `# source: X3 reports/f5-x3-measure-2026-10-20.md (warm model)` | The same NEW test, one more assert: `max_output_tokens` is an `int`, a multiple of 64 and `>= 256` (the rule's floor). Green on BASE (512); RED on BASE comes from T1's comment assert, which covers both lines (the count of two) | `configs/cobalt/modelaccess.yaml` (`:79-80`) |
| COLD | ASK DESK (`## DECISIONS` 1). No admitted command unloads `mainframe` (the only unload in the repo is `lms unload --all` at `ops/start_mainframe.sh:242`, a production restart path; `lms`, `launchctl` and `curl` are not on `BUILD-HUB.md:14`, `:16`). DEFAULT, the nearest admitted read: RUN — asserts nothing. The builder runs `grep -n -F "Model loaded successfully" /Users/cobalt/cobalt/ops/logs/mainframe.log` and quotes it whole (the `mainframe` model's own load times; read only, no model call), then computes in the report `COLD-PROXY = the largest load time + the X3 max 4.97 s` and the ×1.5 value (`cold > 10 s` → cold × 1.5 up to a multiple of 5 s). It does NOT apply the proxy: T1 stays 10 unless the desk's answer to `## DECISIONS` 1 says so. If the desk answers with an admitted way to unload `mainframe`, the row becomes ONE `checkpoint.narrative` call right after the unload, as card 945 R1 makes its calls (scratch pytest, `run_in_background`, deleted before the commit), under this TIME GATE: the RUN step starts at 20:35 ET or later (the no-voice window) and must end before 07:00 ET; before 20:35 or at/after 07:00 → do not run; `FAILED: COLD — outside the 20:35–07:00 window (<date output>)` | — (tool output quoted in the report) | none (read only) |

ORDER: COLD, T1, T2, then RESTARTS and the suites.

Suites, quoted whole in the build report: `uv run pytest -q -p no:cacheprovider tests/cobalt/test_checkpoints_offline.py tests/cobalt/test_modelaccess_config.py tests/cobalt/test_checkpoints_registry.py` → `0 failed` (the NEW test RED on BASE first); then the deploy gate's pass (BUILD-HUB `## W`, all three suites) → `0 failed`, `0 errors`.

## NOT IN THIS JOB
- Loading any plist: `com.cobalt.checkpoint-0715/-0745/-0815/-0845` stay unloaded and in `bootstrap-owed`, gated on X2, X4–X7, X10, X12, X13 and X5 (contention with voice, before load).
- `configs/cobalt/jobs.yaml`: the four checkpoint rows' `timeout_s: 300` and their comment stay (card 731 DECISION 4; the NEW test reads them, never edits them).
- `local.plan`, `local.embed`, any other `modelaccess.yaml` key; `src/`; `ops/`; any migration; any database; any production command.
- Any call to `mainframe` unless `## DECISIONS` 1 is answered with an admitted unload; any `lms`, `launchctl` or `curl`.
- X5 and the 07:15 contention; X2; re-deciding the values rule (R2217, R2248).
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md` (on BASE) `## §0`, `### R1`, `### V1`.
- `configs/cobalt/modelaccess.yaml:30-38` (the `# source:` style), `:52-58` (the `local.embed` JIT-load comment), `:63-82`.
- `docs/30 - Design/F5-FINAL-2026-10-11.md:88`, `:138`, `:177`, `:235`.
- `tests/cobalt/test_checkpoints_offline.py:553-558`; `tests/cobalt/test_modelaccess_config.py:69-80`; `tests/cobalt/test_checkpoints_registry.py:17-27`.
- `src/cobalt/modelaccess/config.py:31`, `:150`; `src/cobalt/jobs/config.py:453`, `:463`.
- `configs/cobalt/jobs.yaml:86` (aset reads `modelaccess.yaml`), `:102-112` (`com.cobalt.mainframe`), the checkpoint rows' comment.
- `ops/start_mainframe.sh:241-242`, `:295`, the heartbeat loop (60 s ping, self-heal reload).
- `docs/40 - DevDocs/cobalt/prefill/checkpoints.md:19`.

## CHECK ASKS
- X1 Are the only changed lines of `modelaccess.yaml` the two values and their two comment lines of `checkpoint.narrative`, and do the values follow the rule from the X3 report's numbers (or the desk's cold answer)?
- X2 Does the NEW test pin only invariants (no 10, no 256 spelled), read through `load_routes` and `load_job_registry`, and go RED when a comment is put back to `UNMEASURED`?
- X3 COLD: is the proxy computed from the quoted log lines and left unapplied (or the desk's answer applied as stated), with no model call and no unload made?
- X4 RESTARTS re-derived: `com.cobalt.aset` only (`jobs.yaml:86`)?

## DEPLOY PROOF
- `grep -c -F "source: UNMEASURED" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `2` · after `0`
- `grep -c -F "# source: X3 reports/f5-x3-measure-2026-10-20.md (warm model)" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `2`
- the sheet answers after the aset restart · `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/` · exit 0, `200`
- checkpoint plists stay on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` · exit 0, listed

## DECISIONS
1. ASK DESK: the COLD leg. No admitted command unloads `mainframe` (`git grep -n -i "unload\|keep_alive" main -- src ops` finds only `ops/start_mainframe.sh:242` `lms unload --all`, inside the production start script; BUILD-HUB `:16` never types `lms`, `launchctl`, `curl`). Default: the COLD row reads the model's own load times from `ops/logs/mainframe.log` (read only) and reports `COLD-PROXY` unapplied; T1 stays 10. Drafter's read at 21:12: two lines, `Model loaded successfully in 8.67s.` (`:12`) and `5.47s.` (`:31`), both 2026-09-09; proxy 8.67 + 4.97 = 13.64 s > 10 → ×1.5 = 20.46 → `timeout_s` 25. The desk says either "apply the proxy" (T1 = 25, the comment says so), or names an admitted unload (the row becomes one live call in the window), or "stays 10".
2. FACT for decision 1: the model is held loaded. `com.cobalt.mainframe` loads with no `--ttl` (`ops/start_mainframe.sh:295`) and its heartbeat pings `mainframe` every 60 s and reloads on a failure; an idle unload at 07:15 is not expected while it runs. The `local.embed` 7.5 s JIT figure (`modelaccess.yaml:55`) is another model, not held. The 07:15 risk the log shows is a busy server, not a cold one: `mainframe.log:58007-58014`, 2026-10-20 07:14:00 OK → 07:17:00 `heartbeat FAILED: no response` (the 120 s ping) → reload refused (`identifier mainframe already exists`) → 07:18:30 OK. That is X5's ground, not this card's.
3. BAND LOW: two config values, one test, one DevDocs line, a read-only RUN row. If the desk answers decision 1 with a live call (945's shape, BAND HIGH), the desk raises BAND before the launch.
4. CLASS K2, RESTARTS `com.cobalt.aset`: `modelaccess.yaml` is in aset's `reads:` (`jobs.yaml:86`); tests and docs restart nothing. The four checkpoint one-shots re-read the file each run and are unloaded. The builder's `cobalt jobs restarts` line overrides the header if it differs.
5. BASE `20dd871d` (the 945 tip), not main `f185458c`: the `# source:` comments cite the X3 report, which lives only on `ops/f5-x3-measure`; `git diff --stat de976722 main -- src configs tests ops` is empty, so the code is main's.

## RECORDS
- F5 X3 30/30 warm p95 3.53 s max 4.97 s tokens 59 → timeout_s 10, max_output_tokens 256; values card adds one cold-call leg (cold > 10 s → ×1.5 up 5 s); 945 check runs in parallel with the values drafter — brain 9b07db5a 2026-10-20
- Drafter `draft-f5-x3-values` (prompt 957), 2026-10-20 21:11–21:14 EDT (`date`). Reads only; no model call, no network, no git write; nothing committed. `git rev-parse --short=8 main` → `f185458c`; `ops/f5-x3-measure` → `20dd871d` (one commit past `de976722`: the build report).
- RESTARTS class: a `configs/cobalt/modelaccess.yaml` edit restarts `com.cobalt.aset` (`jobs.yaml:86`, `load_routes` from `voice/web.py:176`); F5-FINAL `:235` names the same; card 945 C1's docs-only range was `none`.
- The 945 check report's last line at 21:12: `(run in progress — next step under ## CONTINUE)`.
- Reads: `prompts/CARD.md`, cards 945 and 933 whole, the X3 report whole, `git show main:` of `modelaccess.yaml`, `jobs.yaml`, `F5-FINAL-2026-10-11.md` (`:88`, `:138`, `:177`, `:235`), `BUILD-HUB.md` (`:14`, `:16`, `## W`), `ops/desk/deploy-smoke.sh` (mapped shapes: `ls`, `grep -c -F`, `curl … http://127.0.0.1:5010/`), `ops/start_mainframe.sh`, `tests/cobalt/test_modelaccess_config.py`; `git grep` on main for unload/keep_alive, TTL/JIT, `checkpoint.narrative`, `source: UNMEASURED` (2, `:77`, `:79`), `source: X3` (0); `grep` of `ops/logs/mainframe.log` (load lines `:12`, `:31`; reloads; `:58000-58024`); `cto-2026-10-20.md` R2217, R2248, R2249.
