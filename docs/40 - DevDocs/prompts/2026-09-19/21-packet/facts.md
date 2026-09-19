# P4 build — desk-precomputed facts (2026-09-19, for `review-p4-0919`)

All counts only (L32) — no ticker, no fixture row content quoted here.

## Identity
| item | value |
|---|---|
| branch | `sprint-2/p4` (worktree `/Users/cobalt/cobalt-wt/s2-p4`) |
| tip (as verified) | `d5947e7` (docs-only, fills the READY line's close-commit sha) |
| stop line's own `<close commit>` | `4cc6859` (the commit the READY line names; `d5947e7` is ONE further docs-only commit written after it, same pattern as the archiver branch's own report-fills-its-own-sha step) |
| code tip named in the stop line | `a59ee8c` (`fix(s2-p4): two dev-DB reds are test-side …`) |
| merge-base(main, sprint-2/p4) | `919d562002ade9195203969dbb6c6c5c6e8db50a` |
| main at verification time | `a89105f` (24 desk docs-only commits after `919d562`; `git diff --stat 919d562 main` touches only `docs/`) |
| commits `main..sprint-2/p4` | **45** (`git rev-list --count main..sprint-2/p4`) — the report's own §5 table itemizes 31 (step 1.3, rebased P4-own commits) + 12 (this run's chunks) + 2 close-commits (`4cc6859`, `d5947e7`) = 45 |
| worktree | clean (`git status` / `status --porcelain=2` both empty); untracked = `scratch/` (build briefs, raw TSVs, patches — none ever committed) + the usual `.venv`/`__pycache__`/cache dirs, all `git-ignored` |
| `.env` | absent (`ls -la .env`: No such file or directory) |

## L35 artifact checks
- `git show --stat` of every one of the 45 commits `main..sprint-2/p4`, scanned by script: **zero** hits for a `scratch/` path or a `.env` path in any commit.
- Three-dot diff `main...sprint-2/p4` touches only `configs/`, `docs/`, `ops/`, `src/`, `tests/` — nothing outside those five top-level trees.
- New config file check: only new file under `configs/` is `configs/cobalt/smoke/s2.yaml` (an ADD) — it sits under `configs/cobalt/`, the sanctioned new-core path (not a boundary violation). `configs/cobalt/jobs.yaml` and `configs/cobalt/taxonomy/tunables.yaml` are EDITS to existing files, not new files.

## Three-dot diff-stat (`git diff --stat main...sprint-2/p4`)
157 files changed, 44,153 insertions(+), 190 deletions(-). Non-docs (`src tests configs ops`) portion = **1,580,632 bytes** (verified: sum of the packet's 23 `code-*.diff`/`.partN.diff` files = 1,580,632, exact).

| area | bytes (src/tests/configs/ops diff only) | packet file(s) |
|---|---|---|
| `src/cobalt/radar/*` (9 files) | 42,135 | `code-01-radar.diff` |
| `src/cobalt/replay/{__init__,cli,formations,line,models}.py` | 47,524 | `code-02-replay-core.diff` |
| `src/cobalt/replay/{movers,runner,cards}.py` | 82,494 | `code-03-replay-movers-runner-cards.diff` |
| `src/cobalt/smoke/*` (6 files) | 59,902 | `code-04-smoke.diff` |
| `src/cobalt/{cards,aset,settings,jobs,archiver,dayopen}/*`, `src/cobalt/cli.py`, `src/cobalt/db_query.py` | 65,314 | `code-05-cards-aset-settings-jobs-archiver-dayopen-misc.diff` |
| `src/cobalt/db_migrations/{0008,0009}*.sql`, `.rollback.sql`, `__init__.py`, `cli.py`, `placement.py` | 14,663 | `code-06-migrations.diff` |
| `configs/*`, `ops/*` | 29,510 | `code-07-configs-ops.diff` |
| `tests/cobalt/test_radar_*.py` (12 files) | 32,570 | `code-08-tests-radar.diff` |
| `tests/cobalt/test_replay_{cards,demand,formations,line}.py` | 65,033 | `code-09-tests-replay-a.diff` |
| `tests/cobalt/test_replay_{movers,runner}.py` | 56,812 | `code-10-tests-replay-b.diff` |
| `tests/cobalt/test_smoke*.py`, `test_tenancy.py`, `test_settings_optional.py`, `test_finviz_consumers.py`, `test_jobs_restarts.py` | 93,448 | `code-11-tests-smoke-tenancy-settings-finviz-jobs.diff` |
| `tests/cobalt/test_{cards,cards_picks,aset_store,aset_web,p4_asset_type_evidence,p4_migrations}.py` | 62,607 | `code-12-tests-cards-p4.diff` |
| `tests/fixtures/replay/_cut_p4_fixtures.py` (the cutter — CODE, kept; it is the only file under `tests/fixtures/` that is not fixture data) | 25,996 | `code-13-fixtures-cutter-script.diff` |

**KEPT TOTAL: 678,008 bytes across 13 files, none over 100 KB** (largest is `code-11` at 93,448). No `.partN` split needed once fixture data is out — revised down from the original 23-file/1,580,632-byte packet (2026-09-19, coordinator instruction: a reviewing house must Read→Write and hold every packet file in context; 1.58 MB was too much, and five of the six removed files were pure recorded-session DATA, not logic).

## EXCLUDED FROM THE PACKET (data, not logic)
| path | bytes in the full diff | what it is | which test reads it |
|---|---|---|---|
| `tests/fixtures/radar/pool-metrics.real-shape.csv` | 25,891 | a re-cut real-shape day of radar pool-metrics rows (L45 fixture, attribution/dates stripped) | `test_radar_pool.py`, `test_radar_panel.py` (via `code-08-tests-radar.diff`, kept) |
| `tests/fixtures/replay/bars-day.real-shape.json` | 249,904 | a re-cut real-shape trading day of bar rows | `test_replay_line.py`, `test_replay_formations.py` (via `code-09-tests-replay-a.diff`, kept) |
| `tests/fixtures/replay/cards-day.real-shape.json` | 8,112 | a re-cut real-shape day of card/transition rows | `test_replay_cards.py` (via `code-09-tests-replay-a.diff`, kept) |
| `tests/fixtures/replay/membership-day.real-shape.json` | 498,478 | the 09-14 anchor day's radar-pool membership rows (14,407 lines) — ESCALATE 3 of the build report: now a DIFFERENT session than the re-fetched movers fixtures below | `test_replay_runner.py`, evidence tests (via `code-10-tests-replay-b.diff` / `code-12-tests-cards-p4.diff`, kept) |
| `tests/fixtures/replay/movers-gainers.real-shape.csv` | 58,672 | the 09-19 re-fetch, cut to 60 rows / 151 columns (this run's own AT-1 chunk) | `test_replay_movers.py`, `test_p4_asset_type_evidence.py` (via `code-10`/`code-12`, kept) |
| `tests/fixtures/replay/movers-losers.real-shape.csv` | 61,567 | same re-fetch, losers side | same as above |
| **EXCLUDED TOTAL** | **902,624** | | |

**Byte-sum proof: kept 678,008 + excluded 902,624 = 1,580,632 = the original full three-dot diff, exact.** A finding that needs to read inside one of these six files' actual row content is `UNVERIFIABLE FROM PACKET` for the reviewer; the hub verifies it directly with `git -C /Users/cobalt/cobalt show sprint-2/p4:"<path>"` (covered by the launch line's `show*` rule) rather than staging the data.

## Specs NOT in the packet (coordinator decision, 2026-09-19: one review run, no A/B split — the houses' meters are scarce, keep to the two specs a verdict actually needs)
Only `spec-01-plan-2026-09-15.md` (the Astra-reviewed plan — design intent) and `spec-06-verify-2026-09-19.md` (`13-p4-verify.md`, today's verify prompt — what produced the current tip) are staged. The three intermediate build prompts are NOT in the packet; the hub pulls one only if a specific finding needs it:
| spec | where | pull with |
|---|---|---|
| `2026-09-17/01-p4-build.md` (chunks A/B/C/D shape) | on `main` | `git -C /Users/cobalt/cobalt show main:"docs/40 - DevDocs/prompts/2026-09-17/01-p4-build.md"` |
| `2026-09-17/04-p4-relaunch.md` (movers-fetch script shape) | on `main` | `git -C /Users/cobalt/cobalt show main:"docs/40 - DevDocs/prompts/2026-09-17/04-p4-relaunch.md"` |
| `2026-09-18/01-p4-followup.md` (E2 + K8 fixes, conflict procedure) | on `main` | `git -C /Users/cobalt/cobalt show main:"docs/40 - DevDocs/prompts/2026-09-18/01-p4-followup.md"` |
| `2026-09-18/08-p4-e2-fixes.md` | on `main` | `git -C /Users/cobalt/cobalt show main:"docs/40 - DevDocs/prompts/2026-09-18/08-p4-e2-fixes.md"` |
| `docs/40 - DevDocs/reports/s2-p4-build2-2026-09-18.md` (predecessor's own build report — its content IS staged in full as `build-report-1-build2-2026-09-18.md`, so no pull needed) | on `sprint-2/p4` only | `git -C /Users/cobalt/cobalt show sprint-2/p4:"docs/40 - DevDocs/reports/s2-p4-build2-2026-09-18.md"` |
All four missing prompts are reachable read-only from `/Users/cobalt/cobalt` under the launch line's existing `show*` rule (no new rule needed); the last three need the `sprint-2/p4` branch ref named explicitly (lesson (b)) only where the path is branch-only — the four prompt files above are all on `main` and need no branch ref.

## R16 (ruled 2026-09-19, 11:05 ET — after this build's own stop line, NOT part of what you are checking today)
Dejan ruled fund rule **C**: not-equity = `Asset Type` non-blank **OR** `Industry` = `Exchange Traded Fund` (covers the 5,702 fund tickers the non-blank rule alone would catch, plus the 8 with a blank `Asset Type`; 0 stock rows hit on the sample). It is being built as a SEPARATE tests-first chunk on `sprint-2/p4` (prompt `24-p4-fund-rule.md`, rules ⊆ `13`'s) and will change `configs/cobalt/radar.yaml`'s `not_equity` shape once it lands — a config-shape change → RESTARTS `com.cobalt.radar`. **That chunk is not in this packet and not built yet** (`facts.md`'s confirmation above — `not_equity`/`REQUIRED_HEADERS` untouched — is still accurate for what you are reading); it will come back to the houses as a FOLD round on this same check once it commits. Do not score today's `Asset Type: ESCALATED` as a defect — ESCALATING was the correct, evidence-bound outcome of the code you are reading; R16 is the desk's follow-up decision, made afterward.

**L32 ticker check (no silent redaction):** none of the six EXCLUDED files' content is in the packet. Of the KEPT files, two test-code diffs embed real ticker strings taken from the branch's own committed fixtures: `code-08-tests-radar.diff` (`"NVDA"`, `"MSFT"`, alongside synthetic placeholders `"AAA"`/`"BBB"`/`"CCC"`) and `code-10-tests-replay-b.diff` (`"IMCC"`, `"QNME"`, `"REFR"`, `"MU"` — real, less-common small-cap tickers, e.g. `test_replay_movers.py` asserting `by_ticker["QNME"].excluded_by == "not_in_any_source"`). These are already committed on `sprint-2/p4` today (not new exposure from this packet) and are drawn from the Finviz **whole-market movers/radar screener export** (a public top-gainers/losers scan), not from Dejan's personal DAS trading screens — the specific thing L32 protects. Flagged here rather than redacted, per instruction; the desk can judge whether that distinction holds.

## Row-by-row evidence (Q from Task 1(d))
| row | claim | file:line evidence |
|---|---|---|
| 2 | plan text corrected in place, old wording kept | `docs/40 - DevDocs/plans/plan-s2-p4-2026-09-15.md:185` and `:191` — two `[corrected 2026-09-19 — cto-2026-09-18.md §21 row 2 …]` blocks, both directly under the original sentence, which stays |
| 4 | `kind: compare` machine assertion; K8.3 = K8.1 vs K8.2 | `src/cobalt/smoke/models.py:84` `class CompareOp(str, Enum)`, `:279` `class CompareCheck(_Check)`, `:289` `kind: Literal["compare"]`; grader at `src/cobalt/smoke/checks.py:631`; shipped in `configs/cobalt/smoke/s2.yaml:262` `- id: K8.3` / `:265` `left: K8.1` / `:266` `right: K8.2` |
| 6 | K3's SQL runs on Postgres; HOLD ambiguity confirmed | `tests/cobalt/test_smoke_k3_sql.py:87` `test_k3_statement_parses_and_returns_its_five_counters_on_cobalt_dev`, `:98` `test_k3_hold_row_reads_red_documented_ambiguity` — both `requires_db`, run once against `cobalt_dev` per the build report §4.6: `2 passed in 0.18s` |
| 8 | K9 compares against what the export really had (short side) | `src/cobalt/replay/runner.py:324` `result.movers_by_side = export_counts(exports, top_n=settings.top_n)`; `src/cobalt/replay/models.py:430` `movers_by_side: dict[Side, MoversSideCount] = Field(default_factory=dict)` |

## Migrations 0008 / 0009 (one line each)
- **0008** `src/cobalt/db_migrations/0008_radar_value_movers.sql` — adds `rank_metric`/`rank_value` columns to `system.radar_membership` (`ALTER TABLE … ADD COLUMN IF NOT EXISTS`, additive, idempotent) and creates `system.movers_daily` (`CREATE TABLE IF NOT EXISTS`, append-only, active-flag pattern, no delete). Rollback drops the created table and the two added columns.
- **0009** `src/cobalt/db_migrations/0009_picks_missed.sql` — creates `"user".picks` (one row per FILLED card, `user_id` tenant-owned, FK to `aset_sizings`/`card_transitions`) and (per the build report) `"user".missed` for the F12/F13 missed-movers corpus; both additive `CREATE TABLE IF NOT EXISTS`, idempotent, no touch to any pre-existing table. Rollback drops both tables.
- Both migrations were run forward and rolled back and re-forwarded on `cobalt_dev` in this run (§4.4/§4.7 of the build report): 23 pre-existing tables `OK` (digest before = after) on every pass, the three new relations CREATED / DROPPED / CREATED cleanly, no `CHANGED`, no serialization failure.

## `Asset Type` rule confirmed NOT built
- `git diff main...sprint-2/p4 -- configs/cobalt/radar.yaml`: **empty** — `not_equity:` is byte-identical to main.
- `grep -n "REQUIRED_HEADERS" src/cobalt/replay/movers.py` (post-build): `REQUIRED_HEADERS = ["Ticker", "Change", "Volume"]` — no `Asset Type` added.
- `grep -rn "not_equity" src/cobalt/radar src/cobalt/replay` (post-build): unchanged call sites, one function each side, same as pre-run.
- What WAS built this run: `code-03` (`replay/movers.py` `_params` takes `c` from one source, `cobalt.radar.config.screener_columns()`/`screener_columns_param()`, killing the second `range(151)` literal) and the fixture re-cut at 151 columns (`code-14`/`code-15`). Neither touches `not_equity` or `REQUIRED_HEADERS`.

## Stop line (verbatim, from `docs/40 - DevDocs/reports/s2-p4-verify-2026-09-19.md`, last line)
```
READY 4cc6859 (code tip a59ee8c; one docs-only commit fills this sha in) | rebased onto 919d562 (main now a89105f, docs-only since) | offline 1796/0 | db 2114/0 | cobalt_dev: 0001–0009 | rollback round-trip ok | Asset Type ESCALATED | rows 2 built · 4 built · 6 built (K3 SQL ran, HOLD ambiguity confirmed → ESCALATE 2) · 8 built | RESTARTS: com.cobalt.aset com.cobalt.radar (+ bootstrap com.cobalt.replay) | OWED: three-house check, receipt-reference tribunal, deploy prompt | ESCALATE: 16
```

## `## ESCALATE` — all 16, one line each (full text is in `build-report-2-verify-2026-09-19.md`; this is the index)
1. **ASK DESK** (09:37): which `Asset Type` rule — non-blank, `Industry = Exchange Traded Fund`, or either? Table C = 16 blank-`Asset Type` fund rows (8 distinct tickers) out of 5,702 distinct fund tickers / 28 distinct values. Nothing of the rule built; `not_equity`/`REQUIRED_HEADERS` untouched.
2. K3 HOLD ambiguity CONFIRMED on real Postgres (row 6): a HOLD-stamped pre-deploy row reads FAIL. Desk's decision (accept the documented false positive / row-level discriminator / revert `b327221`'s RETAIN grading); nothing built.
3. The movers fixtures (re-fetched 09-19) and `membership-day.real-shape.json` (09-14 anchor day) are now different sessions; 14 tests re-pointed at real rows that still carry their case; true coherence needs a production DB read. Desk's call.
4. `"v": 152` duplicate literal remains in `radar/throttle.py` and `radar/propose.py` beside `config.export.v`. Not fixed (out of ruled scope).
5. Deploy-prompt consequences: (a) `job.result` gains `movers_by_side` — K9.2/K9.5/K9.3/K9.6 read FAIL/ERROR until the first post-deploy `com.cobalt.replay` run (smoke red-by-design before that night); (b) `radar/throttle.py`'s probe now reads the column declaration from config; (c) `com.cobalt.replay` bootstraps once; (d) restart list = aset + radar; (e) migration proof budget = production's own 104 s × 2.
6. `01-p4-build.md` step 2's builder launch shape (`--allowedTools` variadic, trailing prompt swallowed) cannot run as written; every builder in this run used the prompt-first shape instead. Also the cutter's bare no-arg mode can't re-cut everything anymore (raw inputs partly gone); the new `movers` mode was used.
7. L53 record: two Finviz `/export/screener` requests ≈09:28–09:29 ET Saturday, radar `idle:overnight`, archiver not running; 200/200, no retry.
8. DevDocs gaps: no wiki page yet for `test_p4_asset_type_evidence.py`, `test_replay_movers.py`, `test_smoke_k3_sql.py`.
9. Housekeeping: main moved by docs-only desk commits after the rebase (`919d562`→`a89105f`); `jobs restarts main..HEAD` therefore shows desk docs as `D` — P4's own range is `919d562..HEAD`. Sibling cutters mention the anchor-month string in comments only (no fixture data leak).
10. Three `.env` cycles this run, each `cp` by name / `rm` + `ls -la .env` proven after, no builder ran while it was present.
11–16 (carried from build2, one line each, untouched): C7 FY-3 `inputs_sha256` note (safe only while `"user".missed` is undeployed) · C9 the receipt-reference design question (→ tribunal) · C5 0001's schema-wide grant predates 0002's table moves (ops item) · C10 `sys.modules`-only test injection sweep · C11 replay window seam (session close vs formation/candidate horizons) · C12 L53 gate scores declared windows vs wall-clock.

## RESTARTS claim vs the real diff
`ops/com.cobalt.replay.plist` — **A** (new file, `git diff --name-status main...sprint-2/p4 -- ops`). `configs/cobalt/jobs.yaml` diff adds a NEW job block `label: com.cobalt.replay` (one-shot, `schedule: {at: "21:10", …}`) — this is why the stop line calls it a **bootstrap**, not a restart: there is no existing resident named `com.cobalt.replay` to restart, only a first-ever launch of a new one-shot job whose plist and registry row are both new in this branch. `configs/cobalt/taxonomy/tunables.yaml` is an EDIT (existing file: `radar.finviz_max_rpm` 45→50, plus a new `replay.backup_margin_s` key) — consumed by `cobalt.radar.collector.TokenBucket` and `cobalt.replay.runner`, which is why `com.cobalt.aset`/`com.cobalt.radar` restart and `com.cobalt.replay` bootstraps. No `radar.yaml` change (Asset Type not built) → no RESTARTS attributable to that file, matching the report.

## (g) Prior house-check history of this branch
The ONLY prior cross-house read of anything on this lineage is `prompts/2026-09-16/02-p4-review.md` — Sonnet hub → **Astra only**, 3 rounds, 2026-09-16 ~07:xx ET, REVIEWED commit `f3cc006` (+ report line `14c30f4`): that commit is `docs(plan): S2-P4 plan Astra-reviewed …`, touching ONLY `docs/40 - DevDocs/plans/plan-s2-p4-2026-09-15.md` (43 lines changed) — it is a review of the **plan text**, before any P4 code existed, by **one house**, not the three-house tribunal L67 later required (L67 was ruled 2026-09-18, two days after this review). No code commit on `sprint-2/p4` — none of chunks A/B/C/D (`de5d420`, `c7ed958`, `a566cbc`), none of build2 (`7117272`, `f754246`, `b327221`, `08a54ff`, `b43c281`), none of this verify run's fixes (`05ece47`, `089b069`, `0443112`, `a59ee8c`) — has ever been read by Grok, Gemini, or Astra. **NEVER-CHECKED RANGE = the entire non-docs diff `main...sprint-2/p4` (merge-base `919d562` to tip `d5947e7`), all 45 commits, all `src/`/`tests/`/`configs/`/`ops/` changes.** This is why the packet stages the WHOLE branch's non-docs diff rather than a delta.
