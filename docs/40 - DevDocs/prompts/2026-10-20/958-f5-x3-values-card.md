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
- `## DECISIONS` 1 (the COLD row) is answered: option C, brain 2026-10-20 (R2251) — `timeout_s: 25` from the cold proxy; no model call, no unload.

## ROWS

WHY: F5 is on main with the `checkpoint.narrative` route at UNMEASURED provisional values (`configs/cobalt/modelaccess.yaml:70-82`: `timeout_s: 60` `:78`, `max_output_tokens: 512` `:80`, comments `:77`, `:79`). X3 (`docs/30 - Design/F5-FINAL-2026-10-11.md:177`; FINAL `:88`: each value carries its `source:` comment, never the voice route's 15 s) measured 30 of 30 warm calls: p95 3.53 s, max 4.97 s, max output tokens 59, think_leak 0, empty 0 (`reports/f5-x3-measure-2026-10-20.md` on `ops/f5-x3-measure`, `### V1`). Values rule (R2217, R2248): `timeout_s` = max(2 × p95, cold × 1.5), up to a multiple of 5 s (2 × 3.53 = 7.06; cold proxy = `mainframe.log:12` load 8.67 s + warm max 4.97 s = 13.64 s, × 1.5 = 20.46 → 25; R2251); `max_output_tokens` = 2 × max tokens, up to a multiple of 64, floor 256 (118 → 256). Every `file:line` is `main` at drafting; re-find each by content (BUILD-HUB E3). No `src/` change, no plist, no migration, no database.

| row | what | red first | files |
|---|---|---|---|
| T1 | `configs/cobalt/modelaccess.yaml`, route `checkpoint.narrative` (`:70`): `timeout_s: 60` (`:78`) → `timeout_s: 25`; its comment line `:77` (`# source: UNMEASURED, provisional — X3 owed before load (card 731 DECISION 2). Never the voice route's 15 s.`) → exactly `# source: X3 reports/f5-x3-measure-2026-10-20.md warm p95 3.53 s / max 4.97 s + cold load 8.67 s from the mainframe log (proxy, not a live cold call); rule max(2×p95, cold×1.5) up 5 s`. Find the line by content, not by number. The old `Never the voice route's 15 s.` wording is not in the ruled comment; it stays in this card's WHY (FINAL `:88`) and in the NEW test (`timeout_s` is not `local.plan`'s) | NEW test in `tests/cobalt/test_checkpoints_offline.py`, beside `test_route_is_loaded_and_local` (`:553-558`), in its style: `test_route_budgets_are_measured`. Reads `load_routes().routes["checkpoint.narrative"]` and `load_routes().routes["local.plan"]` through the loader and asserts invariants only (L69): `timeout_s` is an `int`, `> 0`, a multiple of 5, and not `local.plan`'s `timeout_s` (FINAL `:88`); for each of the four `com.cobalt.checkpoint-*` labels, `load_job_registry().spec(label).timeout_s` (`src/cobalt/jobs/config.py:453`, `:463`) is greater than the route's `timeout_s` + 60 (the two 30 s fetches, `configs/cobalt/jobs.yaml` checkpoint comment above `com.cobalt.checkpoint-0715`); the route's block in the file text (from the line `  checkpoint.narrative:` to the end of `routes:`) holds no `UNMEASURED` and exactly two lines holding `# source: X3 reports/f5-x3-measure-2026-10-20.md`. It never spells 25 or 256. RED on BASE: the block holds `UNMEASURED` | `configs/cobalt/modelaccess.yaml` (`:77-78`), `tests/cobalt/test_checkpoints_offline.py` (the NEW test), `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` (ONE dated line `## <date> — f5-x3-values` saying the two values are measured by X3, superseding the UNMEASURED sentence at `:19`) |
| T2 | Same route: `max_output_tokens: 512` (`:80`) → `max_output_tokens: 256`; its comment line `:79` (`# source: UNMEASURED, provisional — X3 owed before load (card 731 DECISION 2).`) → `# source: X3 reports/f5-x3-measure-2026-10-20.md (warm model)` | The same NEW test, one more assert: `max_output_tokens` is an `int`, a multiple of 64 and `>= 256` (the rule's floor). Green on BASE (512); RED on BASE comes from T1's comment assert, which covers both lines (the count of two) | `configs/cobalt/modelaccess.yaml` (`:79-80`) |
| COLD | RULED, option C (R2251): the proxy, no live call. The builder makes no model call and no unload (the only unload in the repo is `lms unload --all` at `ops/start_mainframe.sh:242`, a production restart path; `lms`, `launchctl` and `curl` are not on `BUILD-HUB.md:14`, `:16`). It runs `grep -n -F "Model loaded successfully" /Users/cobalt/cobalt/ops/logs/mainframe.log` and quotes the two lines (`mainframe.log:12` `Model loaded successfully in 8.67s.`, `:31` `5.47s.`, both 2026-09-09) and writes the arithmetic in the report: `COLD-PROXY = 8.67 + 4.97 = 13.64 s`; × 1.5 = 20.46; up to a multiple of 5 s = 25. T1 applies it (`timeout_s: 25`). No TIME GATE: nothing runs against the model | — (tool output quoted in the report) | none (read only) | — (tool output quoted in the report) | none (read only) |

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
- X3 COLD: is the proxy (13.64 s → ×1.5 = 20.46 → 25) computed from the two quoted log lines (`mainframe.log:12`, `:31`) and applied as `timeout_s: 25`, with no model call and no unload made?
- X4 RESTARTS re-derived: `com.cobalt.aset` only (`jobs.yaml:86`)?

## DEPLOY PROOF
- `grep -c -F "source: UNMEASURED" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `2` · after `0`
- `grep -c -F "# source: X3 reports/f5-x3-measure-2026-10-20.md" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `2`
- `grep -c -F "(warm model)" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `1` (T2's line only)
- `grep -c -F "cold load 8.67 s from the mainframe log (proxy, not a live cold call)" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `1` (T1's line)
- the sheet answers after the aset restart · `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/` · exit 0, `200`
- checkpoint plists stay on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` · exit 0, listed

## DECISIONS
1. answered: option C, brain 2026-10-20 (R2251)
2. FACT for decision 1: the model is held loaded. `com.cobalt.mainframe` loads with no `--ttl` (`ops/start_mainframe.sh:295`) and its heartbeat pings `mainframe` every 60 s and reloads on a failure; an idle unload at 07:15 is not expected while it runs. The `local.embed` 7.5 s JIT figure (`modelaccess.yaml:55`) is another model, not held. The 07:15 risk the log shows is a busy server, not a cold one: `mainframe.log:58007-58014`, 2026-10-20 07:14:00 OK → 07:17:00 `heartbeat FAILED: no response` (the 120 s ping) → reload refused (`identifier mainframe already exists`) → 07:18:30 OK. That is X5's ground, not this card's.
3. BAND LOW: two config values, one test, one DevDocs line, a read-only COLD row (the log proxy; no live call, so BAND stays LOW, R2251).
4. CLASS K2, RESTARTS `com.cobalt.aset`: `modelaccess.yaml` is in aset's `reads:` (`jobs.yaml:86`); tests and docs restart nothing. The four checkpoint one-shots re-read the file each run and are unloaded. The builder's `cobalt jobs restarts` line overrides the header if it differs.
5. BASE `20dd871d` (the 945 tip), not main `f185458c`: the `# source:` comments cite the X3 report, which lives only on `ops/f5-x3-measure`; `git diff --stat de976722 main -- src configs tests ops` is empty, so the code is main's.

## RECORDS
- F5 X3 30/30 warm p95 3.53 s max 4.97 s tokens 59 → timeout_s 10, max_output_tokens 256; values card adds one cold-call leg (cold > 10 s → ×1.5 up 5 s); 945 check runs in parallel with the values drafter — brain 9b07db5a 2026-10-20
- 958 timeout_s 25 = cold proxy (mainframe log load 8.67 s + warm max 4.97 s) × 1.5 up 5 s; max_output_tokens 256; no unload string added — brain 9b07db5a 2026-10-20
- Amend drafter `draft-f5-x3-values-cold` (prompt 959), 2026-10-20 21:16 EDT (`date`). Applied option C to the COLD row, T1, header, X3, DEPLOY PROOF, DECISIONS 1, WHY. Reads: prompt 959, this card whole, `grep -n -F "Model loaded successfully" ops/logs/mainframe.log` (`:12` 8.67 s, `:31` 5.47 s), `git show main:configs/cobalt/modelaccess.yaml` (`timeout_s: 60`, `max_output_tokens: 512`, two `source: UNMEASURED` lines), `cto-2026-10-20.md` R2251 (`:21`). Nothing run, no model call, nothing committed. Marker counts to re-prove: `# source: X3 reports/f5-x3-measure-2026-10-20.md` 0→2; `(warm model)` 0→1 (T2 only); `cold load 8.67 s from the mainframe log (proxy, not a live cold call)` 0→1; `source: UNMEASURED` 2→0 (main, read above). Card `timeout_s: 10` / `unapplied` / `ASK DESK` greps: only the quoted T1 `60`-line and the 958 DECISIONS lines remain.
- Drafter `draft-f5-x3-values` (prompt 957), 2026-10-20 21:11–21:14 EDT (`date`). Reads only; no model call, no network, no git write; nothing committed. `git rev-parse --short=8 main` → `f185458c`; `ops/f5-x3-measure` → `20dd871d` (one commit past `de976722`: the build report).
- RESTARTS class: a `configs/cobalt/modelaccess.yaml` edit restarts `com.cobalt.aset` (`jobs.yaml:86`, `load_routes` from `voice/web.py:176`); F5-FINAL `:235` names the same; card 945 C1's docs-only range was `none`.
- The 945 check report's last line at 21:12: `(run in progress — next step under ## CONTINUE)`.
- Reads: `prompts/CARD.md`, cards 945 and 933 whole, the X3 report whole, `git show main:` of `modelaccess.yaml`, `jobs.yaml`, `F5-FINAL-2026-10-11.md` (`:88`, `:138`, `:177`, `:235`), `BUILD-HUB.md` (`:14`, `:16`, `## W`), `ops/desk/deploy-smoke.sh` (mapped shapes: `ls`, `grep -c -F`, `curl … http://127.0.0.1:5010/`), `ops/start_mainframe.sh`, `tests/cobalt/test_modelaccess_config.py`; `git grep` on main for unload/keep_alive, TTL/JIT, `checkpoint.narrative`, `source: UNMEASURED` (2, `:77`, `:79`), `source: X3` (0); `grep` of `ops/logs/mainframe.log` (load lines `:12`, `:31`; reloads; `:58000-58024`); `cto-2026-10-20.md` R2217, R2248, R2249.
