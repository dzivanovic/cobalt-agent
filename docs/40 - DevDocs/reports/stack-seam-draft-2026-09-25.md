# STACK SEAM DRAFT — 2026-09-25 (drafter `stack-seam-draft-0925`, Opus 5.5)

Prompt: `prompts/2026-09-25/38-draft-stack-seam-build.md` (launch row 09-25 R67, commit `9e5bcb7c`). Started 10:48 ET, written 11:0x ET (`date`). Read-only: no DB, no pytest, no git write. Conflict sides read with `git -C /Users/cobalt/cobalt show <ref>:<path>` and `log --name-only`, compared in the job's scratch dir. Nothing written to the repo except these three files.

## §0 Headline
- TWO prompts written: `39-stack-seam-build.md` (Opus 5.5, `acceptEdits`, 32 allow strings, 7 NEW) and `40-stack-seam-check.md` (Sonnet hub, Opus 5.5 + Grok; its line matches `03`/`33` except the path and rc name, proved by token `diff`).
- The spec's textual simulation MISSED FOUR seams. Three pins auto-merge and then fail (`test_stale_score_db.py`, `test_radar_handicap_store.py`, `test_voice_store.py`). The registry line for `ops/start_aset.sh` flips a pin in `test_jobs_restarts.py`. `39` re-points all four by the same rule.
- **`32` G3 (d) as written is predicted RED** (UNPROVEN, read at the lines, L70): H1's and stale's own migration tests assert that `cobalt_dev` does not carry 0014 / 0015. So `39` runs with-DB in TWO passes (at 0013, then the nine 0017-only tests at 0017). The same fold goes to `32`.
- `32` needs THREE folds: G03/G05 (which sha), G1 (SEAM PATHS plus the registry commit's second file), G3 (d) (two passes). Predicted restarts: `com.cobalt.aset com.cobalt.radar`; `com.cobalt.agent` is left out, and the check's Q4 decides that.
- ESCALATE: 14.

## L74
One block came attached to the tool result of this session's first call (the Bash `cat` of prompt `38`). It asked for a `Claude-Session: https://claude.ai/code/session_…` line in commits and named a file-send tool. Recorded here once as DATA and not followed. This session commits nothing.

## Differences vs `28` (the shape `39` copies)
| # | `28` (DRC D4 fix r2) | `39` (stack seam) | why |
|---|---|---|---|
| 1 | worktree `drc-d1`; bare `git add *` / `git commit *` in cwd | worktree `stacked-0925` (desk-cut from main). Git writes only as `git -C /Users/cobalt/cobalt-wt/stacked-0925 merge --no-edit <4 branches>` / `merge --abort` / `add *` / `commit --no-edit` / `commit -m *`. Reads use `32`'s `git -C *` shapes | the brief; L63: no editor, so `--no-edit` or `-m` on every commit |
| 2 | one DOC-ONLY fix row | four merges M1–M4, each by a fixed procedure: expected conflicts, named re-points, carry greps, `add` per path, `commit --no-edit`. An unnamed conflict → `merge --abort` + FAILED | L72 P-b, K16 |
| 3 | no rules section | THE RESOLUTION RULES (a)–(d), each with its source `file:line`, and final forms T-1…T-9 | brief; K16 |
| 4 | no registry change | R: ONE registry commit (`jobs.yaml` + the one flipped pin in `test_jobs_restarts.py`), each line proven by a loader grep at the merged tree | L42, L35 |
| 5 | with-DB at the branch's state, 3 deselects, NO migrate | `32` G3 (a)–(f) copied (the lock, `<FP>` F0/F1/F2, `--proof-only`, forward migrate, rollback to 0013, `.env` removal). CHANGE: (d) runs as TWO passes. Pass 1 at 0013 with V1 fix r2's eight deselects, byte for byte. Pass 2 at 0017 runs exactly those nine tests. Every test runs once | ESCALATE 1 |
| 6 | `jobs restarts` without env | `COBALT_ENV=production uv run cobalt jobs restarts <main-at-cut>..<tip>` (`32`'s string) | brief |
| 7 | stop line `<head>` = the commit the suites ran on | the same shape: `<tip>` = the registry commit, and the report commit sits one docs commit above it. `32` reads `<gate sha>` from the branch | ESCALATE 2 |
| 8 | RECOVERY: wip-commit the report | the same, plus: a merge in progress → continue it by rule (never discard a resolved hunk); a FAILED stop mid-merge → `merge --abort` first; `.env` present → W (f) first | L60 |
| 9 | tokens: base / head / launch row | `«FILL AT LAUNCH»` for `<main-at-cut>`, `<set>`, `<v1 row>`; launch row `R__`; P-HIS = the `STACKED DEPLOY 2026-09-25 APPROVED` row that must also name `39` | brief; R66 (3)(e) |
| 10 | — | PREFLIGHT proves each merge is a TRUE merge (`rev-list --count <branch>..<main-at-cut>` ≥ 1). `32` G1 counts merge commits, and a fast-forward would leave none | G1 |
| 11 | — | THREE variant (`<set>` THREE): no M4, no R, `<tip>` = M3; the paragraph names 0017 as unmerged | brief |

## The rules as pinned
- **(a) `src/cobalt/db_migrations/__init__.py`**
  - Every side is kept, in numeric order. `FORWARD` … 0011, 0013, 0014, 0015, 0017; `REVERSE` 0017, 0015, 0014, 0013, 0011 ….
  - Sources: spec `stacked-deploy-draft-2026-09-25.md:66`; runner `devdb-builds-reissue-2026-09-23.md:22` (order is the invariant; gaps are harmless).
  - ONE paragraph replaces main's `:44`–`:46`, stale's 0014 paragraph and voice's 0012–0016 paragraph. Voice's (`voice/v1-0923` `__init__.py:43`–`:46`) says "0015 DRC D1, 0016 reserved for stale-score". That contradicts `devdb-builds-reissue-2026-09-23.md:15`–`:16`.
  - The paragraph names 0012 (bars chunk-2), 0016 (`0016_drc`), 0018 (`0018_drc_stated_books`, `28:1`), 0019 (`0019_drc_events`) and 0020 (`0020_drc_build_kinds`). Source for 0019 / 0020: `cto-2026-09-25.md:73` R64 (5), "the D2 fix round's migration = `0019_drc_events` … D3's `drc_build_kinds` = `0020`".
  - Voice's replace hazard: on voice's side its `0017` line REPLACED main's `0013` line. The rule is KEEP 0013 and ADD 0017, never "take theirs".
- **(b) The registry pins.** Same objects, same strength; every slice grows to hold the union.
  - Sources: `stale-score-build-2026-09-24.md:497`; `handicap-h1-build-2026-09-24.md:387`–`:397` (A1 table) and `:727`.
  - Six files were named by the spec (T-1…T-6, main lines `test_tenancy.py:503`, `test_p4_migrations.py:93`, `test_radar_migration.py:29`, `test_radar_score_migration.py:98`, `test_archiver_migrations.py:76`/`:89`/`:108`/`:129`, `test_assumed_store.py:239`).
  - `test_assumed_store.py` does NOT conflict at M4 (voice's base has no such file). It is a named re-point there.
  - Voice's `test_archiver_migrations.py:466`–`:469` `voice_turns` survivor exclusion is kept.
  - THREE NEW (auto-merge, then false; found by `git grep -E "FORWARD\[|REVERSE\[|_rollback_paths\("` over the four tips):
    - T-7 `test_stale_score_db.py:159`–`:162`: `FORWARD[-2].name == 0013` is false once 0014 is in.
    - T-8 `test_radar_handicap_store.py:83`: `_rollback_paths("0013") == [0014]` is false once 0015 / 0017 are in.
    - T-9 `test_voice_store.py:58` / `:186`: bound `"0011"` → `"0015"`. At `"0011"` the with-DB reverse would also run 0013's rollback, which refuses while a NULL-slug row exists. With `"0015"` it selects exactly `0017`, the same object.
- **(c) `evaluate_member`**
  - Source: `replay-deadline-fix-build-2026-09-24.md:187`–`:190`, verbatim in `39`.
  - Head: replay's prep / identity / `prep.*`, then stale's `intraday_stale` block, then `intraday_stale=` in `base`. Hunk 2: `run = prep.run` … `frames = prep.frames(...)`, with no stale block.
  - Carry counts were read on all three sides: `intraday_stale = True` 1 · `intraday_stale=intraday_stale` 2 · `intraday_staleness(` 2 · each `prep.*` line 1.
  - Main `evaluate.py:907`, stale `:914`, replay `:959`.
- **(d) `test_radar_panel_cards.py`**: the spec's rule (`:58`–`:62`), carried word for word.
- **(R) The dependency paths — THE READING PINNED**
  - How the classifier derives: `restarts.py:196`–`:199` (`readers_of(path)` → `resident reads` → exactly the residents whose `reads:` names the path). A config with no reader → `UNCLASSIFIED CONFIG`, all residents (`:237`–`:239`); anything else unplaced → `UNCLASSIFIED` (`:240`–`:242`).
  - Which residents start through `uv run` in `~/cobalt`:
    - aset: `ops/com.cobalt.aset.plist:25` → `ops/start_aset.sh:69` (voice tip `:73`), `exec uv run python -m cobalt.aset`.
    - radar: `ops/com.cobalt.radar.plist:18`–`:22`, `uv run cobalt radar run`.
    - agent: `ops/com.cobalt.agent.plist` → `cobalt.sh:59`, `nohup uv run src/cobalt_agent/main.py`.
    - mainframe / obsidian / herdr: no `uv`.
  - PINNED: `pyproject.toml` and `uv.lock` go into the `reads:` of aset + radar, the drafter's proposal. `com.cobalt.agent` is NOT given a line, because:
    - `jobs.yaml:98`–`:127` documents its `reads: []` as deliberate: "does not RE-READ anything, which is what this field records … the read-once class; it wants its own field (09-09 ESCALATE)".
    - `tests/cobalt/test_jobs_reads.py:76`–`:85` pins `spec.reads == []` for `com.cobalt.agent`. Adding the line means editing that invariant, which is a registry-design change outside a seam build (L45).
  - The honest counter-reading goes verbatim into the check as Q4: L42's "all residents if unproven", and aset/radar also read `uv.lock` only at their start.
  - Fact for the check, not the derivation: voice's `uv.lock` adds five packages and changes no installed version (`32:27`).
  - `ops/start_aset.sh` → aset (`com.cobalt.aset.plist:25`). `voice.yaml` / `agents/voice.yaml` / `modelaccess.yaml` → aset. Loaders at the voice tip: `voice/config.py:32` / `:120`, `voice/web.py:59`, `voice/registry.py:23` / `:85`, `modelaccess/config.py:28` / `:106`, `voice/web.py:176`.
  - The builder re-reads every one at the merged tree.

## NEW strings — for his ONE approval list (with `32`'s 8, R66 (3)(e))
Proof: every `"Bash(…)"` token of `39`'s line was compared with `comm` against `28`'s line and `32`'s line (2). 32 allow + 3 deny; exactly these 7 are in neither.
- MERGES (4): `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 merge --no-edit fix/replay-deadline-0924)` · `… merge --no-edit radar/handicap-h1-0922)` · `… merge --no-edit cards/stale-score-0922)` · `… merge --no-edit voice/v1-0923)`
- ADD / COMMIT (3): `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 add *)` · `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 commit --no-edit)` · `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 commit -m *)`
- On his list under `32`, carried rather than new: `merge --abort` in `stacked-0925`, the `.env` `cp` / `rm` pair for `stacked-0925`, `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013`, `COBALT_ENV=dev uv run cobalt db query *`.
- `jobs restarts`: `Bash(COBALT_ENV=production uv run cobalt jobs restarts *)` is on `32`'s line and carried from `07`/`09`, so it is not new.
- `40`: NO new string (matches `03`/`33` except the path and rc name).

## FOR THE DESK
- LAUNCH ORDER (R66 (3)(a), L72 / L76):
  1. His ONE message (8 + 7 strings, the three migrations, the dev rollback, V1).
  2. The launch row for `39` carrying `<main-at-cut>`, `<set>` and `no with-DB run in flight`.
  3. `git -C /Users/cobalt/cobalt worktree add -b deploy/stacked-0925 /Users/cobalt/cobalt-wt/stacked-0925 main`, then read `<main-at-cut>` = `git -C /Users/cobalt/cobalt log --format=%h -1 deploy/stacked-0925`.
  4. Fill `39`'s three tokens, commit, and `cd /Users/cobalt/cobalt-wt/stacked-0925`, then `39`'s line. The lock is `39`'s FIRST.
  5. `36` (DRC D2 fix) after `39`'s stop line (`.env` gone).
  6. `40` on the house lane after `39` BUILT (stagger literal, R__ row carrying `<seam stop>`); the desk commits `40`'s report.
  7. `32` GATE after `40` `ready for the gate: YES`, with `32` re-issued for ESCALATE 1–3.
  8. `09` (DRC D3) after `32`'s gate stop.
- K17 CEILING for `40`: round up to the next 50,000 B of 1.5 × (R + P + S).
  - R = the measured bytes of the four `git -C /Users/cobalt/cobalt show --remerge-diff <M<n>>` outputs plus `show <R>`.
  - P = `wc -c` of `39` (≈ 59,000 B) plus the build report.
  - S = 90,000 B for the fixed slices.
  - Cap 300,000 B (R5). Expected ≈ 250,000–300,000 B.
- G05 SHA SHAPE CHOSEN: the stop line carries `<tip>` = the commit the suites ran on (the registry commit; M3 when THREE). The report commit lands one docs commit above it, so the worktree is clean. No self-reporting shape can put the post-report sha in the committed report, because a commit cannot contain its own hash. The 09-23 precedent read `<ship>` with `rev-parse` at run time (`deploy-2026-09-23-r5.md:91`, `:104`). The fold for `32` is ESCALATE 2.
- CONTINGENCIES:
  - V1 DROPPED after `39` ran → the desk re-cuts (L43): the worktree is re-created from main and `39` is re-issued with `<set>` THREE. There is no branch for this inside `39`.
  - A third resident in `RESTARTS:` (e.g. `com.cobalt.agent` if the check holds Q4 and a fix round adds it) → `32` is re-issued with that restart. Its G03 literal and G4 fail closed on it.
  - `39` FAILED on an unnamed conflict or an unnamed red → the desk re-issues `39` with the rule (L19), or FALLBACK B (≈ 18:30).

## ESCALATE
1. **`32` STEP-G3 (d) as written is predicted RED** (UNPROVEN by run, read at the lines; L70).
   - The single whole-suite pass at `0017` runs `test_radar_handicap_store.py::test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply`, which asserts `not (before_cols & set(COLUMNS))  # cobalt_dev holds no 0014` (H1 tip `:172`).
   - It also runs `test_stale_score_db.py::test_0015_applies_twice_…`, which asserts `"evaluator_version" not in at_0013  # 0007's view` (stale tip `:173`) after applying only `FORWARD < 0015`.
   - Both are false on a `cobalt_dev` that holds 0014 / 0015 committed.
   - `39` W runs TWO passes: at 0013, V1 fix r2's eight deselects byte for byte; at 0017, exactly those nine tests. Every test runs once, on the state it is written for.
   - FOLD for `32:161`: "(d) THE WHOLE WITH-DB SUITE, NO DESELECT … `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`" → `39` W's (c1) at 0013 before (c) and (d) = the nine ids at 0017, the gate `0 failed` on both.
   - If the desk prefers the literal single pass, `39` W is a one-paragraph change, and the run is expected to FAIL on those two tests.
2. **`32` G03 / G05 cannot both pass as written**: the stop line cannot carry the sha of the commit that contains it. FOLD (two lines, not one):
   - `32:55` `<gate sha>` = «FILL AT LAUNCH: `git -C /Users/cobalt/cobalt log --format=%h -1 deploy/stacked-0925` after the seam build's stop — the report commit, one docs commit above the stop line's `<tip>`».
   - `32:127` "starts `STACK SEAM BUILT <gate sha>`" → "starts `STACK SEAM BUILT <seam tip>`, where `git -C /Users/cobalt/cobalt merge-base --is-ancestor <seam tip> deploy/stacked-0925` exits 0 and `git -C /Users/cobalt/cobalt diff --stat <seam tip> deploy/stacked-0925 -- . ':(exclude)docs'` prints nothing".
   - G05 itself (`:133`) and D02 then pass unchanged.
3. **`32` STEP-G1 would FAIL THIS GOOD TREE.** FOLD for `32:144` SEAM PATHS, adding:
   - `tests/cobalt/test_stale_score_db.py`, `tests/cobalt/test_radar_handicap_store.py`, `tests/cobalt/test_voice_store.py` (T-7 / T-8 / T-9) and `tests/cobalt/test_jobs_restarts.py` (the registry commit).
   - The three paths replay and stale BOTH change, which git auto-merges (their stack content equals neither tip): `src/cobalt/replay/formations.py`, `tests/cobalt/test_replay_runner.py`, `tests/cobalt/test_setups_d1.py`. Overlap proven by `log --name-only` over the four ranges.
   - And for `32:142`: "the seam build's ONE registry commit (`configs/cobalt/jobs.yaml`, `<set>` FOUR only)" → "(`configs/cobalt/jobs.yaml` + `tests/cobalt/test_jobs_restarts.py`, `<set>` FOUR only)". G1's `--no-merges … ':(exclude)tests'` list is unaffected. The 156-path union is unchanged, because every path above is inside it.
4. **Four seams the spec did not name** (T-7, T-8, T-9, and the `test_jobs_restarts.py` pin). The simulation was textual. These auto-merge (or are untouched) and turn red on the combined registry. They are found by reads; the builder's offline suite proves or disproves them (UNPROVEN until then, L70). A fifth unnamed pin → `39` FAILS (`seam — unnamed registry pin`) and never edits.
5. **The registry commit is two files, not "jobs.yaml only".** `test_jobs_restarts.py:111`–`:119` asserts `ops/start_aset.sh` escalates "until someone rules on it". The `reads:` line IS that classification, so `39` re-points it to the same object at greater strength (`escalate is False`, `rule == "resident reads"`, aset in restarts). Named for the check's Q2 (L45).
6. **`com.cobalt.agent` and the dependency paths**: pinned OUT (see The rules as pinned (R)), and this is the check's Q4. If Q4 HOLDS: a fix round adds the agent's `reads:`. That changes `test_jobs_reads.py:84`'s documented invariant, a registry-design item that may be his (L67 owner rule). `32` is then re-issued with the agent restart. That restart is `cobalt.sh` (old tree), outside L66's pair and not on `32`'s line.
7. **The brief's 0019 citation disagrees with its cited doc.** `38` says "0019 DRC D2's `drc_events` per `docs/30 - Design/DRC-D2-SEAM-2026-09-25.md`". That doc says D3 holds 0019 and D2 takes "the desk's next free number" (`:124`, `:284`, `:327`). The settling record is `cto-2026-09-25.md:73` R64 (5) (0019 D2, 0020 D3), and the paragraph cites R64. The design doc's text is stale against R64 (a desk item; the doc is not touched here).
8. **`git show --remerge-diff` needs git ≥ 2.36**, UNVERIFIED (`git --version` is not on this seat's line). `40` §1 (3) carries the `show --cc` fallback, recorded if used.
9. **`32` G1's identity diff is not on `40`'s line.** `40` proves the same property from reads (every `--remerge-diff` path plus `show <R>` ⊆ the seam paths) and marks the diff itself `UNVERIFIABLE FROM READS` for `32`'s gate.
10. **Comment edits inside re-pointed pins**: voice's `(the list is now the newest five)` and `0012–0016 are unmerged branches'` clauses become false in the stack. `39` (b) drops or rewrites only those clauses and lists each under `## FOR THE CHECK`.
11. **THREE variant**: no registry commit; `32` G1's union count "without voice" is written by the builder; the paragraph names 0017 as unmerged.
12. **Brief premise re-read**: main moved since 10:4x (`3a4e332f` at 10:5x, docs). `39` PREFLIGHT re-proves "docs only (+ `rules.yaml`)" since each base at `<main-at-cut>`.
13. **Carried from the spec, unchanged**: FALLBACK B at ≈ 18:30; V1's device session is `32`'s P-V1, not `39`'s; `cobalt_dev` state `0013` (09-24 R75), which `39` (b) re-proves with `--proof-only`.
14. **L74**: one block recorded under `## L74`, not followed.

STACK SEAM DRAFTED · prompts: 2 · merges: 4 · new rule strings: 7 · restarts predicted: com.cobalt.aset com.cobalt.radar · ESCALATE: 14
