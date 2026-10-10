# https deploy card, fix-round draft (2026-10-09)

## §0 Headline
- Card `208-deploy-https-card.md` and fix report `https-only-fixround-2026-10-09.md` written; every hash re-read.
- Seam gone: `git diff --stat a1b99495 411f85b2 -- . ':(exclude)docs'` prints nothing; `6e1ccd3d` is an ancestor of `a1b99495`.
- 3 decisions: the `fix report` cell fails the launcher's read; card 156 has no `## DEPLOY PROOF`; M5 is not done yet.

## DECISIONS
- ASK DESK: `desk-launch.sh` `fixed_ok` (`:862`) reads the fix report with `git show <branch head>:<path>`, never from main. `reports/https-only-fixround-2026-10-09.md` exists on main only, so the launcher refuses the card. The card carries the prompt's file as written. Re-point the `fix report` cell to `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/https-only-build-2026-10-09.md` (it is on `411f85b2` and ends with the same `BUILT ·` stop line) before launch. [before the deploy launch] Default: re-point the cell; the pointer file stays.
- ASK DESK: card 156 has no `## DEPLOY PROOF` section, so `deploy-card.sh` would write `«FILL` markers. I built 7 markers and 4 smoke reads from the card's rows and its DEPLOY ORDER (the M5 grep before `0`, after `0`); BEFORE counts read on main, AFTER counts read at `a1b99495`. [before the deploy launch] Default: keep them as written.
- ASK DESK: marker 1 (`bind: lan` in `configs/dev/aset.local.yaml`) reads `1` today, so M5 (his step) is pending; the smoke is RED until it runs. [before the merge] Default: M5 first, then the deploy.

## RECORDS
- `git rev-parse --short=8`: `a1b99495`, `411f85b2`, `6e1ccd3d` each print themselves (2026-10-09).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6e1ccd3d a1b99495` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat a1b99495 411f85b2 -- . ':(exclude)docs'` → nothing.
- `grep -c -F "«FILL"` on the card → 1 (the BASE line).
- The fix report's last non-blank line equals the build report's `BUILT · job: https-only-1009 · tip: a1b99495 …` line (regex match, 1 each).
- Marker counts: BEFORE on main: `bind: lan` 1 (card says `0` at deploy time), `https_url` in voice.yaml 0, `isSecureContext` 0, `L80` in aset/config.py 0, host in s2.yaml 0, in probes.py 0, in deploy-smoke.sh 0. AFTER at `a1b99495`: voice.yaml 1, web.py 2, aset/config.py 2, s2.yaml 4, probes.py 2, deploy-smoke.sh 3.
- Files written: the card, the fix report, this report. No other file edited.

HTTPS DEPLOY CARD DRAFTED · decisions: 3
