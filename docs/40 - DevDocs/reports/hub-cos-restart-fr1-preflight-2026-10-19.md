# hub-cos-restart-fr1 preflight — 2026-10-19 (read-only; seat hub-cos-fr1-preflight)

Card: `prompts/2026-10-19/869-hub-cos-restart-card.md`. Reads only; nothing run but `git` reads and `ls`/`grep`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --name-only bcbf08f9 d59fac71` | DEPLOY-HUB.md, old build report `reports/hub-cos-restart-1019-build-2026-10-19.md`, `tests/ops/test_hub_cos_restart_1019.py`, `tests/ops/test_hub_deferred_1018.py`. Card's PORT list = the 3 non-report files | OK |
| 2 | `git diff --stat bcbf08f9 main -- <3 files>` | empty (no drift) | OK |
| 3 | `git diff --stat main d59fac71 -- <3 files>` | DEPLOY-HUB 7 lines, new test 93, test_hub_deferred 4: the net port change is non-empty and the old report is the only file left out | OK |
| 4 | `git show main:DEPLOY-HUB.md` cites: `:93` `- GATE: exit 0 … within \`com.cobalt.agent com.cobalt.aset com.cobalt.radar\``; `:94` `- THE SET DRIVES THE REST`; `:122` D1 holds `<radar pid>`; `:154` `- (f) \`COBALT_ENV=production uv run cobalt validate\`` | all four found at the card's line numbers; `:93` `Anything else (…)` sentence present | OK |
| 5 | `git show main:tests/ops/test_hub_deferred_1018.py` cites | `:17` THREE, `:74` COS control, `:75`, `:105` `assert COS not in launch` at the card's lines | OK |
| 6 | `git show d59fac71:tests/ops/test_hub_deferred_1018.py` | `THREE` holds the four labels (`:17`) | OK |
| 7 | each PROOF line names its check | PORT row: `git diff d59fac71 <port tip> -- <file>` prints nothing, per file; stop-line count 3 of 3 | OK |
| 8 | `grep «FILL` in card at HEAD | 0 | OK |
| 9 | header: `BASE 5b71dec9`; `git diff --name-only 5b71dec9 main` | 469 card, 869 card, 882 prompt, cto report, draft report — all docs. Main is now `c68efd65`, docs-only drift | OK |
| 10 | header `BAND: HIGH`, `JOB: hub-cos-restart-fr1`, `BRANCH: ops/hub-cos-restart-fr1`, `WORKTREE: hub-cos-restart-fr1`; `rev-parse --verify ops/hub-cos-restart-fr1` | header values as named; branch does not exist yet (exit 1) | OK |
| 11 | `^(CHECK REPORT\|TIP):$` count at HEAD | 2 (both empty) | OK |
| 12 | marker 1 `com.cobalt.cos: not loaded — skipped`, `git grep -c -F` | `main` no output (0); `ops/hub-cos-restart-1019` `…DEPLOY-HUB.md:2`; `d59fac71` `:2`. Card: before 0 · after 2 | OK |
| 13 | marker 2 `com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)` | `main` 0; branch `:1`; `d59fac71` `:1`. Card: before 0 · after 1 | OK |
| 14 | marker 3 `launchctl kickstart -k gui/501/com.cobalt.cos` | `main` 0; branch 0; `d59fac71` 0. Card: before 0 · after 0 | OK |
| 15 | `git diff d59fac71 ops/hub-cos-restart-1019 --stat -- DEPLOY-HUB.md tests/ops` | empty: the old branch head equals the code tip on these files, so checks 12-14 prove the post-port text | OK |
| 16 | K10 RESTARTS: header `RESTARTS: none`; `docs/…/DEPLOY-HUB.md` → docs, `tests/ops/*.py` → tests; no `src/`, no `ops/` file | no resident class; builder's `cobalt jobs restarts` line is the record | OK |
| 17 | open-card overlap: F16 867 (`deploy/f16-close-fr2`), 469, 877 (`cos-probe-1019`, K2) — grep for `DEPLOY-HUB.md`/the two tests | none of the three names a shared file. F5 731 FIX1 names `DEPLOY-HUB.md` (STEP-G (c) `:104` only) and `ops/desk/gate-lists.md` | OK (NOTE 1) |
| 18 | CHECK ASKS | P1, X1, X2, X3, X4 all present (`:49-53`) | OK |
| 19 | drafter decision 1 (old build report not ported, PROOF count 3) | judged below: agree | OK |
| 20 | drafter decision 2 (byte-equal default; re-run stat at launch) | judged below: agree, and re-run here is empty | OK |
| 21 | `git diff HEAD -- 869-hub-cos-restart-card.md`; `git log` on it | empty; last commit `c68efd65` | OK |
| 22 | `git log --merges 5b71dec9..main` | empty | OK |

## ISSUES

- NOTE 1: F5 731 FIX1 and this card both edit `DEPLOY-HUB.md`. Disjoint hunks (`:104` vs `:93`/new line/`:122`/`:154`), so no textual overlap, but whichever deploys second is cut on the other's merged text (the port copies byte-for-byte from `d59fac71`, so it must stay a hunk-wise port if F5 FIX1 merges first; the PORT row already says what to do on drift).
- NOTE 2: X3 still reads `git diff main...ops/hub-cos-restart-1019 -- …`; on the port the branch is `ops/hub-cos-restart-fr1`. The checker should substitute it. Same for X1's `<BASE>`. Not a blocker.
- NOTE 3: card header `BASE: 5b71dec9` is behind `main` `c68efd65`; docs-only drift, fine per the brief.
- Decision 1 (old build report not ported): agree. It describes the old build, and its path is under the old job name.
- Decision 2 (byte-equal default, re-run stat at launch): agree. I re-ran it (check 2): empty.
- Marker fix: marker 1 `after 2` is proven (the `- NOT LOADED` line and D1's clause); this is what failed deploy 879 at 4.7 (d).
- Blocks the card's own build: nothing in the text. The desk's launch (`desk-launch.sh build`) and a fresh worktree `hub-cos-restart-fr1` from `main` are all it needs; the old worktree is not touched.

PREFLIGHT DONE · card: hub-cos-restart-fr1 · checks: 22 · fails: 0 · ready: YES
