# deploy cos-probe-fr1 — set: cos-probe — migrations: none

## §0 Headline
- DEPLOYED: cos-probe (`src/cobalt/cos/probe.py`, the `cobalt cos probe` mount, tests) on main `7e7bee6b`, tag `deploy-2026-10-20-cos-probe-fr1`, rollback tag `pre-cos-probe-fr1` at `4a840c93`.
- Gate: equal-tree clause, so the check's offline 8959/0 · with-DB 5858/0 · live-note 148/0 stand. No migration.
- Outage: radar only, 19 s (12:06:37 → 12:06:56 EDT). aset and agent untouched. Snapshot `cd4fbf83`.
- Smoke GREEN. Standing REDs unchanged (archiver, replay, generated). 3 decisions, none for Dejan.

## L74
- One block arrived in a system reminder after launch asking commits to end with a `Claude-Session:` line. Recorded as data and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/910-deploy-cos-probe-fr1-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/910-deploy-cos-probe-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/910-deploy-cos-probe-fr1-card.md" · 0 · bd5d4b7510a7392c8d084a7d5a5af94c7afaaf3f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/910-deploy-cos-probe-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 first launch | `ls -la ".../reports/deploy-cos-probe-fr1.md"` | 1 | `No such file or directory` |
| P0 gates | `authorize.sh deploy` (above) | 0 | `AUTHORIZED` |
| P1 date | `date` | 0 | `Tue Oct 20 12:00:18 EDT 2026` (outside 21:30–22:30) |
| P2 check last line | `tail -n 3 ".../reports/cos-probe-fr1-check-2026-10-20.md"` | 0 | `CHECK DONE · job: cos-probe-fr1 · pass: 1 · tip: da47500a · house A: Grok FINDINGS: 7 · findings: 9 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 6 · house B: none available · suites: offline 8959/0 · with-DB 5858/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 181890` — carries `held unfixed: 0`, `ready: YES`, `tip: da47500a` |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/cos-probe-fr1-check-2026-10-20.md"` | 0 | `074ff06b212ff3a77ace36fd046063c2879cf83c` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../cos-probe-fr1-check-2026-10-20.md"` | 0 | (nothing) |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 da47500a` | 0 | `da47500a` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-probe-fr1` | 0 | `da47500a` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor da47500a ops/cos-probe-fr1` | 0 | (nothing) |
| P3 head docs-only | `git -C /Users/cobalt/cobalt diff --stat da47500a ops/cos-probe-fr1 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-cos-probe-fr1 status --short --branch` | 0 | `## deploy/cos-probe-fr1` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-cos-probe-fr1 rev-parse --short=8 HEAD` | 0 | `bd5d4b75` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor bd5d4b75 main` | 0 | (nothing) |
| P5 main..BRANCH | `git -C /Users/cobalt/cobalt log --oneline main..deploy/cos-probe-fr1` | 0 | (empty) |
| P6 marker 1 | `ls /Users/cobalt/cobalt/src/cobalt/cos/probe.py` | 1 | `ls: /Users/cobalt/cobalt/src/cobalt/cos/probe.py: No such file or directory` (= before) |
| P6 marker 2 | `grep -c -F "def test_x20_redact_keeps_the_card_fragment_key" /Users/cobalt/cobalt/tests/cobalt/test_hitl_offline.py` | 1 | `0` (= before) |
| P6 marker 3 | `grep -c -F 'csub.add_parser("probe"' /Users/cobalt/cobalt/src/cobalt/cos/cli.py` | 1 | `0` (= before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main da47500a -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 77363` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 77373` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| T merge | `git -C /Users/cobalt/cobalt-wt/deploy-cos-probe-fr1 merge --no-edit da47500a` | 0 | `Merge made by the 'ort' strategy.` — 8 files changed, 1188 insertions(+), 1 deletion(-) (`src/cobalt/cos/cli.py`, `src/cobalt/cos/probe.py`, `tests/cobalt/test_cos_probe.py`, `tests/cobalt/test_hitl_offline.py`, four docs) |
| m1 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `8b1f10f1` = `<m1>` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent bd5d4b75..deploy/cos-probe-fr1` | 0 | `8b1f10f1 Merge commit 'da47500a' into deploy/cos-probe-fr1` |
| tip in branch | `git -C /Users/cobalt/cobalt merge-base --is-ancestor da47500a deploy/cos-probe-fr1` | 0 | (nothing) |
| migrations | `git -C /Users/cobalt/cobalt diff --stat bd5d4b75 deploy/cos-probe-fr1 -- src/cobalt/db_migrations` | 0 | (nothing) — none, as the card says |
| C configs/ops | `git -C /Users/cobalt/cobalt diff --stat bd5d4b75 deploy/cos-probe-fr1 -- configs ops` | 0 | (nothing) |
| C script | `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" bd5d4b75 deploy/cos-probe-fr1` | 0 | `STEP-C: ADMITTED 0` |

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (in `<GATE>`, `.env` No such file) → exit 0, table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr1-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr1-build-2026-10-20.result	A	DOCS	-
src/cobalt/cos/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/cos/probe.py	A	static import reach	com.cobalt.radar
tests/cobalt/test_cos_probe.py	A	test/documentation; no resident	-
tests/cobalt/test_hitl_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
(uv created the gate `.venv` on this first call: `Installed 257 packages in 831ms`.)
- `<restart set>`: `com.cobalt.radar` · `<deferred set>`: empty · `<launchd set>`: empty. No `UNCLASSIFIED` row; `com.cobalt.cos` not in the set.

## L68 GATE
THE EQUAL-TREE CLAUSE holds: one branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat da47500a 8b1f10f1 -- . ":(exclude)docs"` → (nothing); the check's stop line carries with-DB 5858 > 0. The check's suite lines are the gate's, quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr1-check-2026-10-20.md` (lines 149–167):
```
offline 8959/0
with-DB 5858/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
```
- SKIPPED judgment: every line is inside the allowed set. By test, read at `<GATE>`: `test_checkpoints_live.py:36` = `test_dry_run_finds_the_heading_in_real_notes` (line 37); `test_playbook_live.py:31` = `test_live_vault_renders_six_decks` (line 32); `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (line 96).- The check's gate: `cobalt_dev: 0013 — F2 = F0`, `.env` removed. This run took no lock and ran no `gate.sh`.
- G (a0) THE EARLY READ: `ls -la <GATE>/.env` → No such file; `uv run pytest -q -rs -p no:cacheprovider <17 files>` → `265 passed, 163 skipped in 19.65s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db: needs cobalt_dev`).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 8b1f10f1

## Deploy table
| step | command | exit | result verbatim |
|---|---|---|---|
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 113]` |
| D0 porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M` / `??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (outside the accepted and refused lists; present in the session-start status; recorded). No staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path but `rules.yaml` |
| D0 main moved | `git -C /Users/cobalt/cobalt diff --stat bd5d4b75 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| D0 probe tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-cos-probe-fr1` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-cos-probe-fr1' (was bd5d4b75)` |
| D0 probe commit | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 248373a3] scratch: allowlist probe (reverted next line)` · (nothing) · `bd5d4b75 docs(prompts): cos-probe-fr1 card 910 and day report row R2165` |
| D0 tags | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-20-cos-probe-fr1` · `… refs/tags/pre-cos-probe-fr1` | 1 · 1 | (nothing) · (nothing) |
| D1 date | `date` | 0 | `Tue Oct 20 12:03:44 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT RED — 3 job(s) and 2 probe(s)  (2026-10-20 12:03:45 EDT)`; `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200`; `OK   com.cobalt.aset              running   loaded, pid 77363 [launchd probe]`; `OK   com.cobalt.radar             running   running 114 min, heartbeat fresh`; REDs named: `RED  archiver                 last run FAILED — last run 2026-10-20 00:54 UTC (15.2 h ago), rows written 3369418, exit 1`; `RED  radar                    failed_stage bars: poll failures: 1` (CARRIED FAMILY: radar running, heartbeat fresh, `radar.err` `2026-10-20 12:03:09.060 … radar cycle: scanning scan_id=1792512107268`, no traceback); `RED  com.cobalt.archiver          failed    RuntimeError: 5 archiver failure(s): WBD/i1: …Finviz HTTP failed: Client error '400 Bad Request'…`; `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'`; `RED  com.cobalt.generated         failed    GeneratedCommitRefused: … pre-commit: a deploy hub is live — no desk commit on main until its stop line: 79a459de deploy-hub-hub-cos-restart-fr1` |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (same) | 0 | `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 2.1 h old` |
| D1 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `<aset pid>` = `77363` |
| D1 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `<radar pid>` = `77373` |
| D1 agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 35845` | 0 · 0 | `Cobalt is ONLINE (PID: 35845).` · `35845 ??         0:00.03 uv run src/cobalt_agent/main.py` |
| D1 radar tail | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | seven `cards.expire: falling back to the session close (16:00:00)` INFO lines, then `2026-10-20 12:03:09.060 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792512107268` |
| D1 counts | `grep -c` ×8 | — | `<a0>` 289 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| D1 markers | the three `## MARKERS` | 1 · 1 · 1 | `ls: /Users/cobalt/cobalt/src/cobalt/cos/probe.py: No such file or directory` · `0` · `0` (each = before) |
| D1 launchd set | — | — | empty: nothing |
| D1-M | — | — | `MIGRATIONS: none`: not run |
| D2.0 shipped | `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved bd5d4b75 "<card>"` | 0 | (nothing) |
| D2.0 commit | `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy cos-probe-fr1 — gate green on 8b1f10f1" …` · `show --stat HEAD` | 0 · 0 | `[main 4a840c93]` · one file, `docs/40 - DevDocs/reports/deploy-cos-probe-fr1.md | 136 ++++` |
| D2.0 `<pre-merge>` | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `4a840c93` |
| D2.1 | `git -C /Users/cobalt/cobalt-wt/deploy-cos-probe-fr1 merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 `<stack-final>` | `git -C <GATE> rev-parse --short=8 HEAD` · `rev-parse --short=8 7e7bee6b^2` · `merge-base --is-ancestor 8b1f10f1 7e7bee6b` | 0 · 0 · 0 | `7e7bee6b` · `4a840c93` · (nothing) |
| D2.3 docs-only | `git -C /Users/cobalt/cobalt diff --stat 8b1f10f1 7e7bee6b -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| D2.4 before | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 2.1 h old` |
| D2.4 run | `COBALT_ENV=production uv run cobalt backup run` | 0 | `backup: cobalt_brain via pg_dump inside cobalt_memory — 9560.3 MB` · `ssd: snapshot cd4fbf83 — 2 new / 2 changed, 158.7 MB added, 1 pruned` |
| D2.4 after | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `COBALT_ENV=production uv run cobalt heartbeat show` | 0 · 0 | `Tue Oct 20 12:06:13 EDT 2026` (149 s after D1) · `HEARTBEAT RED — 3 job(s) and 1 probe(s)`; `OK   radar                    scanning (rth), members 50`; `OK   com.cobalt.aset              running   loaded, pid 77363`; `OK   com.cobalt.radar             running   running 116 min, heartbeat fresh`; REDs = archiver probe, `com.cobalt.archiver`, `com.cobalt.replay`, `com.cobalt.generated` (all in `<hb0>`); no new RED |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-cos-probe-fr1` | 0 · 0 | `Tue Oct 20 12:06:22 EDT 2026` · rollback tag at `4a840c93` |
| 4.1 `<t down>` | `date` | 0 | `Tue Oct 20 12:06:37 EDT 2026` |
| 4.2 radar | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print gui/501/com.cobalt.radar` | 0 · 113 | (nothing) · `Could not find service "com.cobalt.radar" in domain for user gui: 501` (aset, agent not in the set: no call) |
| 4.3 HEAD | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `4a840c93` = `<pre-merge>` |
| 4.3 merge | `git -C /Users/cobalt/cobalt merge --ff-only deploy/cos-probe-fr1` | 0 | `Updating 4a840c93..7e7bee6b` / `Fast-forward` — 8 files changed, 1188 insertions(+), 1 deletion(-) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`) |
| 4.6 radar | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `launchctl print gui/501/com.cobalt.radar` | 0 · 0 | (nothing) · `state = running`, `pid = 31756` (≠ 77373) |
| 4.6 `<t up>` | `date` | 0 | `Tue Oct 20 12:06:56 EDT 2026` — downtime 19 s |
| 4.6L | — | — | `<launchd set>` empty: nothing |

- `<pre-merge>` → `<stack-final>`: `4a840c93` → `7e7bee6b` · tags: `pre-cos-probe-fr1` at `4a840c93`, `deploy-2026-10-20-cos-probe-fr1` (set after the green smoke at STEP-7)
- `<t down>` 12:06:37 · `<t up>` 12:06:56 · 19 s
- uv sync line: none on the production calls; the gate's first call built its `.venv` (`Installed 257 packages in 831ms`)
- proof cost: none (no migration) · `migrations applied: none` · `<RB>`: none on the card
- snapshot: `cd4fbf83` (ssd)
- RESTARTS done: com.cobalt.radar · LAUNCHD done: none · BOOTSTRAP OWED: none
- THE ROLLBACK STRING (the desk's): (1) CODE: radar down (`launchctl bootout gui/501/com.cobalt.radar`), `git -C /Users/cobalt/cobalt revert --no-edit -m 2 7e7bee6b`, radar up (`launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`); (2) SCHEMA: none (no migration); (3) RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
| row | date | command | result verbatim |
|---|---|---|---|
| first calls | (after `<t up>` 12:06:56) | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 |
| (a) | 12:07:14 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` · `/Users/cobalt/cobalt/cobalt.sh status` | aset `state = running`, `pid = 77363` (SAME, outside the set) · radar `state = running`, `pid = 31756` (NEW, ≠ 77373) · `Cobalt is ONLINE (PID: 35845).` |
| (b) counts | 12:07:19 | `grep -c` Started / Traceback ×2 / TaxonomyConfigError | `289` (= `<a0>`, aset outside the set) · `217` (= `<ta0>`) · `0` (= `<tr0>`) · `0` (= `<tc0>`) |
| (b) aset tail | 12:07:19 | `tail -n 30 /Users/cobalt/cobalt/logs/aset.err` | last lines a `[WRITE] updated … section=aset-cards · unit=card-20261020T103251` diff at 10:32:51; no new start (aset not restarted) |
| (b) radar tail 1 | 12:08:29 (`<t up>` + 93 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | eleven `cards.expire: falling back to the session close (16:00:00)` INFO lines at 12:08:15, then `2026-10-20 12:08:16.224 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792512414000`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN, settled |
| (c) | 12:07:25 | the three `curl` | `/` `200` · `/radar` `200` · `/radar\?frame=phone` `200` |
| (d) | 12:07:25 | the three `## MARKERS` | `/Users/cobalt/cobalt/src/cobalt/cos/probe.py` · `1` · `1` (each = after) |
| (e) first | 12:07:32 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 12:07:33 EDT)`; `OK   radar                    scanning (rth), members 50`; `OK   com.cobalt.radar             running   running 1 min, heartbeat fresh`; REDs: archiver probe, `com.cobalt.archiver`, `com.cobalt.replay`, `com.cobalt.generated` — all in `<hb0>` |
| (e) second | 12:09:23 (111 s after the first's 12:07:33 stamp) | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 12:09:24 EDT)`; `OK   radar                    scanning (rth), members 50`; `OK   com.cobalt.radar             running   running 3 min, heartbeat fresh`; same four REDs as `<hb0>`; no new RED |
| (f) | 12:07:32 | `COBALT_ENV=production uv run cobalt validate` · `COBALT_ENV=production uv run cobalt jobs restarts 4a840c93..7e7bee6b` | exit 0, `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.`, `Placement (docs/PLACEMENT.md): tree clean.` · exit 0, `RESTARTS: com.cobalt.radar` (= `<restart set>`), no `UNCLASSIFIED` |
| (g) | — | — | no migration |
| (s) | — | — | the card's `## SMOKE READS` hold no read line; `<launchd set>` empty. The suites are the gate's (`## L68 GATE`) |
| (h) | 12:09:56 (`<t up>` + 180 s) | the four failure counts · `curl …/radar` | `18` · `60` · `43` · `39` (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none growing) · `200`; no `census` read on the card |

THE CHAIN: every check committed (P2: `074ff06b`) → the tips re-read (P3: `da47500a` = code tip = head) → the merged tree (T: `<m1>` `8b1f10f1`, one merge, no migration) → RESTARTS derived (R: `com.cobalt.radar`) → three suites green on `<m1>` (G: equal-tree clause, the check's offline 8959/0 · with-DB 5858/0 · live-note 148/0; G (a0) 265 passed) → `<stack-final>` `7e7bee6b` = `<m1>` + docs (D2.3) → the landed code (4.3: `Updating 4a840c93..7e7bee6b`) → markers after (d) → no migration (g) → radar up on a new pid, aset and agent untouched (a) → radar cycling (b `12:08:16 radar cycle: scanning`, e) → no set reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

SMOKE: GREEN.

PRE-STOP SELF-CHECK:
1. Every smoke row is quoted with its `date` (rows above).
2. Code tip and head `da47500a` re-read at P3; `git -C /Users/cobalt/cobalt merge-base --is-ancestor da47500a 7e7bee6b` → exit 0.
3. REVERT-READBACK (h) shown: 18 · 60 · 43 · 39 against the same four up-counts. Every count and sha in this report was read from tool output in this run.
4. No conflict marker: STEP-T printed `Merge made by the 'ort' strategy.`; `git -C <GATE> status --short` → (nothing).
5. THE RELEASE: no lock was taken. `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.

## CONTINUE
next: STEP-D0 (gate green at 12:02:33 EDT)
OUTAGE STARTING 12:06:22 EDT — residents of com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
outage ended 12:06:56 EDT, radar up (pid 31756); smoke GREEN 12:09:56; tag set. next: none — the run is closed

## DECISIONS
- D1 · `## RULINGS` names 2026-10-18 R1863, whose last column reads `APPLIED: …`, not `APPROVED`; its text carries `HIS RULING · APPROVED` and `authorize.sh` printed `AUTHORIZED`. The card's one check line is clean (`held unfixed: 0`, `ready: YES`), so no carried defect rests on that row. Default taken: went on with `AUTHORIZED`.
- D2 · THE EQUAL-TREE CLAUSE held, so `gate.sh` did not run; the gate is the check's three suite lines. I also ran G (a0) (offline, 265 passed). Default taken: the clause, as written.
- D3 · Heartbeat `com.cobalt.generated` RED names `deploy-hub-hub-cos-restart-fr1` as a live deploy hub (`79a459de`). That is not this run. The 4.3 HEAD check found no foreign commit, and the fast-forward landed. Default taken: named it, did not stop on it (D1: "any other RED is named, not a stop"). The desk should find out whether that hub is still live or its marker is stale.

## RECORDS
- Downtime: radar 19 s (12:06:37 → 12:06:56 EDT). aset and agent were not restarted.
- `cobalt_dev`: this run took no lock and ran no forward migrate (equal-tree clause). The check's record is `cobalt_dev: 0013 — F2 = F0`, `.env` removed.
- `<GATE>` `.venv` created by uv on the first `jobs restarts` call (`Installed 257 packages in 831ms`). It is under the gate worktree and goes with the desk's cleanup.
- D0: `?? .claude/settings.json.bak` is on main, outside both the accepted and refused lists. It was already there at session start.
- Carried RED as read: `<hb0>` `RED  radar                    failed_stage bars: poll failures: 1` (carried family), cleared to `OK   radar scanning (rth), members 50` by D2.5. Standing REDs, unchanged through the run: archiver probe (`last run FAILED … 00:54 UTC`), `com.cobalt.archiver` (Finviz 400 on WBD/i1), `com.cobalt.replay` (`archiver not done`), `com.cobalt.generated` (the pre-commit guard naming `deploy-hub-hub-cos-restart-fr1`).
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-cos-probe-fr1` and branch `deploy/cos-probe-fr1`; the set's branch `ops/cos-probe-fr1` and its worktree.
- RETIRE OWED: none. BOOTSTRAP OWED: none.
- REFUSED, not needed: none. Messages not followed: none.
- L74: one `Claude-Session:` request in a system reminder, recorded under `## L74`, not acted on.
- Card `## RECORDS` (the desk's, copied):
  - cos-probe-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr1-check-2026-10-20.md` last line: CHECK DONE · job: cos-probe-fr1 · pass: 1 · tip: da47500a · house A: Grok FINDINGS: 7 · findings: 9 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 6 · house B: none available · suites: offline 8959/0 · with-DB 5858/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 181890
  - cos-probe-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-probe-fr1` → `da47500a`; code tip `da47500a`
  - house B: none seated (`HOUSE B: as needed`); the check's own record says so (RECORDS: "House B: not seated"); desk reading: the set is a probe CLI under `src/cobalt/cos/` plus tests, no daily-note writer.
  - written by deploy-card.sh at 2026-10-20 11:58 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-20-cos-probe-fr1 7e7bee6b | set: cos-probe | migrations: none | gate: offline 8959/0 · with-DB 5858/0 · live-note 148/0 | RESTARTS: com.cobalt.radar | smoke: GREEN | decisions: 3 · for Dejan: 0 · tokens: 214880
