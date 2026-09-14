# Heartbeat note absence — design ruling and build plan

2026-09-12. Architect: GPT-6 Astra. Opus reviews; Dejan rules. Design only; no implementation, migration, live email, or production edit performed. Requested destination `/Users/cobalt/tmp/plan-heartbeat-note-absent.md` was denied by the session sandbox; this complete artifact is delivered at `/private/tmp/plan-heartbeat-note-absent.md`.

## 1. Ruling: UNCONDITIONAL DEFER

Adopt `deferred_note_absent` for positively identified absence of today's daily note at ANY hour. Preserve PROBES → COMPOSE → ALERTS → PERSIST → VAULT → FINALIZE and market_reset precedence. Absence does not create a note, create a vault-write row, append a stage failure, or send a corrective RED. It never suppresses another RED.

The deciding evidence is the actual job sweep:

- `src/cobalt/heartbeat/runner.py:98–118` calls all 13 probes AND `jobs.watchdog.sweep`. The complete probe list is database, sheet HTTP, sheet daymode, Obsidian, mainframe, herdr, archiver freshness, seat usage, backup freshness, vault blocks, redactions, radar, email. No dedicated daily-prefill probe exists.
- `configs/cobalt/jobs.yaml:168–173`: `com.cobalt.prefill-daily`, enabled by default, self-supervised one-shot, timeout 600 seconds, 05:15 Mon–Fri. `ops/com.cobalt.prefill-daily.plist:60–66` supplies matching five calendar entries; lines 15–22 declare production environment/vault; lines 24–30 invoke the absolute uv executable with `uv run prefill daily`.
- This command DOES carry F17: `src/cobalt/prefill/cli.py:28–39` wraps prefill in `as_job` and records action, filled/skipped slots, path. `src/cobalt/jobs/wrapper.py:173–196` records exceptions as failed and re-raises; normal completion records exit 0.
- `src/cobalt/jobs/watchdog.py:349–372` detects unloaded jobs; 374–380 detects unregistered jobs; 412–436 detects running jobs with expired timeout and stale/missing heartbeat; 438–444 reports failed/zombie states RED; 447–452 invokes missed-run detection. `is_missed`, 260–280, compares scheduled occurrence, completion and registration. Broken launchctl probing is RED, and a broken entire sweep becomes UNKNOWN/RED at `runner.py:117–126`.
- Missed grace is 30 minutes (`configs/cobalt/taxonomy/tunables.yaml:494–495`). For an established row and never-run prefill, 05:45 exactly is within grace; the first beat strictly AFTER 05:45 reports MISSED. At 05:29 it is not yet MISSED. An already recorded failure is RED at the next sweep regardless of note presence.

Thus a failed or never-run scheduled prefill already has independent detection. A second deadline in the heartbeat would duplicate this policy and create weekend complexity. Choose unconditional defer under the user's deciding rule.

Do not overclaim: this is lifecycle/cadence monitoring, not artifact monitoring. Deletion after successful prefill, writing to a wrong but valid target, incomplete content with exit 0, and a logical hang whose beater stays fresh are not comprehensively detected. Time-bounding the heartbeat would catch some deleted/wrong-target notes, but would not repair that broader contract. These are residual gaps, not evidence that failed/never-run prefill lacks a watchdog. The path diagnosis below makes the mismatch inspectable; it is not an automatic artifact-health probe.

## 2. Schedule, holiday and observed evidence

No cutoff, new tunable, hardcoded deadline, or duplicated holiday logic. Existing watchdog due times derive from the job registry. `tests/cobalt/test_jobs.py:88–105` checks scheduled time AND weekdays against tracked plists. Changing registry/plist alone fails this test. LIVE additionally compares installed versus tracked plists: unit tests cannot detect stale installed copies.

Weekday market holidays are NOT excluded by prefill's registry or `run_daily_prefill` (`src/cobalt/prefill/daily.py:459–528`). Labor Day still has a 05:15 scheduled prefill. The session clock instead makes the entire market holiday overnight; historical control: `docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md:101–114`. Saturday has no scheduled prefill. Test these separately.

Regression evidence: `docs/40 - DevDocs/reports/day-open-2026-09-11.md:276–284` records 21 RED beats from 00:13:04 through 05:14:29, recovery 05:29:33, surviving beats and alert emails. That report calls prefill correlation unverified; `docs/00 - Project/PROJECT-LEDGER.md:1188` subsequently records confirmation from creation-time evidence.

I inspected actual trading-note paths. Friday's note exists at `/Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-11.md`; line 5 says `2026-09-11 T 05:15`. Its CURRENT birth/mtime is 2026-09-11 23:57:27 EDT, so today's stat cannot independently verify original creation time. Replacement might explain it; not investigated. Saturday's corresponding `2026-09-12.md` is absent. No notes were modified. This means absence can persist through a whole weekend, not just five hours nightly.

## 3. Outcome and path contract

Introduce a heartbeat-local typed absence signal carrying the resolved Path, e.g. `DailyNoteAbsent(path)`. Raise it only from `write_note_block`'s explicit target lookup; catch it within `_run_vault_stage` before generic stage-failure handling. Replace bare None for known absence. Unexpected None remains a genuine writer-contract failure. Update direct callers/tests; do not use a second path resolution to reconstruct evidence.

Keep `daily_note_path(beat.at.date())`: it shares ASET config and `resolve_target` with prefill (`src/cobalt/daymode/note.py:238–256`; `prefill/daily.py:467–468`). Establish absence with a stat lookup catching ONLY FileNotFoundError; propagate permission/I/O errors and reject an existing non-regular-file target. Do not catch FileNotFoundError from the entire writer: a missing auxiliary dependency is not missing-note deferral. A target disappearing after the precheck stays a named-path write failure in this bounded patch.

Exact deferred reason:

`daily note absent at {absolute_path}; heartbeat status write deferred; com.cobalt.prefill-daily owns note creation; heartbeat never creates notes (L28.1)`

Example Friday path: `/Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-11.md`. Log DEFERRED at INFO, not ERROR. Remove the stale hardcoded 05:15 sentence from this diagnostic. Market-reset keeps its distinct value/reason and happens BEFORE target lookup (`runner.py:348–356`).

For real failures after resolution, preserve that same path through the redacted reason, e.g. `vault FAILED (VaultWriteError: daily-note target {path}: {underlying detail})`. Unexpected None: `daily-note target {path}: writer returned no result without an absence signal`. Id-less result: `daily-note target {path}: writer returned action={action} without a write id`. Resolution failure: `daily-note target unresolved for {ET_date}: {detail}`; never fabricate a path. Keep `_stage_failure` redaction and safe detail-unavailable fallback (`runner.py:261–278`).

The existing initial log already names the path (`runner.py:151–154`); the durable/operator-visible reason discards it at 359–363. Same gap exists in the id-less message (363), marker exceptions (`src/cobalt/vaultwrite/writer.py:684–687`) and some store/setup exceptions. Add target context at the heartbeat boundary, leaving shared writer semantics unchanged. The shared writer's missing-target refusal ALREADY names the path (669–673). Test both distinctions.

## 4. DB and downstream consumers

Migration REQUIRED; scope is NOT confined to heartbeat and its tests. Deployed database-wide 0003 CHECK permits only written/deferred_market_reset/failed (`src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql:7–12`). Do not edit or reverse 0003 or drop its columns. Main already contains 0004 radar. Use next available **0005_heartbeat_note_absent.sql**, rechecking numbering before build.

0005 transactionally replaces ONLY the vault_outcome CHECK on `system.cobalt_jobs`, preserving NULL and the three old values and adding deferred_note_absent. Verify catalog constraint name/definition first; expected PostgreSQL-generated name is `cobalt_jobs_vault_outcome_check`. Fail on an unexpected definition rather than dropping arbitrary checks. Make repeat application safe. Register forward after 0004 and bounded reverse first (`src/cobalt/db_migrations/__init__.py:29–40`); update positional assertions (`tests/cobalt/test_tenancy.py:455–456`). The bounded 0005 reverse must refuse if new-domain rows exist, then restore the old CHECK without changing data. Normal production CODE rollback RETAINS the expanded CHECK; old code tolerates it. Never reverse 0003. Prove current CLI `--down-to 0004` selects ONLY 0005 before using it as optional schema rollback (`db_migrations/cli.py:204–213`, 242 onward).

`src/cobalt/jobs/store.py:219–235` already persists outcome/reason as text parameters in dedicated columns. No JSON workaround or new history table. This is ONE mutable row per label, not beat history. Initial PERSIST intentionally writes NULL; FINALIZE writes actual outcome/reason (`runner.py:334–342`, 379–385). Keep wrapper ownership/merge and green-summary dedup.

`Beat.green` already makes only failed a vault RED (`render.py:46–52`); note and console already display arbitrary outcomes/reasons (89–94, 137–142). Preserve/test that behavior with unrelated RED. `dm_body` only prints failed vault detail (120–121): add one explicit deferral line when rendering a finalized deferred Beat. Actual initial ALERTS happens before VAULT and cannot know that later outcome; do not reorder or send another DM for benign deferral. Post-vault truth is in console/log/final row. Extend run_beat's deferral log branch (435–436); FINALIZE corrective alert remains exactly failed (389–390).

Day-open is currently a documented manual sweep; a command is owed (`PROJECT-LEDGER.md:1228`). The new close-out checklist must read outcome AND reason AND last_result.green and freshness, not infer failed beats from missing vault-write rows, job done or exit 0. Preserve historical reports; do not rewrite their old findings.

## 5. Other conditions and false-green findings

These are explicit follow-ups, not silently bundled repairs or claims of a comprehensive audit:

1. **Confirmed additional false RED: legitimate id-less unchanged.** `VaultWriter.upsert_unit` returns unchanged without a write id when bytes already match (`writer.py:756–758`, 782–788); heartbeat fails it (`runner.py:362–363`). Normal beat timestamps usually differ; identical-Beat replay demonstrates the valid case. Needs a separate truthful no-op outcome ruling, including human-wins semantics. Do not call it written tonight.
2. **Confirmed dry-run false RED:** writer intentionally has no persisted id in dry run (`writer.py:539–544`), same heartbeat branch fails it. No corrective email/persistence occurs because dry-run gates suppress those. Track with unchanged. Do not use actual dry-run GREEN as tonight's delivery acceptance or weaken the live id requirement incidentally.
3. Missing section/unit/anchor is already supported inside an existing note (`writer.py:693–719`). Missing baseline is a merge diagnostic, not note absence. Id-less skipped exists (775–780), but heartbeat supplies no skip_if, so it is not a reachable normal heartbeat result. No additional legitimate production absence established in those branches.
4. **Vault-blocks false green remains:** all readable counts are OK (`probes.py:380–408`), including heartbeat refusals. Fix report:48 explicitly left it unchanged; blackout report:87–99 and 133–135 explains the hole. Staged heartbeat now reports writer exceptions RED, but the counter is still no independent detector of watcher loss. Actor-specific watcher repair remains open.
5. **Sweep last-exit gap:** last_exit is displayed on a GREEN finding, not evaluated for failure (`watchdog.py:454–470`). Wrapper-before-start failure becomes MISSED later; do not claim immediate last-exit detection. A logical hang with fresh beater is also running/OK (412–436).
6. **Artifact/completeness:** prefill can catch fetch errors and write FAILED placeholders while completing successfully (`prefill/daily.py:489–514`; CLI records no health verdict). Archiver rejects zero rows but doesn't reject partial failures or unrecorded rows_written (`probes.py:306–324`). Mainframe tests TCP acceptance, not successful inference (248–254). These are limited contracts, not proven present outages.
7. **Missing configuration treated as intentional absence:** missing herdr registry entry returns false and is rendered as NOT PROBED/OK (`probes.py:554–557`, 612–619); the deleted job is absent from the sweep too. Registry/plist tests detect tracked drift, but runtime missing-entry semantics deserve separate correction.
8. Sheet HTTP's usability gap has sheet_daymode beside it (150–209). Obsidian probes sync process state; seat usage is window-aware; archiver handles weekend cadence. Backup unarmed/no snapshot and email never-sent/last-failed are already RED (327–377, 767–827). Redaction counts intentionally describe successful protection (411–434). Radar disabled/idle skips active health checks (61–118), correctly describing its parked state. Backup's newest snapshot across armed destinations can conceal one stale leg; multi-leg proof belongs to backup follow-up. No current backup loss established here.

## 6. Numbered tests-first build

1. Pin actual main/dirty set. Observed HEAD: `92fe8a7`; pre-existing modified docs/untracked reports remain untouched. Build in an isolated checkout from actual main, not parked stage 2. Give builder this plan, reports, ledger amendments and current S2 LIVE parked block.
2. Write failing tests for typed absence and exact resolved-path diagnostics. Use the real daily-note marker shape as fixture basis under L45, stripping incidental journal content. Temporary paths supply presence/error states. Keep unexpected None and arbitrary exceptions failed; replace only known-absence expectations (`tests/cobalt/test_heartbeat_runner.py:115–138`).
3. Write integrated beat/sweep tests with fake stores/launchctl, real registry arithmetic and controlled ET clock. Confirm they fail on the regression, not unavailable services.
4. Implement heartbeat-local signal, scoped lookup/error context, outcome constant, logging and finalized-DM display. Preserve stage order, redaction, ownership, alerts and market-reset precedence. No jobs.yaml/plist/prefill/shared-writer/radar/taxonomy edits.
5. Add 0005 and registration tests. Isolated DEV DB proof: upgrade from 0003+0004, repeat full forward application, domain persistence/rejection, bounded 0005 reverse then forward. Never reverse 0003 in this proof.
6. Run gate below; Opus reviews, hub verifies DB evidence, builder resolves findings. Re-run affected checks, pin full baseline/patch SHAs, and write report in the same turn as evidence (ledger:1235). Dejan rules before LIVE.

### Offline acceptance — mandatory pass criteria

- Friday 09-11 **00:13 / 05:14 / 05:29**, absent: deferred_note_absent, exact path, no vault store/writer construction, no absence stage failure, GREEN if other checks healthy, no corrective email. 05:29 existing note + write id: written. 05:29 failed prefill + absent note: deferred AND RED job, normal RED alerts. Never-run at 05:29 is within grace; 05:45:00 still grace; 05:45:01 MISSED/RED. Cover established never-finished and yesterday-completed rows and first-registration exemption.
- Saturday 09-12 before/after 05:15 and 20:30: absent defers, no Saturday prefill due. Labor Day Monday 09-07 20:30: existing written; absent deferred_note_absent; neither market-reset deferred. A never-run holiday weekday prefill still becomes MISSED after its scheduled grace.
- Preserve trading-day 19:59/20:00/20:59/21:00 matrix. In-window absent note yields deferred_market_reset before any path lookup/session refusal. Both deferrals independently preserve RED probe, RED job and stage failure.
- Permission/I/O error, directory target, malformed markers, generic exception, unexpected None and id-less updated result remain failed; path in final reason/console/corrective-email stub. Resolver error names ET date/unresolved target. Preserve redaction safe fallback and corrective email despite FINALIZE DB failure.
- Stage order unchanged. Final row exact outcome/reason; wrapper completion preserves green, red lists, stage failures and dedup date. Exit 0 behavior retained. No note created or bytes altered by deferral; no session_blocks rows from it.
- Migration preserves ALL job fields including outcome/reason by explicit row snapshot, not just generic digests that exclude those fields. CHECK accepts NULL/four values, rejects arbitrary text. Repeated forward safe. Reverse with new-domain row refuses atomically; reverse with old-domain fixtures succeeds without changing 0003 columns or 0004 radar objects; forward succeeds again. No required DB test skipped.
- Focused heartbeat/jobs/restart/tenancy/vaultwriter suites pass; full new-core suite and `cobalt validate` pass under established DEV gates. Any pre-existing failure needs unchanged-baseline proof, never a waiver for a new failure. `git diff --check` clean. No production-connected tests/live-email substitutes. Report dry-run/unchanged limitations as open, not repaired.

## 7. RESTARTS derivation — L42

Law: `PROJECT-LEDGER.md:1148`. Tool: `src/cobalt/jobs/restarts.py:147–198`.

I ran repository static `import_graph`/`reachable` read-only on current main. All six resident roots resolve without dynamic unknowns. Only **com.cobalt.radar**, through entrypoint `cobalt.cli`, reaches both heartbeat.runner and db_migrations. ASET, mainframe, Obsidian, old-tree agent and herdr reach neither. Radar is disabled (`jobs.yaml:156–165`).

**Provisional RESTARTS: com.cobalt.radar — static import reach; disabled, so no running process to restart or enable tonight.**

No plist/config changes planned. Heartbeat is a one-shot and reads new code on each launch. SQL is a non-Python src asset per tool:182–183; explicitly classify it as deploy-time DDL, no cached resident reader. Tests/report require no resident restart. Do not say none merely because heartbeat is one-shot.

Hub must run `uv run cobalt jobs restarts BASE_SHA..PATCH_SHA` FROM final patch checkout, save all rows, reconcile this provisional result, and recompute after rebases/changes and for rollback. Unproven imports require L42 conservative restarts; unclassified paths ESCALATE. Do not bootstrap disabled radar to satisfy a derivation table.

## 8. LIVE — tonight, proofs, rollback triple

L43: one production deploy per evening (`PROJECT-LEDGER.md:1149`). Latest user sequencing controls: heartbeat tonight 09-12, S2-P1 resume tomorrow 09-13. No stage-2 merge, source switch or radar enablement tonight. If tonight's production slot is already consumed, STOP for Dejan's sequencing ruling.

This patch advances main above `s2-p1-stage1`/92fe8a7. It does not conflict with the parked stage-1 implementation; tomorrow's branch must incorporate it and repeat affected gates/restart derivation. Resetting to pre-s2-p1 WOULD conflict and is forbidden (ledger:1206); S2 rollback must selectively revert its own range while preserving heartbeat. The earlier ledger's NOTHING DEPLOYED statement at 1213 is historical, superseded by observed main and the user's parked-state context.

L0. Hub records approved full SHAs, dirty set, stage-1 tag, radar disabled and migration state. Obtain/verify the fresh backup required by existing LIVE procedure; record snapshot id and recovery proof, not an ambiguous success log. Compare installed prefill/heartbeat plists to tracked copies read-only. Inspect actual CHECK catalog definition.

L1. Prevent new code from running against old CHECK. Between ticks, briefly bootout ONLY heartbeat and wait for any in-flight beat to finish; record time. FF-only merge reviewed source preserving known dirty docs. Run `uv run cobalt db migrate --allow-prod` through existing production gate. It replays the fixed list including deployed 0004: idempotence and catalog state must already be proven. Failure rolls back transaction; never resume new code with old CHECK. No other migration or radar activation is authorized.

L2. Verify new CHECK, old columns/row content and unrelated catalog/data unchanged. Bootstrap SAME unchanged installed heartbeat plist. No plist deployment/jobs registration required. This temporary stop/start orders schema/code; it is not an L42 resident restart. Bound pause below one normal interval. If impossible, restore old-code service with compatible schema and halt.

L3. Observe a real scheduled beat. Saturday's absent note should yield final row deferred_note_absent, exact target reason, last_result.green matching real jobs/probes, wrapper exit 0, all six stage logs including FINALIZE (inspect stderr too). No absence-caused corrective email. Unrelated RED still alerts and prevents claiming all-green. Never delete/create a live note to manufacture evidence.

L4. Observe at least two successive scheduled beats, ~15-minute spacing, no gap >20 minutes, no new heartbeat session_blocks rows against recorded baseline, no new absent-note FAILED/corrective email. Saturday cannot prove market_reset: retain Monday's first in-window beat as OWED live proof, supported meanwhile by offline matrix. Monday 05:29 after scheduled prefill is the next scheduled recovery proof if no legitimate note appears earlier. These observations are not another deploy and do not require this session to wait overnight.

L5. Write proofs and OWED observations to close-out report before claiming deployment complete. Tomorrow S2 uses updated main for integration/restart derivation and preserves its original rollback domain; no rollback may discard this patch.

**Rollback triple — dispatch pins actual SHAs/snapshot id:**

1. **CODE:** briefly stop heartbeat; revert only this patch's implementation commits via reviewed inverse patch, preserving S2 stage 1/later unrelated changes and migration registration where needed. No reset --hard. Confirm source/schema compatibility before resuming.
2. **SERVICE:** bootstrap same unchanged heartbeat plist; prove loaded, exit 0, surviving beat. Perform any additional L42 restart only for a running resident; radar stays disabled. Explicit cost: old code resumes known absent-note RED noise.
3. **DATA/SCHEMA:** normally RETAIN additive 0005 CHECK; no vault restore/data rollback needed for deferral. If schema narrowing is explicitly required, use only tested 0005 reverse when no new-domain row exists; otherwise refuse. Never rewrite/drop evidence to pass CHECK, reverse 0003/0004, or restore whole DB merely for this enum. Verified snapshot is the recovery anchor for actual data-loss incidents.

## 9. Builder and dissent

Recommend **GPT-5.6 Sol at high effort**, supplied L29 implementation floor, prepaid. Estimate 60–120 minutes implementation and 30–60 minutes hub DB verification/review: roughly 80–150 Python/SQL lines and 150–250 test lines across runner/render, migration registration/new SQL pair, heartbeat/tenancy tests, plus report. Estimates, not a measured patch.

Against this recommendation: this house authored the earlier None=failed ruling, creating correlated-assumption risk; staged persistence/CHECK rollout beside parked S2 is more subtle than an enum edit. Give Sol the full evidence/parked block and reserve scarce Opus 5 for adversarial review. **Opus 5 becomes the better builder** if review expands into shared writer semantics, artifact-health monitoring or migration-runner redesign, or scope exceeds roughly 400 code/test lines without a clear bounded reason. Never hit an estimate by deleting tests.

Sonnet 5 is not an eligible vault/DB migration builder under L29 (`PROJECT-LEDGER.md:1030`); permitted mechanical hub work is a different task. Local Qwen is not a builder: ledger:1181 says READS AND JUDGES, NEVER COMPOSES. It can give a bounded read-only verdict on saved proofs, with an upfront cost estimate. Anthropic scarcity and supplied Sunday 13:00 ET Fable reset favor reserving Opus for review; waiting for reset misses tonight. Availability/economics are taken from Dejan's supplied context, not independently asserted vendor specs.

DESIGN COMPLETE
