# S2-P4 chunk FY — three Grok findings (Opus 5, headless, offline)

## §0 Headline

FY-1 K3 RETAIN blindness **BUILT** · FY-2 stale `21:05` comment **BUILT** · FY-3 EXPIRED
loses its cause **BUILT**. `1714 passed, 306 skipped, 2 xfailed, 15 warnings in 52.24s` — 0 failed.
6 new tests, each red before its edit (assertions quoted in §3). No commit (hub commits).
ESCALATE 3: the brief's HOLD carve-out premise is FALSE (FY-1, §2); FY-3 changes
`inputs_sha256` for future card misses (safe only because 0009 is not deployed); one other
stale `21:05` found in a live DevDoc, not touched (§5).

## §1 Files changed

| file | change |
|---|---|
| `configs/cobalt/smoke/s2.yaml` | K3 rewritten: one statement, five counters, two graded sets |
| `src/cobalt/db_migrations/0008_radar_value_movers.sql` | comment `21:05` → `21:10` (line 12, comment only) |
| `src/cobalt/replay/cards.py` | EXPIRED carries its recorded reason/cause into `gate_detail`; candidate loader reads `reason`/`evidence`; receipt inputs carry both; docstring |
| `src/cobalt/replay/models.py` | `TransitionRow.reason` / `.cause`, both optional |
| `tests/cobalt/test_smoke.py` | 3 new tests + `k3_gaps` structural checker |
| `tests/cobalt/test_p4_migrations.py` | 1 new test + `RETIRED_SCHEDULE_LITERALS` |
| `tests/cobalt/test_replay_cards.py` | 3 new tests (one is the shape guard, green before and after) |
| `docs/40 - DevDocs/cobalt/smoke/config.md` | new section: K3 grades both writers |
| `docs/40 - DevDocs/cobalt/replay/cards.md` | EXPIRED cause section, receipt + `candidates` lines |
| `docs/40 - DevDocs/cobalt/replay/models.md` | `TransitionRow` gains two fields |
| `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` | migration prose is linted, and why that is safe |

No schema change. No migration behaviour change. Nothing ranks, scores or reaches the card.

## §2 FY-1 — K3 now grades the RETAIN path

The check is one statement, `side: system`, still `K3`:

```
WITH scan AS (SELECT max(last_scan_id) AS id FROM system.radar_pool
              WHERE pool_key = 'primary' AND last_scan_at >= {cutoff}),
admitted AS (SELECT m.rank_metric, m.rank_value,
             m.first_seen_at >= {cutoff} AS inserted_after,
             (m.left_at IS NULL AND m.last_scan_id = scan.id) AS rescanned_after
             FROM system.radar_membership m CROSS JOIN scan
             WHERE m.entered_at IS NOT NULL)
SELECT count(*) FILTER (WHERE inserted_after)                            AS post_deploy_admitted,
       count(*) FILTER (WHERE inserted_after AND rank_metric IS NULL)    AS metric_missing,
       count(*) FILTER (WHERE inserted_after AND rank_value  IS NULL)    AS value_null,
       count(*) FILTER (WHERE rescanned_after)                           AS rescanned_admitted,
       count(*) FILTER (WHERE rescanned_after AND rank_metric IS NULL)   AS rescanned_metric_missing
FROM admitted
```

`expect`: `metric_missing = 0` AND `rescanned_metric_missing = 0`. `known_if`: BOTH
population counts at 0 — the "no admitted row yet → KNOWN" semantics now hold for the
union, not for half of it. `max(...)` returns one row even with no pool row, so a missing
pool leaves `scan.id` NULL and the second set empty rather than dropping the whole result.
`expect_text` rewritten to name both sets and the caveat below.

**ESCALATE 1 — the brief's premise is factually wrong, and it matters.** The brief states
HOLD rows "do NOT touch `last_scan_id`, so they stay outside the set by construction — keep
that carve-out." They do touch it: `src/cobalt/radar/store.py:100-110`, the HOLD branch,
sets `last_scan_id=%s` exactly like RETAIN; only `rank_metric`/`rank_value` are COALESCEd.
So the carve-out is **not** available by construction, and no column distinguishes a HOLD
from a RETAIN after the write (`last_rank`, `below_cap_streak` and `sources` are all written
by both). Consequence: a pre-deploy episode HELD this scan because its only source was
degraded (`radar/pool.py:283-286`) carries its pre-deploy NULL `rank_metric` into the second
set and reads as FAIL.

I built it loud rather than blind, and named the ambiguity in `expect_text` (L1: a false
loud beats a silent miss; a `known` entry exists for exactly this and joins the list only by
Dejan's ruling). A `rescanned_metric_missing` FAIL is read against
`radar_pool.degraded_sources` before anyone rules it known. **If Dejan wants that FAIL
impossible instead, the honest fix is a discriminator on the row (a `held` flag or a
`last_ranked_scan_id` written only by RETAIN/ADMIT) — that is a schema change and was out of
this chunk's bounds.**

**Offline limit:** the SQL cannot run without a database. The structural tests below assert
the shape; `test_committed_queries_run_read_only_on_cobalt_dev` (`requires_db`, in the same
file) is where the statement must be proven to parse and run — **the DB-verification run
must confirm K3 specifically.** It exercises `CROSS JOIN`, a CTE and `FILTER`, none of which
any other committed check uses.

## §3 Tests — red before, green after

| # | test | failing assertion BEFORE the edit (verbatim) |
|---|---|---|
| 1 | `test_k3_covers_the_insert_path_and_the_retain_path` | `E assert ["query does ...ned_admitted'] == []` (gaps: `last_scan_id`, `system.radar_pool`, `last_scan_at >= {cutoff}`, `left_at IS NULL`, `no expect predicate on rescanned_metric_missing`, `no known_if predicate on rescanned_admitted`) |
| 2 | `test_the_k3_coverage_check_refuses_the_first_seen_at_only_shape` | `E assert ["query does ...ned_admitted'] == ['no expect p...tric_missing']` |
| 3 | `test_k3_grades_each_set_and_is_known_only_when_both_are_empty` | `E AssertionError: assert <Verdict.KNOWN: 'KNOWN'> is <Verdict.PASS: 'PASS'>` — the old K3 returns no `rescanned_admitted`, so a live re-scan still read as KNOWN |
| 4 | `test_p4_migration_prose_names_no_retired_schedule_literal` | `E AssertionError: 0008_radar_value_movers.sql names the retired schedule literal(s) ['21:05'] — com.cobalt.replay runs at 21:10 (2026-09-17 R17)` |
| 5 | `test_r1_11_expired_card_carries_its_own_recorded_reason_into_gate_detail` | `E pydantic_core._pydantic_core.ValidationError: 2 validation errors for TransitionRow` / `reason Extra inputs are not permitted` / `cause Extra inputs are not permitted` |
| 6 | `test_the_candidate_loader_reads_the_transition_reason_and_its_cause` | `E assert 'SELECT id, card_id, from_state, to_state, at, reason, evidence FROM card_transitions' in 'def candidates(self, trade_date: date) …'` |

`test_a_non_expired_cards_gate_detail_shape_is_unchanged` is the companion guard: it asserts
the real-shape fixture card 302's `gate_detail` keys are exactly
`["order", "rule_10", "window", "state", "trade_count_band"]` and its `state` keys exactly
`["state", "transition_id", "at", "maps_to"]`. It is GREEN before and after by design — it
exists to fail if the new keys ever leak onto a non-EXPIRED card.

Test 2 also proves the checker bites twice: the pre-fix query shape, and the shipped shape
with its RETAIN predicate removed. Test 5 does not invent the reason prose — it calls the
real `cobalt.cards.expire.radar_expiry(...)` and asserts `cause == "stop_before_arm"`, then
carries that object's own `reason`/`evidence["cause"]` through the replay and back out of
the receipt (L45: real types, no invented fixture; the fixture files were not edited).

Suite, verbatim last line:

```
1714 passed, 306 skipped, 2 xfailed, 15 warnings in 52.24s
```

`COBALT_ENV=dev uv run cobalt validate` was NOT run: the session's permission classifier
refused the env-prefixed command and a mid-run permission ask is a failed run
(PROPOSED-1), so I did not retry it. It is not in this chunk's acceptance line. The shipped
`s2.yaml` is loaded through `SmokeSuite` by five tests in the green suite, so the schema half
of `validate` is covered; the hub should still run `validate` before the merge.

## §4 FY-3 — EXPIRED keeps its gate value and gains its cause

`excluded_by` stays `window` for every EXPIRED card; `0009`'s CHECK and the vocabulary are
untouched. What is added, only when the as-of-trigger state is EXPIRED:

```
gate_detail["state"]["recorded_reason"] = <card_transitions.reason>        # verbatim
gate_detail["state"]["recorded_cause"]  = <card_transitions.evidence->>'cause'>  # verbatim
```

Both are read off the transition, never re-derived. `cards/expire.py` has three causes for
EXPIRED — `deadline` ("window closed at …"), `avoid` ("an avoid predicate turned true") and
`stop_before_arm` ("stop … touched before arm at …") — and `radar_expiry` records the cause
in `evidence`; the 16:05 `expire_due` job records its cause in the reason prose only, so
`recorded_cause` is null there. Null is the honest value for a transition written before
this shipped; nothing is computed to fill it.

Two supporting changes were required for the value to be real rather than always-null:
`MissedStore.candidates` now SELECTs `reason, evidence` (it read neither), and
`TransitionRow` gained the two optional fields.

**ESCALATE 2 — the hash answer, and the condition under which this becomes a STOP.**
`gate_detail` does **not** feed `inputs_sha256`: it lives in `receipt["outputs"]`, and
`inputs_sha256 = sha256_json(inputs)` (`replay/cards.py`). So the brief's stated STOP
condition did not fire on its own terms. But L57 does not stop at the hash: a value in
`gate_detail` that the receipt cannot reproduce is not replayable, and
`test_every_missed_number_replays_from_stored_inputs` asserts `again == miss` on the whole
row. Recording the reason only in `outputs` would have shipped a row that replays to a
different `gate_detail`. So `reason`/`cause` were added to `receipt["inputs"]["transitions"]`
as well — **which does change `inputs_sha256` for every card miss computed from now on.**

That is safe here, and only here: `0008`/`0009` are not on `main`
(`git diff --stat main...HEAD -- src/cobalt/db_migrations` shows both as additions), so
`"user".missed` does not exist in production and no stored receipt can be mismatched. **If
P4 is deployed before this chunk merges, this item becomes a STOP** — a rerun of a past day
would then see every card row's `inputs_sha256` changed, retire it and write a `run_seq + 1`
successor for a change that altered no number. The hub must confirm the merge order.

## §5 Remaining `21:05` hits, classified

Fixed: `src/cobalt/db_migrations/0008_radar_value_movers.sql:12` (the only hit under `src/`).
No file-content checksum exists in the runner —
`grep -n -i "sha256\|checksum\|hash" src/cobalt/db_migrations/{__init__,cli}.py` returns only
`cli.py:73-74`, column names inside `TABLE_DIGEST_EXCLUDED_COLUMNS`, i.e. digests of table
DATA. Nothing else was changed.

| file | n | class |
|---|---|---|
| `docs/40 - DevDocs/cobalt/radar/notes.md:22` | 1 | **STALE** — "the scheduled one-shots … (the 20:30 archiver, the 21:05 replay)" describes the CURRENT total-demand gate. Live DevDoc, wrong number. Not in my scope; recommend the hub fix it with the notes.py page. |
| `configs/cobalt/jobs.yaml:204` | 1 | historical — "moved 21:05 -> 21:10 by R17", the record of the move |
| `docs/40 - DevDocs/cobalt/replay/__init__.md:4` | 1 | historical — same sentence shape |
| `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` | 1 | historical — my own new paragraph, quoting the comment this chunk fixed |
| `tests/cobalt/test_replay_demand.py` | 6 | intentional — L53's refusal proof rolls the replay BACK to 21:05 to prove the overlap is refused. Deleting these would delete the proof. |
| `tests/cobalt/test_smoke.py:118` | 1 | historical — fixture comment, "R17 moved it from 21:05" |
| `tests/cobalt/test_p4_migrations.py` | 5 | unrelated — `'2040-01-03 21:05+00'` timestamp literals in seed rows (3), plus my 2 new `RETIRED_SCHEDULE_LITERALS` occurrences |
| `tests/fixtures/replay/membership-day.real-shape.json` | 3 | unrelated — real-shape timestamps, never edited (L45) |
| `tests/fixtures/radar/bars-rubberband.real-shape.json` | 1 | unrelated — a bar timestamp |
| `docs/40 - DevDocs/plans/plan-s2-p4-2026-09-15.md` | 8 | historical — the plan as written before R17; a dated artifact |
| `docs/40 - DevDocs/prompts/**` (7 files) | 12 | historical — dated dispatch text |
| `docs/40 - DevDocs/reports/**` (16 files) | 36 | historical — dated record, never rewritten |
| `ops/` | 0 | — (`ops/com.cobalt.replay.plist` already carries Minute 10) |

`tests/cobalt/__pycache__/*.pyc` also match; build artefacts, ignored.

## §6 ESCALATE

1. **K3's HOLD ambiguity is real** (§2). The brief's carve-out premise is false against
   `radar/store.py:100-110`. K3 can FAIL on a degraded-source night for a pre-deploy held
   row. Ruling needed: accept the loud false positive with the `expect_text` procedure, or
   add a row-level discriminator (schema change, separate chunk).
2. **FY-3 changes `inputs_sha256` going forward** (§4). Harmless only while `0009` is
   undeployed. Confirm P4 has not deployed before merging; if it has, revert the
   `receipt["inputs"]["transitions"]` half and re-open the item.
3. **`docs/40 - DevDocs/cobalt/radar/notes.md:22` is stale** (§5) — a live DevDoc still
   names a 21:05 replay in the demand-gate description. Left untouched per the brief.

Also for the DB-verification run: K3's statement is the only committed check using a CTE,
`CROSS JOIN` and `FILTER`, and has never run against Postgres.
