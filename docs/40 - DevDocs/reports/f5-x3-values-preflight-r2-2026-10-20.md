# Card 958 (f5-x3-values) — preflight round 2, 2026-10-20

Read-only. Card `prompts/2026-10-20/958-f5-x3-values-card.md` (amended and committed `b4ca6a6b`) against `git show 20dd871d:` (BASE) and the working tree. Numbers are round 1's.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header keys vs `CARD.md` (read whole) | JOB, LADDER, BRANCH, WORKTREE, BASE, TIP (empty), REPORT (in the worktree), CHECK REPORT, HOUSE B `as needed`, BAND `LOW`, RULINGS `2026-10-18 R1863` all present; `CLASS`, `INSTALL`, `RESTARTS` extra keys, as in round 1 | OK |
| 2 | `git -C /Users/cobalt/cobalt show --stat --oneline 20dd871d` | `20dd871d docs(f5-x3-measure): build report — de976722`, 2 files (report + `.result`) | OK |
| 3 | `grep -n -F "«FILL" <card>` | no output | OK |
| 4 | `git -C … diff HEAD --stat -- <card>` · `git log --oneline -3 -- <card>` | empty diff · `b4ca6a6b`, `3a728b47`, `f6c398ef`: committed, unchanged | OK |
| 5 | `git grep -n … 20dd871d -- configs/cobalt/modelaccess.yaml` | `:70 checkpoint.narrative:` · `:77`, `:79` `# source: UNMEASURED, provisional…` · `:78 timeout_s: 60` · `:80 max_output_tokens: 512`; no `(warm model)`, no `source: X3`. All match the card | OK |
| 6 | `git diff 20dd871d main --stat -- configs tests src ops` | no longer empty: 7 files, all `ops/desk/{deploy-outage,deploy-step0,desk-launch}.sh` and `tests/ops/*` (main moved after round 1). No `configs/`, no `src/`, no `tests/cobalt/`, nothing the card touches; the card's `modelaccess.yaml`, `test_checkpoints_offline.py`, `jobs.yaml`, `start_mainframe.sh` are unchanged (see NOTE 3) | OK |
| 7 | arithmetic: 2 × 3.53 = 7.06; 8.67 + 4.97 = 13.64; × 1.5 = 20.46; max → up to a multiple of 5 = 25; 2 × 59 = 118 → floor 256 | `timeout_s 25`, `max_output_tokens 256`; the card's numbers agree | OK |
| 8 | `grep -n -F "Model loaded successfully" ops/logs/mainframe.log` | `12:Model loaded successfully in 8.67s.` · `31:Model loaded successfully in 5.47s.` — the card now says "both undated lines" | OK |
| 9 | `ops/logs/mainframe.log:58006-58014` (DECISIONS 2) | card text unchanged by the amend (diff shows no DECISIONS edit); round 1 matched it | OK |
| 10 | `grep -n -F -e "lms unload" -e "lms load" ops/start_mainframe.sh` | `:242 lms unload --all`, `:295 lms load … --identifier` (no `--ttl`) | OK |
| 11 | `F5-FINAL-2026-10-11.md` at BASE `:88` `:138` `:177` `:235` | `:88` (`source:` comment, never the voice route's 15 s) · `:138` (contention, measured timeout X3) · `:177` (X3 row) · `:235` (RESTARTS `com.cobalt.aset`): match | OK |
| 12 | `git grep … 20dd871d -- tests/cobalt/test_checkpoints_offline.py` | `:553 def test_route_is_loaded_and_local` · `:558 assert route.timeout_s != 15` | OK |
| 13 | `git grep` symbols at BASE | `jobs/config.py:453 def spec`, `:463 def load_job_registry` · `modelaccess/config.py:31 CONFIG_PATH`, `:150 def load_routes` | OK |
| 14 | `git grep … 20dd871d -- configs/cobalt/jobs.yaml` | `:86` aset reads `modelaccess.yaml` · `:102 com.cobalt.mainframe` · checkpoint rows `timeout_s: 300` at `:261,268,275,282` · comment `:256` ("provisional 60 s plus two 30 s"). 300 > 25 + 60 | OK |
| 15 | `test_modelaccess_config.py:69-80`, `test_checkpoints_registry.py:17-27` | unchanged by the amend (the card diff touches no line number); round 1 matched | OK |
| 16 | `grep -n -F "UNMEASURED" "docs/40 - DevDocs/cobalt/prefill/checkpoints.md"` | `:19` holds the sentence the one dated line supersedes | OK |
| 17 | commands the builder needs vs `BUILD-HUB.md:14` | `Read`, `Edit` in the worktree, `grep *`, `uv run pytest *`, `uv run cobalt jobs restarts *`, `git add/commit/diff/log/show`, `sh …/ops/desk/*`; no `lms`, `launchctl` or `curl` in the card's builder steps | OK |
| 18 | DEPLOY PROOF lines 60–63 vs `ops/desk/deploy-smoke.sh:246-285` (`aft=${tail_##* · after }`, `value_is` `:209-224`) | lines 60–63 each end `· after `N`` with nothing after the closing backtick (`0`, `2`, `1`, `1`); `aft` = the whole backticked value → `value_is` takes the backtick branch, no RED of the round-1 kind. The parentheticals moved to `## RECORDS` (first line) | OK |
| 19 | marker counts vs the file | `source: UNMEASURED` 2 → 0, `# source: X3 reports/f5-x3-measure-2026-10-20.md` 0 → 2, `(warm model)` 0 → 1 (T2), `cold load 8.67 s … (proxy, not a live cold call)` 0 → 1 (T1); the amend changed none of the strings or counts | OK |
| 20 | smoke reads (`deploy-smoke.sh` shapes) · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` | `curl … 127.0.0.1:5010/` and `ls` are mapped shapes, lines 64–65 unchanged; the plist is on disk (`ls` exit 0) | OK |
| 21 | T1, T2, X2 agree on what the new test spells | T1: "asserts invariants only … never spells 25 or 256"; T2: "`int` and a multiple of 64 (no floor spelled in the test; the rule's floor of 256 is held by the value in the file, not by the test)"; X2: "no 25, no 256 spelled". `>= 256` and `no 10` gone; the three agree | OK |
| 22 | `grep -n -e RULINGS -e "BAND must" ops/desk/desk-launch.sh` | `:1312` needs JOB…RULINGS, `:1320`–`:1331` RULINGS `<date> R<n>`, `:1955` BAND LOW/MID/HIGH; the card passes both. `## GATE` is the desk's (no launcher grep). `desk-launch.sh` changed on main since round 1, the checked shapes did not | OK |
| 23 | scope fences | rows touch only `modelaccess.yaml`, `test_checkpoints_offline.py`, `prefill/checkpoints.md`; no `src/`, plist, `jobs.yaml`, `ops/` | OK |
| 24 | `git diff 3a728b47 b4ca6a6b -- <card>` (ordered) | 4 hunks: T2 clause, COLD "both 2026-09-09" → "both undated lines", X2 `no 10` → `no 25`, DEPLOY PROOF lines 62–63 trailing text removed, plus one added `## RECORDS` line. No `file:line` and no count changed; every changed number is text (25/256/10), not an anchor | OK |
| 25 | card committed, empty diff against HEAD | `git diff HEAD --stat -- <card>` empty (check 4) | OK |

## ISSUES

- NOTE (round-1 NOTE 1, stays a NOTE): `mainframe.log:12` and `:31` carry no date; line 12 loads `qwen3.8-27b`. The card now says "undated lines". The proxy is a load time from an old log, not a live cold call (the source comment says so).
- NOTE (round-1 NOTE 2, stays a NOTE): `configs/cobalt/jobs.yaml:256` still says "above the route's provisional 60 s" and `tests/cobalt/test_checkpoints_registry.py:23` says "UNMEASURED". The card fences both; the stale text stays after this job. 300 s is still above 25 + 60.
- NOTE 3: main moved past BASE after round 1 (7 files under `ops/desk/` and `tests/ops/`). None are the card's files, so BASE stays; DECISIONS 5's "diff empty" sentence is true only of the `de976722` range it names. The builder branches from `20dd871d`, not main, so those ops files are not in its worktree; the deploy merges them as main's.
- NOTE 4: the build waits on the 945 check (`f5-x3-measure-check-2026-10-20.md`, last line `CHECK DONE · … ready: YES`) by design, not a block of the card. If the check moves the tip, set BASE first (`## GATE`).
- Nothing blocks the build.

PREFLIGHT DONE · card: f5-x3-values · checks: 25 · fails: 0 · ready: YES
