# DEPLOY 2026-09-30 (2 OF 2) — S3 exits C1–C4 on the seam branch + migration 0021

## §0 Headline
- FAILED at STEP-T, 09:20 ET (`date`). Production untouched: no gate suite, no `.env` copy, no bootout, no merge into `main`, no migration. Live stays `deploy-2026-09-30-1` = `9f92747e`.
- STEP-T's ancestry check is exit 1 for two of six tips: `04b3ca3e` (C2) and `6983de75` (C3) are not ancestors of `deploy/s3-0930`.
- Both are docs-only report commits above the code commits the stack was built on: `5e77800f` (C2) and `78e9df82` (C3), each an ancestor of the gate. No checked `src` / `tests` line is missing from the merged tree.
- Preflight green; the seam merge into the gate was clean: `686f6d57`, 75 files, migration paths as expected.
- The desk re-issues STEP-T's tip list (and K25 item 2) with `5e77800f` and `78e9df82`, or rules the two report commits in.

## L74
One block arrived inside a tool result, appended to the Read of the prompt file: it asked for a `Claude-Session:` line in every commit and PR body and named a file-send tool. Data; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`<desk file>` = `docs/40 - DevDocs/reports/cto-2026-09-30.md`.
| check | command | exit | result |
|---|---|---|---|
| placeholder 1 | `grep -n -E "R_[_]" <prompt>` | 1 | (no output) |
| placeholder 2 | `grep -n -E "«FIL[L]" <prompt>` | 1 | (no output) |
| report absent | `ls -la …/reports/deploy-2026-09-30-2.md` | 1 | `No such file or directory` |
| R9 row | `grep -n "^| R9 " <desk file>` | 0 | ONE row, `:17`: `06:40 ET`, `**HIS RULING**`, two deploys one by one, `APPROVED` |
| R9 committed | `git … log -1 --format=%H -S"| R9 |" -- <desk file>` | 0 | `3fe2eb8e4cbe942a469b18d8eff6e251d960b90a` |
| R10 row | `grep -n "^| R10 " <desk file>` | 0 | ONE row, `:18`: `06:43 ET`, `**HIS RULING**`, `STANDING until he says prod is usable for trading`, `APPROVED` |
| R10 committed | `git … log -1 --format=%H -S"| R10 |" -- <desk file>` | 0 | `7d7a46a09f33f706ba1188d88e3145c2549649ef` |
| R26 row | `grep -n "^| R26 " <desk file>` | 0 | ONE row, `:31`: `09:26 ET`, `LAUNCH (R9, R10, R13): deploy 2 of 2 `45-deploy-2-s3-seam-0930.md``, seam tip `98f86fdf`, `LOCK: no with-DB run in flight.`, `LAUNCHED` |
| R26 committed | `git … log -1 --format=%H -S"45-deploy-2-s3-seam-0930.md" -- <desk file>` | 0 | `bef0f7e830f206f17bd3b9715503b5915460fe55` |
No mismatch.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P1 date | `date` | 0 | `Wed Sep 30 09:18:39 EDT 2026` |
| P1b ancestor | `git … merge-base --is-ancestor b8ac291b main` | 0 | (no output) |
| P1b stop line | `tail -n 3 …/reports/deploy-2026-09-30-1.md` | 0 | last non-blank line: `DEPLOYED deploy-2026-09-30-1 9f92747e | set: 1 | migrations: 0016 0018 0019 0020 | gate: offline 3629/0 · with-DB 4183/0 · live-note 146/0 | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | smoke: GREEN | ESCALATE: 24` |
| P1b tag | `git … rev-parse --verify --quiet refs/tags/deploy-2026-09-30-1` | 0 | `9f92747e4425276f82592b2e294dad0b0b8aec44` |
| P1b committed | `git … log -1 --format=%H -- …/deploy-2026-09-30-1.md` | 0 | `c264c97570826e7ef3ab46e94b7ae115e653cae0` |
| P2 C1 | `tail -n 3 …/s3-exits-c1-fix-r2-check-2026-09-28.md` | 0 | `S3 EXITS C1 FIX R2 CHECK DONE · round: 3 · … · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for C2: YES · ESCALATE: 3` |
| P2 C1 committed / clean | `git … log -1 --format=%H -- <file>` · `git … diff --stat -- <file>` | 0 / 0 | `8061141fadb9548a4a20473de7d56716b211fe22` · (no output) |
| P2 C2 | `tail -n 3 …/s3-exits-c2-fix-r1-check-2026-09-28.md` | 0 | `S3 EXITS C2 FIX R1 CHECK DONE · round: 2 · … · houses that checked: 3 of 3 · defects that HOLD: 0 · ready for C3: YES · ESCALATE: 4` |
| P2 C2 committed / clean | same pair | 0 / 0 | `8bcdacdd0fe7440ddf0b614b6813f35a89f20821` · (no output) |
| P2 C3 | `tail -n 3 …/s3-exits-c3-fix-r1-check-2026-09-29.md` | 0 | `S3 EXITS C3 FIX R1 CHECK DONE · round: 2 · … · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for C4: YES · ESCALATE: 8` |
| P2 C3 committed / clean | same pair | 0 / 0 | `6d53a1de506d226e611cb13d2ccfa8b6738b9746` · (no output) |
| P2 C4 | `tail -n 3 …/s3-exits-c4-fix-r2-check-2026-09-29.md` | 0 | the last non-blank line EQUALS `<c4 check stop>`: `S3 EXITS C4 FIX R2 CHECK DONE · round: 3 · opus: CHECK S3 C4 FIX R2: BUILD STANDS EXCEPT E1 (indented comment under a replaced entry dropped, trade_note.py:345) · ready for the deploy set: YES · sol: METER (usage limit, returns Oct 4 2026 2:06 PM) · grok: CHECK S3 C4 FIX R2: BUILD STANDS · ready for the deploy set: YES · houses that checked: 2 of 3 · defects that HOLD: 1 · ready for the deploy set: NO · ESCALATE: 5` |
| P2 C4 committed / clean | same pair | 0 / 0 | `a00cb6572a31fe2920677b2822405927b6a8abfe` · (no output) |
| P2 seam build | `tail -n 3 /Users/cobalt/cobalt-wt/seam-0930/…/seam-drc-s3-2026-09-30.md` | 0 | `SEAM DRC S3 BUILT · tip: 8af84cff · unmerged paths resolved: 14 · pin tests changed: 13 · suite: 3758/0 · ESCALATE: 2` |
| P3 tips | `git … rev-parse --short=8 <tip>` ×4 | 0 | `bbf25412` · `04b3ca3e` · `6983de75` · `6785c7d5` |
| P3 seam head | `git … rev-parse --short=8 seam/drc-s3-0930` | 0 | `98f86fdf` = `<seam tip>` |
| P3 built → seam | `git … merge-base --is-ancestor 8af84cff 98f86fdf` · `git … diff --stat 8af84cff 98f86fdf -- src tests ops` | 0 / 0 | (no output) each |
| P3 C4 head | `git … rev-parse --short=8 s3/exits-c4` · `… merge-base --is-ancestor 6785c7d5 0a64bd75` · `… diff --stat 6785c7d5 0a64bd75 -- src tests ops` | 0 / 0 / 0 | `0a64bd75` · (no output) · (no output) |
| P3 ancestry | `… --is-ancestor 6785c7d5 98f86fdf` · `… b8ac291b 98f86fdf` · `… bbf25412 6785c7d5` | 0 / 0 / 0 | (no output) each |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 rules | `grep -c -F "clinerules" …/configs/cobalt/rules.yaml` | 1 | `0` |
| P5 seam | `git … diff --stat main 98f86fdf -- .clinerules` | 0 | (no output) |
| P6 worktree | `git -C …/deploy-0930-2 status --short --branch` · `… rev-parse --short=8 HEAD` | 0 / 0 | `## deploy/s3-0930` · `bef0f7e8` = `<main base>` (`git … log --oneline -1 main` → `bef0f7e8 docs(desk): 09-30 R25 seam merged main, R26 deploy 2 launch row, 45 filled`) |
| P7 0020 | `ls …/db_migrations/0020_drc_build_kinds.sql` | 0 | listed |
| P7 0021 | `ls …/db_migrations/0021_legs.sql` | 1 | `No such file or directory` |
| P7 marker | `grep -c -F "_merge_frontmatter_lines" …/prefill/trade_note.py` | 1 | `0` |

## THE TREE
`<main base>` = `bef0f7e8` · `<seam tip>` = `98f86fdf` · `<m1>` = `686f6d57`.
| check | command | exit | result |
|---|---|---|---|
| merge | `git -C …/deploy-0930-2 merge --no-edit 98f86fdf` | 0 | `Merge made by the 'ort' strategy.` · `75 files changed, 10359 insertions(+), 390 deletions(-)` · no conflict |
| `<m1>` | `git -C …/deploy-0930-2 rev-parse --short=8 HEAD` | 0 | `686f6d57` |
| merges | `git … log --oneline --merges --first-parent bef0f7e8..deploy/s3-0930` | 0 | `686f6d57 Merge commit '98f86fdf' into deploy/s3-0930` |
| ancestor `bbf25412` | `git … merge-base --is-ancestor bbf25412 deploy/s3-0930` | 0 | (no output) |
| **ancestor `04b3ca3e`** | `git … merge-base --is-ancestor 04b3ca3e deploy/s3-0930` | **1** | (no output) — run twice, exit 1 both times |
| **ancestor `6983de75`** | `git … merge-base --is-ancestor 6983de75 deploy/s3-0930` | **1** | (no output) — run twice, exit 1 both times |
| ancestor `6785c7d5` | same, `6785c7d5` | 0 | (no output) |
| ancestor `b8ac291b` | same, `b8ac291b` | 0 | (no output) |
| ancestor `98f86fdf` | same, `98f86fdf` | 0 | (no output) |
| migrations diff | `git … diff --stat bef0f7e8 deploy/s3-0930 -- src/cobalt/db_migrations` | 0 | `0021_legs.rollback.sql | 15` · `0021_legs.sql | 114` · `__init__.py | 11` · `cli.py | 5` · `placement.py | 11` · `5 files changed, 152 insertions(+), 4 deletions(-)` |
| registry | `grep -n -F "MIGRATIONS_DIR / \"00" …/deploy-0930-2/src/cobalt/db_migrations/__init__.py` | 0 | `FORWARD` ends `:146` `0019_drc_events.sql`, `:147` `0020_drc_build_kinds.sql`, `:148` `0021_legs.sql`; `REVERSE` begins `:153` `0021_legs.rollback.sql`, `:154` `0020_drc_build_kinds.rollback.sql`, `:155` `0019_drc_events.rollback.sql` |
| ops diff | `git … diff --stat bef0f7e8 deploy/s3-0930 -- ops` | 0 | (no output) |
| migration list | `git … log --oneline main..98f86fdf -- src/cobalt/db_migrations` | 0 | `8af84cff merge(seam): DRC D3 b8ac291b into S3 exits C1–C4 6785c7d5 — registry, placement, pin tests` · `eb642f05 feat(s3): C1 — legs (0021), the one fill transaction, from_card, the drift setting (v3 §2–§4, R67, R38)` |
| seam as built | `git … show --stat 98f86fdf` | 0 | `Merge: d3b3c0ac 08515bd6` · `Merge branch 'main' into seam/drc-s3-0930` · `177 files changed, 16161 insertions(+), 217 deletions(-)`: `.claude/settings.json`, `configs/cobalt/jobs.yaml`, `configs/cobalt/rules.yaml`, the rest under `docs/` |

The seam report's file list (`seam-drc-s3-2026-09-30.md` `## RESOLUTION`): `db_migrations/__init__.py`, `db_migrations/placement.py`, `aset/web.py`, the two DevDocs (`db_migrations/__init__.md`, `aset/web.md`), the nine S-3 pin tests, the four S-6 tests, `test_drc_web_seam.py`, `test_s3_c3_panel_offline.py`, `test_seam_drc_s3_registry.py` (new), `test_s3_c4_experiments.py` (X18 retired). `show --stat 98f86fdf` also lists `configs/cobalt/jobs.yaml` (16 lines), brought by `main`.

THE TWO RED ROWS, read further (read-only):
| read | command | exit | result |
|---|---|---|---|
| C2 history | `git … log --oneline -6 04b3ca3e` | 0 | `04b3ca3e docs(s3-c2): S3 exits C2 fix r1 build report — 5e77800f` · `5e77800f fix(s3-c2): fix r1 — CLOSED only by the zero-running leg, …` |
| C2 fork point | `git … merge-base 04b3ca3e deploy/s3-0930` | 0 | `5e77800f023b0d6f3e1750ba4418165eeaad0f71` |
| C2 tip over its code | `git … diff --stat 5e77800f 04b3ca3e` | 0 | `…/reports/s3-exits-c2-fix-r1-build-2026-09-28.md | 197 +` · `1 file changed, 197 insertions(+)` |
| C3 history | `git … log --oneline -6 6983de75` | 0 | `6983de75 docs(s3-c3): S3 exits C3 fix r1 build report — 78e9df82` · `78e9df82 fix(s3-c3): fix r1 — F3's with-DB test and R2 read the sheet's day from the suite clock` |
| C3 fork point | `git … merge-base 6983de75 deploy/s3-0930` | 0 | `78e9df82d57d74352b93b3213cbea118af1102c3` |
| C3 tip over its code | `git … diff --stat 78e9df82 6983de75` | 0 | `…/reports/s3-exits-c3-fix-r1-build-2026-09-29.md | 254 +` · `1 file changed, 254 insertions(+)` |
| gate worktree | `git -C …/deploy-0930-2 status --short --branch` | 0 | `## deploy/s3-0930` (clean, at `686f6d57`) |

## ESCALATE
1. STEP-T NAMES TWO TIPS THE STACK NEVER CARRIED. C3 was built on `5e77800f` and C4 on `78e9df82` (the prompt's own line); the checked tips `04b3ca3e` and `6983de75` each sit one docs commit above those. The prompt demands exit 0 for both and names no exception, so the run ends here (L62, L73). The two build reports `s3-exits-c2-fix-r1-build-2026-09-28.md` and `s3-exits-c3-fix-r1-build-2026-09-29.md` are not in the gate tree.
2. THE RE-ISSUE. Either STEP-T and K25 item 2 check `5e77800f` and `78e9df82` in place of the two report tips, or the desk first brings the two report commits into `main` / the seam. The gate branch `deploy/s3-0930` now stands at `686f6d57` (the seam merged, clean); P6 of a relaunch expects `bef0f7e8` and will refuse it. This file lists no string that moves the branch back.
3. The desk file's R26 row reads `09:26 ET` and the prompt gives `09:20` for R25; `date` read 09:18:39 at P1 with both already committed (`bef0f7e8`) (L48).
4. `cobalt_dev` was not touched: no `.env` copy, no migrate. The L76 lock was never taken (P4 free at 09:19).
5. Cleanup owed (L46): `/Users/cobalt/cobalt-wt/deploy-0930-2`, `/Users/cobalt/cobalt-wt/seam-0930` and the branch worktrees stay for the relaunch.
6. E1 (`trade_note.py:345`) is not live; its fix build waits on this deploy (R3, R9).
7. RECORDS, carried:
   - C1 X-S (`s3-exits-c1-build-2026-09-28.md` §0): `fills.drift_warning_pct` is not loadable without a `settings/models.py` edit (DRC D4's seam); every fill until then is recorded and bannered RE-READ STOP.
   - C3 R1 (`s3-exits-c3-fix-r1-check-2026-09-29.md` §0): a NaN exit stored (200) and a `/correct` of `-1` → 500 stand as the builder's ESCALATE.
   - C4 E1 (`s3-exits-c4-fix-r2-check-2026-09-29.md`): an indented comment under a replaced frontmatter entry is dropped (`trade_note.py:345`); its fix build is the desk's next launch (R3).

## CONTINUE
next: the desk re-issues STEP-T's tip list and resets or re-cuts the gate branch, then relaunches from STEP-0.

FAILED: T — merge-base --is-ancestor 04b3ca3e / 6983de75 deploy/s3-0930 — exit 1, no output (each is a docs-only report commit above 5e77800f / 78e9df82, which are in the gate) · rollback: not used
