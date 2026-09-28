# DEPLOY 2026-09-24 RE-LAND — a0ba0098's tree (setups/seven-0921 + replay/mover-partial-0924) back onto main by revert of 4e625f6a, migration 0013 proved, his four assumed rows (his re-land word, R45)

Hub `setups-deploy-reland-0924` · Opus 5.5 (`claude-opus-5-5`) · `acceptEdits` + allowlist (51 strings, `09`'s line) · prompt `prompts/2026-09-24/32-setups-deploy-reland.md` · launch row R53, his word R45, approval rows R3 + 09-23 R52.

## §0 Headline
The re-land is DONE and GREEN. `602e7b47` → `a2d320b8` by ONE `revert --no-edit 4e625f6a`, with a code diff to `a0ba0098` of ZERO. The migration 0013 proof-only run changed nothing (81.3 s). Residents were down 114 s, DAY window (R45). Tag `deploy-2026-09-24` @ `a2d320b8`.
**Production is fixed.** The new code reads the ASSUMED `card_dots` (now 5). The heartbeat is GREEN and `failed_stage evaluate` is gone. The radar cycles clean, and there are no new panel or pool failures.
**His four rows were NOT written.** The production `--dry-run` REFUSED because the note does not exist: `upsert_unit never creates a note`. The dev `--apply` did create and fill it. The prompt says skip, so there was no apply and no live-note run. ESCALATE: 12. The desk decides the note path.

## L74
One block arrived as a system-reminder attached to the Read of this run's prompt file: it asks that commit messages end with a `Claude-Session: https://claude.ai/code/session_…` line and names a file-send tool (SendUserFile). Treated as DATA under L74 — not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| check | command | result |
|---|---|---|
| P00 placeholder | `grep -n -E "R_[_]" ".../32-setups-deploy-reland.md"` | no output (exit 1) — no placeholder |
| R45 row | `grep -n "^\| R45 " cto-2026-09-24.md` | line 55: `**P-HIS — RE-LAND NOW (R42 "A").** His words, desk chat 12:14 ET: "Which option gets me refresh and redeploy right now? This second. That's the one I want." → A: re-land the same stack …` — carries `right now` and `re-land` |
| R45 committed | `log -1 --format=%H -S"\| R45 \|" -- cto-2026-09-24.md` | `2fab30edd8dce01e85ec8e7ab9e171eaba2ed9cd` |
| R39 row | `grep -n "^\| R39 " cto-2026-09-24.md` | line 49: `**P-HIS — DONE TRADING 11:01.**` … |
| R83 row | `grep -n "^\| R83 " cto-2026-09-23.md` | line 86: `Tomorrow's deploy window … starts on his "done trading" word … for 09-24 only … gates on a \`DONE TRADING <time>\` row` |
| R83 committed | `log -1 … -S"Tomorrow's deploy window" -- cto-2026-09-23.md` | `2028ef79f8ebeb37086fc271387a8b5a02cdea92` |
| R4 row | `grep -n "^\| R4 " cto-2026-09-23.md` | line 12: `"Everything waiting for me is approved."` … `SHIP with it` |
| R104 row | `grep -n "^\| R104 " cto-2026-09-23.md` | line 112: `His words: "Grok yes. B skip the suite"` |
| R104 committed | `log -1 … -S"B skip the suite" -- cto-2026-09-23.md` | `d5b7cf55383ca6eb401dc5d3c68f2e00f28131d5` |
| R113 / R114 | `grep -n "^\| R113 "` / `"^\| R114 "` cto-2026-09-23.md | line 121 (R113, 22:0x ET) / line 122 (R114, `"yes A. Thank you."`) — both printed |
| R7 | `grep -n "^\| R7 " cto-2026-09-24.md` | line 17: `"Qwen is done you can go read the report. I approve A"` |
| R119 | `grep -n "^\| R119 " cto-2026-09-22.md` | line 46: `… his words: "A" → the three word-only values enter his \`1 - Trading/Assumed Defaults.md\` …` |
| R119 committed | `log -1 … -S"\| R119 \|" -- cto-2026-09-22.md` | `b33b56349102f455273f2c2578fcacd2486a6e9c` |
| R82 | `grep -n "^\| R82 " cto-2026-09-23.md` | line 85: `A-19 \`range_break.failed_trap_bars\` = 1 bar … A-20 \`range_break.retest_tolerance_atr\` = 0.10 × \`atr_working\`` |
| R82 committed | `log -1 … -S"\| R82 \|" -- cto-2026-09-23.md` | `81a226bddad0646f0cfba4495fb69bd3b189b175` |
| R118 | `grep -n "^\| R118 " cto-2026-09-23.md` | line 126: `"Let's go with B …"` → `the 09-24 deploy HOLDS \`dist.k.vwap\` (A-16) — STEP-6 writes FOUR rows` |
| R118 committed | `log -1 … -S"\| R118 \|" -- cto-2026-09-23.md` | `54b33bec17c4d64efbbdfc667eae451c676346ee` |
| R3 (launch-line approval) | `grep -n "^\| R3 " cto-2026-09-24.md` | line 13: `His word: "Approved" — … the launch line of \`prompts/2026-09-24/05-setups-deploy.md\` (50 allow strings …), covering the production migration \`0013\` and the STEP-6 vault write …` |
| R3 committed | `log -1 … -S"05-setups-deploy.md" -- cto-2026-09-24.md` | `f173328fb733f5b62247cfaffb2d582f9cf2a42d` |
| 09-23 R52 | `grep -n "^\| R52 " cto-2026-09-23.md` | line 55: `his words 07:0x ET: "Approved all commands you need"` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0923` · `the three \`stacked-0923\` \`merge --no-edit\` + \`merge --abort\`` |
| R52 committed | `log -1 … -S"merge --ff-only deploy/stacked-0923" -- cto-2026-09-23.md` | `d327ff17e6d27f0dc50b957bda6536be604b64e1` |
| R53 (this launch) | `grep -n "^\| R53 " cto-2026-09-24.md` | line 63: `… **LAUNCH \`32-setups-deploy-reland.md\` — \`RE-LAND: a0ba0098 by revert of 4e625f6a\`** …` · folds 1–7 of `33` named · DESK LINE hold written |
| R53 committed | `log -1 … -S"RE-LAND: a0ba0098 by revert of 4e625f6a" -- cto-2026-09-24.md` | `602e7b47546b783297c10d5c4eb3d6a9f46d1294` |

All authorization checks PASS. STEP-6 authorization (R119 / R82 / R118): PASS.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `date` | 0 | `Thu Sep 24 13:18:35 EDT 2026` — 2026-09-24, before 20:20 |
| P1 | `status --short --branch` | 0 | `## main...origin/main [ahead 134]` |
| P1 | `status --porcelain` | 0 | ` M configs/cobalt/rules.yaml` · ` M "docs/40 - DevDocs/reports/seat-usage.md"` · `?? .grok-stdout-2026-09-22.tmp` · `?? day-open-2026-09-24.md` · `?? routing-x5-retro-2026-09-23.md` · `?? voice-v1-check-2026-09-23.md` (all under `docs/40 - DevDocs/reports/`) — KNOWN DIRT only; no staged line; no re-land-added path untracked |
| P1 | `diff configs/cobalt/rules.yaml` | 0 | one line: `-  generated_at: '2026-09-23T19:40:04+00:00'` / `+  generated_at: '2026-09-24T09:15:00+00:00'` — `generated_at` only |
| P1 | `status` (long) | 0 | `On branch main` … `no changes added to commit` — no rebase / revert / unmerged paths |
| P2 | `tag scratch-allow-probe-0924r` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-0924r' (was 602e7b47)` — allowed |
| P3 | `commit --allow-empty -m "scratch: …"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main d6f72e3d] scratch: allowlist probe (reverted next line)` → `602e7b47 docs(desk): 09-24 R53 …` = pre-P3 HEAD — allowed |
| P4 | `rev-parse --short HEAD` | 0 | `602e7b47` = **`<main0>`** |
| P4 | `log --oneline -1 4e625f6a` | 0 | `4e625f6a Revert "Merge branch 'main' into deploy/stacked-0923"` |
| P4 | `merge-base --is-ancestor 4e625f6a HEAD` | 0 | ancestor |
| P4 | `diff --stat 4e625f6a HEAD -- . ':(exclude)docs'` | 0 | nothing printed |
| P4 | `log --oneline 4e625f6a..HEAD` | 0 | 17 docs commits: `602e7b47` R53 · `ae620333` R52 · `4d4e8445` R51 · `dabb9632` DRC v3 · `10c1e64e` · `f9f5cd60` · `1055421c` · `c70b4971` · `8c440c7c` · `93237a25` · `8d931da7` · `2fab30ed` R45 · `9388cadb` · `c14217ba` · `6d28d9e0` · `2d2a8b0e` · `4b0284b7 docs(report): deploy 2026-09-24 stacked setups + mover — FAILED 4.7 (b), rolled back; …` |
| P4 | `rev-parse --short deploy/stacked-0923` | 0 | `a0ba0098` |
| P4 | `rev-parse --verify --quiet refs/tags/deploy-2026-09-24` | 1 | absent → `<tag>` = `deploy-2026-09-24` |
| P4 | `rev-parse --short pre-setups-0924` | 0 | `1118c3d4` (exists, untouched) |
| P4 | `rev-parse --verify --quiet refs/tags/pre-reland-0924` | 1 | absent |
| P9 | `log -1 --format=%H -- …/setups-deploy-reland-review-2026-09-24.md` | 0 | `602e7b47546b783297c10d5c4eb3d6a9f46d1294` |
| P9 | `tail -n 3 …/setups-deploy-reland-review-2026-09-24.md` | 0 | `SETUPS DEPLOY RELAND REVIEW DONE · houses: 2 of 2 · blockers: 0 · folds: 7` |
| P13 | `ls -la /Users/cobalt/cobalt-wt/stacked-0923/.env` | 1 | `No such file or directory` — lock free |
| P14 | `heartbeat show` → `<hb0>` | 0 | `HEARTBEAT RED — 1 probe(s)  (2026-09-24 13:19:00 EDT)` · only RED: `RED  radar                    failed_stage bars: poll failures: 1` (the carried kind) · `OK   com.cobalt.aset              running   loaded, pid 27998` · `OK   com.cobalt.radar             running   running 101 min, heartbeat fresh` · `AMB  com.cobalt.herdr             unmanaged …` (declared interim) · all other lines OK. The incident kind `failed_stage evaluate` is NOT on this read (the radar record shows the bars stage); the incident itself is in the radar.err tail below. No other new RED kind. |
| P14 | `validate` → `<val0>` | 0 | `13 trade_def(s) validated OK from the vault.` · `68 engine tunable(s) loaded` · `literal guard: ACTIVE — 20 vault value(s)` · `Jobs (F17): 16 registered — 6 resident, 10 one-shot. Kill phrase 'COBALT STOP'.` = **`<jobs0>`** · `registry <-> ops/: 16 label(s), exact match.` · `registry <-> plists: schedules and COBALT_ENV agree on every job.` · `Placement (docs/PLACEMENT.md): tree clean.` |
| P14 | `backup status` | 0 | `ssd   local ARMED /Volumes/COBALT-BACKUP/restic` · `newest snapshot: 1.8 h old` (09's 11:31 `f872d756`; no id printed by this command) |
| P14 | `launchctl print …aset` | 0 | `state = running` · `pid = 27998` = **`<aset pid>`** · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P14 | `launchctl print …radar` | 0 | `state = running` · `pid = 28025` = **`<radar pid>`** · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` |
| P14 | `tail -n 8 logs/radar.err` | 0 | `… Input should be 'curve_unset', 'MANUAL', 'input_stale', 'input_unavailable', 'DESK_NA' or 'DEFAULT_UNRULED' [type=literal_error, input_value='ASSUMED', input_type=str]` · `2026-09-24 13:16:45.102 \| ERROR    \| cobalt.radar.runner:cycle:334 - radar S5 evaluate FAILED: ValidationError: 1 validation error for Dot` · `2026-09-24 13:16:45.111 \| INFO     \| cobalt.radar.runner:resident:459 - radar cycle: scanning scan_id=1790270132517` — THE INCIDENT |
| P14 | `grep -c "Started server process" logs/aset.err` | 0 | `33` = **`<a0>`** |
| P14 | `grep -c "Traceback" logs/aset.err` | 0 | `2` = **`<ta0>`** |
| P14 | `grep -c "Traceback" logs/radar.err` | 1 | `0` = **`<tr0>`** |
| P14 | `grep -c "TaxonomyConfigError" logs/radar.err` | 1 | `0` = **`<tc0>`** |
| P14 | `grep -c "radar panel FAILED" logs/aset.err` | 0 | `16` = **`<rp0>`** |
| P14 | `curl … /radar` | 0 | `200` |
| P14 | marker `EVALUATOR_VERSION = "s2p2.2"` | 1 | `0` |
| P14 | marker `unranked_rows` | 0 | `5` |
| P14 | marker `archive_partial_by_side` | 1 | `0` |
| P14 | marker `id: K17` | 0 | `1` = **`<k17_0>`** |
| P14 | marker `Assumed Defaults` in `vault_loader.py` | 1 | `0` = **`<an0>`** |
| P14 | cards read | 0 | `radar.cards_enabled	True` = **`<cards0>`** |
| P14 | slug `attnotnull` (pg_catalog, unscoped) | 0 | `False` — 0013 applied |
| P14 | ASSUMED rows | 0 | `16	377	assumed_formation	ASSUMED` · `32	378	assumed_formation	ASSUMED` · `48	379	assumed_formation	ASSUMED` → **`<n_assumed0>` = 3** |

GATE: proven — commit + tag allowed by the session allowlist

## STEP-R
| step | command | result |
|---|---|---|
| R.1 | `merge-base --is-ancestor a0ba0098 HEAD` | exit 0 |
| R.1 | `diff --stat 4e625f6a a0ba0098 -- . ':(exclude)docs'` | `81 files changed, 20834 insertions(+), 382 deletions(-)` = **`<stack stat>`** (s2.yaml, tunables.yaml, cards/{health,scoring,store}, 0013 pair, db_migrations/__init__, radar/anatomy/*, radar/formation/*, radar/{audit_export,cli,evaluate,evaluate_cli,seam}, replay/{cli,formations,models,movers,runner}, taxonomy/{cli,loader,tunables,vault_loader}, tests + fixtures) |
| R.1 | `diff --stat a0ba0098 1118c3d4 -- . ':(exclude)docs'` | `81 files changed, 382 insertions(+), 20834 deletions(-)` — the same 81 files (what the revert removed) |
| R.1 | `diff --stat 1118c3d4 4e625f6a -- . ':(exclude)docs'` | nothing printed — `4e625f6a`'s code = `1118c3d4`'s |
| R.2 | `backup run` (timeout 600000, foreground) | `backup: cobalt_brain via pg_dump inside cobalt_memory — 1716.1 MB` · `ssd: snapshot d6d3e61d — 4 new / 4 changed, 104.2 MB added, 1 pruned` · `F17: com.cobalt.backup DONE` → snapshot **`d6d3e61d`** (13:20 ET, degraded state incl. the three ASSUMED rows) |
| R.2 | `backup status` | `newest snapshot: 0.0 h old` |
| R.3 | `tag pre-reland-0924 602e7b47` / `rev-parse --short pre-reland-0924` | exit 0 / `602e7b47` = `<main0>` |
| R.4 | — | RESTARTS EXPECTED: `RESTARTS: com.cobalt.aset com.cobalt.radar`, nothing UNCLASSIFIED (`09`'s derivation on this tree); re-derived at 4.5 / 4.7 (f) on `<main0>..<reland>` |

## Deploy table
### STEP-4 — the outage window (calls verbatim)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `Thu Sep 24 13:20:58 EDT 2026` → HARD CLOCK before 19:55 → **`window: DAY (R45)`**, `<revert clock>` = 19:58 · `<t down>` = 13:20:58 |
| 4.1b | `launchctl bootout gui/501/com.cobalt.aset` / `…/com.cobalt.radar` | exit 0 / exit 0, no output |
| 4.1b | `launchctl print gui/501/com.cobalt.aset` / `…/com.cobalt.radar` | exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` / exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.2 | `date` | `Thu Sep 24 13:21:05 EDT 2026` (before 19:58) |
| 4.2 | `rev-parse --short HEAD` / `rev-parse --short deploy/stacked-0923` | `602e7b47` = `<main0>` / `a0ba0098` |
| 4.2 | `git -C /Users/cobalt/cobalt revert --no-edit 4e625f6a` | `[main a2d320b8] Reapply "Merge branch 'main' into deploy/stacked-0923"` · `128 files changed, 24923 insertions(+), 386 deletions(-)` (exactly the inverse of `4e625f6a`) → **`<reland>` = `a2d320b8`**. NOTE: this git names a revert-of-a-revert `Reapply "…"`, not `Revert "Revert "…""` as the prompt expected — same operation; the subject is recorded for RELAUNCH (iii) |
| 4.3 | `rev-parse --short HEAD` / `rev-parse --short HEAD^1` | `a2d320b8` / `602e7b47` = `<main0>` |
| 4.3 | `log --oneline -2` | `a2d320b8 Reapply "Merge branch 'main' into deploy/stacked-0923"` · `602e7b47 docs(desk): 09-24 R53 — …` |
| 4.3 | `diff --stat a0ba0098 HEAD -- . ':(exclude)docs'` | **nothing printed** — the re-landed code is `a0ba0098`'s, byte for byte |
| 4.3 | `diff --stat 4e625f6a HEAD -- . ':(exclude)docs'` | `81 files changed, 20834 insertions(+), 382 deletions(-)` = R.1's `<stack stat>` |
| 4.4 | `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` (timeout 600000, foreground) | exit 0 · `cobalt db migrate — PROOF ONLY on cobalt_brain (READ ONLY, nothing applied)` · 28 tables probed, NO `CHANGED` (e.g. `bars system system 10460354 7189bf2564dc989da5ced9948a14572a 57.80`; `card_dots user user 48 80e318d1a9bfe5a747eff222f039aa03 0.00`; `radar_score system system 734266 … 18.04`) · `28 table(s) probed on cobalt_brain; … Proof cost: total 81.3 s — and a migration pays it TWICE (before and after), inside the outage.` · `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: a2d320b8 (DIRTY: 8 path(s)) · /Users/cobalt/cobalt` |
| 4.4 | read-back `attnotnull` (unscoped pg_catalog) | `attnotnull` / `False` — 0013 applied, nothing pending |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0 · `13 trade_def(s) validated OK from the vault.` · `87 engine tunable(s) loaded` (new code; was 68) · `Jobs (F17): 16 registered — 6 resident, 10 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` · `registry <-> ops/: 16 label(s), exact match.` · `registry <-> plists: schedules and COBALT_ENV agree on every job.` · `literal guard: ACTIVE — 20 vault value(s)` · `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.5 | `COBALT_ENV=production uv run cobalt jobs restarts 602e7b47..a2d320b8` | exit 0 · 128 rows: `configs/cobalt/smoke/s2.yaml M operator command (cobalt smoke); no job reads -` · `configs/cobalt/taxonomy/tunables.yaml M resident reads com.cobalt.aset,com.cobalt.radar` · docs rows `DOCS -` · every `src/cobalt/**.py` row `static import reach` → `com.cobalt.aset,com.cobalt.radar` or `com.cobalt.radar` (`formation/__init__.py` → `-`) · the two `0013` sql files `non-Python src asset -` · every tests row `test/documentation; no resident -` · no `UNCLASSIFIED` · **`RESTARTS: com.cobalt.aset com.cobalt.radar`** |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` / `… /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` | exit 0 / exit 0 — no retry, no kickstart |
| 4.6 | `launchctl print` aset / radar | `state = running` `pid = 53815` (≠ 27998) / `state = running` `pid = 53832` (≠ 28025); paths unchanged |
| 4.6 | `date` | `Thu Sep 24 13:22:52 EDT 2026` → **`<t up>`** |

| field | value |
|---|---|
| `<main0>` → `<reland>` | `602e7b47` → `a2d320b8` (revert of `4e625f6a`) |
| window | `DAY (R45)` |
| `<t down>` / `<t up>` | `13:20:58` / `13:22:52` ET |
| downtime | **114 s** (> 60 s — ESCALATE; the proof-only's own cost 81.3 s) |
| migration proof cost | `Proof cost: total 81.3 s` (once, `--proof-only`) |
| migration 0013 applied | yes (by `09` at 11:32; proved here — read-back `False`) |
| snapshot | restic `d6d3e61d` (ssd), `cobalt_brain` dump 1716.1 MB, 13:20 ET |
| RESTARTS done | `com.cobalt.aset com.cobalt.radar` (L42, from 4.5 and 4.7 (f), both `602e7b47..a2d320b8`) |
| tags | `pre-reland-0924` @ `602e7b47` (`<main0>`) · `pre-setups-0924` @ `1118c3d4` (untouched) · **`deploy-2026-09-24` @ `a2d320b8`** (set 13:28 after the green smoke; `rev-parse --short deploy-2026-09-24` → `a2d320b8`) |
| ROLLBACK SHAPE (L54) | ONE `git -C /Users/cobalt/cobalt revert --no-edit a2d320b8` (proven by `diff --stat 4e625f6a HEAD -- . ':(exclude)docs'` EMPTY; **returns production to the degraded `4e625f6a` state — the ASSUMED rows unreadable again**); 0013 stays; no note was written, so nothing waits on `taxonomy load` |

## Smoke
### STEP-4.7 — on `<reland>` `a2d320b8` (`a0ba0098`'s code)
FIRST CALLS after `<t up>`: `grep -c "radar panel FAILED" logs/aset.err` → `17` = **`<rp_up>`** (P14 `<rp0>` 16; one more panel failure on the OLD code at `13:19:11.828`, before the bootout) · `grep -c "radar pool refresh FAILED" logs/aset.err` → `58` = **`<rpr_up>`**.

| row | `date` | command | result |
|---|---|---|---|
| (a) | `13:22:56` | `launchctl print` aset / radar | `state = running` pid `53815` ≠ `<aset pid>` 27998 / `state = running` pid `53832` ≠ `<radar pid>` 28025 — GREEN |
| (b) | `13:22:59` | `grep -c "Started server process" logs/aset.err` | `34` > `<a0>` 33, ≤ 35 — one clean start |
| (b) | `13:22:59` | `tail -n 30 logs/aset.err` | old-code errors up to `13:19:11.828 … radar panel FAILED …` → `INFO:     Shutting down` → `INFO:     Finished server process [28004]` → `INFO:     Started server process [53821]` → `INFO:     Waiting for application startup.` → `INFO:     Application startup complete.` → `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` — GREEN |
| (b) | `13:22:59` | `grep -c "Traceback"` aset.err / radar.err | `2` = `<ta0>` / `0` = `<tr0>` |
| (b) | `13:22:59` | `grep -c "TaxonomyConfigError" logs/radar.err` | `0` = `<tc0>` |
| (c) | `13:23:04` | curl `/` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` (first attempt each) — GREEN |
| (d) | `13:23:07` | markers | `EVALUATOR_VERSION = "s2p2.2"` `1` (P14 0) · `unranked_rows` `5` · `archive_partial_by_side` `3` (P14 0) · `id: K17` `0` (P14 `<k17_0>` 1) — GREEN |
| (f) | `13:23:12` | `validate` | exit 0 · `Placement (docs/PLACEMENT.md): tree clean.` · `Jobs (F17)` = `<jobs0>` · `87 engine tunable(s) loaded` · registry lines exact — GREEN |
| (f) | `13:23:12` | `jobs restarts 602e7b47..a2d320b8` | exit 0 · `RESTARTS: com.cobalt.aset com.cobalt.radar` = 4.5's line · no `UNCLASSIFIED` — GREEN |
| (g) | `13:23:16` | `attnotnull` read / cards read | `False` / `radar.cards_enabled	True` = `<cards0>` — GREEN |
| (e) read 1 | `13:23:20` | `heartbeat show` | `HEARTBEAT RED — 1 probe(s)  (2026-09-24 13:23:21 EDT)` · only RED: `RED  radar                    failed_stage bars: poll failures: 1; poll CYCU stale since 2026-09-24T17:15:32.517137+00:00` (the carried kind + a `poll <ticker> <reason> since <ts>` finding — allowed) · `OK   com.cobalt.radar             running   running 1 min, heartbeat fresh` · `OK   com.cobalt.aset              running   loaded, pid 53815` — GREEN |
| filler | `13:23:27` | `heartbeat show` (13:23:28) | same finding kinds as read 1 |
| filler | `13:24:00` · `13:24:06` · `13:24:11` · `13:24:17` | `heartbeat show` (13:24:02 / :08 / :14 / :19) | same finding kinds as read 1 each time; radar `running … heartbeat fresh` |
| (b) tail 1 | `13:24:22` (`<t up>` + 90 s) | `tail -n 12 logs/radar.err` | last pre-restart cycle `13:19:37.759`; `13:22:49.432 … F17: com.cobalt.radar RUNNING (timeout 300s, heartbeat every 100s)` + config / vault / finviz-token startup lines to `13:22:49.474`; then **`2026-09-24 13:24:18.124 \| INFO     \| cobalt.radar.runner:resident:459 - radar cycle: scanning scan_id=1790270569533`** — a cycle stamped after `<t up>` (86 s), NO `radar S5 evaluate FAILED`, NO `lifecycle card read failed`, no traceback after `<t up>` → (b) radar-cycle bullet **GREEN**; tails 2 and 3 not needed |
| filler | `13:24:32` · `:39` · `:45` · `:50` · `:56` | `heartbeat show` | same finding kinds |
| (e) read 2 | `13:25:01` (101 s after read 1) | `heartbeat show` | `HEARTBEAT RED — 1 probe(s)  (2026-09-24 13:25:03 EDT)` · only RED: `RED  radar                    failed_stage bars: poll failures: 1; poll CYCU stale since 2026-09-24T17:15:32.517137+00:00` — the SAME finding kind as read 1 · `OK   com.cobalt.radar             running   running 2 min, heartbeat fresh` · `OK   com.cobalt.aset              running   loaded, pid 53815` · no `failed_stage evaluate` on either read — GREEN |
| filler | `13:25:11` … `13:27:47` (every ≈5 s) | `heartbeat show` | same kind to `13:27:04`; from `13:27:10` `HEARTBEAT GREEN — 16 job(s), 12 probe(s), nothing red` · `OK   radar                    scanning (rth), members 50` (the carried bars finding cleared) |
| (h) count | `13:27:52` (`<t up>` + 300 s) | `db query … "SELECT count(*) FROM \"user\".card_dots WHERE na_reason = 'ASSUMED'"` | `5` ≥ `<n_assumed0>` 3 — the three rows are still there; the new radar's cycles wrote 2 more `assumed_formation` dots (recorded, not red) — GREEN |
| (h) heartbeat | `13:27:57` | `heartbeat show` | `HEARTBEAT GREEN — 16 job(s), 12 probe(s), nothing red  (2026-09-24 13:27:59 EDT)` · `OK   radar                    scanning (rth), members 50` · `OK   com.cobalt.radar             running   running 5 min, heartbeat fresh` — **no `failed_stage evaluate`: THE INCIDENT KIND IS GONE** — GREEN |
| (h) panel | `13:28:02` | `grep -c "radar panel FAILED" logs/aset.err` | `17` = `<rp_up>` — no new panel failure since the new code started — GREEN |
| (h) curl | `13:28:04` | `curl … /radar` | `200` — GREEN |
| (h) pool | `13:28:07` | `grep -c "radar pool refresh FAILED" logs/aset.err` | `58` = `<rpr_up>` — GREEN |
| (h) recount | `13:28:09` | `grep -c "Traceback" logs/radar.err` / `grep -c "TaxonomyConfigError" logs/radar.err` | `0` = `<tr0>` / `0` = `<tc0>` — GREEN |

**SMOKE: GREEN** — every row (a)–(h). `cobalt smoke s2` NOT RUN here (by rule; owed after the 21:10 replay).

THE CARD-SURFACE CHAIN (this session reads status codes only): `09`'s L68 gate GREEN on `<stack>` `5e62ea26` (offline 2501/0 · with-DB 2856/0 · live-note 131/0) → `a0ba0098` = `<stack>` + docs (`09` 3.3) → `<reland>` `a2d320b8`'s code = `a0ba0098`'s (4.3, empty diff) → the markers are on production's tree ((d)) → both residents started after the revert and the migration proof ((a), new pids) → the radar cycles with no `S5 evaluate FAILED` ((b) tail 1, 13:24:18) and the heartbeat's `failed_stage evaluate` is gone ((h)) → the sheet logs no new `radar panel FAILED` / `radar pool refresh FAILED` ((h)). The live card in a browser is UNPROVEN until the desk confirms it with him (L70).

## R119
Authorization: R119 / R82 / R118 all present and committed (`## AUTHORIZATION`).

| step | command | result |
|---|---|---|
| 6.1 BEFORE | `ls -la "/Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md"` | exit 1 `No such file or directory` — as expected |
| 6.1 BEFORE parser | `COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt taxonomy tunables --assumed` | `hole     flat_threshold.ema9 … unit=ratio scope=per_indicator(ema9) value=None consumers=['fashionably_late']` · `hole     flat_threshold.vwap … scope=per_indicator(vwap) …` · `hole     range_break.failed_trap_bars … unit=bars scope=global … consumers=['Range Break (primitive)', 'second_chance']` · `hole     range_break.retest_tolerance_atr … unit=atr scope=global …` · `hole     dist.k.vwap … unit=atr scope=per_indicator(vwap) …` · `hole     leg.min_size_atr … unit=atr scope=global …` · `0 assumed row(s), 26 engine hole(s) still null. Writes: none.` — the four keys, `dist.k.vwap` and `leg.min_size_atr` all read `hole` |
| 6.2 | `ls -la /Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml` → absent; Write | written BYTE FOR BYTE as the prompt's block (4 rows; outside every worktree and the vault; never committed) |
| 6.3 DEV PROOF | `COBALT_ENV=dev uv run cobalt taxonomy assumed write --from /Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml --apply` | `[WRITE] created: /Users/cobalt/dev-vault-cobalt/1 - Trading/Assumed Defaults.md · write_id=31611` (diff `@@ -0,0 +1,12 @@` — the `# Assumed defaults` template with an empty `tunables:assumed` unit inside `<!-- cobalt:section assumed -->`) · `[WRITE] updated: … · section=assumed · unit=tunables:assumed · write_id=31613` (diff `@@ -6,7 +6,44 @@`: `-tunables: []` → the four rows `flat_threshold.ema9 0.05 ratio per_indicator(ema9)` · `flat_threshold.vwap 0.05 ratio per_indicator(vwap)` · `range_break.failed_trap_bars 1 bars global` · `range_break.retest_tolerance_atr 0.1 atr global`, each `dynamic: true` `status: proposed` `source: assumed` with its consumers). Both diff paths under `~/dev-vault-cobalt` — **dev proof GREEN; the writer's `global`-scope and `bars`-unit rows are now PROVEN on the dev vault** |
| 6.4 PROD DRY RUN | `COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt taxonomy assumed write --from /Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml --dry-run` | **exit 1** `FAILED: VaultWriteError: REFUSED: /Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md does not exist. upsert_unit never creates a note — call create_if_absent() with a template first (L28.1).` |

6.4's rule: the dry run must show the note CREATED with exactly the four rows; "anything else → `R119: NOT WRITTEN — dry run <what>`; skip to STEP-7". So 6.5 (apply), 6.6, 6.7 and 6.8 were NOT RUN. His vault was not touched; the real note is still absent.

R119: NOT WRITTEN — dry run REFUSED: `--dry-run` on the absent note fails in `upsert_unit` ("does not exist … call create_if_absent() … first"); it cannot preview the create that `--apply` performs (the dev `--apply` created the note and upserted the four rows)
R119 live-note: NOT RUN — rows not written

## ESCALATE
1. **R119 NOT WRITTEN — THE DESK'S FIRST ITEM.** The production dry run REFUSED on the absent note (`upsert_unit never creates a note — call create_if_absent() with a template first (L28.1)`). The dev `--apply` on the equally absent dev note CREATED it and upserted the four rows (write_ids 31611 / 31613). So `--dry-run` cannot preview the first write to a note that does not exist yet, while `--apply` handles it. This is a dry-run defect in `taxonomy assumed write` (or a gap in the prompt's 6.4 expectation), not a vault or code-safety issue. Nothing reached his vault. `ASK DESK: rows by a re-issued STEP-6 (e.g. accept 6.3's dev diff as the preview and run 6.5 --apply, his word needed), or a fix to the dry-run path first? [13:28:45]`. Safe default taken: nothing written.
2. R119 live-note: NOT RUN (rows not written). The expected-GREEN run with the four AWAITING lines (R118) is still owed after the rows land. The second-chance pin stays until then.
3. Radar load: nothing to load (no rows). `cobalt taxonomy load` stays a desk job on his word, after the rows are written. `dist.k.vwap` (A-16) is HELD for his VWAP Continuation sitting (R118); vwap-continuation stays pinned.
4. Downtime **114 s** (> 60 s): `<t down>` 13:20:58 → `<t up>` 13:22:52. The proof-only cost alone was 81.3 s (predicted 100–120 s; `09`'s window was 188 s).
5. `S2 smoke: owed after the 21:10 replay (07 ESCALATE 1)`. `cobalt smoke s2` was not run here: K9.7–K9.12 need a replay job row written by the new code. Tonight's 21:10 replay is the first on the mover fix.
6. The ASSUMED `card_dots`: ids 16 / 32 / 48 (cards 377–379) are still present and read by the new code. (h) counted **5** at 13:27:52: the new radar's cycles wrote 2 more `assumed_formation` dots. All are kept. The ROLLBACK consequence stands: a revert of `a2d320b8` makes every such row unreadable again (production back to the degraded 11:38 state). A rollback now needs those rows handled first. The desk owns that order.
7. The re-land commit subject is `Reapply "Merge branch 'main' into deploy/stacked-0923"`, because this git names a revert-of-a-revert "Reapply". The prompt expected `Revert "Revert "…""` (RELAUNCH (iii) / 4.2). It is the same operation: `128 files changed, 24923 insertions(+), 386 deletions(-)`, parent `602e7b47`, code identical to `a0ba0098`. A relaunch or a later prompt should match `Reapply "…"`.
8. P14 `<hb0>` at 13:19:00 showed radar `failed_stage bars: poll failures: 1`, NOT `failed_stage evaluate`. The incident itself was live in `radar.err` (13:16:45 `radar S5 evaluate FAILED … input_value='ASSUMED'`) and in `aset.err`. `<rp0>` 16 → `<rp_up>` 17: one more panel failure on the OLD code at 13:19:11, before the bootout. From 13:27:10 the heartbeat read fully GREEN.
9. `cobalt_dev` was written only by STEP-6.3's dev-vault proof: `vault_writes` write_ids 31611 / 31613 (fold 7). The dev vault now holds `~/dev-vault-cobalt/1 - Trading/Assumed Defaults.md` with the four rows. The schema was left at 0013 by `09`. No `.env` was copied; `stacked-0923/.env` stayed absent (P13).
10. Gate artifacts / cleanup owed: `deploy/stacked-0923` = `a0ba0098` (re-landed) — its WORKTREE `/Users/cobalt/cobalt-wt/stacked-0923` and the rows folder `/Users/cobalt/cobalt-wt/r119-rows-0923/` (now holds `assumed-rows.yaml`, needed again for the rows) are cleanup owed. The rebased setups branch `126383ea` and mover branch `59532385` stay as they are. Worktrees `setups-c1` and `mover-bars` are cleanup owed. Gitignored scratch owed: `setups-c1/scratch/prints-0923/`, `scratch/prints-0924/`, `scratch/seam-0923/`, `/Users/cobalt/cobalt-wt/stale-marker/tests/cobalt/scratch/`.
11. `cards/stale-score-0922` also edits `tests/cobalt/test_replay_runner.py`; its own deploy's gate proves that seam (L68 SCOPE). The setups r4 HOLD (the test cutter, shipped under R4(a)) still needs its fix → BACKLOG. `09`'s READINGS are carried (`deploy-2026-09-24.md` ESCALATE 9).
12. Rollback artifacts: snapshot restic `d6d3e61d` (13:20, degraded state incl. the 3 rows); tags `pre-reland-0924` @ `602e7b47` and `pre-setups-0924` @ `1118c3d4`; the re-land sha `a2d320b8`; `deploy-2026-09-24` @ `a2d320b8`. What stays applied: migration 0013. What is live: `a2d320b8` (= `a0ba0098`'s code).

## CONTINUE
next: none — run ended (STEP-7 done). A relaunch meets RELAUNCH RULE (iii): HEAD = `<reland>` with a committed stop line → `FAILED: relaunch — the run already ended; the desk decides`.

(history) next: STEP-6 (smoke GREEN; `<reland>` = `a2d320b8`, `<t up>` 13:22:52, `<rp_up>` 17, `<rpr_up>` 58)

THE RELAUNCH RULE (verbatim from the prompt):
"ON A RELAUNCH, BEFORE ANY OTHER CALL after the PLACEHOLDER GATE and AUTHORIZATION: run `date`, `launchctl print gui/501/com.cobalt.aset`, `launchctl print gui/501/com.cobalt.radar`, `git -C /Users/cobalt/cobalt status`, `git -C /Users/cobalt/cobalt rev-parse --short HEAD`, `git -C /Users/cobalt/cobalt log --oneline -3` and `git -C /Users/cobalt/cobalt rev-parse --short deploy/stacked-0923`. ("The report" is THIS run's `deploy-2026-09-24-reland.md`; `<main0>` and `<reland>` are the values it recorded.)
(i) A REVERT IN PROGRESS (`git status` shows `You are currently reverting`, `REVERT_HEAD`, or unmerged paths): bootstrap nothing yet. `git -C /Users/cobalt/cobalt revert --abort`, then `git -C /Users/cobalt/cobalt rev-parse --short HEAD` and `git -C /Users/cobalt/cobalt diff --stat 4e625f6a HEAD -- . ':(exclude)docs'`. HEAD = `<main0>` and the diff EMPTY → the tree is the degraded pre-re-land code: bootstrap every resident not loaded with 4.6's calls, then end `FAILED: relaunch — a revert was interrupted and aborted; production is back on <main0> (degraded); the desk decides · rollback: not used — aset: <UP|DOWN> — radar: <UP|DOWN>`. HEAD = `<reland>` and `git -C /Users/cobalt/cobalt diff --stat a0ba0098 HEAD -- . ':(exclude)docs'` EMPTY → the STEP-5 revert was interrupted before it landed and the new code is intact: bootstrap every resident not loaded with 4.6's calls, end `FAILED: relaunch — STEP-5 revert interrupted; new code kept; the desk decides · rollback: not used — aset: <UP|DOWN> — radar: <UP|DOWN>` (fold 2, `33` C9). Anything else → bootstrap nothing, end `FAILED: relaunch — revert state unresolved — <HEAD> <stat> · rollback: not used — aset: DOWN — radar: DOWN` with every resident not loaded named. Never a second revert on this path.
(ii) HEAD = `<main0>` (nothing re-landed; a committed stop line would have moved `main`, so the earlier run either ended on the UNCOMMITTED BETWEEN line or has no stop line): bootstrap every resident not loaded with 4.6's calls; then, if `date` is 2026-09-24 and before 19:55 ET, or at/after 20:00 and before 20:20 ET, re-read P14's log baselines (`<a0>` `<ta0>` `<tr0>` `<tc0>` `<rp0>`) and the heartbeat, record them, and resume at 4.1 (STEP-R's tag and snapshot stand if recorded; if no snapshot id is recorded run R.2, and if `pre-reland-0924` is absent run R.3, first — fold 3, `33` C8). Otherwise end `FAILED: window — relaunched outside both windows, nothing re-landed · rollback: not used`.
(iii) HEAD = `<reland>` (the ONE `Revert "Revert "Merge branch 'main' into deploy/stacked-0923""` commit whose parent is `<main0>`) — IT LANDED. If the report shows a committed stop line above `# SECOND RUN`, end `FAILED: relaunch — the run already ended; the desk decides · rollback: <as that line>`. Otherwise: run 4.3's PROVE THE TREE reads; the first diff not EMPTY → STEP-5 at once. Then, if 4.4's proof table is not recorded complete, run 4.4 (proof-only, read-only — safe to repeat) and 4.5; then bootstrap whichever resident is not loaded with 4.6's calls; then 4.7 onward — unless (v)'s condition holds: then (v) applies first. This holds at any hour.
(iv) HEAD is a `Revert "Revert "Revert …"""` of `<reland>`, or the report's stop line above `# SECOND RUN` carries `rollback: used`: STEP-5 already ran — it is NEVER re-entered. Bootstrap every resident not loaded with 4.6's calls, then end `FAILED: relaunch — STEP-5 already completed; production is on the reverted (degraded) code; the desk decides · rollback: used — migration 0013 applied: yes — aset: <UP|DOWN> — radar: <UP|DOWN>`.
(v) The report shows `## Smoke` complete and green and `## R119` started but no stop line (HEAD = `<reland>`): resume at STEP-6's first unrecorded call (the note is create-if-absent and the unit upsert is idempotent — same rows = no change); STEP-6.8 runs once, after 6.7.
(vi) Any other HEAD → bootstrap nothing; end `FAILED: relaunch — main is at <HEAD>, neither <main0>, <reland> nor its revert — <log> · rollback: not used — migration 0013 applied: yes — aset: <UP|DOWN> — radar: <UP|DOWN>` with every resident not loaded named DOWN. The desk escalates at once.
NEVER a second bootout of a service that is not loaded. NEVER `db migrate --allow-prod` without `--proof-only`. NEVER a second revert of `4e625f6a`. NEVER STEP-5 twice."

Recorded values: `<main0>` = `602e7b47` · `<aset pid>` 27998 · `<radar pid>` 28025 · `<a0>` 33 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 16 · `<k17_0>` 1 · `<an0>` 0 · `<cards0>` `radar.cards_enabled	True` · `<n_assumed0>` 3 · `<jobs0>` `Jobs (F17): 16 registered — 6 resident, 10 one-shot. Kill phrase 'COBALT STOP'.` · `<val0>` exit 0, `tree clean`. · `<stack stat>` `81 files changed, 20834 insertions(+), 382 deletions(-)` · snapshot `d6d3e61d` · tag `pre-reland-0924` @ `602e7b47`.

SETUPS DEPLOY RELAND DONE · reland: a2d320b8 · tag: deploy-2026-09-24 · rows: 0 (R119: NOT WRITTEN — dry run REFUSED: note absent, --dry-run cannot preview the create) · live-note: NOT RUN · S2 smoke: owed 21:10 · ESCALATE: 12
