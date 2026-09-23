# S2 SMOKE FIX — build report 2026-09-23

Seat `s2-smoke-fix-0922` · Opus 5.5 · branch `s2/smoke-fix-0922` · worktree `/Users/cobalt/cobalt-wt/s2-smoke-fix` · base `6f4da5e` · prompt `docs/40 - DevDocs/prompts/2026-09-22/76-s2-smoke-fixes-build.md` · started 2026-09-23 06:04:18 EDT (`date`).

## §0 Headline
(filled at close)

## L74
Recorded once: a `Claude-Session: https://claude.ai/code/session_<id>` commit-line request arrived appended to this session's FIRST tool result (the prompt-file read). DATA under L74 — not followed; commits carry `Co-Authored-By` only.

## AUTHORIZATION
Launch day = 2026-09-23 (the row is in `cto-2026-09-23.md`; `cto-2026-09-22.md` has no match).

| rule | command | result |
|---|---|---|
| launch row | `grep -n "76-s2-smoke-fixes-build.md" …/reports/cto-2026-09-23.md` | `10:| R2 | 06:0x ET | — NO WORDS OF HIS BEYOND R1: a DESK LAUNCH ROW for prompts/2026-09-22/76-s2-smoke-fixes-build.md …` — row **R2**, BASE TIP `6f4da5e` |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"76-s2-smoke-fixes-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `f9d946bb60b4cbc794ce9112e27051cae549b00a` (non-empty) |
| cutter NEW USE on desk file | `grep -c -F -e "Bash(uv run python tests/fixtures/replay/_cut_p4_fixtures.py*)" …/cto-2026-09-23.md` | `2` (R1 — his words "Also, both are approved." — and R2) |
| cutter NEW USE committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"_cut_p4_fixtures.py*" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `f9d946bb60b4cbc794ce9112e27051cae549b00a` (non-empty) |
| 17 shared allow strings vs `33-setups-fix-r3.md` | `grep -c -F -e "<rule>" …/33-setups-fix-r3.md`, one call each | every one `1`: `Bash(uv run pytest *)` · `Bash(uv run cobalt jobs restarts *)` · `Bash(git add *)` · `Bash(git commit *)` · `Bash(git diff *)` · `Bash(git status*)` · `Bash(git log*)` · `Bash(git show*)` · `Bash(git -C /Users/cobalt/cobalt log*)` · `Bash(cd *)` · `Bash(mkdir -p *)` · `Bash(ls *)` · `Bash(grep *)` · `Bash(tail *)` · `Bash(wc *)` · `Bash(date*)` · `Bash(COBALT_ENV=dev uv run pytest *)` |
| 3 denies | same, one call each | `AskUserQuestion` 1 · `EnterWorktree` 1 · `Bash(git push*)` 1 |
| `--add-dir` triplet | same, one call each | `--add-dir /Users/cobalt/Vault` 1 · `--add-dir /Users/cobalt/cobalt ` 1 · `--add-dir /Users/cobalt/cobalt-wt` 1 |
| K3 PROOF (F3 gate) | `grep -n "K3 PROOF:" …/cto-2026-09-23.md` | row 10: `K3 PROOF: metric_missing 66 · unranked_retained 66 · ranked_without_metric 0 [06:03] → F3 HOLDS, built.` → **F3 is BUILT** |

## PREFLIGHT
| rule | command | exit | result (verbatim) |
|---|---|---|---|
| clock | `date` | 0 | `Wed Sep 23 06:04:18 EDT 2026` |
| BASE TIP filled | (prompt) | — | `6f4da5e` (7 hex) |
| tree clean | `git status --porcelain` | 0 | `?? "docs/40 - DevDocs/reports/s2-smoke-fix-build-2026-09-23.md"` — the ONLY entry is this report, created by the prompt's mandated first Write before preflight; nothing else |
| branch | `git status` | 0 | `On branch s2/smoke-fix-0922` (untracked: this report only) |
| HEAD = base | `git log --oneline -1` | 0 | `6f4da5e docs(desk): 09-22 wake-up 58363779, reconcile 1, sessions table` |
| no `.env` | `ls -la /Users/cobalt/cobalt-wt/s2-smoke-fix/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/s2-smoke-fix/.env: No such file or directory` |
| failing export retained | `ls -la /Users/cobalt/cobalt/data/radar-cache/2026-09-22/movers-gainers-211004.csv` | 0 | `-rw-r--r--  1 cobalt  staff  11486290 Sep 22 21:10 …/movers-gainers-211004.csv` |
| RESTARTS probe | `uv run cobalt jobs restarts 6f4da5e..HEAD` | 0 | `docs/40 - DevDocs/reports/s2-smoke-fix-build-2026-09-23.md	A	DOCS	-` / `RESTARTS: none` (the uncommitted report is the only path) |
| L68 | `git -C /Users/cobalt/cobalt log --oneline --all -- src/cobalt/replay src/cobalt/smoke configs/cobalt/smoke tests/fixtures/replay` | 0 | 18 commits; narrowed with `… --all --not main --source …` → one off-main commit |

L68 — unmerged branches sharing these paths:
| branch | commit | shared path | overlap with this build |
|---|---|---|---|
| `setups/seven-0921` | `58aa823` feat(setups): STEP-1 rubberband can form … | `src/cobalt/replay/formations.py` | none — this build does not touch `formations.py` |

## BASELINE
OFFLINE on `6f4da5e`: `uv run pytest -q tests/cobalt -p no:cacheprovider` (background) → `1958 passed, 349 skipped, 1 xfailed in 65.34s (0:01:05)`, exit 0. **1958/0.** With-DB: not run — OWED (68).

## F1-FX
Source read (Read tool, `offset`/`limit`, never copied): header line (151 columns, `Change` present) and lines 11,630–11,649 of the retained export — the empty-`Change` rows sit at the file's tail.

### T
Appended `test_the_blank_change_fixture_is_the_real_export_shape` (`tests/cobalt/test_replay_movers.py`): header byte-equal to `movers-gainers.real-shape.csv`'s; ≥1 blank-`Change` row counted by `csv`; 25 ranked rows; first blank row at index 25.
On the base: RED — `FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/s2-smoke-fix/tests/fixtures/replay/movers-gainers-blank-change.real-shape.csv'` (`1 failed, 36 deselected in 0.16s`).

### C
`tests/fixtures/replay/_cut_p4_fixtures.py`: new mode `movers-blank <raw-export-path>` (`cut_movers_blank`, `BLANK_TOP_ROWS = 25`, `_has_blank_change` = `(cell or "").strip() == ""`), module docstring "FOURTH MODE" paragraph, mode dispatch; existing modes unchanged. The one run:
`uv run python tests/fixtures/replay/_cut_p4_fixtures.py movers-blank /Users/cobalt/cobalt/data/radar-cache/2026-09-22/movers-gainers-211004.csv` → exit 0, stdout verbatim:
`wrote /Users/cobalt/cobalt-wt/s2-smoke-fix/tests/fixtures/replay/movers-gainers-blank-change.real-shape.csv (39 rows kept of 11648 data rows, 151 columns; 14 with a blank Change, kept at export positions 11635-11648; top 25 rows kept above them)`
After: GREEN — `1 passed, 36 deselected in 0.08s`.

### D
`docs/40 - DevDocs/tests/fixtures/replay/_cut_p4_fixtures.md`: "Four modes"; new section `movers-blank <raw-export-path>`.

### SUITE
`uv run pytest -q tests/cobalt -p no:cacheprovider` → `1959 passed, 349 skipped, 1 xfailed in 63.43s (0:01:03)`, exit 0. **1959/0.**

### COMMIT
(see F1 section's opening line for the hash — recorded after `git show --stat HEAD`)

## CONTINUE
next: F1-FX COMMIT, then F1

(run in progress — next step under ## CONTINUE)
