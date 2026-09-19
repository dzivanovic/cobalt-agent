# S2-P4 build 2 — 2026-09-18

DO NOT STOP until BUILT / FAILED. Hub: Sonnet 5, seat `p4-e2-0918`, unattended (R5 09-17 06:03, R6 09-17 06:11, R17 09-17 08:38, R1 list (3) 09-18 06:46, R7 09-18 11:24). OFFLINE by design: no `.env`, no database, no migration.

## §0 Headline
- P4 rebased onto P2 (`976528f`, 4 conflict stops, Opus-resolved); **E2 BUILT** (R1-21 positive half against P2's shipped contract); K8 split + wrapper doc fixed; **Asset Type item STOPPED and ESCALATED** (the real-shape fixture has no such column); 8 Grok findings settled (4 real: 3 fixed, 1 escalated · 4 not real).
- Offline suite `1714 passed, 306 skipped, 2 xfailed, 0 failed`; leak test passes; RESTARTS `com.cobalt.aset com.cobalt.radar`, 0 UNCLASSIFIED.
- **`sprint-2/cards` was rewritten under this run** (desk's stack, tip `db950b5`); P4 sits on the OLD `976528f` lineage — ESCALATE 1.
- ESCALATE: 12. OWED: DB verification + rollback round-trip + second-house re-review, after P2 is on main.

## AUTHORIZATION (verified by this session)
| check | evidence |
|---|---|
| R5 / R6 / R17 committed on main | `cto-2026-09-17.md` rows R5 (06:03), R6 (06:11 "approve."), R17 (08:38 "50 is approved.") |
| R1 (09-18 06:46) list (3) | `cto-2026-09-18.md` R1 |
| the ONE new rule `Bash(git rebase sprint-2/cards)` | `cto-2026-09-18.md` R7 (11:24 "Approved", item (1)), committed `5476410` on main |
| proof of commit | `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` → `5476410`, `77b1a08`, … |
| mismatch | none |

## PREFLIGHT
| probe | result |
|---|---|
| `git status --porcelain` | empty |
| `claude -p --model claude-opus-5 "Reply with exactly the word OK"` | `OK`, no usage-limit message (L47) |
| `git -C /Users/cobalt/cobalt status --porcelain` | ` M docs/40 - DevDocs/reports/seat-usage.md` — not this session's, untouched |
| `uv run pytest --co -q tests/cobalt/test_replay_runner.py` | 23 collected |
No denial during the run. One thing worth knowing: the headless builders' own `COBALT_ENV=dev uv run cobalt validate` was refused by their classifier (chunks E2 and FY); the hub did not run it either (no `.env` this run) — OWED.

## §1 Rebase onto P2
| item | value |
|---|---|
| HEAD before / after | `2d954a5` / `f699478` (before the E2/FX/FY commits) |
| own commits above the base | 23 before = 23 after (`git log --oneline 976528f..HEAD` read in full) |
| P2 tip at 1.1 (what the rebase used) | `976528f` (expected) |
| P2 tip at 14:48 ET | `db950b5` — rewritten stack, merge-base with HEAD now `e12417d` |

Four conflict stops, each ONE Opus headless run (briefs `scratch/rebase-brief-*.md`, notes `scratch/rebase-resolve-*.md`), hub-verified (`git diff --check`, no markers in src/tests/configs/docs, suite):
| stop | replaying | resolution |
|---|---|---|
| 1 (4/23) `2dba001` | 7 files: panel, cards cli/store, migrations `__init__`/placement, 2 tests | both sets: 0006/0007 (P2) + 0008/0009 (P4); one `_named()` helper (L3); merged `fill()` = P4's single-transaction pick under SAVEPOINT + P2's `before_commit`. Run 1b fixed 3 position-pinned tests by name/union (no assertion weakened). Suite then 1564 passed / 0 failed |
| 2 (6/23) `0c95cd1` | 5 DevDocs pages | both sections kept |
| 3 (8/23) `b8311a9` | `radar/notes.py`, `propose.py`, `settings/cli.py`, DevDocs notes | L53: ONE demand computation (P2's `plan_transport_demand` feeds P4's gate via `rpm=demand.steady_rpm`), both refusals survive; `--card` + `--optional` loaders both kept |
| 4 (10/23) `1424e98` | `BACKLOG.md` | both items kept |

Suite right after the rebase: `6 failed, 1673 passed` — the prompt's 1.3 wants 0. All six were `test_replay_runner.py`, one cause (P4's adapter, written for an absent P2, meeting P2's shipped `ReplayFormation`) = step 2's subject; recorded, then fixed by E2.

## §2 Chunk E2 — commit `4ec98f1` (builder report `s2-p4-build-opus-E2-2026-09-18.md`)
| item | result |
|---|---|
| P2's SHIPPED contract (recorded before code, from the tree) | entrypoint `cobalt.radar.evaluate_cli.replay_formations(day, *, pool_key, slug_filter, radar_store, defs_source, daily_source, tunables, defaults, clock, out)` → `ReplayReport`, read-only; marker `cobalt.radar.evaluate.EVALUATOR_VERSION = "s2p2.1"`; returned type `ReplayFormation` |
| plan vs shipped | plan lines 184/189 say `cobalt.radar.evaluate`; shipped is `evaluate_cli` + marker in `evaluate`. Code follows the tree, both imports static (L42), no two-name shim (L3). Plan text is wrong → ESCALATE 2 |
| fields 0009's CHECK needs | `ReplayFormation` gained `membership_id`, `trade_def_md5`, `score_inputs_sha256` — all values `evaluate_member` already returned; additive, P2's own tests untouched and green; no schema change, no nullable shortcut → no STOP |
| binding | `replay/formations.py` (new): two same-day formations persist under the extended key (`formation_at` + member); an open radar card for (member, def, direction) suppresses; cf-R through the ONE formula (`counterfactual` extracted from `replay_card`, both call it) |
| tests | `test_replay_formations.py` 21 (20 pass, 1 `requires_db` skip), 5 new runner tests; the six reds green — the five "run order" tests now inject an explicit `unavailable_formations`, the sixth simulates absence at the import itself (exact line, no rows kept). `test_r1_21_a_present_but_incompatible_p2_fails_loud` kept and strengthened: it had been passing for the wrong reason (`sys.modules` injection does not override `import a.b.c as x`) |
| tests-first evidence | new formations file red at collection (`ModuleNotFoundError`); runner tests' red quoted; one regression guard honestly marked "no red"; the builder's sandbox refused `git restore`/`patch -R`, so three per-test reds are indirect — stated in its report §6.3 |
| hub verification | suite re-run by the hub `1704 passed, 306 skipped, 2 xfailed`; `git diff --stat` 14 files +674/−100 + 4 new; no fixture/migration/config touched |

## §3 Chunk FX — commit `5f72185` (`s2-p4-build-opus-FX-2026-09-18.md`)
| item | result |
|---|---|
| (a) smoke K8 | split: **K8.1** (`job_row`, system side: `input_stale = 0`, `trade_date`, `card_misses` printed) + **K8.2** (`sql`, user side: `incomplete = 0`, `card_rows` printed). NO grant, no migration (desk ruling, L32). The framework carries no value between checks, so `card_rows = job.card_misses` is now a printed-number hand comparison → ESCALATE 4. Test reads the SHIPPED yaml + the shipped migrations (granted set parsed from `GRANT` statements, not hard-coded) and fails on K8-as-it-was (bite proof); 2 of 3 new tests red before the edit, the third is the bite proof (passes by construction, said so) |
| (b) `REQUIRED_HEADERS` / Asset Type | **STOPPED by the hub, ESCALATE 3.** Fixture `tests/fixtures/replay/movers-gainers.real-shape.csv` (and `-losers`) real header row, verbatim: `"No.","Ticker","Industry","Country","Exchange","Market Cap","P/E","Shares Float","Insider Ownership","Institutional Ownership","Short Float","Short Interest","Performance (5 Minutes)","Average True Range","Shortable","Gap","Average Volume","Relative Volume","Volume","Price","Change"` — no `Asset Type`. Not invented; `movers.py` untouched. **Commit `5f72185`'s subject still says "movers requires Asset Type" because the prompt dictated that text; that part was NOT built.** |
| (c) wrapper heartbeat doc | docstring + DevDoc now state `timeout_s / jobs.heartbeat_fraction`, worked example from shipped numbers (`2400 / 3 = 800 s`); docs only |
| hub verification | suite `1707 passed, 306 skipped, 2 xfailed` (hub-run); s2.yaml/wrapper diff read |

## §4 The eight findings nobody verified (hub, from the code, L35)
| # | Grok's claim | read | verdict | evidence / disposition |
|---|---|---|---|---|
| 1 | MAJOR `radar/notes.py:421` `load_sources` catches `TotalDemandExceeded` into `pool_error` instead of refusing | `radar/notes.py:59-65,412-451`; `radar/runner.py:186,243,364-374` | **NOT REAL** | `pool_error` makes `ParsedSources.frozen`; the runner passes `None` blocks to `decide(...)` when frozen and reports `degraded` — a designed refusal that reaches the scan path (unchanged after the merge with P2's plan) |
| 2 | MAJOR K3 keys on `first_seen_at`, misses a RETAIN'd pre-deploy row | `configs/cobalt/smoke/s2.yaml` K3; `radar/store.py:88-110` | **REAL** (small) — FIXED `91a689d` | plan STEP-9 R1-19 says "re-scanned after deploy"; the RETAIN branch writes `rank_metric` unconditionally. K3 now grades both writers. **The SQL has never run on Postgres, and HOLD also writes `last_scan_id` (my brief's carve-out premise was wrong — the builder caught it), so a degraded-source night can read as a false FAIL** → ESCALATE 6 |
| 3 | MAJOR K9 `full_sides eq true` has no short-export tolerance | `s2.yaml` K9; plan line 230 ("or fewer with export evidence") | **REAL** (larger) — ESCALATE 8 | plan allows a short side with export evidence; the smoke fails it loud and defers to a hand compare of the cached export. Fix needs the replay `job.result` to record per-side export row counts (a result-shape change) — proposal: K9 compares `count = min(top_n, exported_rows)` from the job result. Not built (touches the replay result contract) |
| 4 | MINOR `0008_radar_value_movers.sql:12` says "21:05 replay" | file; `db_migrations/cli.py` (digests are of table data, no file checksum) | **REAL** — FIXED `402bfc0` | comment only; new test forbids the retired literal in 0008/0009 prose |
| 5 | MINOR `replay/cards.py:97` EXPIRED → `window` for every reason | `replay/cards.py:91-97,282-289`; `cards/expire.py` (three causes: deadline / avoid / stop_before_arm) | **REAL** (small) — FIXED `b088b17` | `excluded_by` stays `window` (0009's vocabulary untouched); the transition's recorded `reason`/`cause` now ride in `gate_detail["state"]`. **Changes `inputs_sha256` for card misses computed from now on — safe only while 0009 is undeployed** → ESCALATE 7 |
| 6 | MINOR `archiver_precondition` historical branch: a later clean row satisfies a past `--date` | `replay/runner.py` `archiver_precondition` docstring | **NOT REAL** | documented design ("`cobalt_jobs` keeps one row per label … bar coverage is still checked per ticker"); the compensating control is the R1-12 coverage check → `input_stale`, asserted 0 by K8.1 |
| 7 | MINOR picks: CLI joins `transition_id`, K6 joins `card_id` | `0009_picks_missed.sql:19-20`; `s2.yaml` K6 | **NOT REAL** | `picks.card_id` is `UNIQUE`; equivalent today, and a second pick for one card could not be inserted at all |
| 8 | MINOR `replay/line.py:90` cf-R Σ is a number on an empty day | `replay/line.py:92-96` | **NOT REAL** | L8: the sum always carries its `n` (`+0.0R, n=0`); the average refuses below 30 (`avg: insufficient data (n<30)`) |

Restated for the desk (design questions, nothing built):
- **Followup ESCALATE 3 — replay window seam (DESIGN QUESTION).** `MissedStore.candidates()` (and now the formation path) has no way to pass a card's real window / trade_def into replay, so every replay horizon is the session close; the live path (`cards/expire.py`) has an injectable `trade_def_ref_for`. Harmless today (no card carries a trade_def); whoever builds the trade_def-attachment detector must wire both seams together or replay diverges from live.
- **Followup ESCALATE 5 — L53 gate scores declared windows (DESIGN QUESTION).** `check_scheduled_demand` scores each subject's DECLARED window, never wall-clock now. The nightly path is safe (`archiver_precondition` refuses unless tonight's archiver row is `done`); a human running `cobalt replay nightly --date <past day>` during market hours passes the gate while firing real Finviz traffic beside the resident. Decision: teach the gate wall-clock awareness, or rule "no manual historical replay during market hours".

## §5 Close (offline)
- `uv run pytest -q tests/cobalt tests/taxonomy` → **`1714 passed, 306 skipped, 2 xfailed, 15 warnings in 51.96s`** (0 failed).
- Leak test `test_screen_filter_values_live_only_in_approved_radar_fixtures` → **`1 passed, 1737 deselected`**.
- `uv run cobalt jobs restarts 976528f..HEAD` (P4's own range; `sprint-2/cards..HEAD` is now wrong — the ref moved and shows the stack's `ops/cto-desk.sh` deletion as UNCLASSIFIED, not P4's): **0 UNCLASSIFIED.** Non-docs/non-test rows verbatim:
```
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/smoke/s2.yaml	A	operator command (cobalt smoke); no job reads	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
ops/README.md	M	operations documentation; no resident	-
ops/com.cobalt.replay.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.replay	-
src/cobalt/**  (archiver, aset, cards, cli, dayopen, db_query, jobs, radar, replay, settings, smoke)	M/A	static import reach	com.cobalt.aset and/or com.cobalt.radar (no other resident)
src/cobalt/db_migrations/000{8,9}*.sql (+ rollbacks)	A	non-Python src asset	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
  (Full per-path table: `uv run cobalt jobs restarts 976528f..HEAD`, deterministic; docs/tests rows are `-`.)
- One more docs fix folded into the close commit: `docs/40 - DevDocs/cobalt/radar/notes.md:22` "21:05 replay" → "21:10" (FY found it; stale after R17).

## OWED (this run was offline; nothing below has run)
DB verification on `cobalt_dev` after P2 is on main: migrate 0008/0009, the rollback round-trip (`--down-to 0005` then forward, digests), `cobalt validate` (both builders were refused it), and specifically: `test_two_formation_rows_land_under_the_live_unique_index`; `test_card_checks_index_and_receipt_immutability_on_cobalt_dev` (rolls back to 0005 and re-applies only 0006/0007, so with 0008/0009 registered it drops P4's objects — passes in a rolled-back transaction, confirm); K3's new SQL (only committed check with a CTE + `CROSS JOIN` + `FILTER`); `MissedStore.candidates()`'s new `reason, evidence` SELECT; then the second-house re-review.

## ESCALATE (12)
1. **`sprint-2/cards` was rewritten during this run** (desk's stack: ops-0918 + P2, tip `db950b5`, gate second run). P4 is rebased onto the old `976528f`. P2's code is unchanged by the stack (a fixture row + ops commits), so E2 binds to the same contract. The next rebase must be onto MAIN after the stack lands; a re-rebase onto the new branch would drop the patch-identical old P2 commits and re-hit the ops-side files. Desk's call.
2. **Plan lines 184/189 name the wrong entrypoint** (`cobalt.radar.evaluate`); shipped = `cobalt.radar.evaluate_cli.replay_formations` + `cobalt.radar.evaluate.EVALUATOR_VERSION`. Plan needs the correction; code follows the tree, no shim.
3. **Movers `Asset Type` (Grok MAJOR, plan line 191):** the L45 real-shape fixtures (`tests/fixtures/replay/movers-{gainers,losers}.real-shape.csv`, header row quoted in §3) have NO `Asset Type` column, so either the plan's "required headers `Ticker, Change, Asset Type, Volume`" is wrong or the `v=152` export is the wrong view. Consequence today: every mover is `asset_type = "unreported"` and stays in the benchmark, so the non-equity drop the plan wants never runs in production. Ruling needed: a different export view that carries it, or a benchmark rule without it.
4. **K8/K9 tenancy reading + a lost machine assertion.** (a) `counts_agree` (card rows = job `card_misses`) is now a hand comparison of two printed numbers; restoring it needs a new smoke check kind that compares two checks — a framework build, ruled first. (b) Desk wording "no user-side query names a `system.` relation" read literally also forbids K9's read of `system.movers_daily`, which 0008 grants to `cobalt_user` on purpose (the `missed.mover_id` FK); implemented as "user-side may name a `system.` relation exactly where a migration GRANTs it". Confirm or say split K9 too.
5. **Same defect class as K8, wider (no migration touched):** 0001's schema-wide grant ran before 0002 moved the tables into `system`, so `cobalt_user` has SELECT on none of `bars`, `cobalt_jobs`, `cobalt_kill_switch`, `cobalt_redactions`, `cobalt_email_sends`, `session_blocks`, though 0001's comment says user-side jobs read `bars`. No smoke check names them; any user-side reader of `system.bars` would fail the way K8 did. Migration-level ruling.
6. **K3 (commit `91a689d`, revertable alone):** SQL never run on Postgres; HOLD rows also write `last_scan_id` (`radar/store.py:100-110`) so a degraded-source night can read K3 red on a held pre-deploy NULL. Accept the loud false positive (procedure in `expect_text`: read against `radar_pool.degraded_sources`), or add a row-level discriminator (schema change, its own chunk), or revert the commit. My brief's "HOLD stays outside by construction" premise was wrong; the builder found it.
7. **FY-3 (commit `b088b17`) changes `inputs_sha256` for card misses computed from now on** (reason/cause also enter the stored inputs so the row replays, L57). Safe only while 0009 is undeployed (`"user".missed` absent in production). If P4 deploys before this merges, revert the `receipt["inputs"]["transitions"]` half.
8. **K9 short-side (REAL, larger):** proposal in §4 row 3 — record per-side export row counts in the replay `job.result`, K9 compares `count = min(top_n, exported)`.
9. **E2 receipt reference is content-addressed**, not a row id: P2's read-only replay reads no `system.radar_score` row, so a formation's receipt carries `(membership_id, trade_def_md5)` + `inputs_sha256`. Enough to resolve and to detect divergence; a hard FK would be a P2-side change plus a `missed` schema change — a ruling, not a build decision.
10. **Test sweep worth doing:** any test that injects a module through `sys.modules` alone injects nothing when the code does `import a.b.c as x` (E2's builder found `test_r1_21_a_present_but_incompatible_p2_fails_loud` passing for the wrong reason).
11. **DESIGN QUESTION (followup 3): replay window seam** — restated in §4; formation horizons are session close for the same reason (E2 builder ESCALATE 4).
12. **DESIGN QUESTION (followup 5): L53 gate vs wall-clock** — restated in §4.

BUILT 9c4284c (code b088b17) | on sprint-2/cards 976528f (branch since rewritten to stack db950b5 — ESCALATE 1) | offline: 1714 passed, 0 failed | E2: built | fixes: K8 y · Asset Type ESCALATED · wrapper doc y | findings: 4 real (3 fixed) / 4 not real / 2 design | OWED: DB verification + rollback round-trip + second-house re-review, after P2 is on main | ESCALATE: 12
