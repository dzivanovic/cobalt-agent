# RADAR BENCHMARK LOAD 2026-09-22

## §0 Headline
- `radar.benchmark` created in production `"user".trader_settings`: `{top_n: 20, min_move_pct: 10}`; sha256 gate verified by the loader, round trip EQUAL.
- Proof read: exactly one row, `{'top_n': 20, 'min_move_pct': '10'}`. Nothing else touched; no restart needed.
- First reader: `com.cobalt.replay` at 21:10 ET tonight. ESCALATE: 2.

## PREFLIGHT

| # | Check | Verbatim | Verdict |
|---|---|---|---|
| P0a | Placeholder gate `grep -n -E "R_[_]" …/01-radar-benchmark-load.md` | (no output) `exit=1` | PASS |
| P0b | `grep -n "^| R1 " cto-2026-09-22.md` | `10:\| R1 \| 06:18 ET \| "approved. we will tune if needed later, do you need a restart" — to the desk's A/B on the replay benchmark: **A = `top_n: 20, min_move_pct: 10`** …` | PASS — value matches |
| P0c | `grep -n "^| R2 " cto-2026-09-22.md` | `12:\| R2 \| 07:02 ET \| "Approved" — to the desk's ONE approval list (06:5x, restated 07:0x): `prompts/2026-09-22/01-radar-benchmark-load.md` (Opus 5, `acceptEdits`) on the reviewed file … sha256 `10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880`; the TWO new strings … `--dry-run` … and the same with `--apply` …` | PASS — file, path, sha256, rule strings match |
| P1 | `date` | `Tue Sep 22 07:03:45 EDT 2026` (Tuesday, 07:03 ET) | PASS — not 20:00–21:00, not 09-23+ → PROCEED |
| P2 | `ls -la …/radar-benchmark.yaml` | `-rw-r--r--  1 cobalt  staff  68 Sep 22 06:20 /Users/cobalt/cobalt/data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml` | PASS — 68 bytes |
| P3 | `grep -n "" …/radar-benchmark.yaml` | `1:optional_settings:` / `2:  radar.benchmark: {top_n: 20, min_move_pct: 10}` | PASS — exact |
| P4 | `git status` | see below | PASS — no merge/rebase markers; `configs/cobalt/rules.yaml` dirty (see ESCALATE) |
| P5 | Last non-blank line of `REVIEW.md` | `RADAR BENCHMARK LOAD REVIEW DONE · houses: 2 of 2 · blockers: 0 · folds: 2` | PASS — blockers 0 |

P4 verbatim:
```
On branch main
Your branch is ahead of 'origin/main' by 31 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   configs/cobalt/rules.yaml
	modified:   docs/40 - DevDocs/reports/cto-2026-09-22.md
	modified:   docs/40 - DevDocs/reports/seat-usage.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	docs/40 - DevDocs/prompts/2026-09-19/31-packet/p2-dark-settings.yaml
	docs/40 - DevDocs/prompts/2026-09-19/31-packet/p2-live-settings.yaml
	docs/40 - DevDocs/prompts/2026-09-20/16-packet/
	docs/40 - DevDocs/reports/day-open-2026-09-22.md
	docs/40 - DevDocs/reports/stale-marker-check-2026-09-22.md

no changes added to commit (use "git add" and/or "git commit -a")
```

GATE: P0–P5 pass → CONTINUE: step 1.

## STEP 1 — dry-run

`COBALT_ENV=production uv run cobalt settings load --optional /Users/cobalt/cobalt/data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml --sha256 10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880 --dry-run`
```
cobalt settings load — DRY RUN from optional:radar-benchmark.yaml

  + radar.benchmark
      db  : (absent)
      file: {"min_move_pct": "10", "top_n": 20}

DRY RUN — 1 setting(s) would change. Nothing written.
```

| Criterion | Loader printed | Verdict |
|---|---|---|
| Marker `+` (added, not `~`) | `  + radar.benchmark` | PASS |
| `db  :` = `(absent)` | `db  : (absent)` | PASS |
| `file:` = `{"min_move_pct": "10", "top_n": 20}` | `file: {"min_move_pct": "10", "top_n": 20}` | PASS |
| Footer | `DRY RUN — 1 setting(s) would change. Nothing written.` | PASS |

## STEP 2 — apply

`date` re-check: `Tue Sep 22 07:04:04 EDT 2026` — not 20:00–21:00, not 09-23+ → PROCEED.

`COBALT_ENV=production uv run cobalt settings load --optional /Users/cobalt/cobalt/data/backups/radar-benchmark-2026-09-22/radar-benchmark.yaml --sha256 10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880 --apply`
```
cobalt settings load — APPLY from optional:radar-benchmark.yaml

  + radar.benchmark
      db  : (absent)
      file: {"min_move_pct": "10", "top_n": 20}

applied: {'radar.benchmark': 'created'} (sha256 10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880)
round trip: database == file, every optional key re-validates.
```
Verdict: PASS — `'created'`, round-trip line present, exit 0.

L28 trace: approved by Dejan via the desk — `cto-2026-09-22.md` row R1 (06:18 ET) and row R2 (launch approval, 07:02 ET) · command (above) · sha256 `10aef996246c1172533d58311dd5f2e9f6f118309d697e447f0be5e989d00880` · applied 2026-09-22 07:04 ET.

## STEP 3 — verify

`COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT key, value FROM trader_settings WHERE key = 'radar.benchmark'"`
```
key	value
radar.benchmark	{'top_n': 20, 'min_move_pct': '10'}
```
Verdict: PASS — one row; `top_n` = 20, `min_move_pct` = 10 (numeric, stored as a Decimal string).

Informational, not a gate — `tail -n 20 /Users/cobalt/cobalt/logs/replay.err` (last night's failure; tonight's run at 21:10 ET is the first read of the new row):
```
2026-09-21 21:10:00.557 | INFO     | cobalt.jobs.wrapper:job_run:173 - F17: com.cobalt.replay RUNNING (timeout 1800s, heartbeat every 600s)
2026-09-21 21:10:00.636 | ERROR    | cobalt.replay.runner:run_nightly:463 - replay 2026-09-21 step movers FAILED — TraderSettingsError: "user".trader_settings has no 'radar.benchmark' row — the replay does not invent a benchmark. Load the reviewed file with `cobalt settings load --optional <file> --sha256 <hash> --apply`.
2026-09-21 21:10:00.657 | ERROR    | cobalt.jobs.wrapper:job_run:192 - F17: com.cobalt.replay FAILED — StepFailed: step movers failed — TraderSettingsError: "user".trader_settings has no 'radar.benchmark' row — the replay does not invent a benchmark. Load the reviewed file with `cobalt settings load --optional <file> --sha256 <hash> --apply`.
FAILED: StepFailed: step movers failed — TraderSettingsError: "user".trader_settings has no 'radar.benchmark' row — the replay does not invent a benchmark. Load the reviewed file with `cobalt settings load --optional <file> --sha256 <hash> --apply`.
```
These are all from 2026-09-21 and come before this load. They are the missing-row failure that this load fixes, not new failures.

STEP 4 — not entered.

## ESCALATE

| # | Item | Status |
|---|---|---|
| 1 | L29 / model tier: the drafter's task file named Sonnet + auto mode; the desk corrected this to Opus 5 + `acceptEdits` (header ASK DESK, answered 06:3x). This run ran on Opus 5, not in auto mode. | Informational, closed |
| 2 | P4: `configs/cobalt/rules.yaml` is dirty on `~/cobalt` main. It is not a report or machine-written file, and it was already dirty before this run started. There are no merge or rebase markers, so it is not a gate failure. This hub did not stage or commit it. The desk should confirm who owns it. | For the desk |
| — | `replay.err`: the only lines are the 09-21 21:10 missing-row failures. Nothing new. | Informational |

## Close — git status after commit `b452d2c`
```
On branch main
Your branch is ahead of 'origin/main' by 32 commits.
	modified:   configs/cobalt/rules.yaml
	modified:   docs/40 - DevDocs/reports/cto-2026-09-22.md
	modified:   docs/40 - DevDocs/reports/seat-usage.md
Untracked: 31-packet/p2-dark-settings.yaml, 31-packet/p2-live-settings.yaml, 2026-09-20/16-packet/, day-open-2026-09-22.md, stale-marker-check-2026-09-22.md
```
The commit's own file is clean in that output. Adding this section changes it again, so this section is the only uncommitted part of this report.

RADAR BENCHMARK LOADED 07:04 ET · row: top_n 20 · min_move_pct 10 · sha256 verified · replay next run: 21:10 ET · ESCALATE: 2
