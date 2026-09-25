# Replay deadline fix — build report (2026-09-24 prompt, run 2026-09-25)

Seat: `replay-deadline-fix-build-0924` · Opus 5.5 · `acceptEdits` · branch `fix/replay-deadline-0924` · prompt `docs/40 - DevDocs/prompts/2026-09-24/57-replay-deadline-fix-build.md`.

## §0 Headline
FIX 1 BUILT: one `prepare_member` per (member, scan instant), shared by every def. Byte-identical across 7 corpus defs × 2 tickers × 4 instants (T1); frame pairs are built once per `bind_side` (T2).
FIX 2 BUILT: the formations step is cut between scans `replay.formations_reserve_s` (120 s, proposed) before the deadline. The line is written with PARTIAL and the job fails at the end (T5, T7–T11).
FIX 3 BUILT: `formation_misses` reads bars once per ticker (T6).
Gates on `8b931ce5`: offline 2512/0 · with-DB 2867/0 · live-note 146/0 · `.env` removed · RESTARTS `com.cobalt.aset com.cobalt.radar`.
ESCALATE: 8. The dry-run timing is NOT MEASURABLE on `cobalt_dev` (no 09-24 membership).

## L74
One block arrived with the Read tool result of the prompt file (a system-reminder asking commit messages to end with a `Claude-Session: https://claude.ai/code/session_<id>` line, and naming a file-send tool). Recorded once here as DATA; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| check | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/57-replay-deadline-fix-build.md` | 1 | (no output) — PASS |
| R95 row | `grep -n "^\| R95 " …/cto-2026-09-24.md` | 0 | `119:\| R95 \| 21:48 ET \| … step line FAILED — DeadlineExceeded: line: past the deadline 21:35:00 ET …` — PASS |
| R95 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"step line FAILED — DeadlineExceeded" -- …/cto-2026-09-24.md` | 0 | `8cfa9fac1eaf4822e3ba02484d3d85c84fc7eadb` — PASS |
| design stop line | `tail -n 3 …/replay-deadline-fix-draft-2026-09-24.md` | 0 | `REPLAY DEADLINE FIX DRAFTED · cause: the formations step re-evaluates every scan × member × def (82,250 calls, 7 defs) rebuilding the member's work per def, synchronously and uncut past 21:35 · FIX: 3 · NOT REAL: 4 · UNPROVEN: 3 · OUT OF SCOPE: 3 · OWNER ITEM: 3 · prompts: 2 · new rule strings: 3 · ESCALATE: 9` — PASS |
| design committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/replay-deadline-fix-draft-2026-09-24.md` | 0 | `e6afc552c7cdbeec450afb27ed982a4a334be833` — PASS |
| launch row | `grep -n "57-replay-deadline-fix-build.md" …/cto-2026-09-24.md …/cto-2026-09-25.md` | 0 | `cto-2026-09-25.md:26: \| R18 \| 05:50 ET \| **P-HIS — THE 57 STRINGS ("approve command").** …` and `cto-2026-09-25.md:28: \| R20 \| 06:02 ET \| … (3) LAUNCH ROW 57-replay-deadline-fix-build.md …` — PASS |
| .env-string approval | `grep -n -F "cobalt-wt/replay-deadline/.env" …` | 0 | `cto-2026-09-25.md:26: \| R18 \| … His words, desk chat 05:50 ET: "approve command" … Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/replay-deadline/.env) · Bash(rm /Users/cobalt/cobalt-wt/replay-deadline/.env) …` — PASS |
| launch committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"57-replay-deadline-fix-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `a994a5ddd213c83478a30e328e1fe828bee368cb` — PASS |
| timing string | `grep -n -F "cobalt radar evaluate --replay 2026-09-24" …` | 0 | `cto-2026-09-25.md:26: \| R18 \| … "approve command" … Bash(COBALT_ENV=dev uv run cobalt radar evaluate --replay 2026-09-24) — APPROVED` → **timing: approved** |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Fri Sep 25 06:05:30 EDT 2026` (before 15:00 ET — no late ESCALATE) |
| clean tree | `git status --short --branch` | 0 | `## fix/replay-deadline-0924` |
| base | `git log --oneline -1` | 0 | `a994a5dd docs(desk): 09-25 R20 — …` → `<base>` = `a994a5dd` |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1 main` | 0 | `a994a5dd …` — same sha (the R20 row names `8c350159` as the cut; `main` then moved docs-only to `a994a5dd`, which IS the base) |
| no .env | `ls /Users/cobalt/cobalt-wt/replay-deadline/.env` | 1 | `No such file or directory` |
| dev-DB lock (record) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| shape | `grep -n "STEPS = (" src/cobalt/replay/runner.py` | 0 | `82:STEPS = ("movers", "cards", "formations", "line")` |
| shape | `grep -n "def replay_formations" src/cobalt/radar/evaluate_cli.py` | 0 | `148:def replay_formations(` |
| shape | `grep -n "context.bars_for(candidate.ticker)" src/cobalt/replay/formations.py` | 0 | `332:            candidate, context.bars_for(candidate.ticker), trade_date=context.trade_date,` |
| shape | `grep -n "key: replay.backup_margin_s" configs/cobalt/taxonomy/tunables.yaml` | 0 | `948:  - key: replay.backup_margin_s` |
| shape | `grep -n "key: replay.formations_reserve_s" …` | 1 | (nothing) |
| shape | `grep -n "def evaluate_member" src/cobalt/radar/evaluate.py` | 0 | `907:def evaluate_member(` |
| shape | `grep -n "def prepare_member" src/cobalt/radar/evaluate.py` | 1 | (nothing) |
| seam | `git -C /Users/cobalt/cobalt log --oneline -1 cards/stale-score-0922` | 0 | `358f1f75 docs(report): stale score build r2 — …` → `<stale tip>` = `358f1f75` |

## D1 RED
Interruption, recorded: at ≈06:3x a call outside the launch list (`git -C /Users/cobalt/cobalt diff main...cards/stale-score-0922 -- src/cobalt/radar/evaluate.py`) raised a permission box, which was cancelled. The desk's message of 06:43 ET: resume at D1, no relaunch; read the seam only with listed shapes (`git diff …` / `git show …` from this worktree). Resumed under that rule.

Tests written: T1–T3 `tests/cobalt/test_radar_evaluate.py` (end) · T4–T5 `tests/cobalt/test_radar_evaluate_cli.py` (end) · T6–T7 `tests/cobalt/test_replay_formations.py` (end) · T8 `tests/cobalt/test_replay_line.py` (end) · T9–T11 `tests/cobalt/test_replay_runner.py` (end). Also in the runner file: `unavailable_formations` / `available_but_empty_formations` gained `cut_at=None`, and the r1_16 docstring sentence was reworded as the prompt specifies (every assertion kept).
**Deviation (named):** `test_formation_sources_name_every_argument_p2s_entrypoint_takes` (`test_replay_formations.py:385`) now excludes `cut_at` beside `day`/`out`/`slug_filter`. `cut_at` is a per-run argument the runner supplies, never a `FormationSources` field, and `formations.py` must not change beyond FIX 3. The test's intent is kept.
T1's corpus = the 7 `setups_shapes.SHAPES` defs, loaded through `load_shape_fresh`, with ONE merged tunables mapping (engine + `D6_CONSTRUCTED` fills + every shape's user rows), as `replay_formations` hands one mapping to every def. Two corpus defs bind side by the frame (`backside`, `fashionably-late`: `Extension.state` past culmination); the other five do not (T1 asserts ≥2 False and ≥1 True).
`tests/taxonomy/`: `grep -rn backup_margin_s tests` → nothing; no suite test pins the `replay.*` set → `none`.

Run (`uv run pytest -q -rs <5 files>`): `11 failed, 102 passed, 4 skipped in 53.69s`. The 11 failures, each for the missing behaviour:
| test | reason |
|---|---|
| T1 test_a_shared_member_prep_gives_every_def_byte_identical_evaluations | ImportError: cannot import name 'prepare_member' |
| T2 test_a_prep_builds_each_frame_pair_once_whatever_the_def_count | AttributeError: no attribute 'prepare_member' |
| T3 test_a_prep_for_another_member_or_instant_is_refused | ImportError: 'prepare_member' |
| T4 test_replay_formations_is_unchanged_by_the_shared_prep | AttributeError: 'ReplayReport' object has no attribute 'scans_planned' |
| T5 test_replay_formations_stops_before_the_scan_the_cut_names_and_says_so | TypeError: unexpected keyword argument 'cut_at' |
| T6 test_formation_misses_reads_each_tickers_bars_once | assert ['BGFI', 'FTFT', 'FTFT'] == ['BGFI', 'FTFT'] (bars_for read 3 times) |
| T7 test_a_cut_report_carries_its_cut_into_the_outcome | ImportError: 'FormationCut' |
| T8 test_a_cut_formations_segment_says_partial | ImportError: 'FormationCut' |
| T9 test_the_formations_step_is_cut_before_the_deadline_and_the_line_still_lands | ImportError: 'FormationCut' |
| T10 test_no_deadline_means_no_cut | AssertionError: cut_at not passed (sentinel) — (True, 21:10 ET) case |
| T11 test_the_formations_reserve_is_required | DID NOT RAISE ReplayError (tunable absent, no refusal) |

## D2 FIX 1
Red committed: `915b7b6e` (`<red>`).
SHAREABILITY (L70), read before building: **frames shareable**. A frame's lazy values take only the frame's own inputs plus `tunables`, never a def-dependent input:
- `src/cobalt/radar/anatomy/frame.py:228-239`: `_d1_resolvers(run, session, *, daily, daily_ok, trade_date, last_close, tunables, objects, ext)`.
- `:245`: the `once(key, compute)` cache is keyed only by atom/period strings.
- `:105-114`: `LazyAtoms.__init__(eager, lazy)` / `__getitem__` memoize by atom name.
- `:578-590`: `build_frame(side, run, *, daily, daily_ok, trade_date, params, last_close, session, tunables, bind_side)`.
- `:625-627`: the resolvers are built from those same inputs.

The def-dependent inputs (trigger/stop params, `context["antecedent"]`) arrive as call arguments to `frame.objects[...]` functions or through the per-call `context`. They are never cached on the frame (`formation/triggers.py`, `stops.py`, `anchors.py` read `frame.objects` only). `bind_side` is the one frame input a def chooses, and `MemberPrep.frames(bind_side)` memoizes per value.

Built (`src/cobalt/radar/evaluate.py`):
- `class MemberPrep`, a plain class. Eager: `membership_id`, `as_of`, `closed_i1`, `consumed`, `last_bar`, `last_price`. `series`, `run`, `params` and `daily_ok` are `cached_property`, so each is computed where `evaluate_member` first used it before (after the evaluability / convention early returns, byte-identical including exceptions). `frames(bind_side)` is memoized and built by the existing `_build_frames` with today's arguments.
- `prepare_member(member, *, tunables, defaults, clock)`.
- `evaluate_member(…, prep=None)` builds through `prepare_member` when `prep` is None (L3). With a mismatched `(membership_id, as_of)` it raises `EvaluateError` naming both. `closed_i1` / `consumed` / `last_bar` / `last_price` / `run` / `params` / `daily_ok` / `frames` read from the prep.
- UNTOUCHED: the `intraday_stale` block, `base`, `inputs_sha`, `MemberEvaluation`, the early returns, and everything from `ext, htf = …` down. `EVALUATOR_VERSION` is not bumped.
- `member_frames` → `prepare_member(...).frames(False)`. Byte-identical: today's call passes no `bind_side` (False) and the same argument values.
- `__all__` gains `MemberPrep`, `prepare_member`.

`src/cobalt/radar/evaluate_cli.py`: one `prep = prepare_member(inp, …)` per (member, instant), passed to every def. The resident's calls and `audit_export.py` are unchanged (`prep=None`).
Commit: `d0898f75` (`<fix1>`).

## D3 FIX 2 + FIX 3
- `evaluate_cli.py`:
  - `ReplayReport` gains `scans_planned: int = 0` and `cut_before: AwareDatetime | None = None`.
  - `replay_formations(…, cut_at=None)` materializes the instants once and sets `scans_planned`. Before each instant it asks `cut_at`; on True it sets `cut_before`, prints and `logger.warning`s the CUT line, and breaks.
  - The summary line appends ` · CUT before <HH:MM:SS> ET` only when cut. The module docstring gains one sentence.
- `replay/models.py`: `FormationCut(scans_done, scans_planned, cut_before)`; `FormationOutcome.cut` and `ReplayResult.formation_cut` (Optional, default None); `__all__` gains `FormationCut`.
- `replay/formations.py`: `formation_misses` keeps a per-ticker `bars` dict (FIX 3) and passes `cut` from the report's `cut_before` into the outcome. The only other change is the `FormationCut` import.
- `replay/runner.py`:
  - New constant `FORMATIONS_RESERVE_KEY`. At run start, only when `deadline is not None`, it reads the reserve with the margin's missing-or-unmeasured refusal shape.
  - `formations_step` builds `cut_at = deps.now() >= deadline - reserve`, sets `result.formation_cut`, and logs a warning when cut. `formation_replay(…, cut_at=None)` passes `cut_at` through; `line_step` passes `formation_cut`.
  - After the step loop, ONE `ReplayError` joins archive failures first, then `formations cut at the deadline — k of n scans`. An archive-only message is byte-identical to before.
  - The module docstring's THE DEADLINE paragraph gains one sentence.
- `replay/line.py`: `render_line(…, formation_cut=None)` appends the PARTIAL clause to the formations segment. `ET` is imported from `cobalt.session.clock`.
- `tunables.yaml`: `replay.formations_reserve_s` = 120, duration, global, not dynamic, proposed, `source: dwv`, consumer `cobalt.replay.runner (formations cut)`, placed after `replay.backup_margin_s`. The loader accepted `dwv` (T9–T11 green under `load_tunables`, D4).

Commit: `12fac3cd` (`<fix2>`).

## D4 GREEN + DOCS
GREEN, first run, no code iteration. `uv run pytest -q -rs <the 5 files>` → `113 passed, 4 skipped in 59.08s`: **0 failed, 0 errors**. T1–T11 all pass (the red run's 11 failures are now passes; 102 + 11 = 113). The 4 skips are the env-gated tests: `test_radar_evaluate.py:695` (COBALT_LIVE_VAULT_ROOT, run at D5), `test_replay_formations.py:225` and `test_replay_runner.py:633` (requires_db, D7), and `test_replay_line.py:256` (COBALT_TEST_LIVE_DRC, not part of this gate).
DOCS (`ls` first: all six present, none absent):
- `docs/40 - DevDocs/cobalt/radar/evaluate.md`: new section, 2026-09-25 (`MemberPrep`, `prepare_member`, `prep=`).
- `…/radar/evaluate_cli.md`: `cut_at`, `scans_planned`, `cut_before`, the CUT lines.
- `…/replay/runner.md`: `replay.formations_reserve_s`, the cut, the end-of-run failure.
- `…/replay/models.md`: `FormationCut`, `cut`, `formation_cut`.
- `…/replay/formations.md`: one read per ticker, `cut`.
- `…/replay/line.md`: the PARTIAL clause.
- ADR-0010: the amendment bullet added after its deadline line (`:113`).

Commit: `332f44e1` (then `<tip>`; D6's fix moved `<tip>` to `8b931ce5`).
GREEN re-run on `8b931ce5` (D6 rule) → `113 passed, 4 skipped in 63.10s (0:01:03)`: 0 failed, 0 errors.

## D5 LIVE-NOTE
`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` on `332f44e1` → `146 passed, 1 skipped, 15 warnings in 28.83s`. **GATE PASS: 0 failed, 0 errors** → `<lp>` 146, `<lf>` 0.
The one skip is `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC …`. It does NOT name `COBALT_LIVE_VAULT_ROOT`, so the live-note proof ran.
AWAITING lines, verbatim:
- `AWAITING A RULING: backside`
- `AWAITING A RULING: fashionably-late`
- `AWAITING A DAY: hitchhiker`
- `AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)`

**Re-run on `8b931ce5`** (after D6's fix) → `146 passed, 1 skipped, 15 warnings in 28.08s`. GATE PASS, the same skip (`COBALT_TEST_LIVE_DRC`) and the same 4 AWAITING lines verbatim. **`<lp>` 146 / `<lf>` 0.**

## D6 OFFLINE
`ls …/replay-deadline/.env` → `No such file or directory`.
**Run 1** on `332f44e1`, `uv run pytest -q -rs tests/cobalt tests/taxonomy` → `5 failed, 2507 passed, 361 skipped, 1 xfailed, 15 warnings in 530.90s (0:08:50)`. RED.

All 5 reds have one cause. The card's `tunables_sha256` digests EVERY committed tunables row. The pinned tests map it back to a start digest by excluding the keys each later step added (`ADDED_KEYS` / `STEP3_KEYS`), and the new `replay.formations_reserve_s` row was not in that list. The reds:
- `tests/cobalt/test_rubberband_forms.py:525` `test_t6_a_def_that_formed_before_changes_only_in_the_finals_named_ways`, which uses `test_setups_registries._tunables_digests`;
- `tests/cobalt/test_setups_d1.py:216` `test_f11_the_dots_and_card_score_do_not_move[countertrend]` and `[mixed]`;
- `tests/cobalt/test_setups_registries.py:201` `test_lego_ii_every_card_spec_is_byte_identical_through_the_registries[countertrend]` and `[mixed]`.

This is the D1 clause's case, "a suite test pins the set … of tunables", in `tests/cobalt/` rather than `tests/taxonomy/`. The fix extends each expectation by the ONE new row and nothing else: `tests/cobalt/test_setups_d1.py:53-59` `ADDED_KEYS` and `tests/cobalt/test_setups_registries.py:97-108` `STEP3_KEYS` each gain `"replay.formations_reserve_s"`. No pin hash changed, and every other byte of every card is still pinned. No code can avoid it: a new committed tunable moves every card's `tunables_sha256` by construction (the same for every earlier row these lists carry).
The three files re-run: `85 passed, 6 skipped in 198.30s`. Commit `8b931ce5` → the new `<tip>`. Per D6's rule, D4's command, D5 and D6 are all re-run on `8b931ce5` (below).
**Run 2** on `8b931ce5` → `2512 passed, 361 skipped, 1 xfailed, 15 warnings in 528.09s (0:08:48)`. **GATE PASS: 0 failed, 0 errors** → `<p>` 2512, `<f>` 0.

## D7 WITH-DB + TIMING
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`. The lock was free.
- (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/replay-deadline/.env` → exit 0 (never read or printed). **Lock TAKEN at 07:08 ET** (`date` 07:08:03).
- (c) `COBALT_ENV=dev uv run pytest -q -rs tests/cobalt tests/taxonomy` on `8b931ce5` → `2867 passed, 6 skipped, 1 xfailed, 15 warnings in 661.75s (0:11:01)`. **GATE PASS: 0 failed, 0 errors** → `<dp>` 2867, `<df>` 0. No migrate before or after.
- (c2) timing: approved (AUTHORIZATION). `<t0>` = `Fri Sep 25 07:19:18 EDT 2026`. `COBALT_ENV=dev uv run cobalt radar evaluate --replay 2026-09-24` → exit 0. `<t1>` = `Fri Sep 25 07:19:25 EDT 2026`. The output carries `replay 2026-09-24: no membership episodes for pool 'primary'` (output line 7) and the summary `replay 2026-09-24: scans=0 formations=0 path_b_only=0 counts={} writes: none` → **`replay dry-run 2026-09-24: NOT MEASURABLE ON cobalt_dev (no 2026-09-24 membership)`**.
- (d) `rm /Users/cobalt/cobalt-wt/replay-deadline/.env` → exit 0; `ls …/.env` → `No such file or directory`. **`.env: removed, proven gone`**. The lock was released at ≈07:19 ET.

## RESTARTS
`uv run cobalt jobs restarts a994a5dd..HEAD`, derivation table verbatim:
```
path	change	rule	restart
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
docs/10 - Decisions/ADR-0010-missed-corpus-counterfactual-r-picks.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/evaluate.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/evaluate_cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/formations.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/line.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/models.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/replay-deadline-fix-build-2026-09-24.md	A	DOCS	-
src/cobalt/radar/evaluate.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/evaluate_cli.py	M	static import reach	com.cobalt.radar
src/cobalt/replay/formations.py	M	static import reach	com.cobalt.radar
src/cobalt/replay/line.py	M	static import reach	com.cobalt.radar
src/cobalt/replay/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/replay/runner.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_evaluate_cli.py	M	test/documentation; no resident	-
tests/cobalt/test_replay_formations.py	M	test/documentation; no resident	-
tests/cobalt/test_replay_line.py	M	test/documentation; no resident	-
tests/cobalt/test_replay_runner.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_d1.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_registries.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
**RESTARTS: com.cobalt.aset com.cobalt.radar** (derived, 0 UNCLASSIFIED). `com.cobalt.replay` is a one-shot, not a resident, so the table lists no restart for it. It picks up the change on its next 21:10 run. `com.cobalt.aset` is derived through `tunables.yaml` (a resident read) and the static import reach of `evaluate.py` / `replay/models.py`.

## FOR THE DEPLOY
- Branch `fix/replay-deadline-0924` · `<base>` `a994a5dd` · `<tip>` `8b931ce5`, plus this report's commit on top (docs only).
- RESTARTS line, verbatim: `RESTARTS: com.cobalt.aset com.cobalt.radar`.
- THE SEAM with `cards/stale-score-0922` (`<stale tip>` `358f1f75`, read with `git diff main...cards/stale-score-0922 -- src/cobalt/radar/evaluate.py`):
  - `evaluate_member`'s head. Stale-score inserts its `intraday_stale` block right after `last_price = …` and adds `intraday_stale=` to `base`. This branch changes those four lines to `closed_i1 = prep.closed_i1` … `last_price = prep.last_price` (after the prep / identity lines).
  - Stale-score deletes the old `intraday_stale` block between `params = …` and `daily_ok = …`. This branch changes the lines around it (`run = prep.run`, `params = prep.params`, `daily_ok = prep.daily_ok`, `frames = prep.frames(...)`).
  - The merge keeps stale-score's block at the top and its `intraday_stale=` in `base`, plus this branch's prep lines. Expect a textual conflict in both hunks.
  - Proof on the stacked tree: T1 and T2 (`test_radar_evaluate.py`) re-run there.
  - Stale-score also bumps `EVALUATOR_VERSION` to `s2p2.3` (its `SUPPORTED_EVALUATORS` hunk in `replay/formations.py`). This branch changes only `formation_misses` and one import line there.
  - `tests/cobalt/test_replay_runner.py`: appended at the end, plus the two fakes' `cut_at=None` and the r1_16 docstring sentence (lines ≈190–206, ≈723, ≈734).
- THE DIGEST LISTS: `tests/cobalt/test_setups_d1.py` `ADDED_KEYS` and `tests/cobalt/test_setups_registries.py` `STEP3_KEYS` each gain `replay.formations_reserve_s`. If a sibling branch adds a tunables row, the stacked tree needs both keys in both lists.
- The first live proof: the 2026-09-25 21:10 replay ends DONE before 21:35:00 ET (`logs/replay.err` `F17: com.cobalt.replay DONE`), `DRC-2026-09-25.md` carries the `drc-misses` unit, and the smoke's K7 / K10.1 / K10.2 are green.
  - A night that CUTS writes the line with `PARTIAL: cut before` and ends FAILED. That is the fix working (the line landed) AND a signal that FIX 1 alone did not fit the day. It goes to the desk as the design question in the drafter's ESCALATE, never to a rerun inside the window.
- Rollback per L54: `git revert` of the merge range; ONE `git revert -m 2` if it lands through a stacked gate branch.

## CONTINUE
next: done — CLOSE written; nothing pending. `.env` removed, lock released.

## ESCALATE
1. AUTHORIZATION: **timing: approved** (`cto-2026-09-25.md:26` R18, "approve command"). D0 raised no ESCALATE (06:05 ET, before 15:00; `main` == `<base>`).
2. D1 interruption, recorded: one call off the launch list (`git -C /Users/cobalt/cobalt diff main...cards/stale-score-0922 -- …`) raised a permission box, which was cancelled. The desk resumed the run at D1 by message (06:43 ET) under the rule "only listed shapes". The seam was then read with `git diff main...cards/stale-score-0922 -- src/cobalt/radar/evaluate.py`. Nothing else ran off-list.
3. D2 shareability: **frames shareable**, `anatomy/frame.py:105-114, :228-239, :245, :578-590, :625-627` read (see D2).
4. Test edits outside "append at the end", each named for the check:
   - (i) `test_replay_formations.py:385`, `test_formation_sources_name_every_argument_p2s_entrypoint_takes`: `cut_at` is added to the excluded per-run arguments (D1).
   - (ii) `test_setups_d1.py` `ADDED_KEYS` and `test_setups_registries.py` `STEP3_KEYS` gain the one new row (D6 run 1: 5 reds; the D1 taxonomy clause applied in `tests/cobalt/`).
   - No pin hash and no assertion changed.
5. READING for the check, not built: `MemberPrep` checks only `(membership_id, as_of)`, as specified. It is correct only when every def sharing it uses the same `tunables` / `defaults` / `clock` as the prep. `replay_formations` guarantees that structurally (one `rows`), and the resident never passes a prep. A guard on those three would be a widening, not a FIX row.
6. L74: one block arrived in a tool result (a `Claude-Session:` commit line plus a file-send tool). Recorded once under `## L74`, not followed.
7. **FOR THE DEPLOY:** see `## FOR THE DEPLOY` (the `evaluate_member` seam with stale-score, the digest lists, the first live proof, the rollback shape).
8. **THE MEASUREMENT:** `replay dry-run 2026-09-24: NOT MEASURABLE ON cobalt_dev (no 2026-09-24 membership)`. The check and the desk read it; this build produces no timing evidence. The structural guard is T2 (frame pairs built once per `bind_side`, not once per def).

REPLAY DEADLINE FIX BUILT 8b931ce5 | on a994a5dd | offline 2512/0 | with-DB 2867/0 | live-note 146/0 | .env: removed | FIX: 3 of 3 | replay dry-run 2026-09-24: NOT MEASURABLE ON cobalt_dev | ESCALATE: 8
