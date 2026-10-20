# draft-cos-probe-fr2b — 2026-10-20

## §0 Headline
- Card drafted: `prompts/2026-10-20/923-cos-probe-fr2b-card.md`, job `cos-probe-fr2b`, BAND HIGH, BASE `be5fc23d` (desk resets).
- Spec = `git diff 27c35e37..dfea631a` over `probe.py`, `test_cos_probe.py`, cos `README.md` (234+, 44−); main holds these three files unchanged since `27c35e37`, so the port is a pure re-application.
- Rows: P1 tests (red on BASE code), P2 code (green), D0 README, E1 equality proof (`git diff dfea631a <tip>` empty on the three files), R1 restarts.
- Marker 4 corrected: before `0`, after `2` (`git grep -c` on `dfea631a` → `2`); markers 1–3 re-proven `1`/`2`/`0` on main.
- Two decisions, both with defaults taken in the card.

## DECISIONS
1. ASK DESK: the spec also adds the old job's build report and `.result` (`reports/cos-probe-fr2-build-2026-10-20.md`, 193+; `.result`, 15+), off main since the revert. Port them too? Default taken: not ported; the card lists them as the docs lines outside E1, and the new build writes its own report. [15:00]
2. ASK DESK: should D0 add a README section of the port's own (`## 2026-10-20 — cos-probe-fr2b`)? Default taken: no; the README stays byte-equal to `dfea631a` so marker 4 reads `2` and E1's diff is empty. [15:00]

## RECORDS
- 14:58:21 `date`; read `prompt 922` whole.
- 14:58 read `prompts/CARD.md` whole; `prompts/2026-10-20/918-cos-probe-realhome-card.md` whole; `reports/deploy-cos-probe-fr2.md` whole (`## Smoke` (d), `## DECISIONS` 1, P6 marker rows).
- 14:58 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `9c21facd`; later → `be5fc23d` (`docs(desk): handoff 759331db, drafter 8ef18696 live`).
- 14:58 `git show HEAD:"docs/40 - DevDocs/prompts/BUILD-HUB.md"` → `:14` the build allow list (no `git apply`, `cherry-pick`, `git mv`); `:16` never typed `rm`, `git checkout`, `git restore`, `git merge`.
- 14:58 `git diff --stat 27c35e37..dfea631a` → 5 files, 442+, 44−; `--numstat` → README 6/0, build report 193/0, `.result` 15/0, `probe.py` 81/30, `test_cos_probe.py` 147/14.
- 14:58 `git diff 27c35e37..dfea631a -- cos/README.md` → two sections appended, `## 2026-10-20 — cos-probe-fr2` and `## 2026-10-20 — cos-probe-fr2 (check)`.
- 14:58 `git grep -c -F "## 2026-10-20 — cos-probe-fr2" dfea631a -- cos/README.md` → `2`.
- 14:58 `grep -c -F` on main's tree: marker 1 `1`, marker 2 `2`, marker 3 `0`, marker 4 `0`.
- 14:59 `git diff --stat 27c35e37 be5fc23d` over the three spec files → nothing; over `src tests configs ops` → nothing.
- 14:59 `git merge-base --is-ancestor dfea631a HEAD` → exit 0. `git log --oneline -8` → `ebb5020c` revert of `7c460d39`.
- 14:59 `git log --oneline 27c35e37..dfea631a` → `7b1427af`, `74169800`, `220eaa70`, `3e406f66`, `dfea631a`.
- 14:59 `git grep -n -F "cos-probe-fr2-build" dfea631a -- src tests` → nothing (no code reads the old build report).
- 14:59 `ls reports/cos-probe-fr2-build-2026-10-20.md` → No such file; `ls reports/cos-probe-fr2-check-2026-10-20.md` → listed. `ls /Users/cobalt/cobalt-wt/` → no `cos-probe-fr2b`; `ls prompts/2026-10-20/` → no `923-`.
- 15:00 read `topics/writing-rules.md` whole.
- 15:00:07 `date`. Wrote the card and this report. Committed nothing.

DRAFTED · decisions: 2
