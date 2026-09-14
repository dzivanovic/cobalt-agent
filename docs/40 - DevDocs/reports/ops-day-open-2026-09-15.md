# ops/day-open — day-open in code (RULED 2026-09-14, A)

## §0 Headline
`cobalt day-open` built: six checks (C1-C6), in `src/cobalt/dayopen/`, writing
`docs/40 - DevDocs/reports/day-open-<date>.md` and printing the VERDICT table;
`cobalt day-open verdict "<line>"` is the local seat's one write path. Offline
suite green (949 passed, 239 skipped, 1 pre-existing unrelated failure —
identical on a fresh worktree before this branch, see Tests). `cobalt validate`
cannot run to completion in this worktree (no `.env` — by design, "DB-backed
proof is the hub's step at merge"); confirmed identical `cobalt validate`
passes clean (exit 0) on `~/cobalt`, which has credentials. ESCALATE: 1
(RESTARTS — QWEN.md is an unclassified path).

## Diff summary
| area | what |
|---|---|
| `src/cobalt/dayopen/` (new) | `launchd.py` (C1's `launchctl print` parser), `parse.py` (pure log/table parsers), `checks.py` (C1-C6), `models.py` (Verdict/CheckResult/Overall), `config.py` (tunables), `report.py` (render+write+append), `runner.py` (assembly), `cli.py` (argparse) |
| `src/cobalt/cli.py` | mounts `day-open` |
| `configs/cobalt/taxonomy/tunables.yaml` | +`dayopen.c4_expected_session_blocks` (8, proposed), +`dayopen.c6_max_gap_min` (20, solidified) |
| `QWEN.md` | one paragraph pointing the local seat at `uv run cobalt day-open` |
| `docs/40 - DevDocs/cobalt/dayopen/*.md` (new) | one DevDoc per `.py` file |
| `docs/40 - DevDocs/cobalt/cli.md` | +day-open line, +2026-09-14 addendum |
| `tests/cobalt/test_dayopen_*.py` (new, 8 files) | launchd, parse, config, models, checks, report, runner, cli |
| `tests/fixtures/dayopen/` (new) | real-shape slices of `logs/heartbeat.log`, `logs/heartbeat.err`, `docs/30 - Design/archiver-runs.md`, `logs/archiver.err`, plus `launchctl print` (running = real S1 capture; not-running = constructed from the same real field set) |

Design notes not in the ruling's own text, decided here:
- **OVERALL rule** (models.overall_verdict, written down for L57 replayability):
  RED if any check is ERROR, else AMBER if any is FAIL, else GREEN. ERROR
  outranks FAIL — a broken probe is worse than a bad number.
- **C2's pool-block metric** lives at `"user".trader_settings` key `radar.pool`
  → `block.rank_metric[<session>]` (confirmed real: `radar/notes.py`'s mirror
  write, not invented) — supplementary context only, never fails C2 on its own.
- **C6's "previous evening"** reuses `session.aftermarket_close` (20:00 ET)
  rather than a new tunable — it is the same 20:00 the ruling names.

## Tests
`COBALT_ENV=dev uv run pytest tests/cobalt -q`: **949 passed, 239 skipped, 1
failed** (`test_sheet_daymode_probe.py::...test_the_runner_asks_it_right_after_sheet_http`
— `DbConfigError: Missing Postgres settings`; reproduced on a clean worktree
checkout of `main` with no `.env`, identical failure, before any day-open code
existed — a worktree-environment fact, not a regression).

58 new tests, all offline: C1-C6 each PASS/FAIL/ERROR, the weekend fixture
proving C3's RED-is-idle exemption, C4's SQL asserted `%`-free (every `%` is
part of `%s`, never a LIKE wildcard, per the S4 bug), report write/append/
path-refusal, runner assembly, CLI argparse wiring (bare command vs. `verdict`
subcommand). `cobalt day-open --date 2026-09-14` and
`cobalt day-open verdict "..."` smoke-tested live in the worktree (C1 against
the real `com.cobalt.radar` launchd job, read-only; C5 against the real
committed `archiver-runs.md` — PASS, correctly resolving the previous trading
day across a UTC/ET midnight boundary); the smoke-test report file was deleted
before this commit.

## RESTARTS
`cobalt jobs restarts $(git merge-base HEAD main)..HEAD`:

```
FAILED: RestartError: one or more changed paths were unclassified
QWEN.md    M   UNCLASSIFIED   com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path QWEN.md
configs/cobalt/taxonomy/tunables.yaml   M   resident reads         com.cobalt.aset,com.cobalt.radar
src/cobalt/cli.py                       M   static import reach    com.cobalt.radar
src/cobalt/dayopen/*.py (9 files)       A   static import reach    com.cobalt.radar
docs/**, tests/**                       A/M test/documentation; no resident
```

The code-diff-only answer, as anticipated: **com.cobalt.radar** (`cli.py` and
the new `dayopen` package are reachable from it by static import; the tunables
edit is separately read by `com.cobalt.aset` and `com.cobalt.radar`). But the
tool ESCALATEs and falls back to every resident because `QWEN.md` has no
classifier rule at all — root-level markdown (CLAUDE.md/AGENTS.md/QWEN.md)
appears unclassified today. Per L42, unclassified is never dropped, so this
is the derivation's real, correct output, not a bug in this build: **RESTARTS
is genuinely open** between "com.cobalt.radar only" (the code) and "every
resident" (the tool's conservative fallback) until the classifier gets a rule
for root markdown. Not fixed here — out of this build's scope.

## New seat prompt (three lines, for the allowlist owner)
```
Bash(uv run cobalt day-open *)
```
Morning routine: `uv run cobalt day-open` (reads the VERDICT table it prints),
then `uv run cobalt day-open verdict "<one line>"` to record the seat's own
read.

## ESCALATE
1. RESTARTS is ambiguous per above (QWEN.md unclassified) — Dejan decides
   whether root markdown gets a "no resident reads this" classifier rule, or
   whether an unclassified root-markdown edit should always restart everyone.

READY FOR MERGE 16b8b5910707ba6d71c7ef4013e1d9761e535f6c | RESTARTS: com.cobalt.radar (code-only) / ESCALATE fallback: every resident (QWEN.md unclassified) · ESCALATE: 1
