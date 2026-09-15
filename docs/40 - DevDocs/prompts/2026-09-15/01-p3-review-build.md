MODEL: Sonnet 5 (`claude-sonnet-5`) · SEAT: hub, a fresh Claude Code pane in herdr (not Claude1), started with ONE line, nothing pasted: `cd ~/cobalt && claude --model claude-sonnet-5 --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt "Read 'docs/40 - DevDocs/prompts/2026-09-15/01-p3-review-build.md' and follow it exactly."` · SESSION: fresh · auto mode on · METER: Anthropic small (hub only); Codex = probed in STEP 1, never asked of Dejan

# S2-P3 radar panel — Astra review, Sol build, one commit, READY FOR MERGE; deploy in the 20:05 pause

You are the HUB (L36: the only spawner; L35: you trust artifacts, never reports; L34: every spawn is a job row — `cobalt jobs run` where a command is a registered job, otherwise record the spawn in your report table). You never write source code yourself. You launch, verify, cut fixtures from production reads, commit, and report.

## 0. Wake-up and preconditions (read-only)

1. Read `/Users/cobalt/Vault/Think/6 - Permanent/Memory/INDEX.md`, then the `## NOW` section at the top of `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md`, then `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` in full.
2. Read the plan: `/Users/cobalt/cobalt-wt/s2-p3-radar-panel/docs/40 - DevDocs/plans/plan-s2-p3-2026-09-14.md` (commit adc4ec1 on `sprint-2/radar-panel`). Rulings R1–R4 in it are Dejan's; they are not reopened by anyone today.
3. Verify: `git -C /Users/cobalt/cobalt-wt/s2-p3-radar-panel status --porcelain` is empty; `git -C /Users/cobalt/cobalt-wt/s2-p3-radar-panel log --oneline -1` = adc4ec1; `git -C ~/cobalt log --oneline -1` = 91bfe91 or later on `main`. Rebase the branch on main now: `git -C /Users/cobalt/cobalt-wt/s2-p3-radar-panel rebase main` (docs-only branch; must be clean — if it is not, stop and report).
4. Your report file, written from the first step and updated every step (L48): `/Users/cobalt/cobalt-wt/s2-p3-radar-panel/docs/40 - DevDocs/reports/s2-p3-2026-09-15.md` — §0 Headline ≤5 lines → tables → ESCALATE.
5. `codex exec --help` once, to confirm the flags below exist under the installed version before any launch (dispatch lesson 09-13).

## 1. Codex meter probe (L47 — precondition, never the router)

```
cd /Users/cobalt/cobalt-wt/s2-p3-radar-panel && wc -l "docs/40 - DevDocs/plans/plan-s2-p3-2026-09-14.md"
cd /Users/cobalt/cobalt-wt/s2-p3-radar-panel && codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Run: wc -l 'docs/40 - DevDocs/plans/plan-s2-p3-2026-09-14.md' -- reply with only the number." < /dev/null
```
Exit 0 and the number matches your own `wc -l` and no usage-limit text = Codex UP. Record the probe verbatim in the report. If Codex is DOWN (limit text, non-zero exit, no answer): the review is recorded as `REVIEW: Astra unavailable — ESCALATE 1`, and the build goes to Opus headless (L50) in STEP 4b. Do not wait for a reset (L47).

## 2. Astra review, ≤3 rounds (L29: architect + Astra; L39: no fourth turn)

Round 1 launch (writer profile, because Astra must produce a file — L44 corollary):
```
cd /Users/cobalt/cobalt-wt/s2-p3-radar-panel && codex exec --skip-git-repo-check -m gpt-6-astra -s workspace-write "You are GPT-6 Astra, the cross-house reviewer (LAWS L29). Working directory = the git worktree of branch sprint-2/radar-panel. Read, in this order: /Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md in full; 'docs/40 - DevDocs/plans/plan-s2-p3-2026-09-14.md'; every file and line the plan cites (src/cobalt/aset/web.py, src/cobalt/radar/store.py, tests/cobalt/test_aset_web.py, tests/cobalt/test_radar_notes.py, docs/30 - Design/TRADE-RADAR-CARD-MOCK-v0_1/card-spec.md). Rulings R1-R4 in the plan are Dejan's and are not under review. Review the plan for: (1) factual errors against the code (name every file:line); (2) steps that would violate a law (cite L-number and the sentence); (3) missing tests for a stated behaviour; (4) anything that would make the build fail on first run. Write ONE file: 'docs/40 - DevDocs/reports/p3-review-astra-r1-2026-09-15.md' with a numbered findings table: id | severity BLOCKER/AMEND/NOTE | plan section | finding | evidence file:line | proposed wording. No rewrite of the plan, no design alternatives that contradict R1-R4, no prose outside the table except a 3-line summary at the top. Reply in chat with only the path you wrote." < /dev/null
```
Disposition by the hub (you are the clerk, not the architect): for each finding — (a) factual correction of a name, path, column or line → amend the plan in place, note `[amended 09-15 per Astra R1-<id>]`; (b) a change that contradicts R1–R4 → NOT applied; record it verbatim under `## Dissent (Astra)` in the plan, the plan stands (L29 round-3 rule); (c) a missing test or a first-run failure → amend the plan's §4/§2 accordingly. Write your dispositions table into the report. Round 2 = the same launch with `r2` in the file name and this sentence prepended: "Round 2. Read your R1 file and the hub's dispositions in 'docs/40 - DevDocs/reports/s2-p3-2026-09-15.md' §Review; only findings you still hold, or new ones caused by the amendments." Round 3 only if R2 still holds a BLOCKER; after round 3 the plan stands and every remaining dissent is recorded verbatim. Commit nothing yet.

## 3. STEP-1 of the plan — the hub cuts the L45 fixtures from PRODUCTION READS (read-only; never from an invented row)

Run from `~/cobalt` (it has the credentials; the worktree never does — L41 interim). Reads only; `--prod` with `--side system` / `--side user`; no `%` in SQL (use `~`).
```
cd ~/cobalt && COBALT_ENV=production uv run cobalt db query --side system --prod --format json "SELECT * FROM radar_pool WHERE pool_key = 'primary'"
cd ~/cobalt && COBALT_ENV=production uv run cobalt db query --side system --prod --format json --limit 1000 "SELECT * FROM radar_membership WHERE trade_date = DATE '2026-09-14' ORDER BY id"
cd ~/cobalt && COBALT_ENV=production uv run cobalt db query --side user --prod --format json "SELECT key, value FROM trader_settings WHERE key = 'radar.pool'"
cd ~/cobalt && COBALT_ENV=production uv run cobalt db query --side user --prod --format json --limit 1 "SELECT * FROM aset_sizings ORDER BY id DESC"
```
Transform exactly as plan §3 says (dates shifted to one fixed synthetic day with intra-day offsets kept; scan ids rebased; the 12-hex source suffix zeroed in every `source`/`sources` value; `note_sha256`/`block_sha256` zeroed; `user_id` → 1; no personal attribution) and write the three files under `/Users/cobalt/cobalt-wt/s2-p3-radar-panel/tests/fixtures/radar/` with the exact names in §3. The transform is a small Python script you keep at `tests/fixtures/radar/_cut_panel_fixtures.py` (deterministic, re-runnable, reads its input from files you save under your scratch directory — the raw prod JSON is never committed). Prove before moving on: `grep -E '[0-9a-f]{12}' tests/fixtures/radar/panel-*.json` returns only zero suffixes, and no `2026-09-1` date string remains.

## 4a. Sol build (Codex UP)

```
cd /Users/cobalt/cobalt-wt/s2-p3-radar-panel && codex exec --skip-git-repo-check -m gpt-5.6-sol -c model_reasoning_effort="high" -s workspace-write "You are GPT-5.6 Sol, the builder. Working directory = git worktree of branch sprint-2/radar-panel (never touch ~/cobalt). Read /Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md in full, then 'docs/40 - DevDocs/plans/plan-s2-p3-2026-09-14.md' (as amended; every ruling R1-R4 binds), then 'docs/40 - DevDocs/PLAN-TEMPLATE.md' and the DevDocs pages for src/cobalt/aset/web.py and src/cobalt/radar/store.py under 'docs/40 - DevDocs/cobalt/'. Build STEP-2 through STEP-6 exactly as written: store read layer, view models + builder in src/cobalt/aset/radar_panel.py, pure render functions, the two GET routes, tests in tests/cobalt/test_radar_panel.py against the fixtures in tests/fixtures/radar/ (already cut, do not edit them), one DevDoc per new .py file plus updates to the two touched pages, BACKLOG.md kanban row. Fail-loud per L1/L9; no write path; no alert(/prompt(/confirm(/.focus(/autofocus/http-equiv refresh; Pydantic for every view model; no new dependency. There is no database here: run 'uv run pytest -q tests/cobalt/test_radar_panel.py tests/cobalt/test_aset_web.py' (offline) and then the full offline suite 'uv run pytest -q' — every test you add must pass; the requires_db test is written but is run by the hub. Do not commit (you cannot). When done, write 'docs/40 - DevDocs/reports/s2-p3-build-sol-2026-09-15.md': files changed, tests added, suite result verbatim, anything you could not do. Reply in chat with only that path." < /dev/null
```
If Sol stops on its meter mid-build: one relaunch with "CONTINUE from your report" prepended (L47 bounded wait-exception); a second stop → STEP 4b with the diff left in place.

## 4b. Opus headless fallback (Codex DOWN, or Sol stopped twice) — L50

```
cd /Users/cobalt/cobalt-wt/s2-p3-radar-panel && claude -p --model claude-opus-5 --permission-mode acceptEdits --add-dir /Users/cobalt/Vault "<the identical build prompt from 4a, with 'You are GPT-5.6 Sol' replaced by 'You are Opus 5, the builder'>"
```
A headless Claude launched by a Claude hub gets no shell (dispatch lesson 09-13): pre-authorise Read/Edit/Write via `--permission-mode acceptEdits` and run the test suite yourself afterwards.

## 5. Hub verification (L35) — in the worktree

1. `cd /Users/cobalt/cobalt-wt/s2-p3-radar-panel && uv run pytest -q` — full offline suite green (the one pre-existing unrelated failure noted in `reports/ops-day-open-2026-09-15.md` may appear identically; name it if it does).
2. L45 leak scan: `uv run pytest -q tests/cobalt/test_radar_notes.py -k leak` green, unmodified.
3. DB test on `cobalt_dev` (L41 interim, credentials copied by name, never printed; with `.env` present the suite's DB-backed tests run instead of skipping — the `dev_env` fixture in tests/conftest.py pins `cobalt_dev` and rolls back): `cp ~/cobalt/.env /Users/cobalt/cobalt-wt/s2-p3-radar-panel/.env && cd /Users/cobalt/cobalt-wt/s2-p3-radar-panel && COBALT_ENV=dev uv run pytest -q tests/cobalt/test_radar_panel.py; rm /Users/cobalt/cobalt-wt/s2-p3-radar-panel/.env` — `.env` is gitignored; confirm it is gone with `ls`.
4. `cd /Users/cobalt/cobalt-wt/s2-p3-radar-panel && uv run cobalt jobs restarts main..HEAD` → the `RESTARTS:` line. Expected `com.cobalt.aset` + `com.cobalt.radar`; any other label or UNCLASSIFIED → ESCALATE, never dropped (L42).
5. Read the diff yourself (`git diff main..HEAD --stat` and the routes/render code): no POST, no new dependency, no config change.

## 6. One commit (L46), READY FOR MERGE

```
cd /Users/cobalt/cobalt-wt/s2-p3-radar-panel && git add -A && git commit -m "feat(radar-panel): S2-P3 pool view + card-ladder shell (plan adc4ec1, Astra-reviewed, Sol build)" 
```
Commit message body: RESTARTS line, tests summary, review rounds, dissent count. The report's last line: `READY FOR MERGE <hash> | RESTARTS: <line> · ESCALATE: <n>`. Then reply to Dejan in ≤10 lines: hash, RESTARTS, ESCALATE count, the report path.

## 7. Deploy — inside the 20:00–21:00 ET market_reset pause ONLY, on Dejan's word

Dejan pastes `GO DEPLOY` into this pane at or after 20:05 ET. Do not schedule your own wake-up unless he ran `/login` in this pane immediately before (a wake-up dies with the login token). Sequence (L54 rebase-then-ff; L43 one deploy per evening = this one window; L51 pre-approvals apply):
1. `git -C ~/cobalt status --porcelain` → only machine-written files (commit them as-is per L51-2) or empty.
2. `ops/day-open` 84912db: `git -C /Users/cobalt/cobalt-wt/ops-day-open rebase main` → `cd ~/cobalt && git merge --ff-only ops/day-open`.
3. `sprint-2/radar-panel`: `git -C /Users/cobalt/cobalt-wt/s2-p3-radar-panel rebase main` → `cd ~/cobalt && git merge --ff-only sprint-2/radar-panel`.
4. If `docs/40 - DevDocs/reports/ops-2026-09-15.md` in `/Users/cobalt/cobalt-wt/ops-2026-09-15` ends with `READY FOR MERGE` (the ops session from `02-ops-2026-09-15.md`): rebase and `--ff-only` merge `ops/2026-09-15` the same way. If not READY, skip it and say so.
5. `cd ~/cobalt && COBALT_ENV=production uv run cobalt validate` → exit 0, and `uv run cobalt jobs register` (day-open adds tunables rows; jobs.yaml unchanged unless the ops branch says otherwise).
6. Restarts, derived: `cd ~/cobalt && uv run cobalt jobs restarts <main-before>..HEAD`; then `launchctl kickstart -k gui/$(id -u)/com.cobalt.aset` and `launchctl kickstart -k gui/$(id -u)/com.cobalt.radar` (radar only inside the pause — it is idle now). Every label the derivation names, nothing it does not.
7. Smoke: `curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:5010/` = 200; `curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:5010/radar` = 200 and the ladder shows its empty state; `COBALT_ENV=production uv run cobalt day-open --json | head -c 400` runs; `COBALT_ENV=production uv run cobalt heartbeat show` has no new RED; after 21:00 the first post-reset radar scan lands (`cobalt db query --side system --prod "SELECT last_scan_at, members FROM radar_pool"`).
8. Tag: `git -C ~/cobalt tag deploy-2026-09-15`. Rollback = `git revert` of the merge range + restart aset at once, radar in the next pause.
9. Append the deploy table to your report, last line `LIVE <hash> · RESTARTS done: <labels> · ESCALATE: <n>`; tell Dejan in ≤10 lines. He pushes.
