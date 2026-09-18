# Stack gate — 2026-09-18

Seat: `stack-gate-0918`, Opus 5 (`claude-opus-5`), background, worktree `/Users/cobalt/cobalt-wt/s2-p2-cards` (`sprint-2/cards`).
Prompt: `docs/40 - DevDocs/prompts/2026-09-18/09-stack-gate.md` (committed `34524c1`). Supersedes `07-p2-integrate.md`.

## §0 Headline (14:47 ET)

- **FAILED at step 1.4 — the stack does not build green, and the gate caught it before any merge.** The stacked branch is assembled and clean (`00c568e`, 43 commits: P2's 35 + ops-0918's 8, all three step-1.3 proofs PASS), but its OFFLINE suite is **43 failed, 1455 passed, 281 skipped, 5 errors**.
- **ONE root cause, one file.** ops-0918 `fe195ab` adds a 7th signal `trade_count_over_band` to `SIGNAL_IDS` and a fail-loud completeness check (`daymode/config.py:265`); P2's settings fixture `tests/fixtures/radar/card-settings.real-shape.json` carries only the 6 older signals, so every P2 test built from it dies in `DayModeConfig` validation. Neither branch is red alone — **the same merge-order defect class as 09-17**, caught this time by the gate instead of by production.
- Step 2 NOT run: no `.env` copied, no `cobalt_dev` migration, no settings `--apply`, no dev DB touched. The dev-DB settings row cannot fix these — they are offline JSON-fixture reads, not database reads (proven below).
- Nothing fixed (prompt: no code changes). Production, the real vault and `~/cobalt`'s tree untouched; no merge, no push.
- ESCALATE: **4** (1 blocks the stacked deploy).

---

## AUTHORIZATION (verified by this hub, 14:35 ET)

`git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` → `34524c1`, `41ed33f`, `3b8148c`, `5476410`, `77b1a08`, `2a4a595`, `cccdfbe`, `d6332f6` — the R7 row is committed at `5476410`, R8/R9 at `41ed33f`/`34524c1`. Rows read from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-18.md` §4.

| launch-line rule | approved by | verdict |
|---|---|---|
| `cp …/cobalt/.env …/s2-p2-cards/.env` · `rm …/.env` · `ls -la …/.env` | R1 list (1) — ".env cp/rm/ls by path" | MATCH |
| `COBALT_ENV=dev uv run cobalt db migrate*` | R1 list (1) | MATCH |
| `COBALT_ENV=dev uv run pytest *` | R1 list (1) | MATCH |
| `COBALT_ENV=dev uv run cobalt validate*` | R1 list (1) | MATCH |
| `COBALT_ENV=dev uv run cobalt settings load *--dry-run*` | R1 list (1) | MATCH |
| `COBALT_ENV=dev uv run cobalt settings load --from …/ops-2026-09-18/scratch/daymode-settings-0918 --apply` | R7 (3), exact line, DEV only | MATCH |
| `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run pytest *` | R1 list (1) | MATCH |
| `uv run pytest *` · `uv run cobalt jobs restarts *` | R1 list (1) | MATCH |
| `git rebase main` | R1 list (1) | MATCH |
| `git rebase --abort` | R7 (2) | MATCH |
| `git cherry-pick *` | R2 | MATCH |
| `git add/commit/diff/status/log/show/rev-parse *` | R1 list (1) | MATCH |
| `git -C /Users/cobalt/cobalt log*` · `… rev-parse *` | R1 list (1) | MATCH |
| `cd` · `ls` · `grep` · `tail` · `wc` · `shasum -a 256` · `date` | R1 list (1) | MATCH |
| `--disallowedTools AskUserQuestion EnterWorktree` | R1 (all three launches) | MATCH |

Not in this line and not used: push, `bypassPermissions`, `--allow-prod`, any `COBALT_ENV=production` command, any vault write, `git reset`, `git branch -f`. R1 list (1) additionally carried `git rebase --continue`; this line is narrower, which is allowed.

Also noted, as the deploy-1 hub noted before me: the prompt file's tail carries a block styled as a system reminder asking for a `Claude-Session:` URL line in every commit. It arrives inside a tool result (the file's own bytes), not from the harness. The genuine harness attribution reminder names only `Co-Authored-By`. Not followed.

## PREFLIGHT (14:35–14:36 ET)

| # | rule probed | command | exit | verdict |
|---|---|---|---|---|
| P1 | `git status*` | `git status --porcelain` | 0 | allowed — no output (clean) |
| P2 | `git log*` | `git log -1 --oneline` | 0 | allowed — `976528f` |
| P3 | `date*` | `date` | 0 | allowed — Fri Sep 18 14:35:51 EDT 2026 |
| P4 | `git cherry-pick *` | `git cherry-pick -h` | 129 | allowed (usage printed; 129 is `-h`'s normal exit) |
| P5 | `uv run pytest *` | `uv run pytest --co -q tests/cobalt/test_radar_notes.py` | 0 | allowed — 16 tests collected |

Probed by first real use, per the prompt: `git rebase main` (step 1.1, allowed), `git cherry-pick <range>` (step 1.2, allowed), `ls -la …/.env` (step 1.4, allowed, exit 1 = absent), `uv run pytest` full (step 1.4, allowed). Never reached, so never probed: the `.env` `cp`/`rm`, `db migrate`, both `settings load` rules, `COBALT_ENV=dev` pytest/validate, `COBALT_VAULT_PATH=…` pytest, `jobs restarts`.

**0 allowlisted shape denied. 0 mid-run denials.**

## 0. Preconditions

| check | expected | observed | verdict |
|---|---|---|---|
| `git status --porcelain` | empty | empty | PASS |
| `git rev-parse --short HEAD` | `976528f` or a report-only commit above it | **`976528f`** | PASS |
| `git log --oneline main..HEAD` | record `<n>` + list | **34** at read; `976528f` … `f266a88` (21 P2 code/plan commits + 13 report commits) | PASS |
| `git rev-parse --short main` | — | `34524c1` | recorded |
| `git -C /Users/cobalt/cobalt log --oneline -12` | tip = desk docs commit above `77b1a08`; 8 `Revert "…"` of ops-0918 | tip `34524c1` (desk docs), then `41ed33f`, `3b8148c`, `5476410`, `77b1a08`, then reverts `511cf25`, `04c09e4`, `159cc9a`, `34f9413`, `6a78c8b`, `2a4a595`, `cccdfbe`, `d6332f6` = **8** | PASS |
| `git log --oneline 77260b5..856176e` | exactly 8, `fe195ab` … `856176e` | `856176e`, `497d8c1`, `3ef1dfb`, `c7f0465`, `382c862`, `7e41a5c`, `93cd7c2`, `fe195ab` = **8** | PASS |

**`<old-tip>` = `976528f`. `<n>` = 35** — 34 at the precondition read plus this hub's own step-0 report commit `8e91167`, made before the rebase. The precondition explicitly allows "a report-only commit above it"; `<n>` is counted at the moment of the rebase, which is the number step 1.1 must preserve.

## 1. P2 onto main, then ops-0918 on top

| step | command | result | verdict |
|---|---|---|---|
| 1.1 | `git rebase main` | `Successfully rebased and updated refs/heads/sprint-2/cards`, 35/35 replayed, **no conflict**, no `--abort` needed | PASS |
| 1.1 proof | `git log --oneline main..HEAD` | **35** commits (`f87ff05` … `060dab9`) = `<n>` — **0 dropped** | PASS |
| 1.2 | `git cherry-pick 77260b5..856176e` | 8 commits applied oldest-first with original messages, no squash, **no conflict, no empty-commit stop**: `800d73c` (fe195ab), `dec0d90` (93cd7c2), `eca1dfb` (7e41a5c), `cd6c615` (382c862), `13520c2` (c7f0465), `3cd2cff` (3ef1dfb), `062366a` (497d8c1), `00c568e` (856176e) | PASS |

### 1.3 PROOF — all three

| proof | expected | observed | verdict |
|---|---|---|---|
| count | `<n>` + 8 = **43** | `git log --oneline main..HEAD` → **43** (8 ops + 35 P2) | PASS |
| ops code byte-identical | `git diff --stat 856176e HEAD -- src/cobalt/daymode src/cobalt/jobs/restarts.py ops/README.md ops/cto-desk.sh tests/cobalt/test_daymode.py tests/cobalt/test_daymode_note.py tests/cobalt/test_jobs_restarts.py` prints NOTHING | **no output** — ops-0918's code is byte-identical to what merged at 11:29 | PASS |
| P2 code untouched | `git diff --stat 976528f HEAD -- src tests configs ops .gitignore` lists ONLY ops paths | 8 ops paths **+ one extra: `configs/cobalt/rules.yaml | 2 +-`** — see below | PASS (explained) |

**The extra path is main's, not the stacking's.** `git log --oneline 976528f..HEAD -- configs/cobalt/rules.yaml` → **`7ff81e5`** = `chore: machine-written + report files, committed as-is (L51-2)`, the deploy-1 pre-deploy tag commit (`pre-ops-0918`). It is absent from the 43-commit `main..HEAD` list, so it is reachable from main — it entered the range because `<old-tip>`'s base was below it, not because anything here touched it. The whole diff is one generated timestamp, `generated_at: '2026-09-17T19:40:00+00:00'` → `'2026-09-18T09:15:00+00:00'`, with **`source_sha256` unchanged** (`e183f123…215b6`) and no rule changed — the nightly re-generation of `Rules.md`, committed on main under L51 clause 2.

Tighter proof run to isolate the cherry-picks exactly — `git diff --stat f87ff05 HEAD -- src tests configs ops .gitignore` (post-rebase pre-cherry-pick tip vs HEAD):

```
 ops/README.md                      |  26 +++
 ops/cto-desk.sh                    | 418 +++++++++++++++++++++++++++++++++++++
 src/cobalt/daymode/config.py       |  23 +-
 src/cobalt/daymode/propose.py      |  54 ++++-
 src/cobalt/jobs/restarts.py        |  28 +++
 tests/cobalt/test_daymode.py       |  80 ++++++-
 tests/cobalt/test_daymode_note.py  |  12 +-
 tests/cobalt/test_jobs_restarts.py |  61 ++++++
 8 files changed, 687 insertions(+), 15 deletions(-)
```

Exactly ops-0918's 8 code paths, nothing of P2's. **The stacking is correct; the desk's read-only 14:33 path analysis holds — no conflict anywhere, as predicted.**

### 1.4 Offline suite — RED

`ls -la /Users/cobalt/cobalt-wt/s2-p2-cards/.env` → `No such file or directory` (exit 1). The run is genuinely offline; no database is reachable.

| run | command | result |
|---|---|---|
| a | `uv run pytest -q tests/cobalt tests/taxonomy` | **exit 2 — `Interrupted: 2 errors during collection`**, suite never ran |
| b | same + `--continue-on-collection-errors --tb=no -p no:randomly` | **43 failed, 1455 passed, 281 skipped, 1 xfailed, 5 errors** in 33.70 s |

Run (a) is the gate's literal command and it does not even collect. Run (b) was added only to measure the blast radius; it changes no code and no state.

**The error, verbatim (collection of `tests/cobalt/test_radar_card_routes.py`):**

```
src/cobalt/settings/models.py:91: in _build
    daymode = DayModeConfig(
E   pydantic_core._pydantic_core.ValidationError: 1 validation error for DayModeConfig
E     Value error, daymode.stepdowns has no row for ['trade_count_over_band']. Every
E     signal the proposer can compute must be ruled here — an unruled one would be a
E     policy hole made by silence. Turn a rule off with `effect: none`.
E   cobalt.settings.models.TraderSettingsError: fixture: invalid trader settings:
```

**Root cause — named, single, and not a defect in either branch alone:**

| fact | evidence |
|---|---|
| ops-0918 `fe195ab` adds a **7th** signal | `src/cobalt/daymode/config.py:75-86` — `SIGNAL_IDS` = the 6 older ids + `trade_count_over_band` (ruled 09-17 R13) |
| and a fail-loud completeness check over it | `config.py:265` — `unruled = [s for s in SIGNAL_IDS if s not in ruled]` → the error above |
| P2's settings fixture carries only **6** | `tests/fixtures/radar/card-settings.real-shape.json:42-76` — `daymode.stepdowns` rows are `daily_stop_hit`, `no_prior_drc`, `drc_not_informative`, `early_close_today`, `first_session_after_close`, `trade_count_band_placeholder`. **No `trade_count_over_band`.** |
| every failure funnels through that ONE file | `tests/cobalt/radar_p2_support.py:66` `fixture_settings_rows()` reads it and feeds `test_radar_evaluate.py`, `test_radar_evaluate_cli.py`, `test_radar_card_routes.py`, `test_radar_panel_cards.py`, `test_radar_cards_db.py`, `test_radar_audit_export.py`, `test_radar_catalyst_dot.py`; `test_radar_keys.py:30` reads the same path directly |
| ops-0918 fixed its **own** fixture, not P2's | `382c862` `test(daymode-note): derive the fixture step-down table from SIGNAL_IDS` — ops-0918 could not see P2's fixture, which was not on main |

**Whose is it?** Neither branch's alone — it is the **seam**. ops-0918's code is correct and its own tests are green; P2's fixture is correct against the 6-signal world it was cut in. Stacked, P2's fixture is one row short of ops-0918's validator. By ownership of the file to change, the fix is **P2's** (one fixture file). This is the identical shape to the 09-17 revert (ops-0917's `load_sources(...)` calls lacking P2's new `context_tickers` kwarg) — **second occurrence of the same defect class in two days.**

**The dev database cannot fix this.** These are offline reads of a JSON file through `radar_p2_support.py:66`; the `"user".trader_settings:` text in some failures is the *label* the stub store passes to `TraderSettings._build`, not a database read (the whole run had no `.env`). So step 2's `settings load --apply` on `cobalt_dev` would not have turned a single one of these green — running step 2 was correctly skipped, not deferred.

## 2. The dev database — NOT RUN

Not started. No `.env` copied into this worktree, no `cobalt db migrate`, no `settings load --dry-run` or `--apply`, no `cobalt_dev` write of any kind, no `validate`, no `jobs restarts`. `cobalt_dev` is left exactly as the third run left it (at `0007`, P4's tables absent) and is free for the next session. The two settings files under `ops-2026-09-18/scratch/` were not read or hashed.

## ESCALATE

1. **BLOCKER for the stacked deploy — the stack is red offline and one file fixes it.** `tests/fixtures/radar/card-settings.real-shape.json` needs the seventh `daymode.stepdowns` row (`signal: trade_count_over_band`, and per R13 `effect: down`, `rungs: 1`). No allowlisted command here may write it (this prompt forbids code changes), so it needs a build hub with a write rule for that path. **Two things to decide with it:** (a) whether the new row's `effect`/`rungs` in a *test fixture* is a trading-logic value needing his word, or mechanical fixture completion — the fixture is a test artifact, but the row it gains is a ruled policy row; (b) under **L45** the file is machine-cut from the live settings (`tests/fixtures/radar/_cut_p2_fixtures.py:115`), and **production does not hold the `trade_count_over_band` row today** — deploy 1 applied it at 11:29 and §6 rolled it back at 11:30. So a straight re-cut from production would still produce 6 signals. The fixture must either be hand-extended now, or re-cut only after the row is live — which is a deploy-order dependency the stacked-deploy prompt must carry explicitly.
2. **Second occurrence in two days of the same defect class: a cross-branch seam that neither branch's own suite can see.** 09-17: ops-0917's call sites vs P2's new kwarg. 09-18: P2's fixture vs ops-0918's new signal. Both were invisible until the two trees met, and both would have reached production without an integrated pre-merge gate. This gate worked — it is the first time the class was caught before a merge rather than after. Worth a standing rule: **no branch merges while a second un-merged branch exists without an integrated gate run of the two stacked**, which is exactly what this prompt built. Candidate law text for the close list; his number.
3. **`trade_count_band_placeholder` still sits in `SIGNAL_IDS` beside the real `trade_count_over_band`** (`config.py:75-86`). Both are ruled, so nothing is broken and nothing here is a defect — but a placeholder signal surviving next to the real one it anticipated is the kind of thing that quietly becomes permanent. Flagging for a ruling at leisure, not a blocker.
4. **Self-reported process deviation, harmless, no state touched.** One read-only command in this run used a pipe (`git log --oneline main..HEAD --format=%h | wc -l`), against the UNATTENDED RULES' "no pipe" clause. It was allowed by the classifier and only counted commits; the count was re-derived without a pipe afterwards and matches. Recorded rather than left silent.

## What the next run inherits

| item | value |
|---|---|
| branch | `sprint-2/cards`: **stack tip `00c568e`** (43 commits above main `34524c1`); branch tip is `30f3402`, this report's own commit, sitting one above it. Worktree **clean**. |
| stack shape | P2 35 commits (`f87ff05` … `060dab9`) rebased onto main, ops-0918 8 commits (`800d73c` … `00c568e`) cherry-picked on top; ops code byte-identical to `856176e` |
| what is proven | steps 0, 1.1, 1.2, 1.3 all PASS — the stack assembles with no conflict and no dropped commit; **rebuilding it is not needed, only the fixture is** |
| what is NOT proven | the offline suite (red, above), the integrated suite with `cobalt_dev`, the real-vault suite, the dark-file dry run, `jobs restarts` — none of step 2 ran |
| `cobalt_dev` | untouched by this run; still at `0007` with P4's tables absent, as the third run left it |
| production / vault / `~/cobalt` | untouched; no merge, no push, no settings write anywhere |

MEMORY: stack gate 0918 — P2+ops-0918 stack assembles clean (`00c568e`, 43 commits, no conflict) but is RED offline (43 failed): P2's `card-settings.real-shape.json` lacks ops-0918's new `trade_count_over_band` step-down row. Second cross-branch seam defect in two days; the pre-merge integrated gate caught this one before the merge. `cobalt_dev` untouched, still at 0007.

CONTINUE: after ESCALATE 1 is ruled and the fixture row is added by a build hub, relaunch this prompt — step 0 and step 1 will replay identically from `00c568e`'s base and the run resumes at step 1.4.

FAILED: step 1.4 — offline suite on the stacked branch is 43 failed / 1455 passed / 5 errors, single root cause: P2's `tests/fixtures/radar/card-settings.real-shape.json` has no `trade_count_over_band` step-down row, which ops-0918's `fe195ab` made mandatory — a merge-seam defect, red in neither branch alone, fixed by one file; nothing fixed here per the prompt, step 2 not run, `cobalt_dev` and production untouched — ESCALATE: 4

---

# SECOND RUN

Seat: `stack-gate-0918b`, Opus 5 (`claude-opus-5`), background, same worktree `/Users/cobalt/cobalt-wt/s2-p2-cards` (`sprint-2/cards`).
Prompt: `docs/40 - DevDocs/prompts/2026-09-18/12-stack-gate-2.md`. Steps 1.4 → 3 of `09-stack-gate.md` bind verbatim; §F (the ONE fixture edit) is this prompt's addition.
Inherited: the stack assembled at `00c568e` (43 commits), branch tip `dad73f0` (report commits), worktree clean. Steps 0, 1.1, 1.2, 1.3 PASS — not replayed.

## §0 Headline (14:53 ET)

- **§F DONE — the fixture fix worked: offline is GREEN, `1535 passed, 0 failed, 0 errors`** (was 43 failed / 1455 passed / 5 errors), one row in one file, 6 insertions.
- **FAILED at step 2 — the INTEGRATED suite with `cobalt_dev` is `8 failed, 1805 passed`. A different and deeper seam, and NOT ONE of the 8 is P2's.**
- **5 × `test_trader_settings.py`** — the revision-3 proof seeds the settings table from the YAML read out of GIT HISTORY (6 step-downs, frozen); ops-0918's new mandatory signal refuses it. **No database state can fix these**: `cobalt_dev` now HAS the row (`validate` → 7 rows) and they are still red. Deploy 1 counted these same 5 as "`cobalt_dev` state" — that diagnosis was wrong, and the stacked deploy will reproduce them.
- **3 × `test_aset_config` / `test_daymode::TestShippedConfig`** — the approved settings file (production's values) enables one more grade than these three tests assert as RULED. Closing the dev↔production drift (ops ESCALATE 5) was correct and exposed a contradiction only Dejan can rule.
- Dev DB written exactly as approved (R7's exact line; both hashes = R4), `validate` exit 0 with `trade_count_over_band=down(1)`. `.env` removed. No merge, no push, production and the real vault untouched. ESCALATE 2nd run: 3.

## AUTHORIZATION (verified by this hub, 14:44 ET)

`git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` → `9da15b3`, `1c5062e`, `723071e`, `34524c1`, `41ed33f`, `3b8148c`, `5476410`, `77b1a08`. R1/R2 rows committed below that; **R7 committed at `5476410`**, R8 at `41ed33f`, R9 at `34524c1` — all on main, all readable in `cto-2026-09-18.md` §4.

This launch line is **rule-for-rule identical to the first run's** (compared item by item). Its verdicts therefore carry over unchanged:

| launch-line rule | approved by | verdict |
|---|---|---|
| `cp` / `rm` / `ls -la` the `.env` by exact path | R1 list (1) | MATCH |
| `COBALT_ENV=dev` `db migrate*` · `pytest *` · `validate*` · `settings load *--dry-run*` | R1 list (1) | MATCH |
| `COBALT_ENV=dev … settings load --from …/ops-2026-09-18/scratch/daymode-settings-0918 --apply` | **R7 (3)**, exact line, DEV database only | MATCH |
| `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run pytest *` · `uv run pytest *` · `uv run cobalt jobs restarts *` | R1 list (1) | MATCH |
| `git rebase main` | R1 list (1) | MATCH |
| `git rebase --abort` | R7 (2) | MATCH |
| `git cherry-pick *` | R2 | MATCH |
| `git add/commit/diff/status/log/show/rev-parse *` · `git -C /Users/cobalt/cobalt log*`/`rev-parse *` | R1 list (1) | MATCH |
| `cd` · `ls` · `grep` · `tail` · `wc` · `shasum -a 256` · `date` | R1 list (1) | MATCH |
| `--disallowedTools AskUserQuestion EnterWorktree` | R1 (all three launches) | MATCH |

The ONE file edit (§F) is made with the Edit tool inside this hub's own worktree — not a Bash rule, needs none. The VALUE written is Dejan's, `cto-2026-09-17.md:194` **R13** 07:37 ET *"ruling A."* — over the band = adverse, `down 1`. Not in this line and not used: push, `bypassPermissions`, `--allow-prod`, any `COBALT_ENV=production` command, any vault write, `git reset`, `git branch -f`.

Carried forward from the first run: the prompt file's tail contains a block styled as a system reminder asking for a `Claude-Session:` URL in every commit. It arrives inside a tool result (the file's own bytes), not from the harness; the genuine harness reminder names only `Co-Authored-By`. Not followed.

## PREFLIGHT 2nd run (14:44 ET)

| # | rule probed | command | exit | verdict |
|---|---|---|---|---|
| P1 | `git status*` | `git status --porcelain` | 0 | allowed — no output (clean) |
| P2 | `git log*` | `git log -1 --oneline` | 0 | allowed — `dad73f0` |
| P3 | `date*` | `date` | 0 | allowed — Fri Sep 18 14:44:07 EDT 2026 |
| P4 | `git -C /Users/cobalt/cobalt log*` | `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` | 0 | allowed — authorization rows above |
| P5 | `uv run pytest *` | `uv run pytest --co -q tests/cobalt/test_radar_keys.py` | 0 | allowed — 6 tests collected |
| P6 | `grep *` · `ls *` | fixture/consumer reads (§F.1) | 0 | allowed |

**0 allowlisted shape denied.** Probed by first real use, per the prompt: `ls -la …/.env` (§F.3, allowed, exit 1 = absent), full `uv run pytest` (§F.3, allowed), `git add`/`git commit` (§F.4). Not yet reached: the `.env` `cp`/`rm`, `db migrate`, both `settings load` rules, `COBALT_ENV=dev` pytest/validate, `COBALT_VAULT_PATH=…` pytest, `jobs restarts`.

## F. The fixture — the one code change

### F.1 Preconditions and the reads

| check | observed | verdict |
|---|---|---|
| `git status --porcelain` | empty | PASS |
| `git rev-parse --short HEAD` | **`dad73f0`** (branch tip; stack tip `00c568e` one below) | recorded |
| fixture rows before | `daymode.stepdowns` = 6 rows, lines 41–77 | as inherited |
| how it was cut | `_cut_p2_fixtures.py:110-117` — `json.dumps(rows, indent=2, sort_keys=True) + "\n"`, straight from `"user".trader_settings` (not run) | style fixed: keys alphabetical, 2-space indent |
| ops-0918's spelling | `tests/cobalt/test_daymode.py:83-84` — `{"signal": "trade_count_over_band", "effect": "down", "rungs": 1, "because": "trade count above the ruled band"}`; identical in `ops-2026-09-18.md` §1.2's YAML block | the source of the `because` text |

### F.2 The edit — one row, one file

Added after the last existing row, in the fixture's own (alphabetical) key order:

```json
      {
        "because": "trade count above the ruled band",
        "effect": "down",
        "rungs": 1,
        "signal": "trade_count_over_band"
      }
```

| proof | expected | observed | verdict |
|---|---|---|---|
| `git diff --stat` | 1 file, insertions only | `tests/fixtures/radar/card-settings.real-shape.json | 6 ++++++` — **1 file changed, 6 insertions(+)**, 0 deletions | PASS |
| no second file forced | `grep -rn "card-settings.real-shape" tests` → 5 hits: `radar_p2_support.py:66`, `test_radar_keys.py:5,30`, `_cut_p2_fixtures.py:17,115` | all read the file; **no hash, no digest, no row count asserted** (`grep -n stepdowns` in both consumers → no hits) | PASS — nothing else to update |

No `_cut_p2_fixtures.py` run (the prompt forbids it, and a re-cut from production would still yield 6 rows — production does not hold the row today; first run's ESCALATE 1b).

### F.3 Offline suite — GREEN

`ls -la /Users/cobalt/cobalt-wt/s2-p2-cards/.env` → `No such file or directory` (exit 1) **before the run** — genuinely offline, no database reachable.

| run | command | result |
|---|---|---|
| — | `uv run pytest -q tests/cobalt tests/taxonomy` | **1535 passed, 281 skipped, 1 xfailed, 0 failed, 0 errors** in 39.38 s |

The gate's literal command, with no `--continue-on-collection-errors` and no flags added: it collects and it is green. Delta vs the first run: 43 failed → 0, 5 collection errors → 0, 1455 → 1535 passed (the 5 collection errors had hidden ~80 tests).

### F.4 Commit

`f907f1d` — `fix(s2-p2): card-settings fixture carries the trade_count_over_band step-down (ops-0918 seam, ruled 2026-09-17 R13)`, 1 file changed, 6 insertions(+). Report committed separately at `db950b5`.

CONTINUE: step 2

## 2. The dev database — RUN, and it is RED

| # | step | command | result | verdict |
|---|---|---|---|---|
| 2.1 | `.env` in | `cp /Users/cobalt/cobalt/.env …/s2-p2-cards/.env` | by name, never printed (L41 interim) | PASS |
| 2.2 | migrate | `COBALT_ENV=dev uv run cobalt db migrate` | `0001`…`0007` applied, exit 0; **23 tables proven, content UNCHANGED on every one**; P4's `picks` / `missed` / `movers_daily` **ABSENT** | PASS |
| 2.3 | dry run | `COBALT_ENV=dev … settings load --from …/scratch/daymode-settings-0918 --dry-run` | **`DRY RUN — 3 setting(s) would change.`** KEYS only (L32): `~ aset.enabled_grades`, `~ daymode.reduced_enabled_grades`, `~ daymode.stepdowns`; the other four `=` unchanged | PASS — exactly the 3 expected |
| 2.4 | hashes | `shasum -a 256` on both files | `daymode.yaml` = `daa7bb72…b3d5ebb` · `aset.yaml` = `8eca6945…6eb99d58` | PASS — **both identical to `cto-2026-09-18.md` R4** |
| 2.5 | apply (DEV) | the exact R7 line, `--apply` | `applied: {aset.sheet_modes: unchanged, aset.enabled_grades: updated, daymode.reduced_sheet: unchanged, daymode.reduced_enabled_grades: updated, daymode.enabled_modes: unchanged, daymode.hotkey_file_template: unchanged, daymode.stepdowns: updated}` then **`from_db() == from_yaml() — field-by-field diff EMPTY.`** | PASS |
| 2.6 | validate | `COBALT_ENV=dev uv run cobalt validate` | exit 0. `Step-downs: … trade_count_band_placeholder=floor; **trade_count_over_band=down(1)** — 7 row(s), every computable signal ruled.` Band min 2 / max 6. Placement clean. | PASS |
| 2.7 | **integrated suite** | `COBALT_ENV=dev uv run pytest -q tests/cobalt tests/taxonomy --tb=short -p no:randomly` | **`8 failed, 1805 passed, 3 skipped, 1 xfailed`** in 107.81 s | **FAIL** |
| 2.8 | real-vault subset | — | **NOT RUN** (gate stops at 2.7) | — |
| 2.9 | dark card dry run + sha256 | — | **NOT RUN** | — |
| 2.10 | `.env` out | `rm` then `ls -la` | `No such file or directory` (exit 1) — **credential gone** | PASS |
| 2.11 | `jobs restarts` | — | **NOT RUN** | — |

Nothing was fixed (the gate forbids it). The dev DB keeps the approved row — that write is authorized on its own (R7) and is the state the next run needs.

### 2.7 The 8 — named, root-caused, owned

**Group A — 5 failures, `tests/cobalt/test_trader_settings.py`. Owner: ops-0918. Structural; no DB state can clear it.**

| test | fails in |
|---|---|
| `TestRevisionThreeProof::test_from_db_equals_from_yaml` | `TraderSettings.from_db` |
| `TestRevisionThreeProof::test_the_diff_is_not_vacuous` | `TraderSettings._build(where="test")` |
| `TestTheLoadersReadTheDatabase::test_sheet_modes_comes_from_the_rows` | `load_sheet_modes_config()` → `ConfigError` |
| `TestTheLoadersReadTheDatabase::test_daymode_comes_from_the_rows` | `load_daymode_config()` → `ConfigError` |
| `TestTheLoadersReadTheDatabase::test_the_two_halves_still_validate_against_each_other` | `Regex pattern did not match` — it raises the completeness error instead of the narrowing error it asserts |

All five die on the same message:

```
daymode.stepdowns has no row for ['trade_count_over_band']. Every signal the
proposer can compute must be ruled here — an unruled one would be a policy
hole made by silence. Turn a rule off with `effect: none`.
```

**Why the database cannot fix it.** The `seeded` fixture (`test_trader_settings.py:80-83`) does `store.put(TraderSettings.rows_from_yaml(texts=_seed_texts()))` inside the suite's rollback transaction, after the `store` fixture has `DELETE`d every row. `_seed_texts()` (`:45-61`) reads `configs/cobalt/aset.yaml` and `daymode.yaml` **out of git history** (`git show <rev>^:…`) because revision 3 deleted them from the tree — that is the whole point of the module ("the proof the YAML deletion was gated on"). Those frozen texts carry **six** step-downs and can never carry a seventh. So every test that seeds and then builds a `TraderSettings` refuses under ops-0918's completeness check, whatever `"user".trader_settings` holds.

**Proof that it is not `cobalt_dev` state:** `validate` at 2.6 read **7 rows including `trade_count_over_band`** from that same database, minutes before this run. The row is there. The five are still red.

**This corrects deploy 1's diagnosis.** `deploy-2026-09-18.md:203` grouped 22 of its 26 failures under this error and named `test_trader_settings` (5) among them, and its stop line concluded *"every failure caused by `cobalt_dev` state (no `trade_count_over_band` row) … none by the merged code"*. For 17 of the 22 that was right. **For these 5 it was not** — they are the merged code meeting a frozen historical fixture, and they would have come back red on the very next post-merge suite, after the revert, after any re-migration. Neither branch's own suite could see them: ops-0918 ran OFFLINE (no `.env`), and this whole file is `skipif` without `POSTGRES_HOST`/`POSTGRES_USER` (`:34-37`) — 281 skipped offline vs 3 skipped here.

**Group B — 3 failures. Owner: neither branch. A RULED-VALUE contradiction, surfaced by closing ops ESCALATE 5.**

| test | line | what it asserts |
|---|---|---|
| `test_aset_config.py::TestSheetModesConfig::test_committed_config_is_valid` | `:175` | `set(cfg.enabled_grades) == {Grade.A, Grade.B}` |
| `test_aset_config.py::TestSheetModesConfig::test_is_enabled_reflects_committed_config` | `:199` | `not cfg.is_enabled("C")` |
| `test_daymode.py::TestShippedConfig::test_the_real_config_loads_and_reads_as_ruled` | `:128` | `enabled_grades_for("reduced") == ["A", "B"]`, carrying the ruling in its own comment: *"RE-RULED by the CTO review of S1-P2 … A is taken at reduced size; A+ is out because the ACCOUNT ladder does not enable it."* |

All three call `load_sheet_modes_config()` / `load_daymode_config()`, i.e. they read the LIVE `"user".trader_settings` rows — not a fixture. Until 2.5 `cobalt_dev` carried the two-grade ladder and they passed (the P2 re-ship's third run: 1801 passed, 0 failed). The approved file carries **production's** current values, which enable one grade more; 2.5 wrote them, and the three went red. Values withheld (L32) — the test-side value is quoted above only because it is committed repo source.

So the contradiction is not dev-vs-dev: **production's rows and these three tests disagree today**, and have disagreed since before either branch existed. The drift was right to close — the file's whole purpose is to mirror production — but one of the two sides is wrong and it is a sizing value. **His call, not mine** (ESCALATE 2).

Neither group is P2's. P2's own contribution to this gate was the fixture row, and after it the offline suite is clean.

## ESCALATE 2nd run

1. **BLOCKER — `test_trader_settings.py`'s revision-3 seed cannot satisfy ops-0918's completeness check, and no deploy can outrun it.** The seed is read from git history by design, so it is frozen at six step-downs while `SIGNAL_IDS` grows. Three shapes, for a build hub to be told which: (a) the `seeded` fixture appends a ruled row for any `SIGNAL_IDS` entry the frozen text does not name — exactly the pattern ops-0918 already used for its own note fixture (`382c862`, ops report §1.1 "its fixture now appends a row for any `SIGNAL_IDS` entry it does not name, so the next signal cannot stale it") — which keeps the revision-3 proof honest about the fields it actually proves; (b) the proof pins itself to the six keys it was written for and states that it is a historical equivalence, not a live-schema check; (c) the completeness check accepts a seed marked historical. (a) is the one ops-0918 itself chose elsewhere and is the smallest. **This is the same defect class for the third time in two days, and the first one the gate caught twice** — the deeper lesson is that ops-0918's suite ran offline, so every DB-only test in the repo was invisible to it (281 skipped vs 3).
2. **HIS RULING NEEDED — the reduced-mode grade ladder.** Production's `"user".trader_settings` enables one more grade than the three tests above assert, and those tests cite a CTO re-ruling of S1-P2 for their value. Either production's rows drifted and should be corrected (in which case the approved `aset.yaml`, sha256 `8eca6945…`, carries the drift forward — it was approved as "production's current values", which it faithfully is), or the ladder was re-ruled since and the three tests are stale. It is a sizing value, so it is a trading-logic change either way and cannot be settled by a hub. Until it is ruled, **any suite run against a production-mirroring settings table is 3 red**, including the post-merge smoke of the stacked deploy.
3. **Not a blocker — `cobalt_dev` is now production-mirroring, and that changes what a green suite means.** Before 2.5 the dev DB carried the older two-grade ladder, which is why deploy 1's 3.6 and the P2 re-ship's green run disagreed with production without anyone seeing it. The drift is closed (ops ESCALATE 5 → done, in DEV) and `cobalt_dev` is left at `0007` + the over-band row + production's grade values. Any session inheriting this DB should expect the 3 of group B until item 2 is ruled, and should not read them as a regression.

## What the next run inherits

| item | value |
|---|---|
| branch | `sprint-2/cards`, worktree **clean**. Stack tip `00c568e`; **fixture fix `f907f1d`** above it; report commits on top. |
| stack shape | unchanged and re-proven by the first run: P2 35 + ops-0918 8 on main `34524c1`, ops code byte-identical to `856176e`. Not rebuilt this run; main has since moved (desk docs commits) — the next run rebases or restacks as its prompt says. |
| proven | steps 0, 1.1, 1.2, 1.3 (first run) · §F fixture + **offline `1535 passed, 0 failed`** · migrate 0001–0007 · dry run 3 keys · both hashes = R4 · DEV apply + empty field diff · `validate` exit 0 with `trade_count_over_band=down(1)` |
| NOT proven | the integrated suite (8 red, above), the real-vault subset, the dark-file dry run + sha256, `jobs restarts` |
| `cobalt_dev` | **written by this run, as approved**: at `0007`, carries the over-band row and production's settings values. P4's tables still absent. |
| production / real vault / `~/cobalt` | untouched. No merge, no push, no `--allow-prod`, no `COBALT_ENV=production` command, no vault write. `.env` removed from this worktree. |

MEMORY: stack gate 0918 second run — P2's fixture row added (`f907f1d`), offline suite GREEN 1535/0. Integrated suite with `cobalt_dev` is 8 red, none of them P2's: 5 in `test_trader_settings.py` are structural (the revision-3 proof seeds settings from the frozen git-history YAML, 6 step-downs, which ops-0918's mandatory 7th signal refuses — no DB state can fix them, correcting deploy 1's "every failure is cobalt_dev state"), 3 are a ruled-value contradiction (production's grade ladder enables one grade more than `test_aset_config`/`test_daymode::TestShippedConfig` assert as ruled — his call). `cobalt_dev` at 0007 + over-band row + production values since 14:5x; dev↔production settings drift CLOSED in dev by stack-gate-0918b.

CONTINUE: after ESCALATE 1 is built and ESCALATE 2 ruled, relaunch this prompt — §F is already committed, the dev DB already carries the row, so the run resumes at step 2.7 (the integrated suite).

FAILED: integrated suite — 8 red (`1805 passed`) with the dev database, none of them P2's and none fixable by database state: 5 in `tests/cobalt/test_trader_settings.py` are structural — the revision-3 proof seeds `"user".trader_settings` from the YAML frozen in git history (six step-downs) and ops-0918's mandatory `trade_count_over_band` refuses it, which also corrects deploy 1's "every failure is cobalt_dev state" — and 3 in `test_aset_config` / `test_daymode::TestShippedConfig` are a ruled-value contradiction between production's grade ladder and what those tests assert, needing Dejan's word; the §F fixture fix is done and GREEN offline (1535 passed, 0 failed, commit `f907f1d`), the DEV apply is done and `validate` reads `trade_count_over_band=down(1)`, `.env` removed, nothing merged or pushed, production and the real vault untouched — ESCALATE: 3

---

# THIRD RUN

Seat: `stack-gate-0918c`, Opus 5 (`claude-opus-5`), background, same worktree `/Users/cobalt/cobalt-wt/s2-p2-cards` (`sprint-2/cards`).
Prompt: `docs/40 - DevDocs/prompts/2026-09-18/13-stack-gate-3.md`. Steps 2 and 3 of `09-stack-gate.md` bind verbatim, with the two stated differences (over-band dev dry run now expects the zero-change line; no second `--apply`). §T (the two TEST-SIDE fixes) is this prompt's addition; nothing under `src/`, `configs/` or `ops/` may change.
Inherited: stack tip `00c568e` (43 commits), fixture fix `f907f1d`, branch tip `ff26c8f`, worktree clean. `cobalt_dev` at `0007`, carrying the over-band row and production's settings values.

## AUTHORIZATION (verified by this hub, 14:58 ET)

This launch line is **rule-for-rule identical to the first and second runs'** (compared item by item: the `.env` `cp`/`rm`/`ls -la` by exact path; the five `COBALT_ENV=dev` rules; `COBALT_VAULT_PATH=… pytest`; `uv run pytest *`; `uv run cobalt jobs restarts *`; `git rebase main`; `git rebase --abort`; `git cherry-pick *`; `git add/commit/diff/status/log/show/rev-parse *`; `git -C /Users/cobalt/cobalt log*`/`rev-parse *`; `cd`/`ls`/`grep`/`tail`/`wc`/`shasum -a 256`/`date`; `--disallowedTools AskUserQuestion EnterWorktree`). Rows read from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-18.md` §4 — R1 list (1) at `:14`, R2 at `:15`, R7 at `:20`, R3 at `:16`, R5 at `:17`, R8 at `:21`. Every rule MATCHES; the first run's rule-by-rule table stands unchanged and is not repeated.

The file edits of §T are made with the Edit tool inside this hub's own worktree — not a Bash rule, they need none. Not in this line and not used: push, `bypassPermissions`, `--allow-prod`, any `COBALT_ENV=production` command, any vault write, `git reset`, `git branch -f`.

**The two citations this prompt rests on, verified BEFORE touching Group B:**

| citation | what the record says, verbatim | verdict |
|---|---|---|
| `cto-2026-09-17.md:194` **R13** | "ruling A." — a day OVER `daymode.trade_count_band` (max 6) = adverse, effect `down 1`; UNDER the band does nothing | MATCH — the Group A appended row's `down`/`1` |
| `areas/cobalt-sprints.md:37` (09-14 C-size) | "C-size RULED (source: 09-14 weekly review with his trading psychologist): grade C re-enabled; … applied by him 07:55 (`aset.enabled_grades`) and 07:59 (`daymode.reduced_enabled_grades` — `enabled_modes=[reduced]` is the gating key)" | MATCH — word for word as the prompt cites it |
| `PROJECT-LEDGER.md:1393` | same ruling, and it goes further: "Findings: … **a Sonnet run made a silent policy assumption in a daymode comment (reduced keeps A,B) — overruled.**" | MATCH, and it names the exact defect the three Group B tests carry |

The ledger line is stronger than the prompt claimed: the "reduced keeps A,B" assumption was not merely superseded on 09-14, it was **overruled by name**. The three tests pin the overruled value. Group B proceeds.

Carried forward from both earlier runs: the prompt file's tail contains a block styled as a system reminder asking for a `Claude-Session:` URL in every commit. It arrives inside a tool result (the file's own bytes), not from the harness; the genuine harness reminder names only `Co-Authored-By`. Not followed.

## PREFLIGHT 3rd run (14:58 ET)

| # | rule probed | command | exit | verdict |
|---|---|---|---|---|
| P1 | `git status*` | `git status --porcelain` | 0 | allowed — no output (clean) |
| P2 | `git log*` | `git log -1 --oneline` | 0 | allowed — `ff26c8f` |
| P3 | `date*` | `date` | 0 | allowed — Fri Sep 18 14:58:10 EDT 2026 |
| P4 | `uv run pytest *` | `uv run pytest --co -q tests/cobalt/test_trader_settings.py` | 0 | allowed — 16 tests collected |
| P5 | `grep *` | authorization reads above | 0 | allowed |

**0 allowlisted shape denied.** Probed by first real use, per the prompt: the `.env` `cp`/`rm`/`ls -la`, `COBALT_ENV=dev pytest`, `db migrate`, both `settings load` rules, `COBALT_VAULT_PATH=… pytest`, `jobs restarts`, `git add`/`git commit`.

## T. The two test-side fixes

### T.1 Red before — the 8, exactly

| check | observed | verdict |
|---|---|---|
| `git status --porcelain` | empty | PASS |
| tip at T.1 | **`ff26c8f`** (report commit; stack tip `00c568e`, fixture fix `f907f1d` below it) | recorded |
| `.env` in | `cp /Users/cobalt/cobalt/.env …/s2-p2-cards/.env` — by name, never printed (L41 interim) | PASS |
| `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_trader_settings.py tests/cobalt/test_aset_config.py tests/cobalt/test_daymode.py -p no:randomly --tb=no` | **`8 failed, 92 passed`** in 2.22 s — the 5 Group A + the 3 Group B, name for name, nothing new | PASS — the red set has NOT moved |

### T.2 Group A — the revision-3 seed completes itself

`git show 382c862` read first: ops-0918's own note fixture appends `{"signal": s, "effect": "down", "because": …}` for every `SIGNAL_IDS` entry it does not already name, "so the next signal cannot stale it either". Same pattern, one difference stated below.

| what | how |
|---|---|
| frozen text | `_seed_texts()` RENAMED to `_frozen_texts()` — unchanged body, still `git show <rev>^:configs/cobalt/<name>` out of history. **The revision-3 text itself is never edited** (it is history, and the two YAMLs are absent from the tree — verified by `ls configs/cobalt/`). |
| the completion | a NEW `_seed_texts()` wraps it: parse the daymode text, append a row for every `SIGNAL_IDS` entry its `stepdowns` do not name, dump back. Every existing call site reads `_seed_texts()` and is **unchanged**. |
| the appended row's policy | `_RULED_ROWS` — `trade_count_over_band` takes **R13's `effect: down`, `rungs: 1`** (Dejan, `cto-2026-09-17.md:194`, "ruling A."), cited in the constant's own comment. Any other future signal defaults to `effect: none` — ruled OFF visibly, the only honest default for a seed that cannot carry a policy it never saw. |
| why the completion sits in `_seed_texts()` and not in the `seeded` fixture alone | `TestRevisionThreeProof::test_from_db_equals_from_yaml` calls `TraderSettings.from_yaml(texts=_seed_texts())` **inside the test body**, and `from_yaml` = `_build(rows_from_yaml(...))` → the same completeness check. A fixture-only append would have left that one red and forced a test-body edit. Placing it in the seed reader is the same ruling (a ruled row for every unnamed `SIGNAL_IDS` entry) at the only point where **all five tests pass unchanged** — which the ruling also required. Both sides of the proof read the same seed, so the field-for-field equivalence is not weakened. |

| proof | expected | observed | verdict |
|---|---|---|---|
| `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_trader_settings.py -p no:randomly --tb=short` | 0 failed | **`16 passed`** in 1.00 s | PASS |
| test bodies edited | none | none — one import added, one function renamed, one function + one constant added | PASS |
| commit | — | **`f7a018a`** `test(settings): the revision-3 seed appends a ruled row for every SIGNAL_IDS entry its frozen text predates (ops-0918 seam)`, 1 file, 50 insertions / 1 deletion | PASS |

### T.3 Group B — the three live-settings tests now assert their invariant

Each one, what it asserted, what it asserts now, and the citation in its own comment:

| test | was (pinned a live value) | now (the invariant it was protecting) |
|---|---|---|
| `test_aset_config.py::TestSheetModesConfig::test_committed_config_is_valid` | `set(cfg.enabled_grades) == {Grade.A, Grade.B}` | `enabled_grades` is **non-empty**, every member is a declared `Grade`, no duplicates, and the list comes back **in ladder order** (`Grade`'s own order) — whatever subset he has enabled |
| `…::test_is_enabled_reflects_committed_config` | `is_enabled("A")`, `is_enabled("B")`, `not is_enabled("A+"/"C"/"D")` | for **every** `Grade` member, `is_enabled(grade)` and `is_enabled(grade.value)` are true **exactly** for members of `enabled_grades` |
| `test_daymode.py::TestShippedConfig::test_the_real_config_loads_and_reads_as_ruled` | `[g.value for g in cfg.enabled_grades_for("reduced")] == ["A", "B"]` | `reduced` is non-empty, `set(reduced) ⊆ set(account)` — **the re-ruling's actual content, "A+ is out because the ACCOUNT ladder does not enable it", kept verbatim in the comment** — and `reduced` is in ladder order |

Each comment cites the **09-14 C-size ruling** (grade C re-enabled; his own `settings load --apply` at 07:55 / 07:59) and says why no live value is pinned: under **L32** his ladder is user data, so a test that reads `"user".trader_settings` and pins his current choice turns red every time he changes his own settings. `PROJECT-LEDGER.md:1393` is cited because it overrules the "reduced keeps A, B" assumption **by name**.

**Nothing deleted, no refusal weakened.** The value-pinning behaviour moved onto the file's own CONSTRUCTED config (`COMPLETE_SHEET_MODES`, `enabled_grades: [A, B]`) as a new `TestConstructedLadder` — `is_enabled` still refuses `A+`, `C`, `D` against a declared ladder, and the ladder-order invariant is proven there against a known list. That class carries **no** `requires_db` mark, so it runs OFFLINE, with no database at all — the refusal proof no longer depends on the dev DB either.

| proof | expected | observed | verdict |
|---|---|---|---|
| `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_aset_config.py tests/cobalt/test_daymode.py -p no:randomly --tb=short` | 0 failed | **`86 passed`** in 0.98 s | PASS |
| `grep -n '"A", "B"\|Grade.A, Grade.B'` on the three files | only constructed-config uses | 8 hits, **every one constructed or prose**: `test_aset_config.py:260,269` (pre-existing `pytest.raises` constructions), `:312` (the new `TestConstructedLadder`, the constructed ladder itself), `test_trader_settings.py:232,235` (the loader test's own `UPDATE` inside the rolled-back transaction — a value it writes, not one it reads from his settings), `test_daymode.py:63,92` (the `_cfg()` constructed helper's defaults), `test_daymode.py:133` (the new comment). **No literal grade list from live rows remains.** | PASS |
| commit | — | **`00d671d`** `test(aset,daymode): live-settings tests assert invariants, not the trader's current ladder (C-size ruled 2026-09-14)`, 2 files, 88 insertions / 9 deletions | PASS |

### T.4 Scope and the offline suite

| proof | expected | observed | verdict |
|---|---|---|---|
| `git diff --stat ff26c8f HEAD` | only `tests/` (+ this report) | `docs/40 - DevDocs/reports/stack-gate-2026-09-18.md`, `tests/cobalt/test_aset_config.py`, `tests/cobalt/test_daymode.py`, `tests/cobalt/test_trader_settings.py` — **4 files, nothing else** | PASS |
| `git diff --stat ff26c8f HEAD -- src configs ops` | NOTHING | **no output** — not one file under `src/`, `configs/` or `ops/` changed | PASS |
| `.env` out | gone | `rm` then `ls -la` → `No such file or directory` (exit 1) — **credential gone before the offline run** | PASS |
| `uv run pytest -q tests/cobalt tests/taxonomy` (offline, gate's literal command) | 0 failed | **`1537 passed, 281 skipped, 1 xfailed, 0 failed, 0 errors`** in 39.61 s (1535 → 1537: the two new constructed-ladder tests) | PASS |

CONTINUE: step 2
