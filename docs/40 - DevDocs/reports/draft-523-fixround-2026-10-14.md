# draft-523-fixround — 2026-10-14

## §0 Headline
- One row, `FR-T1`, added after `R5` in `prompts/2026-10-13/523-hub-text-card.md`; existing rows and header untouched.
- It rewrites four tests of `tests/ops/test_hub_text_1013.py` to pin only 523's own lines by content, and deletes `test_h1_the_launch_line_and_every_other_line_stand`.
- Red: `HEAD:…/DEPLOY-HUB.md:11` (launch line) differs from `ce548f10:…:11`. Green: builder runs `test_hub_text_1013.py` and `test_hub_lines.py` (unchanged).
- RESTARTS home: `tests/` → none. Nothing was run; reads only.

## DECISIONS
- ASK DESK: delete `test_h1_the_launch_line_and_every_other_line_stand` outright rather than rewrite it (the launch line is already pinned by `tests/ops/test_hub_lines.py`). Default: delete. [2026-10-14]
- ASK DESK: keep `test_h3_the_launcher_still_carries_the_shadow_exception` unchanged (reads `desk-launch.sh`, not a hub line or a commit). Default: unchanged. [2026-10-14]
- ASK DESK: the row's red proof is the diff of two revs, not a test run (no `uv run` on this seat's allow line); the builder's first run is the live red. Default: as written. [2026-10-14]

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `ef0637b6`; `… rev-parse --short=8 3894a878` → `3894a878`.
- `git show 3894a878:tests/ops/test_hub_text_1013.py` read whole: `BASE = "ce548f10"`, `base_text` (git show), `hub_line`, tests h1 (2), h2, h3 (2).
- `git show HEAD:docs/40 - DevDocs/prompts/DEPLOY-HUB.md` read: `claude --bg ` line at `:11`; P1 at `:57` is the old text (the set was reverted, `cdf2233c`).
- `git show ce548f10:…/DEPLOY-HUB.md` read; `git diff -U0 ce548f10 HEAD -- …/DEPLOY-HUB.md` → 15 hunks, `@@ -11 +11 @@` among them (the launch line, `<launchd strings>` added); P1 `:57` not in the diff.
- `git log --oneline ce548f10..HEAD -- …/DEPLOY-HUB.md` → `cdf2233c`, `1bdc32b8`, `3894a878`, `c1fc230d`, `6c3402af`, `01fb7297`.
- `git show HEAD:tests/ops/test_hub_lines.py` read: pins launch lines by content (`hub_line`), no commit or BASE hash.
- `reports/deploy-hub-text-1013.md` last line: `FAILED: smoke (s) — …test_h1_the_launch_line_and_every_other_line_stand red … BASE ce548f10 pinned`.
- Row shape: `prompts/2026-10-13/446-k5-gate-card.md` row `FR1` (lines 32-33, after the last row `R2`) and `CARD.md` read (grep: the fix-round paragraph at `:48`, a long line, not read whole).
- RESTARTS class home: `tests/` → "test/documentation; no resident" (`src/cobalt/jobs/restarts.py:246`, as cited by 446 FR1 and card 523 R5; not re-read here).
- Not proved: the reds/greens by running (no `uv run`); the 15-hunk count is from the diff output read above.

DRAFTED · decisions: 3
