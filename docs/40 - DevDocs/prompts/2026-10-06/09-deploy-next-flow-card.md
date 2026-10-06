JOB: deploy-next-flow-1006
LADDER: OFF-LADDER — workflow set, cto-2026-10-05.md 2026-10-05 R387
BRANCH: deploy/deploy-next-flow-1006
WORKTREE: deploy-next-flow-1006
BASE: main
TIP: 987ab80d
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-next-flow-1006.md
RULINGS: 2026-10-05 R438, 2026-10-05 R412
TAG: deploy-2026-10-06-next-flow
MIGRATIONS: none
SET: workflow2

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/next-flow-1006` | `987ab80d` | `987ab80d` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/next-flow-check-2026-10-06.md` | `held unfixed: 0` and `ready: YES` |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/next-flow-1006`): `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/BUILD-HUB.md`, and the build report `docs/40 - DevDocs/reports/next-flow-build-2026-10-06.md` (the one report commit `30f1dc02`; docs only). The check's fix commit `987ab80d` touches the two hub files only. RESTARTS: none (each file is `docs/**`, DOCS, no resident; check report RESTARTS line `RESTARTS: none`). No `ops/desk/` script, no `tests/` path and no `src/` path is in the diff. Hub-text change: gated merged first (L68).

## MARKERS
- `grep -c -F "THERE IS NO SECOND PASS: both outside houses run in this one session" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`
- `grep -c -F "START HOUSE A AND HOUSE B AT ONCE, two different houses" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`
- `grep -c -F "## PASS 2 — a launch whose message starts" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `1` · after `0`
- `grep -c -F "AFTER A CHECK there is ONE fix round for every finding left" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`
- `grep -c -F "ONE fix round is yours, on this same card" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`
- `grep -c -F "<WORKTREE> all --deploy [--deselect <id>]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`
- `grep -c -F "<WORKTREE> all --deploy [--deselect <id>]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`
- `grep -c -F "grep -n -F \"pass 1: whole (deploy)\" <log>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`
- `grep -c -F "L36 only the two houses this file names, started at once" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`
- `grep -c -F "L36 only the one house of your pass" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `1` · after `0`
- `grep -c -F "every block you and the house wrote" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `1` · after `0`
- `grep -c -F "every block you and both houses wrote" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`

## SMOKE READS
- both houses in one pass (F1) · `grep -c -F "THERE IS NO SECOND PASS: both outside houses run in this one session" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · exit 0, a count of 1 or more
- one fix round (F2) · `grep -c -F "ONE fix round is yours, on this same card" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · exit 0, a count of 1 or more
- deploy gate's pass at build (F3) · `grep -c -F "grep -n -F \"pass 1: whole (deploy)\" <log>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · exit 0, a count of 1 or more
- deploy gate's pass at check (F3) · `grep -c -F "<WORKTREE> all --deploy [--deselect <id>]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · exit 0, a count of 1 or more
- check fix O1 · `grep -c -F "L36 only the two houses this file names, started at once" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · exit 0, a count of 1 or more

## RECORDS
- next-flow: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/next-flow-check-2026-10-06.md` last line: CHECK DONE · job: next-flow · pass: 1 · tip: 987ab80d · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 3932/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 1 · for Dejan: 1 · tokens: 144225
- next-flow: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/next-flow-1006` → `987ab80d` (also the head of `git -C /Users/cobalt/cobalt log --oneline main..ops/next-flow-1006`); code tip `987ab80d` (the check's fix commit); the job card's own TIP header reads `e249bd83` (the build tip); build report commit `30f1dc02` sits between them (docs only).
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- `DEPLOY-HUB.md` is not shipped. No outside house read this set: house A none, overruled 2026-10-02 R47 (the brain's ruling R488); house B none available.
- Open item O7 (check report `## OPEN`, FOR DEJAN): LAWS L67 (LAWS.md:338) still describes the second pass; the desk folds R438 into LAWS at deploy (L58); the job ships no law text.
- AFTER values above were read from the checked-out worktree `/Users/cobalt/cobalt-wt/next-flow-1006` (HEAD `987ab80d`, verified), BEFORE values from main's working tree, at drafting time 2026-10-06; the deploy re-proves each with `git -C /Users/cobalt/cobalt show 987ab80d:<path>`.
- Absent today: `git rev-parse --verify` of `deploy/deploy-next-flow-1006` and of `deploy-2026-10-06-next-flow` both failed; `ls` of `/Users/cobalt/cobalt-wt/deploy-next-flow-1006` and of the REPORT path both failed.
