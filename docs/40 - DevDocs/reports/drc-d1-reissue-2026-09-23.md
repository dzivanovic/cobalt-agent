# DRC D1 re-issue for 2026-09-23 — drafter `drc-d1-reissue-0923` (Opus 5.5)

## §0 Headline
- `prompts/2026-09-23/53-drc-d1-build.md` (= `48` re-issued whole, L19) and `54-drc-d1-check.md` (= `53` re-pointed, L67) are WRITTEN. Nothing launched, nothing committed.
- BASE = `main` at the moment the desk runs `worktree add`. D1 goes first; D4 (`51`) is not started and shares no path with D1.
- Migration **`0015`**, with a re-derive rule at D1-5. D1-5 now also names the three registry seam files.
- Dev-DB lane: D1 builds offline alongside the siblings and holds `cobalt_dev` for ONE with-DB block, gated on `ls /Users/cobalt/cobalt-wt/*/.env`.
- New rule strings: **0**. The `.env` pair is his, in 09-22 R105. ESCALATE: 4.

## L74
A `Claude-Session` attribution block came in attached to the first file read. Recorded once here and not followed; this run makes no commit.

## Facts read (13:19–13:25 ET, `date`)
| fact | command / source | result |
|---|---|---|
| main tip | `git log --oneline -1 main` | `97244e46` at 13:21. The desk fills BASE at `worktree add` time. |
| main migrations | `ls src/cobalt/db_migrations` | `0001`…`0011` |
| every branch | `git log --all --name-only --format= -- src/cobalt/db_migrations` | also `0012_bars_partitioned_parent` (`bars/chunk-2-0920` only, unmerged, last commit 09-21) and `0013_tunables_slug_nullable` (`setups/seven-0921`, `deploy/stacked-0923`) |
| H1 | `27-handicap-h1-build.md:73,93` | `0014_radar_handicap`. It is not yet on any branch: the `radar/handicap-h1-0922` tip is a docs commit that is already an ancestor of main. |
| stale-score | `31-stale-score-build.md:1` | ONE **conditional** migration, used only if STEP-3 builds R40's exclusion. No number given. |
| sibling report | `ls reports/devdb-builds-reissue-2026-09-23.md` | absent at 13:25. `46` / `47` are not yet written. |
| D4 | `ls /Users/cobalt/cobalt-wt/` · `git branch -a` | no `drc-d4` worktree and no `drc/*` branch |
| D1 ∩ D4 paths | `51` CLOSE:40 | D4 asserts `git diff <base> -- src/cobalt/drc src/cobalt/db_migrations` is EMPTY. D1 touches no `settings/`, `aset/`, `prefill/` or `configs/` path. → disjoint. |
| registry seam | `tests/cobalt/test_archiver_migrations.py:125-143`; `git diff main deploy/stacked-0923 --stat` | The registry test pins `numbers == list(range(1, 12))`. Setups re-pinned it to `[*range(1, 12), 13]` and also edited `db_migrations/__init__.py` (+11) and `test_tenancy.py` (3 lines). `48`'s D1-5 named none of these files. |
| `.env` pair | `cto-2026-09-22.md` §4 R105 (`123f7ad5`) | "Approved" — both `drc-d1` strings verbatim, "for `48`–`57` only" |
| grok/agy | same R105 | "through 2026-10-07" for the DRC check hubs |
| dev-DB lane now | `ls /Users/cobalt/cobalt-wt/*/.env` | `no matches found` (free, 13:19) |
| E1 | `ls …/_imports/drc` | `2026-09-18`, `_reference` |

## Migration number + lane rule
- **The number is `0015`.** `0012` belongs to bars chunk-2, `0013` to setups (deploys tonight), and `0014` to H1 (reserved even though no branch carries it yet).
- **Re-derive at D1-5** (written into `53`):
  - Take `git log --all --name-only` over `db_migrations`.
  - Add `0014` and any number `reports/devdb-builds-reissue-2026-09-23.md` reserves.
  - If nothing in that set is ≥ `0015`, the number is `0015`. Otherwise it is the highest + 1.
  - Record the list. The desk renumbers at the L68 gate.
- **Registry (the L72 P-b seam):** D1 adds its pair to `FORWARD` / `REVERSE` and re-pins the contiguity test to its own tree: `[*range(1, 12), 15]` on a main base, with the siblings' numbers named. The combined pin, `[*range(1, 12), 13, 14, 15]` while `0012` is unmerged, is written at the L68 gate. `placement.py` gets additive entries only.
- **Lane rule:**
  - D1-0…D1-6 run offline. PREFLIGHT only records the `.env` glob; it never fails on it.
  - The with-DB baseline runs at BASELINE only if the lane is free. Otherwise it is deferred and labelled "on HEAD, not on base".
  - The with-DB suites run in ONE `## WITH-DB` block.
  - The gate runs immediately before the `cp`: `ls -la /Users/cobalt/cobalt-wt/*/.env`, where "no matches found" means free. After the `cp`, exactly one `.env` may be listed.
  - If the lane is held: wip-commit and stop with `FAILED: WITH-DB — dev-DB lane held — <path> — …`. The desk relaunches with one `CONTINUE:` line. The builder never waits in a loop.

## NEW strings (for the desk's ONE list)
None. The `53` line = `48`'s line byte for byte, except the prompt path. Its two `.env` strings are R105's. The `54` line = the old `53`'s line, except the prompt path.
- ONE reading for his list (not a string): **"R105 ('for `48`–`57` only') covers the 09-23 re-issues `53` (build) and `54` (check)."** Both prompts RECORD this reading and continue unless a row of his says otherwise.

## ESCALATE
1. **R105 scope reading.** R105 names the 09-22 numbers. `53` and `54` are the same prompts re-issued whole. Put the reading above on his ONE list. If he declines, the `.env` pair and grok/agy after 09-23 become NEW.
2. **Stale-score's conditional migration is the known unknown for `0015`.** `46` is not written yet (13:25). If `46` numbers its migration `0015`, D1's re-derive only catches it once that branch carries the file. The desk should assign stale-score `0016` (after D1), or D1 takes `0016`. Either way this has to be settled in `devdb-builds-reissue-2026-09-23.md` before both launch (L72 P-b).
3. **Siblings' stagger vs D1's hold.** `31`'s PREFLIGHT (carried into `46` / `47`) FAILS if any `.env` exists. If a sibling launches while D1 is inside `## WITH-DB` (two suites), that sibling fails PREFLIGHT. The desk should sequence sibling launches around D1's with-DB block, or give them the same record-not-fail rule.
4. **The DRC stack order changes to D1 → D4 → D2 → D3.** `51` (base "main") and `49` (base "D1's tip") must be re-pointed by the desk before they launch: D4 from D1's tip (or its fix round's), D2 from D4's. `50` is unchanged. `53` and `54` only name this. `0012` stays unmerged on `bars/chunk-2-0920`, so main's registry will read 11 → 13 after tonight; each branch's pin records that.

DRC D1 REISSUED · migration: 0015 · new rule strings: 0 · ESCALATE: 4
