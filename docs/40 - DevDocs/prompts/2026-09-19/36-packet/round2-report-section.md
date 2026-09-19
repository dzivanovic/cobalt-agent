
# ROUND 2 (tribunal fold)

Seat `p4-round2-0919`, prompt `docs/40 - DevDocs/prompts/2026-09-19/32-p4-round2.md`, worktree `/Users/cobalt/cobalt-wt/s2-p4`, branch `sprint-2/p4`. OFFLINE BY DESIGN — `cobalt_dev` is held by `ops-0919-db` (bg `e810326c`) and was not connected to, migrated, rolled back or read at any point in this run.

**§0.** Both blockers closed: **A1 FIXED** (the formation reconcile now keys on P2 having run, so an empty rerun retires its predecessors — R2-1) and **A3 PINNED** with `radar/pool.py` untouched, its L52 disclosure still owed to Dejan. A2 pinned as-is (design gap escalated, no behaviour changed), A4's cutter transforms built (fixture NOT regenerated, nothing personal ever shipped), A5's merge-order test no longer the same case twice.
Offline **1829 passed / 0 failed** (baseline 1818/0, +11 named new tests, skips unchanged at 324). RESTARTS: `com.cobalt.radar`, 0 UNCLASSIFIED.
**OFFLINE BY DESIGN: `cobalt_dev` untouched — no DB test ran this round; the two edited `@requires_db` merge-order parametrizations owe their first run to P4's DB step.**
**ESCALATE: 5** — A2 (deadline scope), A3 (L52 ruling owed), R2-1 (line-number drift), **R2-2 (the desk's A3 pre-read names the wrong half of the sort key — the disclosure text needs correcting)**, R2-3 (no `requires_db` twin for A1, with reason). Carried untouched: A6, A7, A8, A9/A10.

## ROUND 2 AUTHORIZATION

| check | command | result |
|---|---|---|
| 16 allow strings ⊂ `13-p4-verify.md` | `grep -c -F '<string>' '…/13-p4-verify.md'` ×16 | every one printed `1` |
| 16 allow strings ⊂ `24b-p4-fund-rule.md` | `grep -c -F '<string>' '…/24b-p4-fund-rule.md'` ×16 | every one printed `1` |
| deny rules in both | `grep -c -F -- '--disallowedTools "AskUserQuestion" "EnterWorktree"' <both>` | `1` and `1` |
| 13 committed on main | `git -C /Users/cobalt/cobalt log --oneline -1 -- "…/13-p4-verify.md"` | `db2dcb1 docs(desk): 09-19 P4 prompt check round 2 — 0 launch blockers, 7 findings folded (text only); p4-verify launches` — MATCHES the prompt's `db2dcb1` |
| 24b committed on main | `git -C /Users/cobalt/cobalt log --oneline -1 -- "…/24b-p4-fund-rule.md"` | `4177649 docs(desk): 09-19 P4 fund-rule chunk 24b — step 3 redesigned (decide at ingest, no migration; rules = 24's)` — MATCHES the prompt's `4177649` |
| L67 work item recorded | `git -C /Users/cobalt/cobalt log --oneline -1 -- "…/reports/cto-2026-09-19.md"` | `238374f docs(desk): 09-19 P4 round-2 fix launched (763578e6); A1 + A3 block P4, A3 ruling owed (L52 disclosure)` (no equality required; recorded) |

The 16 strings are a strict subset of both approved lists; no string in this launch line is absent from either file. Authorization holds.

## ROUND 2 PREFLIGHT

| rule | command | exit | allowed/DENIED |
|---|---|---|---|
| `Bash(date*)` | `date` | 0 | allowed — `Sat Sep 19 12:22:19 EDT 2026` |
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — EMPTY |
| `Bash(git status*)` | `git status` | 0 | allowed — long form quoted below |
| `Bash(git log*)` | `git log --oneline -3` | 0 | allowed — tip `c40f03c`, code tip `2738cdc` beneath |
| `Bash(ls *)` | `ls -la .env` | 1 | allowed — `ls: .env: No such file or directory` (the required answer) |
| `Bash(ls *)` | `ls -la scratch` | 0 | allowed — 50 entries, recorded below, none added to git |
| `Bash(git -C /Users/cobalt/cobalt *log*)` | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `238374f docs(desk): 09-19 P4 round-2 fix launched (763578e6); A1 + A3 block P4, A3 ruling owed (L52 disclosure)` |
| `Bash(git diff *)` | `git diff --stat main -- src/cobalt/radar/` | 0 | allowed — the standing-constraint capture, quoted below |
| `Bash(grep *)` | `grep -c -F …` ×34 (authorization) | 0 | allowed |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_replay_runner.py tests/cobalt/test_p4_migrations.py` | 0 | allowed — `48 tests collected in 0.10s` |
| `Bash(uv run pytest *)` | `uv run pytest -q tests/cobalt tests/taxonomy` (`run_in_background`) | 0 | allowed — BASELINE below |

NO DENIALS. Rules in the launch line not probed at preflight because their first real use is the probe: `Bash(git add *)`, `Bash(git commit *)`, `Bash(git show*)`, `Bash(uv run cobalt jobs restarts *)`, `Bash(cd *)`, `Bash(mkdir -p *)`, `Bash(wc *)`, `Bash(git -C /Users/cobalt/cobalt status*)` (UNATTENDED-LAUNCH §6: a rule with no harmless variant inside its own pattern is probed by its first real use).

**`git status`, LONG FORM, IN FULL:**

```
On branch sprint-2/p4
nothing to commit, working tree clean
```

Branch is `sprint-2/p4`. No "rebase in progress", no "You have unmerged paths".

**`git log --oneline -3`:**

```
c40f03c docs(report): s2-p4 fund rule R16 (retry 0919b) — built via option B, ESCALATE 17 resolved; offline 1818/0, db 2136/0, 0 stock rows hit; 4 new ESCALATE
2738cdc fix(s2-p4): not-equity for movers decided at ingest from the parsed export, never through the movers_daily round trip (R16 "C", ESCALATE 17 option B)
db1c095 test(fixtures): dropped-under-new-rule count in the evidence mode
```

Expected tip `c40f03c` on top with the code tip `2738cdc` beneath it — as the prompt predicted for a first launch.

**BASELINE (verbatim, `uv run pytest -q tests/cobalt tests/taxonomy`):**

```
1818 passed, 324 skipped, 1 xfailed, 15 warnings in 55.69s
```

`failed` = 0. `passed` = 1818, matching the R16 close exactly. Skips 324, xfail 1 — these are the numbers this round's close is compared against.

**STANDING CONSTRAINT, PREFLIGHT CAPTURE — `git diff --stat main -- src/cobalt/radar/`:**

```
 src/cobalt/radar/collector.py    |   4 +-
 src/cobalt/radar/config.py       |  91 ++++++++++++-
 src/cobalt/radar/evaluate_cli.py |  23 ++++
 src/cobalt/radar/models.py       |  13 +-
 src/cobalt/radar/notes.py        | 277 +++++++++++++++++++++++++++++++++++++--
 src/cobalt/radar/pool.py         |  63 +++++++--
 src/cobalt/radar/propose.py      |  42 ++++--
 src/cobalt/radar/runner.py       |   4 +-
 src/cobalt/radar/store.py        |  40 ++++--
 src/cobalt/radar/throttle.py     |  18 ++-
 10 files changed, 527 insertions(+), 48 deletions(-)
```

**`ls -la scratch` (recorded; NOTHING here is ever added to git — L32):** `.launch-marker`, `agy-out.md`, `asset-type-evidence.md`, `at0-brief.md`, `at1-brief.md`, `bars-day-raw.tsv`, `card-transitions-day-raw.tsv`, `chunk-A-stderr.log`, `chunk-A-stdout.log`, `e2-brief.md`, `e2-src.patch`, `f1-brief-v2.md`, `f1-brief.md`, `f1-builder-output-v2.txt`, `f1-builder-output.txt`, `fix-db-reds-brief.md`, `fr1-brief.md`, `fr1-builder-report.md`, `fr2-brief.md`, `fr2-builder-report.md`, `fx-brief.md`, `fy-brief.md`, `jobs-restarts.txt`, `LAWS.md`, `membership-day-raw.tsv`, `movers-gainers-raw.csv`, `movers-losers-raw.csv`, `p4-devdoc-sections.md`, `p4b-devdoc-append.py`, `pool-metrics-raw.csv`, `proof_rows.py`, `rebase-brief-1.md`, `rebase-brief-1b.md`, `rebase-brief-2.md`, `rebase-brief-3.md`, `rebase-brief-4.md`, `rebase-brief-v1.md`, `rebase-resolve-1.md`, `rebase-resolve-1b.md`, `rebase-resolve-2.md`, `rebase-resolve-3.md`, `rebase-resolve-4.md`, `rebase-resolve-v1.md`, `render_k9.py`, `review/`, `step0-sizings.json`, `tr-brief.md`, `tr2-brief.md`.

## ROUND 2 — 1. A1, the empty formation rerun (BLOCKER 1 of 2) — FIXED, commit `f07b483`

**`facts.md` row A1: CONFIRMED on the live tip**, with one line-number correction (see ESCALATE R2-1 below). The guard, quoted verbatim from `src/cobalt/replay/runner.py` **line 426** (the prompt's index card says `:425`; `facts.md` row A1 says "real file 425–430", which contains it):

```
        if rows and not dry_run:
            result.reconcile["formation"] = deps.missed.reconcile(
                run_id=result.replay_run_id, trade_date=trade_date, kind="formation", rows=rows)
            state["formation_rows"] = deps.missed.current(trade_date, "formation")
```

Confirmed against the siblings: `movers_step` reconciles at `runner.py:369` `if not dry_run:` and `cards_step` at `runner.py:398` `if not dry_run:` — neither carries a row-count condition. Only the formation kind does.

**The status spelling, read at the source before the condition was written** (the prompt's stop-and-escalate condition — it does NOT apply; there is exactly one spelling and it is a named constant):

| fact | file:line |
|---|---|
| `FORMATION_UNAVAILABLE = "unavailable"` — one named constant, one spelling | `src/cobalt/replay/models.py:27` |
| the ONLY producer of that status: P2 absent | `src/cobalt/replay/runner.py:208` `return FormationOutcome(status=FORMATION_UNAVAILABLE)` |
| the ONLY other producer of a status: the capability marker | `src/cobalt/replay/formations.py:343` `status=evaluator_version, rows=tuple(rows),` |
| and that marker is constrained to a known set, so "available" is a closed set of one today | `src/cobalt/replay/formations.py:81` `SUPPORTED_EVALUATORS = frozenset({"s2p2.1"})`, enforced `:145` |
| `grep -rn 'unavailable' src/cobalt/replay/` → no second spelling anywhere (the other hits are prose, the DRC line text, and `cards.py`'s unrelated `stop_at_card_level_exemption`) | — |

**THE FIX** (`runner.py:426`, the only behavioural line changed in this step):

```
        if outcome.status != FORMATION_UNAVAILABLE and not dry_run:
```

`result.formation_misses`, the `MISS formation …` print lines and everything else in the step are byte-identical.

**TESTS FIRST — RED, quoted:** `uv run pytest -q tests/cobalt/test_replay_runner.py -k "retires_the_days_predecessors or never_reconciles_the_formation_kind or suppresses_it_in_the_run"` on the tip `c40f03c` + the new tests, BEFORE the runner edit:

```
FAILED tests/cobalt/test_replay_runner.py::test_an_open_radar_card_for_the_formations_subject_suppresses_it_in_the_run - AssertionError: assert 'missed.reconcile:formation' in ['job_store.get', 'c...
FAILED tests/cobalt/test_replay_runner.py::test_an_available_p2_with_no_formations_still_retires_the_days_predecessors - AssertionError: assert 'missed.reconcile:formation' in ['job_store.get', 'c...
2 failed, 1 passed, 31 deselected in 2.91s
```

**GREEN, after the fix, same command:**

```
3 passed, 31 deselected in 2.81s
```

Whole replay surface after the fix — `uv run pytest -q tests/cobalt/test_replay_runner.py tests/cobalt/test_replay_formations.py tests/cobalt/test_replay_line.py tests/cobalt/test_replay_cards.py` → `93 passed, 5 skipped in 12.63s`.

**What each test is:**

| test | what it pins | before | after |
|---|---|---|---|
| `test_an_available_p2_with_no_formations_still_retires_the_days_predecessors` (NEW) | the R2-1 case the plan names: P2 present and compatible (`status == "s2p2.1"`), formation list EMPTY, `dry_run=False` → `missed.reconcile` IS called for `kind="formation"` with `rows == []`, `inserted == 0`, and a predecessor seeded into the fake's current set is gone afterwards | RED | GREEN |
| `test_an_absent_p2_never_reconciles_the_formation_kind` (NEW) | the legitimate skip: `status == "unavailable"`, no rows → `missed.reconcile:formation` NOT in calls | **GREEN before AND after** — stated plainly, as the prompt requires; it is a pin of the half of the guard that was always right | GREEN | GREEN |
| `test_an_open_radar_card_for_the_formations_subject_suppresses_it_in_the_run` (`:362`, ONE assertion changed) | an AVAILABLE P2 with everything suppressed still reconciles | RED | GREEN |

**The changed assertion, before → after** (every other assertion in that test is byte-identical — the counts tuple `(1, 0, 1)` and the `formations: 0 not taken (no_card) · cf-R Σ +0.0R, n=0 · suppressed 1` line both stand unchanged):

```
-    assert "missed.reconcile:formation" not in calls
+    # P2 RAN here (available, everything suppressed): an available run with
+    # zero surviving rows still reconciles, so the day's predecessors are
+    # retired (plan STEP-1 R2-1). Only `unavailable` skips the reconcile.
+    assert "missed.reconcile:formation" in calls
+    assert result.reconcile["formation"].inserted == 0
```

The old assertion was wrong, not the plan: that test drives the REAL P2 binding (`formations=runner_mod.formation_replay`, `formation_sources=p2_sources`), so P2 ran, produced one candidate, and suppressed it. Under `reconcile`'s own contract ("retire every predecessor this run") a run that produced no surviving row must still retire the predecessors of the run before it. No ESCALATE is raised against the plan here.

**The `requires_db` twin: NOT written, and why (L3, L45).** The prompt asks for one "if and only if the suite's existing pattern has one for the sibling kinds". It does not: the whole branch carries exactly ONE `requires_db` test of reconcile semantics, `tests/cobalt/test_p4_migrations.py:394 test_missed_rerun_reconciles_in_the_ruled_order_against_the_live_unique_index`, and it is written at the SQL level on `kind='mover'` only — there is no card twin and no per-kind pattern to follow. That test already pins the exact R2-1 retirement this fix makes reachable ("A subject whose miss disappears on rerun: step (1) only", `test_p4_migrations.py:431-447`), and it is kind-agnostic SQL: a formation copy would assert the same index and the same check constraint with one string changed. Writing one would be a second copy of a proven path. Nothing new is OWED to the DB step from A1.

## ROUND 2 — 2. A2, the deadline's actual scope — PINNED, no behaviour changed, commit `b136768`

**`facts.md` row A2: CONFIRMED** on the live tip. Quotes:

| the row's claim | what the code says |
|---|---|
| `check_deadline` runs only between steps and before the vault write | `runner.py:455` `check_deadline(name)` inside the `for name, step in zip(STEPS, …)` loop, and `runner.py:447` `check_deadline("line (before the vault write)")`. `grep -n 'check_deadline' src/cobalt/replay/runner.py` → definition `:292`, and call sites `:381` (per card candidate, inside `cards_step`), `:447`, `:455`. No other call site. |
| only `run_async` work is under `wait_for` | `runner.py:304-305` `async def bounded(): return await asyncio.wait_for(coro, timeout=remaining)` |
| `formation_source(...)` and `missed.reconcile(...)` are synchronous | `runner.py:410` `outcome = deps.formation_source(` and the three `deps.missed.reconcile(` calls at `:370` (mover), `:399` (card), `:434` (formation) — plain calls, none wrapped in `run_async`. The only `run_async` call sites are `:322`, `:323`, `:347`, all collector/archive work. |
| the module docstring states the design | `runner.py:26-31`, verbatim: "THE DEADLINE (R1-16). `timeout_s` bounds a stall, not a healthy long run. … a running step is cut at the deadline (async work under `wait_for`); the vault write is re-checked immediately before it lands, so no write is ever late." |

Line-number note: the pre-vault-write check is at `:447` **after this round's step-1 commit** (it was `:440` before — the prompt's number — the +7 lines being step 1's comment). No other drift.

**A test of the "crosses the deadline → raises rather than writes" shape ALREADY EXISTS** and was not duplicated (L3): `test_r1_16_a_deadline_passing_between_steps_stops_before_the_vault_write`, `tests/cobalt/test_replay_runner.py:142`. **The missing half, now added:** that test accepts `failed.value.step in {"formations", "line"}`, so the between-steps `check_deadline` satisfies it and the `:447` check is never proven to be the thing that refuses. `grep -rn 'before the vault write' tests/ src/` returned exactly ONE hit before this commit — `runner.py:447` — no test anywhere asserted that check by its own name.

**The two tests added:**

| test | what it pins |
|---|---|
| `test_r1_16_the_check_immediately_before_the_vault_write_is_what_refuses_a_late_run` | the deadline is crossed by SYNCHRONOUS work inside the line step (`deps.drc_path`), AFTER that step's between-steps check has passed, so only `:447` can refuse: asserts `step == "line"`, `DeadlineExceeded`, `"line (before the vault write)" in str(error)`, no `writer` call, and the DRC note byte-identical to before. This is spec R1-16's stated bar, asserted directly. |
| `test_r1_16_a_synchronous_step_is_not_cut_mid_flight_the_documented_limitation` | the LIMITATION, asserted as the current contract: `missed.reconcile` for `kind="mover"` pushes the clock past the deadline mid-call and still RUNS TO COMPLETION — its rows are current, `result.mover_misses` matches them — and the run stops at the NEXT `check_deadline`, one step later (`step == "cards"`). Its docstring names it as the documented limitation and points at the A2 ESCALATE line below. |

**RED/GREEN, stated honestly: both are GREEN on their first run, and there is no RED phase to quote, because A2 changes NO code** — the prompt rules the fix (bounding synchronous work) a design change and NOT this round's. `uv run pytest -q tests/cobalt/test_replay_runner.py -k "r1_16"` → `5 passed, 31 deselected in 0.47s` (3 pre-existing + 2 new). They are not vacuous: each discriminates by construction — the first fails if any other `check_deadline` fires (it asserts the exact message and `step == "line"`), the second fails if the synchronous call is ever cut (it asserts the reconcile's rows exist and the failure lands one step LATER).

NOT done, deliberately, per the prompt: no timeout was added around a DB commit; `run_async` is untouched.

## ROUND 2 — 3. A3, the ranking sort key — PINNED, `pool.py` NOT TOUCHED, commit `5652260`

**VERDICT: crash-removal only — the conclusion of `facts.md` row A3 and of the desk's pre-read is CONFIRMED. But ONE OF THE PRE-READ'S THREE CLAIMS IS FACTUALLY WRONG about which half of the key tuple this branch edited, and the code wins (ESCALATE R2-2 below).** The corrected argument reaches the same place: no input that previously ran ranks differently, and no pool membership changes.

**The three claims, each confirmed or contradicted with a quote:**

**Claim 1 — "BOTH `max(...)` calls in the key tuple carry the NEW `is not None` filter (`pool.py:189`, `pool.py:198`)": HALF WRONG.** Both carry the filter *today* (`pool.py:189` and `pool.py:198`, confirmed by reading the file) — but only `:189` is new. `git diff main -- src/cobalt/radar/pool.py` contains exactly ONE added filter line, inside element 1's generator:

```
                 key=lambda name: (
+                    # None-filtered like the value expression below: a name
+                    # with no value on one list and a value on another
+                    # used to raise TypeError here (found S2-P4 STEP-2).
                     max(
                         (
                             source.metrics.get(name, {}).get(session_metric)
                             for source in sources if source.kind == "list" and name in source.tickers
+                            and source.metrics.get(name, {}).get(session_metric) is not None
                         ),
                         default=None,
                     ) is None,
```

Element 2 (`-(max(…, default=0))`) appears nowhere in the diff — it is unchanged by this branch.

**Claim 2 — "Pre-edit, element 2 was `-(max(<unfiltered gen>, default=0))`; any generator containing a `None` raised `TypeError` THERE": CONTRADICTED.** `git show main:src/cobalt/radar/pool.py` shows element 2 ALREADY carrying the filter on main, and element 1 carrying none — the exact opposite assignment:

```
                 key=lambda name: (
                     max(
                         (
                             source.metrics.get(name, {}).get(session_metric)
                             for source in sources if source.kind == "list" and name in source.tickers
                         ),
                         default=None,
                     ) is None,
                     -(
                         max(
                             (
                                 source.metrics.get(name, {}).get(session_metric)
                                 for source in sources if source.kind == "list" and name in source.tickers
                                 and source.metrics.get(name, {}).get(session_metric) is not None
                             ),
                             default=0,
                         )
                     ),
                     name,
                 ),
```

So the pre-edit crash was raised by **element 1**, not element 2, and this branch fixed element 1.

**The conclusion survives the correction — the corrected proof, case by case.** Pre-edit element 1 is `max(<unfiltered>, default=None) is None`; post-edit it is `max(<filtered>, default=None) is None`. Enumerating every input:

| the name's values across the lists carrying it | pre-edit element 1 | post-edit element 1 | same? |
|---|---|---|---|
| no lists carry it (empty generator) | `default=None` → `True` | `default=None` → `True` | SAME |
| exactly one value, `None` | `max` of one item → `None` → `True` | filtered → empty → `True` | SAME |
| exactly one value, a number | that number → `False` | that number → `False` | SAME |
| ≥2 values, all numbers | max → `False` | max → `False` | SAME |
| ≥2 values, any `None` among them (incl. all-`None`) | **`TypeError`** — `>` between `NoneType` and a number, or between two `NoneType` | filtered → `True` or a number | the ONLY input whose behaviour changed, and pre-edit it did not run at all |

Element 2 and element 3 (`name`) are byte-identical on both sides. **Therefore every input that did not raise produces an IDENTICAL key tuple, hence identical order and identical ranks.** The edit converts a crash into a defined placement, exactly as the pre-read concluded.

**Claim 3 — "`union` is consumed at `pool.py:206` only as `position = union.index(ticker) + 1`, never the `candidates` set": CONFIRMED.** `grep -n 'union' src/cobalt/radar/pool.py` → exactly two hits, `:179` (the `sorted(...)` assignment) and `:206` (`position = union.index(ticker) + 1`). `position` is one component of the outer `key` tuple at `:209`; the candidate set is never filtered by it, so pool MEMBERSHIP cannot move either.

**What the pre-edit crash actually did (checked, not assumed):** `decide(...)` is called at `src/cobalt/radar/runner.py:186`, which is OUTSIDE every `try` in `cycle()` (the first `try:` is at `:191`). `grep -rn 'except TypeError' src/cobalt/radar/` → one hit, `evaluate.py:282`, unrelated. So the pre-edit `TypeError` propagated out of the scan cycle — a loud crash, never a caught-and-degraded alternate ranking. Nothing silently took a different path.

**THE PINNING TEST** (in the EXISTING module `tests/cobalt/test_radar_pool.py`, which already covers `_ranked` through the public `decide` — no new module, L3):

| test | what it pins | result |
|---|---|---|
| `test_list_union_orders_by_value_descending_then_name_when_every_value_is_present` | all four names carry an rvol: expectation built from the key tuple itself (value descending, ties by name), NOT from a golden blob — `{"DDD": 1, "BBB": 2, "CCC": 3, "AAA": 4}` for rvol 9.0 / 4.0 / 4.0 / 1.0, all ADMIT | GREEN first run |
| `test_a_name_with_no_value_on_any_list_sorts_after_every_name_that_has_one` | two valueless names sort after every valued one and are ordered by name between themselves (`{"BBB": 1, "AAA": 2, "YYY": 3, "ZZZ": 4}`), with their `rank_value` None | GREEN first run |

`uv run pytest -q tests/cobalt/test_radar_pool.py` → `14 passed in 0.77s` (12 before, +2).

**RED/GREEN, honestly: both are GREEN on their first run and there is no RED to quote** — exactly the case the prompt anticipates. There is no code change in this step to make them fail; they are regression pins of today's order, and forcing an artificial RED would have meant changing `pool.py`, which this step forbids. Their value is that the predicted rank maps were written from the key tuple BEFORE running them and matched exactly — which is itself the confirmation that the key tuple reads as claimed.

**Deliberately NOT asserted:** neither test uses the one input whose behaviour the filter changed (a name with a value on one list and `None` on another). Pinning that case would settle Dejan's L52 ruling from inside the suite — and both tests as written pass under the filtered AND the unfiltered key, so a revert does not silently break them. The test block's comment says so in the file.

**`src/cobalt/radar/pool.py` was not edited, not reverted, not re-worded, not commented.** Proven at the close below.

## ROUND 2 — 4. A4, the cutter's two missing transforms — FIXED, fixture NOT regenerated, commit `39d76af`

**RE-VERIFIED ON THE CURRENT TIP — the hub's read holds exactly, and there is NO new finding:**

| check | command | result |
|---|---|---|
| owner id in the committed fixture | `grep -c user_id tests/fixtures/replay/cards-day.real-shape.json` | **`0`** |
| any free-text spelling | `grep -c -i -E 'reason\|note\|comment\|memo\|thesis\|rationale' <same file>` | **`0`** |
| size | `wc -c <same file>` | **`7544`** — the hub's 7,544 B to the byte |
| keys, read from the file | sizings `created_at, direction, entry, id, state, stop, ticker`; transitions `at, card_id, from_state, to_state` | matches the hub's lists exactly |

**Nothing personal shipped. `facts.md` row A4's "BLOCKER framing NOT REAL" is CONFIRMED, and the residual MINOR is CONFIRMED too.** Spec-01 §3, quoted verbatim from `docs/40 - DevDocs/prompts/2026-09-19/21-packet/spec-01-plan-2026-09-15.md:249`:

> `| tests/fixtures/replay/cards-day.real-shape.json | aset_sizings + card_transitions for the STEP-0 day (unfilled crossed, unfilled uncrossed, filled, passed, ≥2 filled overlapping for rule_10) | user_id → 1; all timestamps shifted to a fixed synthetic day with intraday offsets kept; free-text reasons → "<reason>" |`

Of those three transforms, only the date shift was implemented: `_anonymize` (`tests/fixtures/replay/_cut_p4_fixtures.py:154-155` before this commit) is `_HEX_SUFFIX_RE.sub("@000000000000", _shift_dates(text))` and nothing else. Both missing transforms are key-level and cannot be done by either text pass.

**THE FIX** — `strip_personal(rows)` added to the cutter and wired into `cut_cards_day` for BOTH arrays (`strip_personal(day_cards)` and `strip_personal(_tsv_rows(trans_text))`), inside the existing `_anonymize(json.dumps(...))` sandwich so the hex scrub and the date shift are byte-identical. `user_id`/`trader_id` → `1`; `reason`/`note`/`comment`/`rationale`/`thesis` → the literal `"<reason>"`; a NULL free-text cell stays NULL (a missing note is not free text, and its nullability is part of the real shape); input rows are copied, never mutated. The docstring narrative Astra flagged is rewritten to say that all three §3 transforms are now implemented, that the raw reads select neither column so the committed cut is unchanged, and that the tickers and card ids ARE the commissioned fixture (L45 real-shape), not an anonymization gap.

**TESTS FIRST — RED, quoted** (`uv run pytest -q tests/cobalt/test_p4_asset_type_evidence.py -k "owner_id or free_text or neither_column"`, before the cutter change):

```
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_the_committed_cards_fixture_carries_no_owner_id_and_no_free_text - AttributeError: module '_cut_p4_fixtures' has no attribute 'PERSONAL_ID_FIE...
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_the_cutter_flattens_the_owner_id_and_replaces_a_free_text_reason - AttributeError: module '_cut_p4_fixtures' has no attribute 'strip_personal'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_a_row_carrying_neither_column_is_returned_unchanged - AttributeError: module '_cut_p4_fixtures' has no attribute 'strip_personal'
3 failed, 19 deselected in 0.08s
```

**GREEN after:** `uv run pytest -q tests/cobalt/test_p4_asset_type_evidence.py` → `22 passed in 0.09s` (19 before, +3).

**Honesty about the first test's RED**, since the prompt asks for it either way: the regression pin's FIXTURE assertions (the key sets, the two arrays) were GREEN from the start — the fixture is clean, exactly as the hub found. It went red only on its last two lines, which assert the fixture's keys do not intersect the cutter's declared personal-field sets, and those sets did not exist yet. **That is the stated purpose of that test: it is a regression pin, not a bug report.** It now fails the day a re-cut lets either class of column in.

**The cutter was NOT RE-RUN and the committed fixture was NOT REGENERATED.** The cutter reads `scratch/` raw exports and its run rule is not in this session's allowlist; `git diff --stat -- tests/fixtures/replay/` shows one file changed, `_cut_p4_fixtures.py` (+48/−2) — `cards-day.real-shape.json` is untouched, still 7,544 B as committed.

**Why these tests live in `test_p4_asset_type_evidence.py` (L3):** it is the one module that already loads the cutter by path (`_load_cutter`, `:69-81`). A new module would have meant a second loader for the same script.

## ROUND 2 — 5. A5, the vacuous "both merge orders" test — FIXED offline, DB run OWED, commit `9045260`

**`facts.md` row A5: CONFIRMED, both halves.**

| the row's claim | proof on this tip |
|---|---|
| `FORWARD` contains P2's 0006/0007, so the docstring's premise is false | `src/cobalt/db_migrations/__init__.py:56-57` — `MIGRATIONS_DIR / "0006_radar_score.sql",` and `MIGRATIONS_DIR / "0007_radar_cards.sql",` sit inside `FORWARD = (…)` between 0005 and 0008 |
| both parametrizations applied the same base | `test_p4_migrations.py:301` (pre-fix) `base = [p for p in FORWARD if _migration_version(p) < 8]`, outside the `if order == …`, so `p4_before_p2` already had 0006/0007 and `_simulate_p2_card_columns`'s `ADD COLUMN IF NOT EXISTS` was a no-op in it |
| the module docstring was stale | pre-fix `:9-10`: "P2's 0006/0007 are not in this tree (P2 not merged — hub report STEP-0)" |
| `_seed_membership` ran only AFTER the first apply, so the digest equality was not about pre-existing rows | pre-fix `:306` seeds after `:305` `_apply(conn, [FWD_0008, FWD_0009])` — and it could not have run earlier: its INSERT named `rank_metric,rank_value`, the two columns **0008 itself adds** |

That last point is why the seed could not simply be moved: moving the old `_seed_membership` above the first apply would have failed on columns that do not exist yet. The fix had to make a no-value seed possible.

**THE FIX — three parts:**

1. **`_merge_order_bases(order)`** returns `(applied before 0008/0009, applied after them)`. `p2_before_p4` → `(everything below 0008, [])`. `p4_before_p2` → `(everything below 0008 EXCEPT 0006/0007, [0006, 0007])`. The `@requires_db` test now uses it, and in the `p4_before_p2` half applies `p2_after` — P2's OWN migrations, not just the simulated columns — in the P2 position, before `_simulate_p2_card_columns` and the re-apply.
2. **`_membership_insert(ticker, scan_id, value)`** builds the seed statement; `value is None` names NEITHER new column, so a row can be seeded BEFORE 0008 runs. The `@requires_db` test now seeds `P4PRE` (no value) before the first apply, asserts it survives with `(rank_metric, rank_value) == (None, None)`, and only then seeds `P4A` with its non-null post-deploy value. **Every pre-existing assertion is kept** — the two `_content(...) == before` equalities, the three digest equalities, the two `to_regclass` NULL checks, the repeated-reverse no-op and the final re-apply all stand unchanged; nothing was deleted or weakened.
3. **The module docstring is rewritten** to say what is true on the rebased tree, and it records the stale claim and why it mattered rather than quietly dropping it.

**TESTS FIRST — the RED I CAN prove offline, quoted** (the helpers temporarily renamed so the new tests ran against a tree without them, then renamed back — the two new tests are the only thing that moved):

```
FAILED tests/cobalt/test_p4_migrations.py::test_the_two_merge_orders_no_longer_build_the_same_base - NameError: name '_merge_order_bases' is not defined
FAILED tests/cobalt/test_p4_migrations.py::test_a_row_can_be_seeded_before_0008_adds_its_columns - NameError: name '_membership_insert' is not defined
2 failed, 16 deselected in 0.07s
```

**GREEN after:** `uv run pytest -q tests/cobalt/test_p4_migrations.py` → `14 passed, 4 skipped in 0.04s` (12 passed before, +2; the 4 skips are the 3 `@requires_db` tests, one of them parametrized ×2).

| new offline test | what it proves without a database |
|---|---|
| `test_the_two_merge_orders_no_longer_build_the_same_base` | `FORWARD` really contains 0006/0007 (the docstring's premise is false); the two base lists are NOT equal; `p2_before_p4`'s base contains P2's versions and holds nothing back; `p4_before_p2`'s base contains NEITHER and holds back exactly `{6, 7}`; neither order's lists ever include 0008/0009 |
| `test_a_row_can_be_seeded_before_0008_adds_its_columns` | the no-value seed names neither `rank_metric` nor `rank_value` and carries exactly `(ticker, scan_id, scan_id)`; the valued seed names both and appends the value |

**THE OFFLINE BOUNDARY, STATED PLAINLY: `test_0008_0009_apply_twice_reverse_and_reapply_on_populated_membership` was EDITED BUT NOT RUN.** It is `@requires_db` and `cobalt_dev` is held by `ops-0919-db` (bg `e810326c`) for the whole of this run. Its verification — both parametrizations — is OWED to P4's later DB step and is named again in the ESCALATE section and in the stop line. What this round proves about it is what the registry and the statement builder can show; the SQL behaviour is unproven until that run.

## ROUND 2 — 6. CLOSE (OFFLINE)

**Suite — `uv run pytest -q tests/cobalt tests/taxonomy`, verbatim:**

```
1829 passed, 324 skipped, 1 xfailed, 15 warnings in 56.11s
```

Against the PREFLIGHT BASELINE `1818 passed, 324 skipped, 1 xfailed, 15 warnings in 55.69s`:

| | baseline | close | movement |
|---|---|---|---|
| failed | 0 | **0** | none — the bar this round had to hold |
| passed | 1818 | 1829 | **+11**, and every one is named below |
| skipped | 324 | **324** | **UNCHANGED** — this round added no `requires_db` test (ESCALATE R2-3) |
| xfailed | 1 | 1 | none |

**The +11, by step, by name:**

| step | test | file |
|---|---|---|
| 1 (A1) | `test_an_available_p2_with_no_formations_still_retires_the_days_predecessors` | `tests/cobalt/test_replay_runner.py` |
| 1 (A1) | `test_an_absent_p2_never_reconciles_the_formation_kind` | same |
| 2 (A2) | `test_r1_16_the_check_immediately_before_the_vault_write_is_what_refuses_a_late_run` | same |
| 2 (A2) | `test_r1_16_a_synchronous_step_is_not_cut_mid_flight_the_documented_limitation` | same |
| 3 (A3) | `test_list_union_orders_by_value_descending_then_name_when_every_value_is_present` | `tests/cobalt/test_radar_pool.py` |
| 3 (A3) | `test_a_name_with_no_value_on_any_list_sorts_after_every_name_that_has_one` | same |
| 4 (A4) | `test_the_committed_cards_fixture_carries_no_owner_id_and_no_free_text` | `tests/cobalt/test_p4_asset_type_evidence.py` |
| 4 (A4) | `test_the_cutter_flattens_the_owner_id_and_replaces_a_free_text_reason` | same |
| 4 (A4) | `test_a_row_carrying_neither_column_is_returned_unchanged` | same |
| 5 (A5) | `test_the_two_merge_orders_no_longer_build_the_same_base` | `tests/cobalt/test_p4_migrations.py` |
| 5 (A5) | `test_a_row_can_be_seeded_before_0008_adds_its_columns` | same |

11 named, 11 in the count. One existing test (`test_an_open_radar_card_for_the_formations_subject_suppresses_it_in_the_run`) had one assertion changed and still passes, so it moves no number. No other movement to escalate.

**RESTARTS — `uv run cobalt jobs restarts 2738cdc..HEAD`, VERBATIM:**

```
path	change	rule	restart
docs/40 - DevDocs/reports/s2-p4-verify-2026-09-19.md	M	DOCS	-
src/cobalt/replay/runner.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_p4_asset_type_evidence.py	M	test/documentation; no resident	-
tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_pool.py	M	test/documentation; no resident	-
tests/cobalt/test_replay_runner.py	M	test/documentation; no resident	-
tests/fixtures/replay/_cut_p4_fixtures.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```

**0 UNCLASSIFIED.** Every changed path is one this prompt named — `src/cobalt/replay/`, `tests/cobalt/`, `tests/fixtures/replay/`, `docs/40 - DevDocs/`. No `scratch/`, no `data/`, no `configs/`. The one restart is `com.cobalt.radar`, derived by static import reach from the single source file this round touched (`replay/runner.py`); it is already in the branch's standing `RESTARTS:` line from the R16 close (`com.cobalt.aset com.cobalt.radar`), so this round adds no new resident to the deploy.

**STANDING CONSTRAINT — `git diff --stat main -- src/cobalt/radar/` at CLOSE:**

```
 src/cobalt/radar/collector.py    |   4 +-
 src/cobalt/radar/config.py       |  91 ++++++++++++-
 src/cobalt/radar/evaluate_cli.py |  23 ++++
 src/cobalt/radar/models.py       |  13 +-
 src/cobalt/radar/notes.py        | 277 +++++++++++++++++++++++++++++++++++++--
 src/cobalt/radar/pool.py         |  63 +++++++--
 src/cobalt/radar/propose.py      |  42 ++++--
 src/cobalt/radar/runner.py       |   4 +-
 src/cobalt/radar/store.py        |  40 ++++--
 src/cobalt/radar/throttle.py     |  18 ++-
 10 files changed, 527 insertions(+), 48 deletions(-)
```

**BYTE-IDENTICAL to the PREFLIGHT capture above** — same ten files, same per-file counts, same `527 insertions(+), 48 deletions(-)`. Not one line was added to `src/cobalt/radar/`.

**`src/cobalt/radar/pool.py` appears ZERO times in this round's own diff** — `git diff --stat 2738cdc HEAD`:

```
 .../reports/s2-p4-verify-2026-09-19.md             |  43 ++++++-
 src/cobalt/replay/runner.py                        |   9 +-
 tests/cobalt/test_p4_asset_type_evidence.py        |  66 ++++++++++
 tests/cobalt/test_p4_migrations.py                 | 134 +++++++++++++++++---
 tests/cobalt/test_radar_pool.py                    |  54 +++++++++
 tests/cobalt/test_replay_runner.py                 | 135 ++++++++++++++++++++-
 tests/fixtures/replay/_cut_p4_fixtures.py          |  50 +++++++-
 7 files changed, 470 insertions(+), 21 deletions(-)
```

Seven paths. `src/cobalt/radar/pool.py` is not among them; the only `radar` name is `tests/cobalt/test_radar_pool.py`, a test file. `git diff --stat 2738cdc HEAD -- src tests docs` returns the identical seven, so nothing changed outside those three trees either.

**Tree — `git status --porcelain`:** empty after the report commit below. **`ls -la .env`** → `ls: .env: No such file or directory` (quoted because the file is gitignored, so `git status` could never prove its absence).

**Commits, this round, one per item:**

| sha | item |
|---|---|
| `f07b483` | A1 — the formation reconcile keyed on P2 availability (fix + 2 new tests + 1 assertion updated) |
| `b136768` | A2 — the deadline's real scope pinned (2 new tests, no behaviour change) |
| `5652260` | A3 — the pool union ordering pinned (2 new tests, `pool.py` untouched) |
| `39d76af` | A4 — the cutter's two spec §3 transforms + the fixture pinned clean (3 new tests) |
| `9045260` | A5 — the merge-order test de-vacuumed + stale docstring (2 new offline tests, `@requires_db` test edited, not run) |

`git show --stat HEAD` was read after every one; no commit carries a `scratch/` path or any path this prompt did not name.

## ROUND 2 ESCALATE

**A2 (deadline scope):** the execution deadline bounds only async work and the pre-vault-write check; formation_source() and missed.reconcile() run synchronously past it. Spec R1-16's stated bar is met (no late vault write, margin held) and runner.py:26-31 documents the design. Bounding synchronous DB work is a design change — NOT made this round. Desk/Dejan to rule before or after deploy.

**A3 (L52):** the union sort key's None-filter in radar/pool.py:189,198 was shipped undisclosed in S2-P4 STEP-2. This chunk did not touch it. Effect per this round's read: crash-removal only. Dejan's ruling owed — waive-and-disclose or revert.

**R2-1 (line number, MINOR).** The prompt's index card places the A1 guard at `runner.py:425`; on the tip it was at **`:426`**. `facts.md` row A1 says "real file 425–430", which contains it. Recorded, not silently reconciled. (The same step's fix then moved the pre-vault-write `check_deadline` from `:440` to `:447`, which is why step 2 quotes `:447` where the prompt says `:440`.)

**R2-2 (the desk's A3 pre-read is WRONG about which element this branch edited — the conclusion survives, the reasoning does not).** The pre-read states: "Pre-edit, element 2 was `-(max(<unfiltered gen>, default=0))`. Any generator containing a `None` raised `TypeError` there". `git show main:src/cobalt/radar/pool.py` shows the OPPOSITE: on main, **element 2 already carried the `is not None` filter and element 1 did not**, and `git diff main -- src/cobalt/radar/pool.py` contains exactly ONE added filter line, inside **element 1**'s generator (`pool.py:189`). So `pool.py:198` is not a new filter at all — it is P2-era code this branch never touched, and the "new filter" is one line, not two. The verdict is unchanged (every input that did not raise produces an identical key tuple — the case table in §3 above proves it for element 1), but anyone re-deriving the L52 disclosure from the pre-read's wording would be reasoning from a false premise. **The disclosure Dejan is asked to rule on should say: one added filter, in element 1, at `pool.py:189`.**

**R2-3 (A1's `requires_db` twin: NOT written, deliberately).** The branch has no per-kind `requires_db` reconcile pattern to follow — one SQL-level test exists (`test_p4_migrations.py::test_missed_rerun_reconciles_in_the_ruled_order_against_the_live_unique_index`, `kind='mover'`) and it already pins the R2-1 retirement the A1 fix makes reachable. A formation copy would be a second copy of a proven path (L3). If the desk wants one anyway, it is a rename of that test's `kind` literal.

**OWED: the first run of every `requires_db` test this branch carries — nothing in this round ran against a database.** `cobalt_dev` is held by `ops-0919-db` (bg `e810326c`) and was not connected to, migrated, rolled back or read. By name, the ones this round TOUCHED and therefore owes first:

| test | file | why it is owed |
|---|---|---|
| `test_0008_0009_apply_twice_reverse_and_reapply_on_populated_membership[p2_before_p4]` | `tests/cobalt/test_p4_migrations.py` | **EDITED this round** (A5): new base list, new pre-existing seed, new assertion |
| `test_0008_0009_apply_twice_reverse_and_reapply_on_populated_membership[p4_before_p2]` | same | **EDITED this round**, and this is the half that was vacuous — its first genuine run has never happened |

This round added NO new `requires_db` test (see R2-3), so the branch's skip count is unchanged. The branch's other `requires_db` tests were untouched here and carry whatever standing the R16 close gave them (that close ran them: `db 2136/0`) — but the two rows above have NOT been run in their current form by anyone.

**The cards fixture was NOT regenerated.** `tests/fixtures/replay/cards-day.real-shape.json` is byte-for-byte as committed (7,544 B). Only the cutter script changed. Re-cutting needs `scratch/` raw exports and a run rule this session does not have.

**Carried, not fixed this round (from `facts.md`'s own list — nothing dropped silently):**

| row | state |
|---|---|
| **A6** mixed-session fixtures can false-pass F13 | REAL, owned by build-report-2's ESCALATE 3 / ESCALATE 13. Re-cutting membership needs a production DB read this offline run may not do. Untouched. |
| **A7** K3 reads a permitted frozen HOLD as red | REAL, already ESCALATE 2. The desk owes a ruling before the deploy smoke. Untouched. |
| **A8** build-report-2 wording ("16 fund tickers blank" vs 8 distinct tickers, `build-report-2:162` vs `:149`) | REAL, MINOR. The desk's to fix before the memory fold. Untouched. |
| **A9 / A10** | carried by reference / UNVERIFIABLE FROM READS. Untouched. |

RULING OWED (one line each, for the desk to put to Dejan): **(1)** A3 — waive-and-disclose or revert the `pool.py:189` filter (L52), with R2-2's correction in the disclosure; **(2)** A2 — whether bounding synchronous replay/DB work inside the deadline becomes a design item, before or after this deploy.

MEMORY: a reconcile that retires predecessors is keyed on whether the producing step RAN, never on how many rows it produced — a row-count guard silently makes retirement conditional on there being something to insert (S2-P4 `replay/runner.py` formation step, tribunal A1) [stated 2026-09-19 · Code].
MEMORY: on a rebased branch, a test parametrized over "both merge orders" is vacuous unless its base list actually holds the other branch's migrations back — `FORWARD` already contains them, so `< 8` filters produce one case twice (S2-P4 `test_p4_migrations.py`, tribunal A5) [stated 2026-09-19 · Code].

Stop-line sha convention, as at the R16 close on this branch: it names the CODE TIP (`9045260`, step 5), and the docs-only report commits follow it (`1a93416`, then this line's own).

P4 ROUND2 9045260 | offline 1829/0 | A1 A2 A4 A5: FIXED (A2 PINNED — design gap escalated, no behaviour changed) | A3: PINNED, pool.py untouched — L52 ruling owed | RESTARTS: com.cobalt.radar | OWED requires_db: 2 | ESCALATE: 5 | cobalt_dev: untouched
