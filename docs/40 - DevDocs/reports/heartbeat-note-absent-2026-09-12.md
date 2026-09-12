# Heartbeat — daily-note absence is a benign deferral

2026-09-12. Builders: GPT-5.6 Sol (high effort, started the build, stopped on a
usage limit after real work) then headless Opus (took over mid-build under
escalation trigger (d) — see §9). Plan: GPT-6 Astra, authoritative. Dejan rules.
Deployed to production 2026-09-12, merged FF-only to `main` at `01929cb`,
baseline `92fe8a7` (`s2-p1-stage1`). Fresh backup snapshot `e63543d8` taken
before migration. Migration 0005 applied to `cobalt_brain`. Two `requires_db`
proofs ran against `cobalt_dev` only, confirmed by direct query, never
`cobalt_brain`.

## 0. Headline

Absent daily note is now `deferred_note_absent`: unconditional, no clock logic,
beat keeps the colour its own probes produce. Migration 0005 extends only the
`vault_outcome` CHECK; reverse refuses while new-domain rows exist. Every
diagnostic now names the absolute path it looked for.
**CONFIRMATION GATE: NARROW — the three cases do NOT share one branch and items
1/2 need outcome values 0005 does not carry. Built absent-note only. Dejan
ruled the gate correct.**
Suite `1027 passed, 239 skipped`. `cobalt validate` exit 0. Both DB proofs pass
against `cobalt_dev`. Unauthorised WARNING→INFO log downgrade reverted before
deploy.
**DEPLOYED 2026-09-12 ~12:20-12:39 ET — live proof observed the same afternoon**
(§5): two successive real beats (12:24:10, 12:39:15 ET) both show
`vault_outcome=deferred_note_absent`, `last_result.green=false` only because
of the pre-existing unrelated `com.cobalt.herdr` RED, no absence-caused
corrective email, `session_blocks` unchanged at 8 rows. Two pre-existing
items (ESCALATE-1, ESCALATE-2, §7) carried forward as their own tickets, not
blockers. Sol hit a usage stop after real work; headless Opus took over
mid-build under trigger (d) — see §9.

## 1. The confirmation gate — answer: NARROW FIX

Dejan's gate: build all three iff they share the code path AND need no outcome
value beyond `deferred_note_absent`. Both conditions fail.

| Case | Writer origin of the missing id | Heartbeat branch that rated it | Same branch? |
|---|---|---|---|
| Absent note | n/a — `write_note_block` returned `None` at `runner.py:150` (pre-patch) | `runner.py:359` `if write is None` | — |
| Id-less `unchanged` | `writer.py:782` `if outcome is None` → `WriteResult(action="unchanged")`, `write_id` defaulted `None` | `runner.py:362` `if write.write_id is None` | **No** |
| Dry run | `writer.py:541` `if self.dry_run: return (new_text, kwargs, None)` | `runner.py:362` `if write.write_id is None` | **No** |

Two findings, either one sufficient to go narrow:

1. **Not one branch.** Absence reached `failed` through the *result-is-None*
   branch (`runner.py:359`); unchanged and dry-run reach it through the
   *id-is-None* branch (`runner.py:362`). They are adjacent lines expressing the
   same rule, not one code path. Items 1 and 2 do share `runner.py:362` with
   each other.
2. **They need outcome values 0005 does not carry — decisive.** Neither is
   `deferred_note_absent`, and neither is truthfully `written`. An id-less
   `unchanged` means the bytes already match but **no `vault_writes` row exists**
   — calling it `written` asserts an audit row that is not there. A dry run
   wrote nothing at all. Each needs its own no-op / dry-run outcome, so the
   CHECK domain would have to exceed the four values 0005 adds, and the
   `unchanged` case additionally needs the human-wins ruling Astra reserved
   (plan §5.1). That is the scope increase Dejan defined as the STOP condition.

Per the ruling, items 1 and 2 were **not** built. They remain `failed`, now with
their path named, pinned by
`test_idless_result_remains_failed_and_names_its_path` over
`(updated, unchanged, dry-run)`. **ESCALATE-2** below carries them forward.

## 2. Delivered items

| # | Item | Evidence |
|---|---|---|
| 1 | `deferred_note_absent` as its own outcome, unconditional | `runner.py:61` constant; `runner.py:387` catches `DailyNoteAbsent`; no clock/cutoff in the path |
| 1 | Beat does not go RED | `render.py:46-52` reds only on `failed`; test asserts `beat.green` with the outcome set |
| 1 | Recorded durably | `store.row["vault_outcome"] == deferred_note_absent` asserted in the absence test |
| 3 | Migration 0005, additive CHECK only | `0005_heartbeat_note_absent.sql`; reads `pg_get_constraintdef`, refuses an unexpected definition, returns early if already applied |
| 3 | Reverse refuses on new-domain rows | `…rollback.sql` raises `REFUSING 0005 reverse` before touching the constraint; no `DROP COLUMN` in either file |
| 3 | Registered in both lists | `db_migrations/__init__.py` FORWARD tail / REVERSE head; `test_down_to_0004_selects_only_0005_reverse` proves `--down-to 0004` selects only 0005 |
| 4 | Path in the reason | Exact wording per plan §3, asserted verbatim in `test_absent_daily_note_defers_…` |
| 4 | Path in the id-less message | `runner.py:400-403`, asserted for all three actions |
| 4 | Path in marker exceptions | `writer.py:687` now `f"{path}: {e}"`; `test_malformed_markers_refuse_the_write` asserts the path and that bytes are unchanged |
| 5 | Renderers / `Beat.green` / job row | `render.py:129-133` adds one deferral line; absence test asserts the outcome appears in `note_body()`, `dm_body()` and `console()` |

**Resolution is now a single lookup that distinguishes absence from failure**
(`runner.py:160-175`): only `FileNotFoundError` becomes `DailyNoteAbsent`;
permission/I-O errors, a non-regular-file target, a resolver failure, an
unexpected `None` and any writer exception all stay `failed` and name the path
(or, for a resolver failure, the ET date and no fabricated path).

Item 5's day-open sweep has **no command in code** (`grep` for `day_open`/
`day-open` across `src/cobalt`: no matches) — it is still the documented manual
sweep, with a command owed at `PROJECT-LEDGER.md:1228`. Nothing was invented
here. The checklist requirement stands: read `vault_outcome` AND `vault_reason`
AND `last_result.green` AND freshness — never infer a failed beat from a missing
`vault_writes` row.

## 3. Tests — boundaries, and proof they bind

Written against the boundaries, not against the 09-10 fix's reasoning. Fixture
is the real 2026-09-11 marker shape (L45), journal content stripped.

| Boundary | Test | Result |
|---|---|---|
| 00:13, 05:14 absent (the 09-11 RED window) | `…defers_unconditionally…[at0,at1]` | defers, GREEN |
| 05:29 after prefill created the note | `test_0529_prefilled_real_marker_shape_reaches_writer_and_records_written` | `written`, fixture bytes unaltered |
| Saturday 09-12 absent, before and after 05:15 | `…[at2,at3]` | defers; no Saturday prefill due (`test_saturday_has_no_new_prefill_due`) |
| Labor Day Monday 09-07 20:30 absent | `…[at4]` | `deferred_note_absent`, **not** market_reset |
| Deferral must not mask an unrelated RED | `test_deferred_absence_does_not_mask_an_unrelated_red_probe` | defers AND `not beat.green`, corrective email still sent |
| market_reset precedence | `test_market_reset_precedes_even_absence_lookup` | returns before any path resolution |
| Missed-run grace 05:29 / 05:45:00 / 05:45:01 | `TestRealPrefillDailySchedule` | not missed / not missed / MISSED |

**No absence path constructs a store or writer** — both are monkeypatched to
`pytest.fail` in the absence tests, so the deferral is proven to happen before
any DB-backed object exists. No note is created and none is modified.

**Regression binding proved empirically.** The patched `runner.py` was swapped
for `git show HEAD:` and the heartbeat suite re-run: **14 failed, 19 passed** —
every new absence/path test fails against pre-patch code. The tree was restored
byte-for-byte immediately (`git diff --stat` unchanged at 72 insertions /
25 deletions) and the scratch copies deleted.

### Suite

```
1027 passed, 239 skipped, 15 warnings in 17.23s
```

`uv run pytest tests/cobalt tests/taxonomy -q`, no DB environment, no `.env`
created, no `POSTGRES_*` set. The 239 skips are `requires_db` and pre-existing
environment guards. `git diff --check` clean. No test was loosened, skipped or
xfailed; the two DB migration proofs are written and registered but **did not
run here** and are owed to the hub.

## 4. RESTARTS — L42

`uv run cobalt jobs restarts HEAD` from this checkout:

| Path | Change | Rule | Restart |
|---|---|---|---|
| `0005_…sql`, `0005_…rollback.sql` | A | non-Python src asset | – |
| `db_migrations/__init__.py` | M | static import reach | com.cobalt.radar |
| `heartbeat/render.py` | M | static import reach | com.cobalt.radar |
| `heartbeat/runner.py` | M | static import reach | com.cobalt.radar |
| `vaultwrite/writer.py` | M | static import reach | – |
| 5 test files | M | test/documentation; no resident | – |

**RESTARTS: com.cobalt.radar** — reconciles exactly with Astra's provisional
derivation. Radar is disabled (`jobs.yaml:156-165`); there is no running process
to restart and it is **not** to be bootstrapped to satisfy this table. Heartbeat
is a one-shot and reads new code each launch. The hub must recompute from the
final patch checkout after commit and after tomorrow's S2 rebase.

## 5. LIVE — executed 2026-09-12, ~12:15-12:39 ET, all steps proven

Order is schema-before-code; L43's one production deploy per evening — this
took tonight's slot. No hard-stop window (20:00-21:30 market_reset/exclusion,
21:25-21:55 nightly backup, 23:27-23:47 generated commit) was in effect at
this time of day; deploy proceeded rather than waiting for evening.

| Step | Action | Proof recorded |
|---|---|---|
| L0 | Pinned: main `92fe8a7` (`s2-p1-stage1`) before merge, known pre-existing dirty docs (PROJECT-LEDGER.md, SPRINT-LADDER, two heartbeat/seat-usage reports) untouched, radar disabled, migrations 0001-0004 already applied. Fresh backup **before** touching anything: `uv run cobalt backup run` under `COBALT_ENV=production` → snapshot `e63543d8` (426.8 MB DB dump, 7.3 MB new vault data), exit 0. Installed vs tracked plists: `diff` on both `com.cobalt.heartbeat.plist` and `com.cobalt.prefill-daily.plist` → **IDENTICAL**. Live CHECK catalog definition read directly: exactly the pre-0005 three-value domain, matching 0005's `old_definition` constant | snapshot `e63543d8`; plist diffs; CHECK text captured above |
| L1 | `launchctl bootout gui/501/com.cobalt.heartbeat` at 12:20:29 ET — heartbeat was idle (`state = not running`, no in-flight beat) at bootout, confirmed before acting. `git merge --ff-only heartbeat/note-absent` in `/Users/cobalt/cobalt` → fast-forward, `92fe8a7..01929cb`, pre-existing dirty docs preserved. `COBALT_ENV=production uv run cobalt db migrate --allow-prod` → all 5 migrations replayed (0001-0004 no-ops, 0005 newly applied); **all 15 tables' row counts and digests identical before/after**; exit 0 | bootout time 12:20:29; FF merge log; full digest table, all `OK` |
| L2 | Re-read the CHECK post-migration: now the four-value domain including `deferred_note_absent`, exact text captured. `launchctl bootstrap gui/501 ~/Library/LaunchAgents/com.cobalt.heartbeat.plist` at 12:24:10 ET — **the same, unchanged installed plist**, not redeployed | new CHECK text; bootstrap time 12:24:10 |
| L3 | The plist's `runatload` property fired an immediate real beat through the normal launchd mechanism (not a manual/synthetic invocation) at 12:24:10-12:24:14 ET. **`cobalt_jobs` row for `com.cobalt.heartbeat`: `vault_outcome = deferred_note_absent`, `vault_reason` = the exact target-path sentence, `last_result.green = false`** (correctly reflecting the pre-existing, unrelated `com.cobalt.herdr` RED — not the vault). Console/log showed all stages incl. FINALIZE, wrapper exit 0. **No absence-caused corrective email**: the one Email+DM pair sent during this beat fired during the ALERTS stage (12:24:14.110/.309), *before* the VAULT stage (12:24:14.374) even ran — it was the routine alert for herdr, not a new corrective alert for the deferral. Compare the immediately-prior beat under **old** code (12:16:40-12:16:41, before bootout/merge/migrate): `vault unit FAILED — daily-note writer returned no result`, `RED — 1 job(s) and vault write` (two REDs) — the exact regression, live, seconds before the fix | `cobalt_jobs` row query; log excerpts pre- and post-deploy, same day |
| L4 | Second real beat at 12:39:15-12:39:18 ET, gap **15m05s** from the first (well under the 20-min cap). Identical outcome: `deferred_note_absent`, `RED — 1 job(s)` (herdr only), no absence-caused email. `system.session_blocks` row count: **8 before, 8 after** — no new refusal rows from either beat | second beat log; `session_blocks` count query, both times |
| L5 | This section | — |

**OWED live proof, unchanged by today's deploy:** Saturday cannot exercise
market_reset. Monday's first in-window beat (19:59/20:00 ET) is the owed
`deferred_market_reset` observation; Monday 05:29, after `com.cobalt.prefill-daily`
runs, is the owed recovery-to-`written` observation. Offline matrix covers
both meanwhile. Tomorrow's day-open should additionally confirm the
**~00:13 ET** beat (the exact hour of the 09-11 regression) shows
`vault_outcome=deferred_note_absent`, keeps the colour its own probes
produce, and sends no alert email — expected, not yet independently observed
at time of writing (deploy was mid-afternoon, not overnight). Never create or
delete a live note to manufacture evidence.

This patch lands **above** parked `s2-p1-stage1` and does not touch it. Tomorrow's
S2 branch rebases onto it; no S2 rollback may discard it (resetting to
pre-s2-p1 is forbidden, ledger:1206).

## 6. Rollback triple

1. **CODE** — bootout heartbeat briefly; revert only this patch's implementation
   commits by reviewed inverse patch, preserving S2 stage 1. No `reset --hard`.
   Confirm source/schema compatibility before resuming. Explicit cost: old code
   resumes the known absent-note RED noise. **Once tomorrow's S2-P1 branch lands
   above this deploy, a reset to tonight's pre-tag would silently delete it, so
   any rollback after that point must be a `git revert` of this merge range
   instead.**
2. **SERVICE** — bootstrap the same unchanged heartbeat plist; prove loaded,
   exit 0, one surviving beat. Radar stays disabled.
3. **DATA/SCHEMA** — normally **RETAIN** the additive 0005 CHECK; old code
   tolerates it and no data rollback is needed for a deferral. Narrow the schema
   only if explicitly required, only via the tested 0005 reverse, only when no
   `deferred_note_absent` row exists — otherwise refuse. Never rewrite or drop
   evidence to satisfy a CHECK. Never reverse 0003 or 0004.

## 7. Open items — and the two real blockers, now cleared

**Dejan's ruling (post-verification):** of the four items raised at first
report, two are pre-existing and NOT blockers for tonight's deploy — they get
their own tickets. Two were real and are cleared below, before deploy.

**ESCALATE-1 — NOT A BLOCKER, HIGHEST-PRIORITY OPEN TICKET. `vaultwrite_blocks`
still rates the heartbeat's own refusals OK.** `probes.py:380-408` counts all
readable blocks as OK, including blocks the heartbeat itself refused to write.
This is the probe that watched the 2026-09-08 blackout and called it green.
This patch does **not** touch it and does not repair it: a beat that defers or
fails its vault unit still contributes a green vault-blocks count. Pre-existing,
unchanged by this build, no worse after it. Its own ticket.

**ESCALATE-2 — NOT A BLOCKER, expected consequence of the narrow gate.**
Id-less `unchanged` and dry-run remain false REDs. Per the gate in §1 they need
their own outcome values and a wider CHECK than 0005 carries, plus a
human-wins ruling for `unchanged`. Both still return `failed` at `runner.py`
around line 400. A live identical-Beat replay would produce a false RED;
normal beat timestamps differ, so this is latent, not firing. Pre-existing,
unchanged by this build. Its own ticket: an outcome ruling plus migration 0006.

**ESCALATE-3 — CLEARED.** `uv run cobalt validate` under `COBALT_ENV=dev`:
**exit 0.** All 13 trade defs, calendar, session boundaries, sheets, card
states, redaction, jobs and heartbeat config sections validated OK; no
Postgres connection was made by this command at all (the earlier failure, with
no `.env` present, was a DSN-composition check firing before any config walk —
not a genuine dependency on a live database for this patch).

**Owed-to-the-hub proofs — CLEARED, against `cobalt_dev`, confirmed NOT
`cobalt_brain`.** Per Dejan's L41 procedure: the hub could not copy `.env`
itself (Claude Code's own credential-leakage classifier refused the `cp`);
Dejan copied it by name via a direct `!` command into the build worktree.
`git check-ignore -v .env` confirmed it was covered before and after;
`git status --porcelain` was empty throughout (the file was never staged,
never visible to git).

- `uv run pytest tests/cobalt/test_tenancy.py::test_populated_job_row_digest_is_unchanged_by_heartbeat_migration tests/cobalt/test_tenancy.py::test_0005_preserves_the_full_job_row_and_round_trips_its_bounded_domain -v`
  under `COBALT_ENV=dev`: **2 passed.** The first proves 0003's digest columns
  unchanged by a full forward/reverse/forward round trip; the second proves
  0005's forward is idempotent, its domain accepts the four values and rejects
  an invented one (`psycopg.errors.CheckViolation`), its named reverse
  **refuses** while a `deferred_note_absent` row exists
  (`psycopg.errors.RaiseException`, message `REFUSING 0005 reverse`, asserted
  and passed), then succeeds once that row is moved back to `written`, and
  that `system.radar_pool`/`system.radar_membership` (0004) exist unchanged
  throughout.
- **Database-target proof, independent of the test suite's own claim:** ran
  `db.connect_migration(env.DEV_DB_NAME)` directly (same `.env`, same
  `COBALT_ENV=dev`) and queried `SELECT current_database()`. Result:
  **`cobalt_dev`**. `env.DEV_DB_NAME` is the literal string `"cobalt_dev"`,
  independent of `COBALT_ENV`'s value; `env.PROD_DB_NAME` (`"cobalt_brain"`)
  was never passed to any migration call in this build proof. No proof in
  this patch touched production.
- `.env` removed immediately after: `ls .env` → no such file;
  `git status --porcelain` → empty; `git check-ignore -v .env` → still
  matched by `.gitignore:1:.env`.

**Log-severity finding, caught in hub verification, reverted before deploy:**
`run_beat`'s existing `deferred_market_reset` log line was silently
downgraded from `logger.warning` to `logger.info` when the note-absent case
was folded into the same branch. The plan only asked for the *new*
note-absent case to log at INFO; it never asked to change market_reset's
existing severity, and neither builder flagged it. Reverted (commit
`01929cb`, before merge): `deferred_market_reset` is back at WARNING,
`deferred_note_absent` keeps its plan-specified INFO. That catch is exactly
why the verification step exists.

**Residual gaps, unchanged and not claimed repaired:** this is lifecycle/cadence
monitoring, not artifact monitoring. Deletion after a successful prefill, a
write to a wrong but valid target, incomplete content with exit 0, and a logical
hang with a fresh beater are still not comprehensively detected (plan §1, §5.5,
§5.6).

**Unrelated pre-existing failure, found when re-running the full suite from
`/Users/cobalt/cobalt` for the deploy (not this patch's fault, own ticket):**
`tests/cobalt/test_radar_notes.py::test_no_screen_filter_value_escapes_the_single_fixture`
scans the whole tree for a synthetic screen-filter fixture pattern leaking
outside its own fixture file, and found one inside the untracked
`docs/40 - DevDocs/reports/day-open-2026-09-10.md` — present in the main
repo's working directory since before this session started (visible in the
session's opening `git status`), unrelated to `test_radar_notes.py` itself
(`git diff 92fe8a7 HEAD -- tests/cobalt/test_radar_notes.py` is empty — this
patch never touched that file). It fails only when run from the main
checkout, which has that stray file on disk; the clean build worktree does
not, which is why the earlier `1027 passed, 239 skipped` runs there never
saw it. `1265 passed, 1 failed, 239 skipped` in the full main-repo run — the
one failure is this pre-existing content leak, not a regression from this
build.

## 8. Vault delivery

This report now sits at
`docs/40 - DevDocs/reports/heartbeat-note-absent-2026-09-12.md` on `main`
(merged FF-only at `01929cb`), reachable through the vault symlink
`0 - Projects/Cobalt -> /Users/cobalt/cobalt/docs`. The interim
`docs/_inflight/heartbeat-note-absent-2026-09-12.md` copy (placed during the
build, when the report lived only on the unmerged branch) is deleted now that
the report has landed on main, per standing vault-delivery convention.

## 9. Hub addendum — build routing and the Sol→Opus handoff

**Recorded per Dejan's standing/addendum rulings on routing evidence.**

- **Assessment's choice:** Astra's plan §9 recommended GPT-5.6 Sol at high
  effort as builder (Opus reserved for review), citing the correlated-
  assumption risk of using the same house that authored the `None = failed`
  rule now being corrected.
- **Launch 1 — Sol.** Meter state at launch: not checked (`codex /status`
  requires a terminal; non-interactive `codex exec` was launched directly).
  Sol ran ~10 minutes, produced a real, in-scope diff (9 files, 610
  insertions, both 0005 migration files), then hit `codex`'s usage limit
  (reset quoted as 11:45 AM) — **trigger (d)**, a worker stopping on its own
  usage meter.
- **Switch — Sol → Opus.** Original dispatch said wait out the reset and
  relaunch Sol once. Dejan amended this mid-build: a meter stop is trigger
  (d) regardless of house, and the fix is an immediate handoff, never a wait,
  except where a second author reconstructing a coherent diff would cost
  more than the wait. The hub judged that exception did not apply here —
  Astra's plan is written at a level of explicit, line-cited detail designed
  for exactly this kind of house switch — and launched headless Opus without
  waiting for the reset.
- **Launch 2 — Opus.** Meter state: Anthropic weekly meter scarce until
  Sunday 13:00 ET per standing context; spent deliberately on this
  escalation trigger, not opportunistically. Opus was given
  `CONTINUE from the report and the working tree; do not redo completed
  work. You are taking over from another house mid-build — verify what
  exists before extending it.` prepended to the identical brief.
- **What Opus had to verify before extending:** that the confirmation-gate
  answer was actually NARROW (the prior house's diff implied it but never
  stated it — no report existed yet); that the delivered items matched the
  gate; that the regression bound empirically rather than by assumption
  (Opus swapped in pre-patch `runner.py` and reran, getting 14 failed/19
  passed, then restored the tree byte-for-byte); and the RESTARTS
  derivation. Opus wrote the gate answer, the regression-binding proof, and
  the full report — none of that existed when Sol stopped.
- **Hub's own verification (ground truth, not either worker's claims):**
  scope gate, offline pytest gate, migration SQL read directly, migration
  registration order read directly, render.py/writer.py/runner.py diffs read
  in full, boundary tests read and confirmed to assert real behavior against
  the real production note marker shape (`2026-09-11.md`, L45), not an
  invented fixture.
- **One finding not in either worker's report:** `run_beat`'s existing
  `VAULT_DEFERRED` (market_reset) log line was silently downgraded from
  `logger.warning` to `logger.info` when the note-absent case was folded
  into the same branch (`runner.py` around line 435). The plan only asked
  for the *new* note-absent case to log at INFO; it never asked to change
  market_reset's existing severity. Low severity — it changes only log
  level, not outcome, grading, or persistence — but it is an unrequested
  behavior change to already-shipped code, flagged here rather than
  silently accepted.
