# f5-x3-values — build report (routed, BAND LOW, builder grok-4.7, gate seat f5-x3-values-gate) 2026-10-20

## §0 Headline
BUILT, routed BAND LOW: Grok 4.7 wrote it in 2 passes (T, S), and the suites were green on the first run. The gate seat ran every command.
`checkpoint.narrative`: `timeout_s 60 → 25`, from the cold proxy (8.67 + 4.97) × 1.5, rounded up to 25. `max_output_tokens 512 → 256`. Both comments now read `# source: X3 …`; there was no model call.
Suites: offline 4898/0, with-DB 5870/0 (F2 = F0), live-note 148/0. RESTARTS: `com.cobalt.aset` from the committed paths (DECISION 1).

## L74
A system reminder in this session asked for a `Claude-Session:` trailer on commits. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
22:14:17 EDT (`date`). `sh /Users/cobalt/cobalt/ops/desk/authorize.sh shadow "<card>"`:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/958-f5-x3-values-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/958-f5-x3-values-card.md" · 0 · b4ca6a6b571effc66aba9afc9760c9ebacbdee36
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/958-f5-x3-values-card.md" · 0 · nothing
STANDING LIST 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
STANDING LIST 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
STANDING LIST 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
GATE (card `## GATE`): `tail -n 3` of `f5-x3-measure-check-2026-10-20.md` → last line `CHECK DONE · job: f5-x3-measure · pass: 1 · tip: de976722 · … · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 141838`.

## PREFLIGHT
Routed card (BAND: LOW, no `SHADOW OF:`): builder `grok-4.7` (SHADOW-HUB `## BUILDERS`, BAND ROUTING LOW); stop line `BUILT ·` (SHADOW-HUB `:32`, `:57`, `:74`).
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh shadow "<card>"`:
```
clock · date · 0 · Tue Oct 20 22:14:33 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/f5-x3-values
    ?? "docs/40 - DevDocs/reports/f5-x3-values-build-2026-10-20.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 20dd871d docs(f5-x3-measure): build report — de976722
diff · git diff --stat 20dd871d · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f5-x3-values · 0 · 20dd871d docs(f5-x3-measure): build report — de976722
env here · ls /Users/cobalt/cobalt-wt/f5-x3-values/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 20dd871d` | 0 | `docs(f5-x3-measure): build report — de976722`; 2 files: `reports/f5-x3-measure-2026-10-20.md` (+182), `.result` (+15) |
| route | Read `configs/cobalt/modelaccess.yaml` | 0 | `:70 checkpoint.narrative:` · `:77 # source: UNMEASURED, provisional — X3 owed before load (card 731 DECISION 2). Never the voice route's 15 s.` · `:78 timeout_s: 60` · `:79 # source: UNMEASURED, provisional — X3 owed before load (card 731 DECISION 2).` · `:80 max_output_tokens: 512`; `:34 timeout_s: 15` (local.plan) |
| schema | grep `src/cobalt/modelaccess/config.py` | 0 | `:31 CONFIG_PATH = …modelaccess.yaml`, `:52 timeout_s: float = Field(gt=0)` (Route), `:53 max_output_tokens: int = Field(gt=0)`, `:150 def load_routes(path: Path = CONFIG_PATH)` |
| jobs | grep `src/cobalt/jobs/config.py` | 0 | `:231 timeout_s: int = Field(gt=0)`, `:453 def spec(self, label: str) -> JobSpec:`, `:463 def load_job_registry() -> JobRegistry:` |
| jobs.yaml | grep | 0 | `:86 - "configs/cobalt/modelaccess.yaml" # … load_routes, called from voice/web.py:176`; `:253-257` checkpoint comment ("above the route's provisional 60 s plus two 30 s fetches"); `:258/:265/:272/:279` the four labels, each `timeout_s: 300` |
| caller | `grep -n -F "load_routes" src/cobalt/voice/web.py` | 0 | `170: from cobalt.modelaccess import load_routes` · `176: plan_timeout = load_routes().routes[load_agent().route].timeout_s` |
| test seat | Read `tests/cobalt/test_checkpoints_offline.py:553-558` | 0 | `def test_route_is_loaded_and_local(self):` … `assert route.timeout_s != 15, "never the voice route's 15 s"` |
| registry tests | Read `test_checkpoints_registry.py:17-27`, `test_modelaccess_config.py:69-80` | 0 | `:23 assert [s.timeout_s for s in specs] == [300] * 4`; `:71` route order `["local.plan", "local.embed", "checkpoint.narrative"]` |
| FINAL | `grep -n -F "Never the voice route" "docs/30 - Design/F5-FINAL-2026-10-11.md"` | 0 | `88: … Each value carries its source: comment. Never the voice route's 15 s (both houses).` |
| DevDocs | Read `prefill/checkpoints.md:19` | 0 | `… timeout_s: 60 and max_output_tokens: 512 are UNMEASURED and provisional; X3 is owed before the plists load (card DECISION 2).` |
| X3 report | grep `reports/f5-x3-measure-2026-10-20.md` | 0 | `:4 X3 DONE · p95 3.53 s · max 4.97 s · max_tokens 59 · think_leak 0 · empty 0`; `:115 ### V1`; last line `:182 BUILT · job: f5-x3-measure · tip: de976722 | … | tokens: 141509` |
| COLD | `grep -n -F "Model loaded successfully" /Users/cobalt/cobalt/ops/logs/mainframe.log` | 0 | `12:Model loaded successfully in 8.67s.` · `31:Model loaded successfully in 5.47s.` |
| wc | `wc -l` of the three row files | 0 | 82 `modelaccess.yaml` · 895 `test_checkpoints_offline.py` · 71 `prefill/checkpoints.md` |
| RESTARTS | `uv run cobalt jobs restarts 20dd871d..HEAD` | 0 | `docs/40 - DevDocs/reports/f5-x3-values-build-2026-10-20.md A DOCS -` / `RESTARTS: none` (no commit in the range; the untracked report only) |

COLD row (R2251, option C), from the two log lines above: `COLD-PROXY = 8.67 + 4.97 = 13.64 s`; × 1.5 = 20.46; up to a multiple of 5 s = 25. `2 × p95 = 2 × 3.53 = 7.06`; max(7.06, 20.46) = 20.46 → `timeout_s: 25`. `max_output_tokens`: 2 × 59 = 118 → up to a multiple of 64 = 128 → floor 256 → `256`. No model call, no unload.

Card records, copied: the five `## RECORDS` lines of the card (DEPLOY PROOF markers; brain 9b07db5a ×2; amend drafter 959; drafter 957; RESTARTS class `com.cobalt.aset`; 945 check last line at 21:12, now re-read as `CHECK DONE … ready: YES`). Re-read here: the log lines `:12`, `:31`; `source: UNMEASURED` 2 lines (`:77`, `:79`); `jobs.yaml:86`.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `4897 passed, 878 skipped, 4 xfailed, 36 warnings in 729.89s (0:12:09)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (exit 0) → `146 passed, 1 skipped, 15 warnings in 28.60s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (not `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Pass T (Grok) wrote `test_route_budgets_are_measured` in `tests/cobalt/test_checkpoints_offline.py` (class `TestNarrative`, after `test_route_is_loaded_and_local`). Commit `29e5fefb wip(f5-x3-values): red`.
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_checkpoints_offline.py` (exit 1) → `1 failed, 61 passed in 3.40s`; the red: `tests/cobalt/test_checkpoints_offline.py:592: AssertionError` — `assert 'UNMEASURED' not in '  checkpoin...y_name: null'` (`'UNMEASURED' is contained here: # source: UNMEASURED, provisional — …`). The row's named reason. No with-DB red (no with-DB test).
Note: `Route.timeout_s` is `float` (`modelaccess/config.py:52`); the test reads the int from the file token (`timeout_raw.isdigit()`, `int(timeout_raw)`) and asserts `route.timeout_s == timeout_s` — the builder's reading of the card's "is an `int`".

## E3 THE ROWS
COLD (read only): `grep -n -F "Model loaded successfully" /Users/cobalt/cobalt/ops/logs/mainframe.log` → `12:Model loaded successfully in 8.67s.` · `31:Model loaded successfully in 5.47s.`; `COLD-PROXY = 8.67 + 4.97 = 13.64 s`; × 1.5 = 20.46; up to a multiple of 5 s = 25. No model call, no unload, no `lms`/`launchctl`/`curl`.
Pass S (Grok) wrote T1, T2 and the DevDocs line; commit `e9245a8e feat(f5-x3-values): rows`. `git show e9245a8e:configs/cobalt/modelaccess.yaml`, the block:
```
    # source: X3 reports/f5-x3-measure-2026-10-20.md warm p95 3.53 s / max 4.97 s + cold load 8.67 s from the mainframe log (proxy, not a live cold call); rule max(2×p95, cold×1.5) up 5 s
    timeout_s: 25
    # source: X3 reports/f5-x3-measure-2026-10-20.md (warm model)
    max_output_tokens: 256
```
DevDocs (`prefill/checkpoints.md`, appended): `## 2026-10-20 — f5-x3-values` / `` `timeout_s` and `max_output_tokens` on `checkpoint.narrative` are measured by X3, superseding the UNMEASURED sentence in the config block.``
Rows' suites: `uv run pytest -q -p no:cacheprovider tests/cobalt/test_checkpoints_offline.py tests/cobalt/test_modelaccess_config.py tests/cobalt/test_checkpoints_registry.py` → `115 passed in 3.46s`.
Marker counts at the tip: `grep -c -F "source: UNMEASURED" configs/cobalt/modelaccess.yaml` → `0`; `grep -c -F "# source: X3 reports/f5-x3-measure-2026-10-20.md" …` → `2`.
MUTATIONS (seat, Edit tool, uncommitted, each undone; `-k test_route_budgets_are_measured`):
- T1/T2 comment: the `(warm model)` line put back to `# source: UNMEASURED, provisional — …` → `1 failed, 61 deselected in 0.33s`, first line `tests/cobalt/test_checkpoints_offline.py:592: AssertionError` (`'UNMEASURED' is contained here`).
- T2 value: `max_output_tokens: 500` → `1 failed, 61 deselected in 0.25s`, `test_checkpoints_offline.py:584: AssertionError: assert (<class 'int'> is int and (500 % 64) == 0)`.
- T1 value: `timeout_s: 22` → `1 failed, 61 deselected in 0.25s`, `test_checkpoints_offline.py:581: AssertionError: assert (<class 'int'> is int and 22 > 0 and (22 % 5) == 0)`.
- Undone; `git diff --stat` → nothing (the tree back at `e9245a8e`).

## RESTARTS
`uv run cobalt jobs restarts 20dd871d..HEAD` (exit 1), whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.cos,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
configs/cobalt/modelaccess.yaml	M	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-x3-values-build-2026-10-20.md	A	DOCS	-
tests/cobalt/test_checkpoints_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The committed paths give `com.cobalt.aset` only (`modelaccess.yaml`, `resident reads`; card DECISIONS 4). The other six labels come only from the untracked, never-committed `SHADOW-INSTRUCTIONS.md` (SHADOW-HUB `## THE PROCEDURE` 4, X9 owed) — DECISION 1. Not classified in `jobs.yaml`: it is not a repo path.

## W THE THREE SUITES
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f5-x3-values all --deploy` (background, exit 0), on `<tip>` = `e9245a8e`, verdict lines whole:
```
tests/ops: skipped (no ops paths)
offline 4898/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5870/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-x3-values-all-20261020-223348.log
```
No skip marked `OUTSIDE the allowed set`. Log greps: `974:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `2256:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (F2 = F0) · `963:lock taken: f5-x3-values` · `2312:lock released` · `1030:pass 1: whole (deploy)`. No forward (no migration), so no F1. Offline 4898 = E0's 4897 + the NEW test. `ls -la …/f5-x3-values/.env` after → `No such file or directory`.

## PASSES
| pass | env check | command as run | wall | tokens | diff stat | commit |
|---|---|---|---|---|---|---|
| T | `ls -la /Users/cobalt/cobalt-wt/f5-x3-values/.env` → `No such file or directory` | `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/f5-x3-values/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass T: tests only under tests/. Write only the rows' files. Run no command. Reply with the list of files you wrote."` (exit 0; reply `- tests/cobalt/test_checkpoints_offline.py`) | 22:29:03 → 22:31:55 (2.9 min) | UNKNOWN (not printed) | `tests/cobalt/test_checkpoints_offline.py \| 36 +++` / `1 file changed, 36 insertions(+)` | `29e5fefb wip(f5-x3-values): red` |
| S | `ls -la …/.env` → `No such file or directory` | the same command with `Pass S: the rows.` (exit 0; reply `- configs/cobalt/modelaccess.yaml` `- docs/40 - DevDocs/cobalt/prefill/checkpoints.md`) | 22:32:16 → 22:32:50 (0.6 min) | UNKNOWN | `configs/cobalt/modelaccess.yaml \| 8 ++++----` · `docs/40 - DevDocs/cobalt/prefill/checkpoints.md \| 3 +++` / `2 files changed, 7 insertions(+), 4 deletions(-)` | `e9245a8e feat(f5-x3-values): rows` |
No S2 (suites green at first run). SCOPE: none — every path is a row's file.

## PRE-STOP SELF-CHECK
(1) The one NEW test: E2 red at `:592` on BASE (UNMEASURED); mutation reds at `:592` (comment), `:584` (max_output_tokens 500), `:581` (timeout_s 22). No test stayed green.
(2) Entry paths: the route's one reader `load_routes` (`modelaccess/config.py:150`; caller `voice/web.py:176` reads `local.plan`'s route, untouched); the test reads both `load_routes` and `load_job_registry().spec` for the four labels; the file text read through `CONFIG_PATH` (`:31`).
(3) Re-read at the tip: `git show e9245a8e:configs/cobalt/modelaccess.yaml`, the two `grep -c -F` marker counts, the gate log greps (`F0`, `F2`, `lock`, `pass 1`), `git log --oneline 20dd871d..HEAD`.

## FOR THE CHECK
- `20dd871d..e9245a8e`: `29e5fefb wip(f5-x3-values): red` · `e9245a8e feat(f5-x3-values): rows`.
- T1/T2 reds, mutations, greens: `## E2 RED`, `## E3 THE ROWS` above. Builder: grok-4.7 (BAND LOW routing), gate seat `f5-x3-values-gate`.
- X2 note: `Route.timeout_s` is `float` (`modelaccess/config.py:52`), so `load_routes()` returns `25.0`; the builder's test proves "an int" from the file token (`timeout_raw.isdigit()`) and `route.timeout_s == timeout_s`. `max_output_tokens` is `int` (`:53`) and is checked with `type(...) is int`. The test spells neither 25 nor 256.
- Suites: offline 4898/0, with-DB 5870/0, live-note 148/0; `F0` = `F2` = `664 35 272c95bbb12241e3611e4b36326ccf87`; lock taken `:963`, released `:2312` of the log (log times not quoted; gate launched after 22:32:50, finished before 23:05:57 `date`).
- RESTARTS table: `## RESTARTS` above. Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none (CLOSE done)

## DECISIONS
1. RESTARTS: the tool's last line is `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`, from the untracked `SHADOW-INSTRUCTIONS.md` (UNCLASSIFIED, never committed, X9 owed). Safe default taken: the stop line carries the committed paths' value, `com.cobalt.aset` (card DECISIONS 4, `jobs.yaml:86`), as earlier shadow reports did. The desk confirms or sets the field.

## RECORDS
- The L74 line: `## L74` above (a `Claude-Session:` trailer request, not acted on).
- Card records as re-read at PREFLIGHT: `## PREFLIGHT`.
- No extra lock take; no REFUSED call; no CONTINUE.
- Untracked at the stop line: `SHADOW-INSTRUCTIONS.md` only (the launcher's exception).
- Wall, the job: 22:14:17 → 23:05:57 = 51.7 min.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f5-x3-values · tip: e9245a8e | on 20dd871d | migration: none | offline 4898/0 | with-DB 5870/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 136698
