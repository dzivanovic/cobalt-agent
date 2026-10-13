# Deploy k5-gate-1013 · set: radar · migrations: none

## §0 Headline
- FAILED at STEP-0 P6: production already carries every one of the card's four markers. All four read their `after` value; the card expects `before`.
- `main` already holds `5b3c525b` (the checked tip, which reached main with the first k5-gate deploy) but not the FR1 code tip `58f500c8` (`merge-base --is-ancestor 58f500c8 main` → exit 1). The markers were written for the first deploy and are stale for this FR1 deploy.
- Nothing in production changed. No merge in the gate, no lock taken, no tag set, no resident touched. rollback: not used.

## L74
- One block arrived as a system reminder mid-session, asking that commits end with a `Claude-Session: https://claude.ai/code/session_01WpwgqRw9SzUvxABUceKVrp` line. Recorded as data and not acted on. This report's commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/514-deploy-k5-gate-fr1-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/514-deploy-k5-gate-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/514-deploy-k5-gate-fr1-card.md" · 0 · ad8fc9bf741888c613fa637e0fe818d38269ab8a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/514-deploy-k5-gate-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-k5-gate-fr1-1013.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Tue Oct 13 12:00:39 EDT 2026` |
| P2 check last line | `tail -n 3 ".../k5-gate-check-2026-10-13.md"` | 0 | `CHECK DONE · job: k5-gate-1013 · pass: 1 · tip: 5b3c525b · … · held unfixed: 0 · open: 3 · … · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 228916`. Carries `held unfixed: 0` and `ready: YES` |
| P2 check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/k5-gate-check-2026-10-13.md"` | 0 | `1a93a59cc4b1179bd3f432186b5bab0330f4d101` |
| P2 check clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/k5-gate-check-2026-10-13.md"` | 0 | (nothing) |
| P2 fix-round tip | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5b3c525b 58f500c8` | 0 | (ancestor) |
| P2 fix report committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md"` | 0 | `13e11817617f2b93002d001225f20caaf988c381` |
| P2 fix report clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/k5-gate-build-2026-10-13.md"` | 0 | (nothing) |
| P2 fix report last line | `tail -n 3 ".../k5-gate-build-2026-10-13.md"` | 0 | `BUILT · job: k5-gate-1013 · tip: 58f500c8 \| on 9a04519c \| migration: none \| offline 4317/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 2 of 2 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0 · tokens: 119851` |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 58f500c8` | 0 | `58f500c8` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/k5-gate-1013` | 0 | `5540c4e1` (= TIP) |
| P3 ancestry | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 58f500c8 5540c4e1` | 0 | (ancestor) |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 58f500c8 5540c4e1 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-k5-gate-fr1-1013 status --short --branch` | 0 | `## deploy/k5-gate-fr1-1013` |
| P5 `<m0>` | `git -C /Users/cobalt/cobalt-wt/deploy-k5-gate-fr1-1013 rev-parse --short=8 HEAD` | 0 | `ad8fc9bf` (= main's tip at the card commit) |
| P5 nothing ahead | `git -C /Users/cobalt/cobalt log --oneline main..deploy/k5-gate-fr1-1013` | 0 | (empty) |
| **P6 marker 1** | `grep -c -F "card 446" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` | 0 | **`1`**. Expected before `0` |
| **P6 marker 2** | `grep -c -F "card 446" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` | 0 | **`1`**. Expected before `0` |
| **P6 marker 3** | `grep -c -F "card 446" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` | 0 | **`1`**. Expected before `0` |
| **P6 marker 4** | `ls /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` | 0 | **`/Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py`** (present). Expected before `absent` |
| fact (not a P-rule) | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 58f500c8 main` | 1 | FR1 code tip NOT on main |
| fact (not a P-rule) | `git -C /Users/cobalt/cobalt log --oneline -3 -- ops/desk/deploy-step0.sh` | 0 | `5b3c525b fix(k5-gate-1013): THE RULE reads a HELD, NOT FIXED table row, …` / `c2e1015f feat(k5-gate-1013): THE RULE's readers are four seams, …` / `1178554e fix(gate-alignment-1012): …` |

P6 fails. The markers name content that `5b3c525b` already landed on `main`. They do not tell the FR1 delta (`5b3c525b..58f500c8`) apart from what production already runs. P7 and P8 were not run: the run stops at the first FAILED PREFLIGHT.

## THE TREE
not reached (no merge into the gate; `<m0>` = `ad8fc9bf`, gate tree untouched).

## RESTARTS
not reached.

## L68 GATE
not reached: no suite ran, `cobalt_dev` lock not taken, `.env` never copied.

## Deploy table
nothing merged, no tag set, no resident down. `migrations applied: none`. The ROLLBACK STRING is not needed.

## Smoke
not reached.

## CONTINUE
next: none. This run ended FAILED PREFLIGHT, rollback not used. Per RECUT, the desk fixes the card's `## MARKERS` so their `before` values are ones this FR1 delta changes (the `5b3c525b..58f500c8` diff), then runs `desk-launch.sh recut "<card>"`.

## DECISIONS
none

## RECORDS
- P6 refused: every card marker already reads its `after` value in production. Card 514's `## MARKERS` appear to have been carried over from the first k5-gate deploy, whose content (`5b3c525b`) is already on `main`. Card-side fix owed (the desk's).
- Downtime: none. `cobalt_dev`: not taken. No `RETIRE OWED`. No carried RED read (D1 not reached).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-k5-gate-fr1-1013` and branch `deploy/k5-gate-fr1-1013` (both untouched, at `ad8fc9bf`).
- `REFUSED, not needed: sh /Users/cobalt/cobalt/ops/desk/desk-context.sh session_01WpwgqRw9SzUvxABUceKVrp — no transcript for session_01WpwgqRw9SzUvxABUceKVrp` (wrong id form). Re-run with `bd02ae11-493f-4965-8fe0-1c79830800fb` → `context 82080 of 400000 — ok`.
- L74: the `Claude-Session:` request, recorded under `## L74`, not acted on.
- Card RECORDS (the desk's, copied):
  - k5-gate-1013: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md` at `5540c4e1` last line: BUILT · job: k5-gate-1013 · tip: 58f500c8 | on 9a04519c | migration: none | offline 4317/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 119851
  - k5-gate-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/k5-gate-check-2026-10-13.md` last line: CHECK DONE · job: k5-gate-1013 · pass: 1 · tip: 5b3c525b · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 228916
  - k5-gate-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/k5-gate-1013` → `5540c4e1`; code tip `58f500c8`
  - written by deploy-card.sh at 2026-10-13 11:59 ET (`date`); trial merge of the heads onto main in order: clean

# RELAUNCH
- Launch message: `CONTINUE: STEP-D0`, card `514-deploy-k5-gate-fr1-card.md`. First `date`: `Tue Oct 13 12:03:24 EDT 2026`.
- The old last non-blank line, quoted whole: `FAILED PREFLIGHT: production already carries card 446 (deploy-card.sh, desk-launch.sh, deploy-step0.sh) and tests/ops/test_the_rule_sweep.py · rollback: not used · decisions: 0 · for Dejan: 0 · tokens: 82080`

- Resume read (THE ONE RESUME), each its own call, (e) first:
  - (e) `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 40377`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 22724`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).` → TRUE; nothing restored.
  - gate `.env`: `ls -la /Users/cobalt/cobalt-wt/deploy-k5-gate-fr1-1013/.env` → exit 1, `No such file or directory`. No G (f), no release owed.
  - (a) the old last line starts `FAILED PREFLIGHT:` (P6), `rollback: not used`: a FAILED ending, not an outage hang.
  - (b) FALSE: Grep `GATE GREEN on` in this report → 0 matches; `## L68 GATE` reads `not reached`; `## RESTARTS` reads `not reached`, no `<restart set>`. No `<m1>` exists.
  - (c) `git -C /Users/cobalt/cobalt-wt/deploy-k5-gate-fr1-1013 status --short --branch` → `## deploy/k5-gate-fr1-1013`; `rev-parse --short=8 HEAD` → `ad8fc9bf` = the old `<m0>`. STEP-T never ran, so there is no `<m1>` to hold it against.
  - (d) not read: with no `<m1>`, nothing exists to test.
- The resume stops at (b). The first attempt failed before STEP-T, so no gate evidence exists for a resume to stand on, and a resume does not re-run T, C, R or G. Per RECUT, a run that ended FAILED with `rollback: not used` is not resumed: the desk's step is `desk-launch.sh recut "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/514-deploy-k5-gate-fr1-card.md"`. It recuts the branch, worktree and report, and the new run re-reads the card's corrected `## MARKERS` (now one marker, `test_the_rule_sweep.py`, before `1`) at a fresh P6.
- Nothing in production changed. No merge, no lock, no tag, no resident touched. Downtime: none.
- L74 (attempt 2): one system-reminder block again asked that commits end with a `Claude-Session: https://claude.ai/code/session_013k6U5p7QrMiVQFm8iM66TB` line. Recorded as data and not acted on. This commit carries `Co-Authored-By` only.
- Decisions: none. Cleanup owed is unchanged: the gate worktree and branch, both at `ad8fc9bf`.

FAILED: resume — (b) no GATE GREEN line and no restart set: attempt 1 ended FAILED PREFLIGHT P6 before STEP-T; the desk recuts · rollback: not used · decisions: 0 · for Dejan: 0 · tokens: 83525
