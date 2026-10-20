# f5-x3-measure preflight r2 — card 945 — 2026-10-20 (18:12 EDT)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --short=8 main` | `10eb6f66`; BASE `5347f90e` trails by desk commits only; TIP empty (expected) | OK |
| 2 | `git diff HEAD --stat -- <card 945>` | empty (card committed; the card text read is the text at `main`) | OK |
| 3 | header: JOB f5-x3-measure, LADDER OFF-LADDER R2217, CLASS K2, INSTALL none, BRANCH, WORKTREE, REPORT, CHECK REPORT, BAND HIGH, RESTARTS none | all present; `cto-2026-10-20.md:25` R2217 `DESK RECORD (brain, L79): X3 = K2 probe …` | OK |
| 4 | RULINGS `2026-10-18 R1863` | `cto-2026-10-18.md:90` `HIS RULING · APPROVED` | OK |
| 5 | `git show main:configs/cobalt/modelaccess.yaml`: `checkpoint.narrative`, `timeout_s: 60`, `max_output_tokens: 512`, `# source: UNMEASURED` x2, api_base `127.0.0.1:1234/v1`, model `mainframe`, `no_think`, `forbid_nonempty`, `json_schema` | match (route at `:70`, values at `:78`, `:80`; read by content) | OK |
| 6 | `configs/cobalt/prefill.yaml` | `:38 route: checkpoint.narrative`, `:39 narrative_max_lines: 3` | OK |
| 7 | `checkpoints.py` grep | `WRITER :91`, `PHRASES :115`, `parse_groups :200`, `compute_delta :283`, `_response_schema :394`, `_SYSTEM :405`, `narrate :413` | OK |
| 8 | `client.py` / `config.py` grep | `call_sync :89`, lowering `:99-102`, `think_leak :73/:79/:83`, `empty :85`, `output_tokens :159`, `latency_ms :160` (perf_counter), `ModelAccessConfig :132`, `load_routes :150` | OK |
| 9 | `test_checkpoints_offline.py` grep | `groups_csv :65`, `figures :75`, `IDX_0745 :393`, `IDX_0815 :394`, `ENTRIES :470` | OK |
| 10 | **FAIL 10 re-proof** `git show main:tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` | marker line `# synthetic shape — X2 real capture owed before load`, header line, 11 rows = 13 lines; the card's READ now says "13 lines at BASE (line 1 marker …, line 2 header, 11 rows)" | OK |
| 11 | F5-FINAL `:177` X3, `:88`, `:138` | match the card's quotes | OK |
| 12 | **FAIL 13 re-proof** BUILD-HUB `:14` allow list vs the commands the card gives the builder: `uv run pytest -q -rP tests/cobalt/test_x3_calls_scratch.py` (`Bash(uv run pytest *)`), `date` (`date*`), `sh /Users/cobalt/cobalt/ops/desk/scratch-clean.sh "<path>"` (`sh …/ops/desk/*`), `git status`, `git diff <BASE>..HEAD --stat`, `uv run cobalt jobs restarts <BASE>..HEAD`, `ls` | every one on the list; no `uv run python`, `cat`, `mkdir`, `rm`, `curl` | OK |
| 13 | BUILD-HUB `:70` | "Write each row's `red first` test and each RUN row's test … A RUN row's command (`-rP` …) → quote WHOLE; it asserts nothing" — the builder writing the RUN test is sanctioned | OK |
| 14 | BUILD-HUB `:26` | "Long runs `run_in_background`, read whole" — background run sanctioned (card gives the 600 s foreground reason) | OK |
| 15 | BUILD-HUB `:72` + `ops/desk/scratch-clean.sh` | "A stray scratch path in the worktree is removed with `sh …/scratch-clean.sh "<path>"`"; the script accepts `$WT/<name>/…` of a registered worktree when the path is wholly untracked (`?? `) — so the test must never be `git add`ed; the card says so. `tests/ops/test_build_hub_no_clutter.py:18-19,47-48` pin the `:72` text | OK |
| 16 | `git grep -F x3_calls main` | only job docs (card 945, prompt 948, drafts, round-1 report); no test, no code reads the name | OK |
| 17 | lifted timeout restored: the lift is a `ModelAccessConfig` copy in the process; `configs/cobalt/modelaccess.yaml` is not edited (ROWS, NOT IN THIS JOB, X1); C1 runs `git status` and `git diff <BASE>..HEAD --stat`; `git status --short -- configs/cobalt/modelaccess.yaml` now empty | nothing left changed at the stop line | OK |
| 18 | no plist load, no production write: NOT IN THIS JOB bars plists, `jobs.yaml`, any database, any production command; only calls are the 30 to `127.0.0.1:1234` | holds | OK |
| 19 | time gate: `date` (admitted, `date*`) before R1 and before the first call, 20:35–07:00 ET; stop lines `FAILED: X3 — outside the 20:35–07:00 window (<date output>)`, `FAILED: X3 — window closed after <n> of 30 calls`, `X3 DONE · p95 … · think_leak <n> · empty <n>`, `FAILED: X3 — mainframe unreachable …` | present and checkable; `date` now `Tue Oct 20 18:12:15 EDT 2026`, so a build now would stop on the gate | OK |
| 20 | values rule: card V1 and `## RECORDS` `VALUES CARD RULE` | same formula (`max(2×p95, max)` up to 5 s; p95 ≥ 55 s → measured; tokens `2×max` up to 64, floor 256; `# source: X3 reports/f5-x3-measure-2026-10-20.md`; `think_leak`/`empty` > 0 → HELD) | OK |
| 21 | RESTARTS `none` (docs only; report is the only file) | consistent with card 912 R1 | OK |
| 22 | note 3, background run: R1 text, DECISION 1 | run_in_background, wait for notice, read whole, no re-run | OK |
| 23 | note 4, `figures()` shape: R1 names `figures()`; `test_checkpoints_offline.py:71-79` | `figures(indices, sectors)` -> `{"indices": {t: {price, change_pct}}, "sectors": {name: {change, rel_volume "1.00", perf_week "0.50"}}}`; `sectors` is a `{name: change-string}` dict | OK |
| 24 | note 5, desk launches after 20:35 ET: TIME GATE | "the hub launches it at or after 20:35 ET and it ends before 07:00"; desk next step `cto-2026-10-20.md:120` says the same | OK |
| 25 | stale `## RECORDS` lines about the desk-staged `/tmp` script (amend report names "Admitted strings" and "How a probe reaches the route") | see NOTE 1 | OK (note) |
| 26 | tests/cobalt autouse fixtures vs the scratch test location (`tests/cobalt/conftest.py`) | see NOTES 2, 3; neither blocks | OK (note) |

## ISSUES
- NOTE 1: card `## RECORDS` still says `uv run pytest /tmp/…` ("Admitted strings" line) and "the script's self-removal is the desk's staging" (NOT TRACED line); DECISION 1 says the staged script is DROPPED and names the in-worktree path. A builder reading RECORDS first could look for a `/tmp` file and find none; DECISION 1 and R1 are explicit and the builder cannot write outside `Edit(//Users/cobalt/cobalt-wt/**)` anyway, so risk is low. Strike the two lines at the next amend if one comes; no block.
- NOTE 2: BUILD-HUB `:72` first sentence says a RUN probe is "staged outside the worktree"; the card puts it in the worktree at `tests/cobalt/…`. `:70` ("Write … each RUN row's test") and `:72` last sentence (scratch-clean of a worktree path) admit it, and the builder's Write is limited to the worktree glob, so this is the only writable place. Not a block.
- NOTE 3: `tests/cobalt/conftest.py` autouse fixtures apply to the scratch test: `frozen_session_clock` freezes `cobalt.session.clock.now_utc` to 2026-09-03 14:00 UTC, so the in-test 07:00 gate must read the real wall clock (`datetime.now(ZoneInfo("America/New_York"))`), never `now_utc`; `dev_env` pins `COBALT_ENV=dev`; `dev_db_tx` opens `cobalt_dev` (rolled back) only if `POSTGRES_HOST` and `POSTGRES_USER` are set, otherwise it is a no-op — the builder has no `.env` copied, so no database is reached, as DECISION 1 says.
- NOTE 4: `parse_groups` (`:200`) returns name -> row dict, while `figures()` takes `{name: change-string}`; R1 sends the builder to `figures()`, so it builds the `Change` map from the parsed rows. Fine for a builder.
- NOTE 5: now 18:12 ET; a build launched before 20:35 ET stops on the gate. The desk's own plan already launches at or after 20:35.
- Blocks the card's own build: nothing.

PREFLIGHT DONE · card: f5-x3-measure · checks: 26 · fails: 0 · ready: YES
