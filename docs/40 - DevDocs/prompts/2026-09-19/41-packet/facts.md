# Facts packet — `38-deploy-p4.md` (DEPLOY 2, S2-P4)

Every line below is the CTO desk's own measurement, read from the tree and the reports at 12:5x ET on 2026-09-19. It is a **CLAIM to spot-check**, never settled fact on its own (L35). Where a house's or the hub's own read disagrees with this file, **the tree wins** and the difference is an ESCALATE line.

## 1. What ships, and what does not

| item | value |
|---|---|
| branch merged | `sprint-2/p4` ONLY |
| branch tip when this packet was written | `21bcd5f` (`docs(report): s2-p4 round-2 stop line — P4 ROUND2 9045260, offline 1829/0, ESCALATE 5`); code tip beneath it `9045260` |
| worktree | `/Users/cobalt/cobalt-wt/s2-p4`, branch `sprint-2/p4`, clean |
| merge-base with main | `919d562` |
| commits `main..sprint-2/p4` | **56** |
| main tip when this packet was written | `33462d8` |
| main's drift since `919d562` | **DOCS ONLY** — `git diff --stat 919d562 main -- . ':(exclude)docs'` prints NOTHING. This is why the rebase at §4.1 cannot change code, and why the byte-identity proof there is the real gate. |
| NOT merged here | `ops/2026-09-19` and `archiver/append-0919` — deploy 3, Sunday. They appear in this deploy ONLY as the other two legs of §1's L68 gate. |
| migrations shipping | **0008** `0008_radar_value_movers.sql` · **0009** `0009_picks_missed.sql` |
| settings writes | **NONE.** No `settings load` in any spelling; no `"user".trader_settings` row is read for writing, written, or reverted. |
| new scheduled job | `com.cobalt.replay`, plist `ops/com.cobalt.replay.plist` (arrives with the merge) |

## 2. The migrations — what `CREATED` is allowed to mean at §4.5

Read from the SQL on `sprint-2/p4`:

| migration | objects |
|---|---|
| `0008_radar_value_movers.sql` | `ALTER TABLE system.radar_membership` (adds `rank_metric`, `rank_value` — nullable, additive) · `CREATE TABLE IF NOT EXISTS system.movers_daily` (+ owner `cobalt_system`, index `movers_daily_trade_date`) |
| `0009_picks_missed.sql` | `CREATE TABLE IF NOT EXISTS "user".picks` (+ owner `cobalt_user`, index `picks_picked_at`) · `CREATE TABLE IF NOT EXISTS "user".missed` (+ owner `cobalt_user`, index `missed_trade_date`) |
| `0008 …rollback.sql` | `DROP TABLE IF EXISTS system.movers_daily` · `ALTER TABLE … DROP COLUMN IF EXISTS rank_value, rank_metric` |
| `0009 …rollback.sql` | `DROP TABLE IF EXISTS "user".missed` · `DROP TABLE IF EXISTS "user".picks` |

**Sides, for §6.3's read-back:** `movers_daily` = system; `picks`, `missed` = user. The prompt still instructs the hub to take each side **from the proof table it actually prints**, never from this file.

**Proof-cost budget.** Deploy 1 measured production's own number this morning: BEFORE 47.4 s + AFTER 46.6 s = **94.1 s total**, slowest table `bars` (8,834,532 rows). `cobalt_dev`'s 12 s (1.04 M rows) is NOT a prediction (`s2-p4-verify-2026-09-19.md` §4.4). 0008/0009 add no `bars` rows, so 94 s is the figure to budget; ≈59 % of deploy 1's whole outage was this proof.

**Never rolled back unattended.** The rollback files exist and `--rollback --down-to 0007` is their path, but that flag is absent from the deploy's allowlist in every spelling by design (§8 (3)).

## 3. The five deploy-prompt consequences (`s2-p4-verify-2026-09-19.md` ESCALATE 5 (a)–(e)) — each and how `38` answers it

| # | consequence, as the verify hub wrote it | where `38` answers it |
|---|---|---|
| (a) | the replay `job.result` shape gains `movers_by_side`; until the first `com.cobalt.replay` run, K9.2/K9.5 read FAIL and K9.3/K9.6 ERROR — "a smoke run before that night is red by design" | §6.5 — `cobalt smoke s2` is NOT run and its redness is never this deploy's verdict |
| (b) | `radar/throttle.py`'s probe now takes the column declaration from the radar config | §6.2 — radar log must start clean on the merged config; first live proof Monday 04:00 ET |
| (c) | `com.cobalt.replay` bootstrap once | §5.3 — its own step; a failed bootstrap is an ESCALATE, never a §8 trigger |
| (d) | restart list = aset + radar | §5.1/§5.2 — `RESTARTS: com.cobalt.aset com.cobalt.radar`, 0 UNCLASSIFIED |
| (e) | migration proof budget = production's own 104 s × 2, not dev's 12 s | §0 P13 (read-only preflight) + §4.5 with `timeout` 600000; deploy 1's measured 94.1 s is the live number |

## 4. ESCALATE 21 (a)–(d), the fund rule R16 — deploy-facing half

- (a) `com.cobalt.radar` restarts: config-shape change + static import reach; `com.cobalt.aset` imports `radar.config` and restarts with it (L42, one action). The one config file whose SHAPE changed is `configs/cobalt/radar.yaml` — a REPO file inside the merge, so a `git revert` takes code and config back in one action and there is no settings row to travel with it.
- (b) the live radar collector now requires `Industry` in every screen export (`required_headers`); `export.columns: "0-150"` carries it (151 columns, `Industry` present in all 16,307 sampled files), so no config change is owed — but a screen narrowed by the vault pool block would fail LOUD.
- (c) mover-miss `inputs_sha256` changes for rows computed from now on; safe only while `"user".missed` is undeployed — **this deploy is the moment that stops being true**, which is why 0009 ships in the same merge as the rule.
- (d) live effect: the radar drops every non-blank-`Asset Type` row and every `Industry = Exchange Traded Fund` row. Evidence sample: 643,998 rows / 16,307 files, 5,702 distinct fund tickers, **dropped 131,348, stock rows hit 0**.

## 5. K3 / A7 — the check the deploy smoke must NOT fail on (ESCALATE 2)

Confirmed on real Postgres (`s2-p4-verify-2026-09-19.md` §4.6, test `test_k3_hold_row_reads_red_documented_ambiguity`): a HOLD-shaped row (pre-deploy `first_seen_at`, `rank_metric` NULL, `last_scan_id` = the pool's post-cutoff scan) makes `rescanned_admitted ≥ 1` and `rescanned_metric_missing ≥ 1`, and the framework's grader returns **FAIL** naming `rescanned_metric_missing` — indistinguishable by column from a RETAIN defect. The desk's ruling is OWED (options: accept the loud false positive with the `degraded_sources` procedure already in K3's `expect_text` — the verify hub's recommendation; a row-level discriminator = schema change; or revert the `b327221` RETAIN grading). Until it is ruled, `38` §6.5 keeps `cobalt smoke s2` out of the deploy entirely and forbids "smoke red" as a verdict.

## 6. L68 — the gate, and the three unmerged branches

Law text, verbatim: *"No branch merges while a second unmerged branch exists, unless an integrated pre-merge gate on the stacked tree is green — the offline suite and the with-DB suite run on the branch that combines them, before the merge, never after it in `~/cobalt`."*

| branch | tip at writing | worktree | lands in |
|---|---|---|---|
| `sprint-2/p4` | `21bcd5f` | `/Users/cobalt/cobalt-wt/s2-p4` | **deploy 2 — this prompt** |
| `ops/2026-09-19` | `a868a69` at the ref when this packet was written (the ops DB run's stop line names code `d860bf7` / report `be00506`; take the live tip, not this number) | `/Users/cobalt/cobalt-wt/ops-2026-09-19` | deploy 3 (Sunday) |
| `archiver/append-0919` | `cdd71fe` | `/Users/cobalt/cobalt-wt/archiver-append` | deploy 3 (Sunday) |

Gate branch built by the deploy hub: `stack/deploy2-0919` at `/Users/cobalt/cobalt-wt/stack-deploy2-0919`, from `main`, then three ordinary merges (P4, ops, archiver). It is a **gate artifact**: never merged, never pushed, never rebased; the desk removes it at the close.

Reference suite numbers, for context only — the gate's own bar is `0 failed`, nothing else:
- P4 alone: offline `1829 passed, 324 skipped, 1 xfailed`, 0 failed · DB `2136/0` plus the two owed `requires_db` tests that `37-p4-db-run.md` runs.
- ops-0919: `offline 1608/0 (302 skipped)` · `db 61/0` · `cobalt_dev: 0001–0009, unchanged`.
- archiver, offline: `1866 passed, 320 skipped`, 0 failed. **Its with-DB run is NOT clean** — stop line `ARCHIVER DB d2099e1 | offline 1866/0 (320 skipped) | db 154/3 …`: 20 of its 23 `requires_db` tests pass, **3 are RED and stay red**: `test_the_user_role_has_no_grant_on_either_table[archive_progress]` and `[archive_incidents]` (DB-1 — `0001_schemas.sql:124` blanket `GRANT SELECT ON ALL TABLES IN SCHEMA system TO cobalt_user` + `:150-152` `ALTER DEFAULT PRIVILEGES`; the spec's §11 sentence is not achievable without an explicit `REVOKE`, a tenancy ruling OWED from Dejan) and `test_the_own_connection_upsert_survives_another_transactions_rollback` (DB-2 — unobservable under conftest's autouse single-transaction fixture; the alternatives are narrowing the test, which L45's companion ruling forbids, or amending conftest RULING 7). **Consequence for this deploy: the three-branch with-DB gate CANNOT be green while those three are red**, which is why `38` §0 P15 makes a later `db <p>/0` line on that branch a hard PREFLIGHT precondition and refuses "green except known reds".
- **Step-order trap, proven not asserted (archiver DB run, run 1 = `12 failed, 145 passed`):** with `cobalt_dev` at 0001–0009 and the archiver's two tables dropped, 20 of its 23 `requires_db` tests cannot run — only 3 are self-contained round trips; seven need the tables via the `real_connect` fixture and thirteen via `BarStore().ensure_schema()`, which creates neither. **So the stacked gate must apply FORWARD (0001–0011) before the suite, and restore to 0001–0009 after it** (`38` §1.4 (b)→(g)).
- `cobalt_dev` expected state at gate time (before §1.4): **0001–0009** — `archive_progress` / `archive_incidents` ABSENT, P4's `movers_daily` / `picks` / `missed` PRESENT. After §1.4 (f): back to exactly that, proven against the baseline table.
- **Likely conflict point when the stack is built:** P4 and the archiver both edit `src/cobalt/db_migrations/__init__.py` (`FORWARD`/`REVERSE`) and both touch `placement.py`, `src/cobalt/cli.py`, `configs/cobalt/taxonomy/tunables.yaml`, `archiver/runner.py`, `archiver/store.py` (the archiver build's own cross-branch ESCALATE (iii)). A conflict there is the integration seam L68 exists to surface — reported, never resolved inside the deploy.

## 7. Cards — live, and untouched by this deploy

`reports/cards-golive-2026-09-19.md`, last line: `CARDS LIVE 12:30:01 ET · file sha256 f3663399… · stored values: match · resident logs clean: yes · rollback: not used · ESCALATE: 1`. `radar.cards_enabled` is **true** in `"user".trader_settings` since 12:30:01 ET (R20). Consequences carried into `38`: the six `settings load` strings of `02-deploy-stack-3.md` are DROPPED from the launch line; `mkdir -p …/pre-stack-0919/daymode-settings-rollback` is DROPPED (no rollback directory is built, because no settings file is read); `radar evaluate --replay *` is DROPPED (deploy 1 used it as P2's DARK proof; with cards enabled it has not been established that a replay stays read-only, so it is not typed at all); §8 never turns the cards dark in any branch; §6.4 READS the row back as a smoke check.

## 8. Names, tags, window

| name | value | why |
|---|---|---|
| session | `deploy-p4-0919` | deploy 1 was `deploy-stack-0919` |
| report | `docs/40 - DevDocs/reports/deploy-p4-2026-09-19.md` | `deploy-2026-09-19.md` is deploy 1's |
| pre-deploy tag | `pre-p4-0919` | the durable rollback point; the restic snapshot is pruned by the 21:40 nightly (ops ESCALATE 4) |
| deploy tag | `deploy-2026-09-19b` | `deploy-2026-09-19` already exists (deploy 1, `2893a7f`); `git tag` refuses a duplicate. The `b` keeps the date sortable and marks the second deploy of the same date. Had the run been scheduled for Sunday it would be `deploy-2026-09-20`; the prompt fixes the name at approval and refuses (`FAILED: window`) rather than renaming itself. |
| rollback directory | **none** | no settings file is loaded |
| window | START only when `date` ≤ **18:30 ET, Saturday 2026-09-19** | L43's 20:00–21:00 / overnight-idle restart window binds **"on a trading day"**; Saturday is not one and no scanning session can be open (`radar cycle: idle:overnight`), which is the basis deploy 1 ran on at 08:19 ET today under 09-18 R3/R5. The 18:30 cap is margin against tonight's one-shots — `com.cobalt.archiver` 20:30 ET and the nightly backup 21:40 ET — not against L43. Re-checked before bootout and at 5.2; ≥ 19:40 ET before bootout = plain `FAILED: window`. |

## 9. Tags and jobs, production state before the deploy

- Tags present: `deploy-2026-09-19`, `pre-stack-0919`, `pre-stack-0918`, `pre-ops-0918`, `deploy-2026-09-17`, `pre-s2-p2`, `deploy-2026-09-16`, `deploy-2026-09-15`, `s2-p1`, `s2-p1-stage1`, `pre-s2-p1`, `pre-assessment`.
- Jobs before the merge: **15 registered — 6 resident, 9 one-shot** (deploy 1's `cobalt jobs register` output). After the merge + `jobs register`: **16 — 6 resident, 10 one-shot** (`cobalt validate` on `cobalt_dev` with P4 applied reported exactly that, with `registry <-> ops/: 16 label(s), exact match` and `registry <-> plists: schedules and COBALT_ENV agree on every job`).
- `com.cobalt.replay` plist, read in full: `COBALT_ENV=production`, `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`, `uv run cobalt replay nightly`, `WorkingDirectory /Users/cobalt/cobalt`, `RunAtLoad false`, `StartCalendarInterval` Mon–Fri **21:10** local (ET), logs `logs/replay.log` / `logs/replay.err`. Bootstrapping it on a Saturday arms it and runs nothing until **Monday 2026-09-21 21:10 ET**.
- Production heartbeat at deploy 1 (08:16 and 08:21 ET): **GREEN**, 15 jobs, 12 probes, nothing red; the only non-OK line was the standing `AMB com.cobalt.herdr unmanaged` (declared interim). `ENTERED RED` count in `logs/heartbeat.log`: 93 before and after deploy 1.
- Duplicate-table probe (P11's query) returned **zero rows** at 06:57 and 08:16 ET today.

## 10. Known dirt on main at writing (for §3.1)

` M docs/40 - DevDocs/reports/seat-usage.md` · untracked `docs/40 - DevDocs/prompts/2026-09-19/31-packet/p2-dark-settings.yaml` and `p2-live-settings.yaml` — copies of files under gitignored `data/backups/`, **never `git add`ed** (the desk's own ESCALATE-1 of 12:10 ET); the desk's live `cto-2026-09-19.md` is also expected to be modified when the hub runs.

## 11. What this packet could NOT establish

1. Whether `COBALT_ENV=production uv run cobalt radar evaluate --replay <date>` stays read-only now that `radar.cards_enabled` is true — deploy 1's `writes: none` was measured in DARK mode. Not typed in `38` at all.
2. The exact stop line `37-p4-db-run.md` will write (the prompt is committed, the run had not finished): `38` §2.2 keys on its declared shape `P4 DB <sha> | … | owed requires_db: <names → PASSED>` and fails loud if it is absent or different.
3. Whether the gate's stacked suites go green — no house has run P4 + ops + archiver together, and **as of now they cannot**: the archiver branch carries three red `requires_db` tests (DB-1 ×2, DB-2) awaiting rulings from Dejan. `38` P15 turns that into a hard stop rather than an exception. **OPEN for the desk: this deploy is not launchable until either those three reds are resolved on `archiver/append-0919`, or Dejan rules the narrower L68 reading (gate only what is about to land = P4 on main).** Neither is this packet's to choose.
4. Whether `ops/2026-09-19`'s ref will still read `a868a69` at gate time (its round-3 check was in flight). `38` records the live tip rather than asserting this one.
