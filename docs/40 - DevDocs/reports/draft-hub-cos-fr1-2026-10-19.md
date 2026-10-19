## §0 Headline
Card 869 is re-headed in place as port job `hub-cos-restart-fr1`: BASE `5b71dec9`, TIP empty, new branch, worktree and report paths, `BAND: HIGH`.
Row PORT added (3 files from `d59fac71` by Edit/Write; main has not touched any of them since `bcbf08f9`). ORDER line and a scoped CHECK ASKS (P1, then X1-X4 unchanged) added.
Marker 1 in `## DEPLOY PROOF` now reads `before 0 · after 2`. Proved: main 0/0/0, `ops/hub-cos-restart-1019` 2/1/0. Nothing run but reads; nothing committed.

## DECISIONS
- ASK DESK: the old build report `reports/hub-cos-restart-1019-build-2026-10-19.md` is in `git diff --name-only bcbf08f9 d59fac71` but is not ported (it belongs to the old build). Default: not ported, PROOF count is 3 files. [18:20]
- ASK DESK: `git diff --stat bcbf08f9 main -- <3 files>` was empty at drafting; the PORT row says to re-run it at launch and fold any drift into the same row. Default: byte-equal to `d59fac71` for all three. [18:20]

## RECORDS
- 2026-10-19 18:20 EDT (`date`). `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `5b71dec9`.
- Read: prompt 881; card 869 (before and after edit); `prompts/2026-10-19/846-draft-f16-port.md`; `prompts/2026-10-13/468-f21-card.md`.
- `git diff --name-only bcbf08f9 d59fac71` → `DEPLOY-HUB.md`, old build report, `tests/ops/test_hub_cos_restart_1019.py`, `tests/ops/test_hub_deferred_1018.py`.
- `git diff --stat bcbf08f9 main -- <those three>` → empty.
- Marker 1 `com.cobalt.cos: not loaded — skipped`: `git grep -c -F` on main → no output (0); on `ops/hub-cos-restart-1019` → `DEPLOY-HUB.md:2`.
- Marker 2 `com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)`: main → no output (0); branch → `:1`.
- Marker 3 `launchctl kickstart -k gui/501/com.cobalt.cos`: main → no output (0); branch → no output (0).
- Edited only card 869. `file:line` proofs against `git show d59fac71:<file>` / `git show main:<file>` were not needed: the PORT row cites no new line number; the card's R1-R3 cites are unchanged and stay context (builder re-finds by content, BUILD-HUB E3).

DRAFTED · decisions: 2
