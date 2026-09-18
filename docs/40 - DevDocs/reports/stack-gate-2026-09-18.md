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

## §0 Headline (14:5x ET)

- **§F DONE — the seam is closed by one row in one file and the offline suite is GREEN: `1535 passed, 0 failed, 0 errors`** (was 43 failed / 1455 passed / 5 errors).
- The row is Dejan's R13 of 09-17 (`down 1`), spelled byte-for-byte as ops-0918 ships it (`test_daymode.py:83`, ops report §1.2): `because: "trade count above the ruled band"`.
- `git diff --stat` = 1 file, **6 insertions, 0 deletions**. No second file involved: no hash/digest and no row count is asserted against this fixture anywhere.
- Step 2 (dev DB) next; `cobalt_dev` still untouched by this run at this point.
- ESCALATE 2nd run: see below.

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

CONTINUE: step 2
