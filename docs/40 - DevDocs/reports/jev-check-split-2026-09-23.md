# JEV CHECK SPLIT — `36-reissue-jev-check.md` (drafter `jev-check-reissue-0923`, Opus 5.5) — 2026-09-23 12:44 ET

## §0 Headline
- `29-jev-trial-check.md` re-issued in place (L19, whole file) as **CHECK A — the secret and network path**: 17 files. The measured packet is 207,942 B plus headers ≈ 215,200 B, against the 230,000 B ceiling.
- `37-jev-trial-check-b.md` written as **CHECK B — everything else**: 12 files. The measured packet is 175,316 B plus headers ≈ 180,800 B. It gates the merge and the trial runs (N3), never the probe.
- All 29 files of `47fafe5..45f647a` are in exactly one part, and each file is staged WHOLE. 0 unassigned. Rule strings are byte-identical to `29`'s (diffed: 22 of 22 launch-line tokens, both files). New strings: 0.
- `31`'s gate needs no re-issue. It requires the last line to start `JEV TRIAL CHECK DONE` and to carry `secrets LEAK that HOLD: 0`, `defects that HOLD: 0` and `probe gate: READY`, committed under `jev-trial-check-2026-09-2*.md`. A's stop line keeps that shape (adding `part: A (secret + network path)`) and keeps that path. B's path `jev-trial-check-b-…` never matches the glob.
- ESCALATE: 3.

## How the fit was found (measured, `wc -c` at `45f647a`; worktree bytes = `git show 45f647a:<path>` for every code file, checked file by file)
- Run 1's packet staged each file TWICE: once in the per-commit `log -p` history (174,464 B) and once in full at the tip (67,634 B). 27 of the 29 range files are NEW in the range (`git log --diff-filter=A`), and a new file's full content at the tip IS its whole change. Each part therefore stages its new files whole, once. The two CHANGED files (`src/cobalt/cli.py`, `docs/40 - DevDocs/cobalt/cli.md`) are staged as diffs.
- Within-range test weakening can no longer be seen in a whole file. It moved to a hub check: (vi) in each part reads `git log -p` over that part's test files.
- Context is trimmed to what each part's questions cite, by named line range, with every anchor line verified. A: the plan's §1 and §5–§7, the R1–R4 rows plus `31`'s `## THE PROBE`, the build report's R1–R4 plus `## DISCOVERY` plus the run-3 `## ESCALATE` block, and the door's OpenAPI schema excerpt. B: the whole plan, the R1/R5/R6 rows, part A's four modules as read-only context, and the report's §0/R1/R5/R6/DISCOVERY/ESCALATE/CLOSE.

## The split (every file of `47fafe5..45f647a`, bytes at `45f647a` unless noted)
| # | file | new/changed | part | bytes |
|---|---|---|---|---|
| 1 | `src/cobalt/classify/config.py` | new | A | 14,014 |
| 2 | `src/cobalt/classify/collector.py` | new | A | 25,239 |
| 3 | `src/cobalt/classify/ledger.py` | new | A | 4,433 |
| 4 | `src/cobalt/classify/cli.py` (probe; discover and trial glue ride along) | new | A | 6,449 |
| 5 | `ops/run_classify_trial.sh` | new | A | 954 |
| 6 | `tests/cobalt/test_classify_config.py` | new | A | 6,942 |
| 7 | `tests/cobalt/test_classify_keys.py` | new | A | 9,264 |
| 8 | `tests/cobalt/test_classify_discover.py` | new | A | 8,095 |
| 9 | `tests/cobalt/test_classify_door.py` | new | A | 16,420 |
| 10 | `tests/fixtures/classify/openrouter-model-entry.real-shape.json` | new | A | 1,076 |
| 11 | `tests/fixtures/classify/openrouter-systemone-response.openapi-example.json` | new | A | 298 |
| 12 | `tests/fixtures/classify/systemone-openapi-example.json` | new | A | 2,111 |
| 13 | `docs/40 - DevDocs/cobalt/classify/config.md` | new | A | 2,425 |
| 14 | `docs/40 - DevDocs/cobalt/classify/collector.md` | new | A | 5,913 |
| 15 | `docs/40 - DevDocs/cobalt/classify/ledger.md` | new | A | 1,551 |
| 16 | `docs/40 - DevDocs/cobalt/classify/cli.md` | new | A | 3,385 |
| 17 | `docs/40 - DevDocs/tests/fixtures/classify/_classify_fixtures.md` | new | A | 2,037 |
| 18 | `src/cobalt/classify/models.py` | new | B | 8,508 |
| 19 | `src/cobalt/classify/trial.py` | new | B | 8,055 |
| 20 | `src/cobalt/classify/__init__.py` | new | B | 936 |
| 21 | `configs/cobalt/classify/trial.yaml` | new | B | 20,356 |
| 22 | `tests/cobalt/test_classify_models.py` | new | B | 4,973 |
| 23 | `tests/cobalt/test_classify_trial.py` | new | B | 8,517 |
| 24 | `docs/40 - DevDocs/cobalt/classify/models.md` | new | B | 2,224 |
| 25 | `docs/40 - DevDocs/cobalt/classify/trial.md` | new | B | 2,775 |
| 26 | `docs/40 - DevDocs/cobalt/classify/__init__.md` | new | B | 595 |
| 27 | `src/cobalt/cli.py` (the `log -p` diff) | changed | B | 1,190 |
| 28 | `docs/40 - DevDocs/cobalt/cli.md` (the `log -p` diff to the branch tip, including the docs-only `199fa08`) | changed | B | 2,784 |
| 29 | `docs/40 - DevDocs/reports/jev-trial-build-2026-09-23.md` (claim sections §0/R1/R5/R6/DISCOVERY/ESCALATE/CLOSE, from the branch tip) | new | B | 31,190 |

| part | files | checked bytes | context bytes | questions | measured total | + headers / file list | ceiling |
|---|---|---|---|---|---|---|---|
| A | 17 | 110,606 | 88,866 | 8,470 | **207,942** | ≈ 215,200 | 230,000 |
| B | 12 | 92,103 | 77,051 | 6,162 | **175,316** | ≈ 180,800 | 230,000 |

Largest staged file per part (the ≤ 38,000 B part rule): A `contract.md` ≈ 26,370 · B `build-report.md` ≈ 31,190.

## What the desk must write on the launch rows
- `29` (check A): the new literal `29-jev-trial-check.md CHECK A` (run 1's R49 row cannot satisfy it) + `no other house hub is running`, in `R__`.
- `37` (check B): `37-jev-trial-check-b.md CHECK B` + `no other house hub is running`, in `R__`. The row goes in only after A's report has stopped (B's PREFLIGHT checks this).
- Both prompts gate on THIS report being committed (`-S"JEV CHECK SPLIT"` on `reports/jev-check-split-2026-09-2*.md`).
- Both prompts pin `47fafe5..45f647a`. Any other built line fails PREFLIGHT, and the split is then re-measured.

## ESCALATE
1. **`31`'s body text is stale; its gate is not.** Its WHY and INDEX CARD still describe a "chat-response fixture … marked `SHAPE: published schema, not yet a live capture`". The build wrote two OpenAPI-example fixtures, marked `SHAPE: OpenRouter OpenAPI example, not yet a live capture` (door `systemone`, R47). The fixture glob `openrouter-*response*.json` that `31` relies on does match the build's file. This prompt allowed only a re-issue of the gate line, and the gate line matches, so `31` is untouched. The desk decides whether `31` needs an L19 re-issue of that wording before it launches.
2. **A's report replaces run 1's committed FAILED report** at `reports/jev-trial-check-2026-09-23.md` (committed in `8fdaeca`). The path is kept on purpose so that `31`'s gate glob reads part A only. Run 1 stays in git history, and A's §0 names `8fdaeca`.
3. **New context item in A: a public OpenAPI excerpt from gitignored scratch.** It is `scratch/docs-openrouter/submit-a-system-one-request.md` lines 337–436 and 843–1032 (8,397 B), the door's authority under R47. It is staged so checkers can test "field for field" without the 44,795 B whole file. A's PREFLIGHT key-scans it before staging. Run 1's list excluded "scratch/ of the build". This is a deliberate exception, stated in `29` §1.

L74: no block asking for a `Claude-Session` line arrived inside a tool result in this run. Nothing was committed, so no attribution line applies.
L32: no ticker written. L41: no key material written (key NAMES only).

JEV CHECK SPLIT · A: 207942 B · B: 175316 B · files unassigned: 0 · new rule strings: 0 · ESCALATE: 3
