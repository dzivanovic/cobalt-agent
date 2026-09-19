# CARDS GOLIVE APPLY 2026-09-19

## §0 Headline
Cards are LIVE in production. ONE settings load applied at **12:30:01 ET** — `radar.cards_enabled` false→true plus three new `card.*` keys, from the R20-approved file (sha256 `f3663399…65f0`).
Dry-run matched R20's values exactly on every criterion; no `htf_level_proximity`, no float noise, no extra key, no deletion.
Stored values re-read from `"user".trader_settings`: all four present and identical. `cobalt validate` exit 0. Heartbeat GREEN, no new red. Resident logs carry nothing after the apply. Sheet + radar panel both 200.
Rollback: NOT USED. No git write, no commit, no merge, no restart.
ESCALATE: 1 (pre-existing 09-18 lines in `aset.err`, older than the apply — recorded, not a trigger).

## PREFLIGHT

| # | Check | Result | Evidence |
|---|---|---|---|
| P1 | Window (not inside 20:00–21:00 ET) | **PASS** | `Sat Sep 19 12:29:27 EDT 2026` — 7 h 30 min margin to 20:00 ET |
| P2 | sha256 of both cards | **PASS** | live `f3663399b1cbb5ba94edadc7b929900a09be02439c84ffc24f89c12ea81c65f0` · dark `945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca` — both exact |
| P3 | Both files present, non-empty | **PASS** | live 362 B, mtime Sep 19 11:54 · dark 44 B, mtime Sep 17 07:18 |
| P4 | `~/cobalt` clean, no other hub mid-operation | **PASS** | see verbatim below |
| P5 | R20 committed on main | **PASS** | tip `cfb2b15` (desk/report commit); `cto-2026-09-19.md` last touched by `cfb2b15`, tree clean for that path; R20 row found at line 33 |
| P6 | House-check gate, `blocks the launch: 0` | **PASS** | see verbatim below |
| P7 | Heartbeat baseline | **RECORDED** | GREEN, 15 jobs / 12 probes, nothing red; one pre-existing `AMB com.cobalt.herdr` (declared interim) — 12:29:46 EDT |

**P4 verbatim (`git -C /Users/cobalt/cobalt status`):**
```
On branch main
Your branch is ahead of 'origin/main' by 43 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   docs/40 - DevDocs/reports/seat-usage.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	docs/40 - DevDocs/prompts/2026-09-19/31-packet/p2-dark-settings.yaml
	docs/40 - DevDocs/prompts/2026-09-19/31-packet/p2-live-settings.yaml
```
Only the machine-written `seat-usage.md` is dirty; the two untracked yaml files are the desk's `31-packet` copies, left untracked by design (desk ESCALATE-1, L32). No merge markers, no rebase in progress, no sign of another hub mid-operation.

**P5 verbatim (`git -C /Users/cobalt/cobalt log --oneline -5`):**
```
cfb2b15 docs(desk): 09-19 cards apply check — 0 launch blockers, four text fixes folded into 30 (launch line unchanged); apply launches
238374f docs(desk): 09-19 P4 round-2 fix launched (763578e6); A1 + A3 block P4, A3 ruling owed (L52 disclosure)
b38bedf docs(desk): 09-19 P4 round-2 fix chunk prompt (32 + facts) — offline, rules a subset of 13 and 24b
31b2681 docs(desk): 09-19 archiver Grok whole-build read prompt (33 + packet); sessions table 12:14
87d12c2 docs(desk): 09-19 wake-up of 6fb22298; cards apply prompt + its house check (30, 31, packet — settings copies left untracked)
```
R20's row is on main (line 33 of the committed `cto-2026-09-19.md`): `| R20 | 11:57 ET | "Approve cards" — HITL approval (L7 interim / L61 / L28) …` naming the same file and the same sha256 as this run's command.

**P6 verbatim (last line of `review-cards-apply-0919/REVIEW.md`):**
```
CARDS APPLY CHECK · grok: RUN AFTER FIXES 5 · gemini: RUN AFTER FIXES 3 · astra: METER · houses that read it: 2 of 3 · hub-verified REAL: 4 (blocks the launch: 0) · NOT REAL: 2 · UNVERIFIABLE: 1
```
Begins `CARDS APPLY CHECK`, `blocks the launch: 0` → gate open.

**GATE: CONTINUE: step 1** — all seven passed, nothing touched.

## STEP 1 — live `--dry-run` (R20 string 1)

```
cobalt settings load --card — DRY RUN /Users/cobalt/cobalt/data/backups/cards-live-2026-09-19/p2-live-settings.yaml
sha256 f3663399b1cbb5ba94edadc7b929900a09be02439c84ffc24f89c12ea81c65f0

  ~ radar.cards_enabled
      db  : false
      file: true
  + card.proposed_key
      db  : (absent)
      file: {"a_min": "0.7", "a_plus_min": "0.9", "b_min": "0.5", "c_min": "0.4"}
  + card.curves
      db  : (absent)
      file: {"Extension.leg_count": [["0", "10"], ["1", "10"], ["2", "6"], ["3", "3"], ["5", "1"]], "atrs_from_open": [["1", "1"], ["3", "10"]], "rvol": [["1.2", "1"], ["5", "10"]]}
  + card.shadow_promotion_bar
      db  : (absent)
      file: {"median_max": "1", "pairs": 30, "sessions": 10, "within2_min": "0.9"}

DRY RUN — 4 card setting(s) would change. Nothing written.
```

| Criterion | Verdict | Read from the output |
|---|---|---|
| `radar.cards_enabled` — `~`, false → true, not already true | **PASS** | `~ radar.cards_enabled` · `db : false` · `file: true` |
| `card.proposed_key` — `+`, exactly four bands, numerically 0.9 / 0.7 / 0.5 / 0.4 | **PASS** | `a_plus_min "0.9"` = 0.90 · `a_min "0.7"` = 0.70 · `b_min "0.5"` = 0.50 · `c_min "0.4"` = 0.40 — four keys, no fifth |
| …decimal-clean, no binary-float noise | **PASS** | every value a clean quoted decimal; no `0.9000000000000000222`-class string anywhere |
| `card.curves` — `+`, exactly three curves | **PASS** | `Extension.leg_count`, `atrs_from_open`, `rvol` — three, no fourth |
| `atrs_from_open` = [[1,1],[3,10]] | **PASS** | `[["1", "1"], ["3", "10"]]` |
| `rvol` = [[1.2,1],[5,10]], `1.2` clean | **PASS** | `[["1.2", "1"], ["5", "10"]]` — `1.2` exact, no noise |
| `Extension.leg_count` = [[0,10],[1,10],[2,6],[3,3],[5,1]], integers | **PASS** | `[["0","10"],["1","10"],["2","6"],["3","3"],["5","1"]]` — five anchors, every leg count an integer |
| NO `htf_level_proximity` anywhere in the output | **PASS** | the string does not occur in the dry-run output at all |
| `card.shadow_promotion_bar` — `+`, exactly four numbers | **PASS** | `sessions 10` · `pairs 30` · `median_max "1"` · `within2_min "0.9"` — numerically 10, 30, 1, 0.9, matching R20's `{10, 30, 1, 0.90}`. Field names as the sha256-pinned file carries them: `median_max`, `pairs`, `sessions`, `within2_min` |
| NOTHING ELSE — one `~`, three `+`, no `-`, no `card.alignment_default`, no other key | **PASS** | four marker lines total; zero `-` lines; footer `4 card setting(s) would change` |

Quoting, key order and trailing zeros compared numerically per the print-shape rule — no criterion failed on formatting. **STEP 1 PASSED.**

## STEP 2 — live `--apply` (R20 string 2)

Window re-checked immediately before the write: `Sat Sep 19 12:30:01 EDT 2026` — outside 20:00–21:00 ET and earlier than 19:45 ET. Proceeded.

```
cobalt settings load --card — APPLY /Users/cobalt/cobalt/data/backups/cards-live-2026-09-19/p2-live-settings.yaml
sha256 f3663399b1cbb5ba94edadc7b929900a09be02439c84ffc24f89c12ea81c65f0

  ~ radar.cards_enabled
      db  : false
      file: true
  + card.proposed_key
      db  : (absent)
      file: {"a_min": "0.7", "a_plus_min": "0.9", "b_min": "0.5", "c_min": "0.4"}
  + card.curves
      db  : (absent)
      file: {"Extension.leg_count": [["0", "10"], ["1", "10"], ["2", "6"], ["3", "3"], ["5", "1"]], "atrs_from_open": [["1", "1"], ["3", "10"]], "rvol": [["1.2", "1"], ["5", "10"]]}
  + card.shadow_promotion_bar
      db  : (absent)
      file: {"median_max": "1", "pairs": 30, "sessions": 10, "within2_min": "0.9"}

applied: {'radar.cards_enabled': 'updated', 'card.proposed_key': 'created', 'card.curves': 'created', 'card.shadow_promotion_bar': 'created'}; deleted: []
round trip: CardSettings.from_rows(db) == reviewed file — EQUAL.
```

Exit 0, no error, `deleted: []`, round trip EQUAL.

**L28 trace:** approved by Dejan via the desk — `cto-2026-09-19.md` row R20 (11:57 ET) · command `COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/cards-live-2026-09-19/p2-live-settings.yaml --sha256 f3663399b1cbb5ba94edadc7b929900a09be02439c84ffc24f89c12ea81c65f0 --apply` · sha256 `f3663399…65f0` · applied **2026-09-19 12:30:01 ET**.

## STEP 3 — VERIFY (read-only)

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 3.1 | Four rows stored in `"user".trader_settings` | **PASS** | four rows, all present and non-null — verbatim below |
| 3.2 | `cobalt validate` exit 0 | **PASS** | exit 0, no traceback; `Card states: 8 states, 11 legal edges, 4 terminal, every state reachable.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| 3.3 | Heartbeat vs P7 baseline — no NEW red | **PASS** | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red (2026-09-19 12:30:15 EDT)`; the single `AMB com.cobalt.herdr` was already present at P7 and is unchanged; `sheet daymode … half sheet — cards are accepted` |
| 3.4 | `radar.err` / `aset.err` — nothing after 12:30:01 naming cards / card settings / `CardSettingsError` / `trader_settings` | **PASS** | `radar.err` last 60 lines are all `INFO … radar cycle: idle:overnight`, newest `12:30:07.402` — no traceback, no refusal. `aset.err`'s newest timestamped lines are from **2026-09-18**; nothing at all is timestamped after the apply → no qualifying line |
| 3.5 | Sheet + radar panel liveness | **PASS** | `http://127.0.0.1:5010/` → `200` · `http://127.0.0.1:5010/radar` → `200` (liveness only — panel card VALUES are not verified here; Dejan's own look, or Monday's 04:00 ET premarket day-open, is that check, since no scan runs today) |

**3.1 verbatim:**
```
key	value
radar.cards_enabled	True
card.proposed_key	{'a_min': '0.7', 'b_min': '0.5', 'c_min': '0.4', 'a_plus_min': '0.9'}
card.curves	{'rvol': [['1.2', '1'], ['5', '10']], 'atrs_from_open': [['1', '1'], ['3', '10']], 'Extension.leg_count': [['0', '10'], ['1', '10'], ['2', '6'], ['3', '3'], ['5', '1']]}
card.shadow_promotion_bar	{'pairs': 30, 'sessions': 10, 'median_max': '1', 'within2_min': '0.9'}
```
`radar.cards_enabled` = `True`; the three `card.*` values present, non-null, and identical to the reviewed file (the loader's own round trip already proved equality).

**GATE: 3.1–3.4 all clean → verification PASSED, rollback NOT USED.**

## STEP 4 — ROLLBACK

NOT ENTERED. No apply error, no verification red. The dark card at `data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml` (sha256 `945e42f8…d3ca`, verified present at P3) remains the one-command rollback if Monday's premarket shows a problem.

## ESCALATE

1. **`aset.err` carries pre-existing errors from 2026-09-18, unrelated to this run** — recorded verbatim per the verify rule, NOT a rollback trigger (all older than the 12:30:01 apply):
   ```
   2026-09-18 11:30:27.429 | ERROR    | cobalt.aset.web:radar:852 - radar panel FAILED: FAILED: radar bars: poll failures: 1
   2026-09-18 11:34:07.172 | ERROR    | cobalt.aset.web:radar:852 - radar panel FAILED: FAILED: radar bars: poll failures: 1
   2026-09-18 15:44:35.856 | ERROR    | cobalt.aset.web:radar:852 - radar panel FAILED: FAILED: radar bars: poll failures: 2
   2026-09-18 15:48:19.387 | ERROR    | cobalt.aset.web:radar:852 - radar panel FAILED: FAILED: radar bars: poll failures: 2
   ```
   The panel answers 200 today and the heartbeat is green; whether those 09-18 poll failures are closed is the desk's to judge, not this run's.

Noted, not escalated: `AMB com.cobalt.herdr` (present at P7 baseline, declared interim in `configs/cobalt/jobs.yaml`, unchanged by this run); the two untracked `31-packet/*.yaml` copies seen at P4 (the desk's own ESCALATE-1 — this hub added nothing to git).

## Notes on what this run did NOT do
No git add, no commit, no merge, no migration, no restart, no push. Settings are re-read on every call, so L43/L66's residents-down rule did not apply — there is no code change here. This report is left UNCOMMITTED for the desk (L51-2 pattern).

CARDS LIVE 12:30:01 ET · file sha256 f3663399… · stored values: match · resident logs clean: yes · rollback: not used · ESCALATE: 1
