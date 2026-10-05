JOB: deploy-s3-1005
LADDER: S3-P3 · F14
BRANCH: deploy/s3-1005-attempt2
WORKTREE: deploy-1005-1-attempt2
BASE: main
TIP: 3e40359a 6269f05e 47ec01c5
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-s3-1005-attempt2.md
RULINGS: 2026-10-03 R326, 2026-10-03 R327, 2026-10-05 R368
TAG: deploy-2026-10-05-1-attempt2
MIGRATIONS: none
SET: s3

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `drc/k3-surfaces-1004` | `3e40359a` | `3e40359a` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md` | `held unfixed: 0` and `ready: YES` |
| 2 | `f15/p2-replay-1004` | `437c7299` | `6269f05e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md` | `held unfixed: 0` and `ready: YES` |
| 3 | `ops/cobalt-guard-b-1004` | `47ec01c5` | `47ec01c5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cobalt-guard-b-check-2026-10-04-r3.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "def superseded_stated_ids" /Users/cobalt/cobalt/src/cobalt/drc/store.py` · before `0` · after `1`
- `grep -c -F "def corpus(" /Users/cobalt/cobalt/src/cobalt/cards/predictions.py` · before `0` · after `1`
- `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `3`

## SMOKE READS
- drc-k3 tests · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_drc_k3.py` · exit 0, a count of 1 or more
- f15-p2 replay tests · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_f15_p2_replay.py` · exit 0, a count of 1 or more
- cobalt-guard-b awk fence · `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more

## RECORDS
- G (d2): SKIPPED for this JOB only, by his 2026-10-05 R368 (`cto-2026-10-05.md`; L73 his direct instruction is the override): record `G (d2) — SKIPPED (his R368)` and go on to the gate call; the post-merge D2.4 validate is the check and rolls back on red. No `.env` in the gate (L41, L76). `03d` is not in this deploy.
- drc-k3: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md` last line: CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · suites: offline 3871/0 · with-DB 863/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0
- drc-k3: head `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/k3-surfaces-1004` → `3e40359a`; code tip `3e40359a`
- f15-p2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md` last line: CHECK DONE · job: f15-p2 · pass: 1 · tip: 437c7299 · house A: Grok FINDINGS: 0 (Sol METER) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 20 · ready: YES · decisions: 0 · for Dejan: 0
- f15-p2: head `git -C /Users/cobalt/cobalt rev-parse --short=8 f15/p2-replay-1004` → `6269f05e`; code tip `437c7299`
- cobalt-guard-b: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cobalt-guard-b-check-2026-10-04-r3.md` last line: CHECK DONE · job: cobalt-guard-b · pass: 1 · tip: 47ec01c5 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3782/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: YES · decisions: 1 · for Dejan: 0
- cobalt-guard-b: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cobalt-guard-b-1004` → `47ec01c5`; code tip `47ec01c5`
- FOLLOW-UP CARDS OWED (R326): (2) F15 P2 X11 — the no-trigger row: a card that EXPIRES with its entry never traded through gets no `missed` row (`replay_card` → `no_trigger`, `replay/runner.py:431-432`) and reads `awaiting nightly replay` for good (`reports/f15-p2-build-2026-10-04.md` DECISION 3 on `f15/p2-replay-1004`).
- THE WINDOW (P1 (iv), L73): his ruling row R327 (`cto-2026-10-03.md`, 10-05 06:19 ET, `HIS RULING · APPROVED — pending fold`) is his direct instruction that the S3 set deploys this morning, 2026-10-05, at any hour; it overrules L66 / L43 for THIS deploy, `JOB: deploy-s3-1005`, `SET: s3`, only. Every check of the set derives `RESTARTS: com.cobalt.aset com.cobalt.radar` (guard-b `none`), so window (v) does not hold.
- trial merge of the heads onto main (`57c7502c`), `git -C /Users/cobalt/cobalt merge-tree --write-tree --name-only --no-messages`, git objects only: `main 3e40359a` → clean `6fdc7001`; `main c96b5118` (holds `3e40359a`: `merge-base --is-ancestor 3e40359a c96b5118` exit 0) → clean `08de26af`; `c96b5118 6269f05e` → clean `c02eeec7` and `main 6269f05e` → clean `022d9f19`; `main 47ec01c5` → clean `e78a2a55` and `6269f05e 47ec01c5` → clean `eecf9303`. No conflict. The chain is two-way steps (no commit-tree on this seat); STEP-T is the binding merge.
- MARKERS and SMOKE READS (desk answer to the drafter's ASK 3): before read on the `main` checkout (`grep -c -F` → `0`; `ls` of `reconcile.py` and the three test files → `No such file or directory`); after read in each job's worktree at 06:2x EDT — `store.py` `1` (`drc-k3-1004`), `reconcile.py` listed (`drc-d5-1004`), `predictions.py` `1` (`f15-p2-1004`), `bare-guard.py` `3` (`cobalt-guard-b-1004`); tests `54` / `27` / `32`. The head commit that adds each string: `git log -S` → K3 `49948783`, P2 `735d0344`, guard-b `c74edcd3`; `reconcile.py` added by D5 `3c1f75b8` (`--diff-filter=A`). No other head of the set touches these four files.
- MIGRATIONS `none`: `git -C /Users/cobalt/cobalt diff --stat main 6269f05e -- src/cobalt/db_migrations` → nothing; `main 47ec01c5` → nothing; three-dot `main...<head>` for both → nothing.
- written by hand by the drafter `deploy-s3-draft` at 2026-10-05 06:24 EDT (`date`), in deploy-card.sh's form (the script refuses drc-d5: `held unfixed: 1`), desk row R328.
- D5 (c96b5118) dropped by the desk's R378 (L43): G (c) red, K3-6 on the K3/D5 seam, deploy-s3-1005-attempt2.md; D5's seam fix is a build on card 03 (R376).
