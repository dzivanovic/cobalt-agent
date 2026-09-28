# SMOKE-ONLY DEPLOY DRAFT — 2026-09-23 (seat `smoke-only-deploy-draft-0923`, Opus 5.5)

## §0 Headline
Wrote `prompts/2026-09-23/68-smoke-only-deploy.md`. It re-issues `59` for `s2/smoke-fix-0922` alone: rebase-then-ff (L54) through `07`'s own `merge --ff-only deploy/stacked-0923`, no mid-run commit, no migration, no live-note step and no vault write. Both residents go down.
Wrote `prompts/2026-09-23/69-review-smoke-only-deploy.md`, the L67 read (Grok + Gemini + an Opus reader, house lane, stagger `62` / `65` / `19` PAUSED).
Dev DB at `0013`: **harmless**. No test or code on main or the branch reads `tunables.slug` nullability, and there is no migration ledger. The with-DB gate is the run-time proof.
New rule strings: **0**. A machine check matched all 43 tokens of `68` against `07` and all 16 of `69` against `08`. ESCALATE: 8.
Started 16:01 ET, done 16:1x ET. Nothing run, committed or launched (L36). The only writes are these three files.

## Delta from `59`
| area | `59` | `68` | why |
|---|---|---|---|
| branches | setups + smoke fix | smoke fix ONLY; setups NAMED as not shipping | L43 / R78; L68 SCOPE |
| merge shape | gate branch: two merges, then `main` merged INTO the gate, then ff; rollback ONE `revert -m 2` | REBASE-THEN-FF: the gate `merge --no-edit s2/smoke-fix-0922` must FAST-FORWARD (gate = branch = `<ship>`); `main` ff's to it. Rollback = `git revert --no-edit <pre-merge>..<ship>` | L54 as scoped 09-22 R82 C12 ("Rebase-then-ff on every single-branch merge"; the gate-branch `-m 2` is the SIBLING exception). The gate worktree is kept because `07`'s only `--ff-only` and `.env` strings name `deploy/stacked-0923` / `stacked-0923` |
| mid-run commit | REQUIRED at 2.8 (to create the main-into-gate merge) | NONE. The report stays untracked until STEP-7 or a pre-bootout FAILED. P12 + 3.1 require `main` == `<main-at-gate>` | a commit on main would break the fast-forward |
| migration | 0013 prod `--allow-prod` (+ proof-only P14-M, 4.4, read-back) | none. P14 records `<slug0>` and smoke (g) requires it UNCHANGED | the branch ships none. 2.6 FAILs on any `db_migrations` or `taxonomy/migrations` path |
| dev DB | (b3) forward migrate to 0013 | (b2) proof-only baseline only. No forward migrate | the branch ships no migration. P7 = the decision below |
| live-note 2.3 (d) | `COBALT_LIVE_VAULT_ROOT` run of 3 test files | NOT carried | the branch's 10 paths carry no `@requires_vault` marker (git grep on the branch hit `radar_p2_support.py`, `test_radar_evaluate.py`, `test_replay_line.py`, `test_catalyst.py`, none of the 10). ESCALATE 5 |
| STEP-6 R119 vault write | dev → dry-run → apply | NOT carried. `R119: NOT IN THIS DEPLOY` | rides with setups |
| backup snapshot 3.4 | `backup run` | dropped | no schema change. `05` (09-22, no migration) took none; the rollback point is the tag `pre-smoke-0923` + git revert. ESCALATE 4 |
| preflight | P5/P6 ×3, P8 blind values, P9 `stacked-deploy-review` | P5/P6 smoke only. P8 dropped. P9 = `smoke-only-deploy-review-2026-09-23.md` (`69`). P7 = dev-DB state + `ls -la /Users/cobalt/cobalt-wt/*/.env` lane check. P12 adds `main` == gate | one branch |
| markers | `s2p2.2` → 1, `unranked_rows` ≥ 1 | `unranked_rows` ≥ 1; `s2p2.2` must STAY 0 | proves the dropped branch did not land |
| tags | `pre-stacked-0923`, `deploy-2026-09-23` | `pre-smoke-0923`, `deploy-2026-09-23` | — |
| relaunch rule | (i)–(vi) around the `-m 2` merge and the migration | (i)–(v) around the ff and the ranged revert (a partial revert is named, never resumed blind) | shape change |
| report / seat | `deploy-2026-09-23-r3.md`, `stacked-deploy-r3-0923` | `deploy-2026-09-23-r5.md`, `smoke-only-deploy-0923`, placeholder `R__L` | as briefed |
| stop line | `STACKED DEPLOY DONE …` | `SMOKE ONLY DEPLOY DONE <ship> · tag deploy-2026-09-23 · branches: 1 (setups dropped, R78) · migration: none · …` | — |
| unchanged | — | window (R5, 19:55 / 19:58), L66 both-down shape, `.env` discipline, P14 baseline incl. the carried per-ticker radar kind and the known replay RED, 4.7 smoke rows (a)–(f), STEP-5's one-path rule, L74 | — |

## THE DEV-DB DECISION
**HARMLESS. No step is needed before `68`.** The evidence is the drafter's reads at 16:0x ET, on main `e4f45faa` and branch `s2/smoke-fix-0922` (`17dd21b7`):
- **What 0013 does.** It is a single `ALTER TABLE "user".tunables ALTER COLUMN slug DROP NOT NULL`, inside a `DO` block that is a NOTICE when the table is absent (`setups-c1/src/cobalt/db_migrations/0013_tunables_slug_nullable.sql`). It creates and removes no table, column or row.
- **No migration ledger.** Main's `src/cobalt/db_migrations/__init__.py` is an ordered FORWARD tuple of idempotent scripts, and "nothing asserts contiguity". Main's `migrate --proof-only` neither knows nor looks for 0013. `59` 2.3 (b3) showed every table `OK` with digests unchanged after 0013.
- **No test reads it.** `grep -rn "NotNullViolation\|is_nullable\|attnotnull\|0013\|slug IS NULL" tests/` finds three nullability reads on main and the same on the branch:
  - `test_tenancy.py:268` and `test_radar_score_migration.py:390` read ONLY `column_name = 'user_id'`;
  - `test_vault_restore.py:557` reads `vault_writes.sync_revert_of`.
  - No test pins `tunables.slug` and none expects a NotNull error. `41`'s `0017` red came from the placement test, which counts TABLES (`58` WHY); 0013 adds no table.
- **No code reads it.** `src/cobalt/taxonomy/store.py:127`, `:136` read `SELECT key, row FROM tunables`, and `:185` inserts a non-NULL slug. `test_taxonomy_store.py:66-82` empties `tunables` inside a never-committed transaction.
- **Supporting evidence, not proof.** `59`'s with-DB suite ran GREEN at 0013 (`2849 passed, 6 skipped, 1 xfailed`) on a tree that contained this branch's code, plus the setups code.
- **If the run goes red anyway.** `68` 2.3 (c) + P7 name the dev-DB-seam FAILED line. The lawful restore is a dev-DB hub run from `setups-c1` with `58`'s string `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0011`. That string is NEW to `07`'s list: R72 approved it for `0017` only, so it needs his word again. Its reverse REFUSES while a `slug IS NULL` row exists. It is not in `68`'s list.

## NEW strings
| launch line | tokens | checked against | not in source | NEW |
|---|---|---|---|---|
| `68` (3) | 43 (40 allow + 3 deny) + `--add-dir` ×2 | `07` line 6 (57 tokens: 54 allow + 3 deny) | 0 | **0** |
| `69` | 16 (10 allow + 3 deny + `--add-dir` ×3) | `08`'s launch line | identical (diff empty) | **0** |
Dropped from `07`, 14 allows: `setups-c1 rebase main` / `--abort`, `stacked-0923 merge --no-edit setups/seven-0921`, `… merge --no-edit main`, `COBALT_LIVE_VAULT_ROOT=… uv run pytest *`, `COBALT_ENV=dev uv run cobalt db migrate`, `backup run*`, `backup status*`, prod `db migrate --allow-prod --proof-only`, prod `db migrate --allow-prod`, and the four `taxonomy` strings.
One string is NAMED for his word and is NOT in either file: the dev rollback string above, needed only if 2.3 (c) goes red on the dev DB.

## ESCALATE
1. **The shape: rebase-then-ff under the gate name.** L54 (scoped 09-22) makes a single-branch merge rebase-then-ff. `07`'s only `--ff-only` string names `deploy/stacked-0923`, so the gate fast-forwards onto the branch and `main` fast-forwards onto the gate. This requires NO commit on main from launch to STEP-4.3. **ASK DESK:** re-cut the gate (bare command (1)) AFTER the desk's last commit (the `R__L` launch row), and hold all commits until the stop line. P12 / 3.1 FAIL safely before any bootout if main moved. [16:1x]
2. **R5's set-aside.** `68` reads R5 ("after I am done trading", with the radar window set aside) as covering today's ONE deploy EVENT, which has not happened yet: `07`, `41` and `59` all stopped before a merge. R78 has no words of his. **ASK DESK:** confirm, or get his word. The safe default in `68` is to proceed under R5, as `59` did. [16:1x]
3. **R52 carries a subset.** `68`'s authorization reads R52 (`07`'s ONE list, "Approved all commands you need") plus R78 (the drop) and `R__L`. No new approval row is asked for.
4. **The backup snapshot is dropped** (no schema change; `05` precedent). If the desk wants it, `07`'s two `backup` strings can go back in with no NEW string.
5. **The live-DRC reach is UNPROVEN (L70).** `tests/cobalt/test_replay_line.py:256` is `@requires_vault` (env `COBALT_TEST_LIVE_DRC`). It imports `cobalt.replay.line`, which imports `.models` (`src/cobalt/replay/line.py:49`, `FORMATION_UNAVAILABLE, ReplayError`), a file this branch changes. The branch does not touch that test, and `07` has no string for that env var. It stays UNPROVEN unless the desk adds a NEW string on his word.
6. **The glob lane check.** P7's `ls -la /Users/cobalt/cobalt-wt/*/.env` expects zsh `no matches found`. It is covered by `07`'s `Bash(ls *)` and follows `58` step 2's precedent. `69` Q1 asks the houses to test the spelling.
7. **Still owed to the setups deploy:** migration `0013` (prod), `EVALUATOR_VERSION s2p2.2`, the R119 note, and the `tests/cobalt/test_replay_runner.py` seam with this fix (that deploy's own gate, L68 SCOPE). `cobalt_dev` stays at 0013 until then.
8. **Placeholders.** `68` has `R__L` ×3 (desk launch row) and its placeholder gate. `69` has `R__V` (its own launch row). The `R__L` text inside `69` is a quote and is never filled there. The desk writes these literals on `69`'s row: `62 is not running`, `65 is not running`, `19 is PAUSED`, each with `69-review-smoke-only-deploy.md`. Timing: `68` is ≈63 KB (two packet parts) and each house gets 15 min, so launch `69` by ≈16:30 to leave the window.

SMOKE ONLY DEPLOY DRAFTED · migration: none · dev db: harmless · new rule strings: 0 · ESCALATE: 8
