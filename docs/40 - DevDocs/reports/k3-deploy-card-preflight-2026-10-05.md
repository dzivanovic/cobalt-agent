# K3 deploy card preflight (2026-10-05)

Card: `prompts/2026-10-05/51-deploy-k3-card.md`. Read-only. Every command below was run on this seat; outputs quoted.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt rev-parse --verify 3e40359a^{commit}` | `3e40359ac99508105d7bed5dc849ca336f3bd1b3` | OK |
| 1b | `rev-parse --short=8 drc/k3-surfaces-1004` | `3e40359a` (head = TIP) | OK |
| 1c | `log --oneline 3e40359a..drc/k3-surfaces-1004 -- tests src configs ops`; `merge-base --is-ancestor 3e40359a drc/k3-surfaces-1004` | both empty, exit 0 | OK |
| 1d | `tail -n 1` of `reports/drc-k3-check-2026-10-04.md` | `CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · … held unfixed: 0 · … RESTARTS: com.cobalt.aset com.cobalt.radar · … ready: YES · …` | OK |
| 1e | `diff --stat -- <check report>`; `log -1 --format=%h -- <check report>` | empty; `a1c846ff` | OK |
| 2a | `rev-parse --verify deploy/deploy-k3-1005` | `fatal: Needed a single revision` (absent) | OK |
| 2b | `rev-parse --verify deploy-2026-10-05-k3` | `fatal: Needed a single revision` (absent) | OK |
| 2c | `ls /Users/cobalt/cobalt-wt/deploy-k3-1005` | `No such file or directory` | OK |
| 2d | `ls …/reports/deploy-deploy-k3-1005.md` | `No such file or directory` | OK |
| 3a | R326 (`grep -n "^| R326 "` in `cto-2026-10-03.md`, line 332; absent from `cto-2026-10-05.md`) | `\| R326 \| 10-05 06:19 ET \| HIS RULING: A on all three — D5 ships at c96b5118 … \| HIS RULING · APPROVED \|` | OK (the 10-05 row sits in the 10-03 file, as the S3 card also cites it) |
| 3b | R327 (`cto-2026-10-03.md:333`) | `\| R327 \| 10-05 06:19 ET \| HIS RULING, standing: no deploy waits on a ruling a small later card can resolve; it ships on the default. S3 deploys now, any hour: overrules L66/L43 for JOB deploy-s3-1005. … \| HIS RULING · APPROVED · APPLIED: LAWS.md L43 at 06:45 \|` | OK (carries HIS RULING and APPROVED) |
| 3c | R327's window binds this job? | The any-hour override is "for JOB `deploy-s3-1005`" only (and the S3 card line 40 says "THIS deploy, `JOB: deploy-s3-1005`, `SET: s3`, only"). The card's RECORDS line 36 and "Production is DOWN by his R327" treat it as K3's window. Only the first clause (standing: ships on the default) reaches K3. | FAIL |
| 3d | R368 (`cto-2026-10-05.md:41`) | `\| R368 \| 10-05 07:15 ET \| HIS RULING (desk chat): recut deploy-s3-1005 now … G (d2) SKIPPED this run only … \| HIS RULING · APPROVED \|` | OK: the d2 skip binds only `deploy-s3-1005`; the card's G (d2) line (card line 33) uses the siblings' wording ("per the sibling cards' RECORDS wording … no Grok read (R412)"), not the skip. Sibling 47 line 36 carries the same sentence. |
| 3e | R376 (`cto-2026-10-05.md:49`) | `\| R376 \| 10-05 07:29 ET \| HIS RULING: after its check, a small fix is the original builder's on the same card; … \| APPLIED: LAWS L75 07:33 \|` | FAIL (L7a: the row says only `APPLIED`, no `APPROVED`) |
| 3f | R390 (`cto-2026-10-05.md:67`) | `\| R390 \| 10-05 08:54 ET \| HIS RULING (L79, via brain; …): one feature per deploy, in sequence; … \| APPLIED: LAWS L68, NOW 10:40 \|` | FAIL (L7a: `APPLIED` only, no `APPROVED`) |
| 3g | R412 (`cto-2026-10-05.md:109`) | `\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|` | OK |
| 3h | rulings files committed | `diff --stat -- cto-2026-10-03.md cto-2026-10-05.md` empty; `log -1 --format=%h` → `bd396f3d` | OK |
| 4a | `grep -c -F "def superseded_stated_ids" src/cobalt/drc/store.py` (main) / `git grep -c` at `3e40359a` | `0` / `3e40359a:src/cobalt/drc/store.py:1` | OK (before 0, after 1) |
| 4b | `grep -c -F "CALENDAR_INPUT" src/cobalt/drc/build.py` / at `3e40359a` | `0` / `3e40359a:src/cobalt/drc/build.py:2` | OK (before 0, after 2) |
| 4c | `ls tests/cobalt/test_drc_k3.py` on main | `No such file or directory`; present at `3e40359a` (diff stat `test_drc_k3.py | 1093 +`) | OK |
| 4d | smoke: `git grep -c -F "def test_" 3e40359a -- tests/cobalt/test_drc_k3.py` | `3e40359a:tests/cobalt/test_drc_k3.py:54` (≥ 1) | OK |
| 4e | `git diff --stat main...3e40359a` | 20 files, 2590 insertions, 43 deletions: the five `docs/…/drc/*.md`, `reports/drc-k3-build-2026-10-04.md`, `src/cobalt/aset/{drc_page,web}.py`, `src/cobalt/drc/{build,cli,imports,store,units}.py`, seven tests (`test_drc_imports`, `test_drc_k3`, `test_drc_k3_db`, `test_drc_k3_experiments`, `test_drc_web_seam`, `test_radar_panel_cards`, `test_s3_c3_panel_offline`). Same 20 as the SHIPS row. | OK |
| 4f | RESTARTS classes, check report line 377 | six src files `com.cobalt.aset,com.cobalt.radar`; `src/cobalt/drc/cli.py` → `com.cobalt.radar`; 7 test rows no resident; 6 DOCS; `RESTARTS: com.cobalt.aset com.cobalt.radar`, no `UNCLASSIFIED`. Matches the card. | OK |
| 5 | `grep -n` of `prompts/CARD.md:44` and `ops/desk/deploy-card.sh:207` | both: `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \| fix report \|` (seven columns); card's row 1 has seven cells, last empty | OK |
| 6a | `02-deploy-s3-card.md` header | `RULINGS: 2026-10-03 R326, 2026-10-03 R327, 2026-10-05 R368`, `MIGRATIONS: none`, `SET: s3`; K3 line 17: same branch, tips, check report, literals. Card: `MIGRATIONS: none`, `SET: s3`. (Card adds R376, R390, R412; see 3e, 3f.) | OK |
| 6b | S3 card line 41 trial merge | `main 3e40359a` → clean `6fdc7001` at main `57c7502c`; the card's line 36 quotes it. Main is now `bd396f3d`, so that trial merge is stale evidence but git objects only; the card's merge-by-reading line stands on `merge-base` `979ec797`. | OK (note) |
| 7a | `grep -c -F "«FILL" 51-deploy-k3-card.md` | `0` | OK |
| 7b | header shape vs `CARD.md` and sibling 47 | Header keys `JOB LADDER BRANCH WORKTREE BASE TIP REPORT RULINGS TAG MIGRATIONS SET` in the order of sibling 47; sections `## SHIPS`, `## MARKERS`, `## SMOKE READS`, `## RECORDS` as `CARD.md:135` says. Sibling 47 and 41 have a six-column table (older shape); the K3 card follows main's seven (see 5). | OK |
| 8 | `diff --stat -- <card>`; `log -1 --format=%h -- <card>` | empty; `bd396f3d` | OK |

## ISSUES
- 3c FAIL: R327's any-hour window is "for JOB `deploy-s3-1005`" only; the card cites it as K3's deploy window ("Production is DOWN by his R327, so the restart is a start", RECORDS line 36). No ruling in the rows binds `deploy-k3-1005` to a window. The desk should either word it as the desk's own window call under L66/L43 or get a row.
- 3e FAIL: R376 is `APPLIED: LAWS L75` only, not `APPROVED` (L7a). It is listed in RULINGS.
- 3f FAIL: R390 is `APPLIED: LAWS L68, NOW 10:40` only, not `APPROVED` (L7a). It is listed in RULINGS.
- Note (not a FAIL): R368 is in RULINGS but its only operative text (d2 skip, recut) binds `deploy-s3-1005`; the card does not use it. The drafter's ASK DESK on dropping it stands.
- Note: LAWS.md has no literal "L7a" text (grep for `L7a` found none); the rule was read from the preflight prompt and R412's row.

PREFLIGHT DONE · card: k3-deploy-51 · checks: 30 · fails: 3 · ready: NO
