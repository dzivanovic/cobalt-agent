JOB: https-only-1009
LADDER: OFF-LADDER — reports/cto-2026-10-09-words.md 2026-10-09 R718
BRANCH: deploy/deploy-2026-10-09-https-only-attempt2
WORKTREE: deploy-https-only-1009-attempt2
BASE: main
TIP: 16559ba4
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-https-only-1009-attempt2.md
RULINGS: 2026-10-09 R718
TAG: deploy-2026-10-09-https-only-attempt2
MIGRATIONS: none
SET: none
TICKERS: none
RESTARTS: com.cobalt.aset com.cobalt.radar (the check's stop line, re-read from the build report's stop line). The deploy runs when READY at any hour (L43, R389). DEPLOY ORDER: M5 (`bind: loopback` in `configs/dev/aset.local.yaml` and the aset kickstart) lands before the merge, or aset crash-loops under KeepAlive.

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/https-only-1009` | `a1b99495` | `16559ba4` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/https-only-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/https-only-build-2026-10-09.md` |

## MARKERS
- `grep -c -F "bind: lan" /Users/cobalt/cobalt/configs/dev/aset.local.yaml` · before `0` · after `0` (M5 done: production binds loopback; DEPLOY ORDER)
- `grep -c -F "https_url" /Users/cobalt/cobalt/configs/cobalt/voice.yaml` · before `0` · after `1` (the https address has its config home)
- `grep -c -F "isSecureContext" /Users/cobalt/cobalt/src/cobalt/voice/web.py` · before `0` · after `2` (the insecure-page test in start() and on load)
- `grep -c -F "L80" /Users/cobalt/cobalt/src/cobalt/aset/config.py` · before `0` · after `2` (lan bind refused, naming L80)
- `grep -c -F "cobalt.taild24291.ts.net" /Users/cobalt/cobalt/configs/cobalt/smoke/s2.yaml` · before `0` · after `4` (the four K4 URLs)
- `grep -c -F "cobalt.taild24291.ts.net" /Users/cobalt/cobalt/src/cobalt/heartbeat/probes.py` · before `0` · after `2` (the two probe defaults)
- `grep -c -F "cobalt.taild24291.ts.net" /Users/cobalt/cobalt/ops/desk/deploy-smoke.sh` · before `0` · after `3` (the curl shape, its case and its refusal text)

## SMOKE READS
- the https address in voice config · `grep -c -F "https_url" /Users/cobalt/cobalt/configs/cobalt/voice.yaml` · exit 0, a count of 1 or more
- the secure-context test in the voice widget · `grep -c -F "isSecureContext" /Users/cobalt/cobalt/src/cobalt/voice/web.py` · exit 0, a count of 1 or more
- aset health over https · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/api/health` · exit 0, `200`
- the radar page over https · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` · exit 0, `200`

## RECORDS
- https-only-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/https-only-check-2026-10-09.md` last line: CHECK DONE · job: https-only-1009 · pass: 1 · tip: 6e1ccd3d · house A: Sol FINDINGS: 4 · findings: 10 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 2 · suites: offline 4061/0 · with-DB 4948/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 180198
- https-only-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/https-only-1009` → `16559ba4`; code tip `a1b99495`; check tip `6e1ccd3d` is an ancestor of `a1b99495` (`git -C /Users/cobalt/cobalt merge-base --is-ancestor 6e1ccd3d a1b99495` → exit 0); `git -C /Users/cobalt/cobalt diff --stat a1b99495 16559ba4 -- . ':(exclude)docs'` prints nothing (the head adds docs only).
- FIX ROUND (his R376, L75; the brain's ruling: no new check): the check passed at `6e1ccd3d`; the build's first attempt was gated on `4dfe6114`; the fix round `a1b99495` moved the card's hunks off the lines voice fix 193 (main `2041a53f`) changed, after S4-P1. The fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/https-only-build-2026-10-09.md` (read at `16559ba4`) ends with the branch report's `BUILT · job: https-only-1009 · tip: a1b99495 …` stop line, byte for byte. No deploy attempt of this job has run: no deploy report exists.
- RULINGS `2026-10-09 R718` (card 156, L80 HTTPS only). The deploy runs when READY at any hour (L43, R389).
- Shipped files, `git -C /Users/cobalt/cobalt diff --stat main...16559ba4` (22 files, 635 insertions, 86 deletions): `configs/cobalt/smoke/s2.yaml`, `configs/cobalt/voice.yaml`, `configs/dev/aset.yaml`, `ops/desk/deploy-smoke.sh`, `src/cobalt/aset/__main__.py`, `src/cobalt/aset/config.py`, `src/cobalt/heartbeat/probes.py`, `src/cobalt/voice/config.py`, `src/cobalt/voice/web.py`, `tests/cobalt/test_aset_config.py`, `tests/cobalt/test_https_only.py`, `tests/cobalt/test_jobs_restarts.py`, `tests/cobalt/test_smoke.py`, `tests/cobalt/test_voice_config.py`, `tests/cobalt/test_voice_web.py`, `tests/ops/test_deploy_smoke.py`, and docs: `docs/40 - DevDocs/cobalt/aset/__main__.md`, `…/aset/config.md`, `…/heartbeat/probes.md`, `…/voice/config.md`, `…/voice/web.md`, `reports/https-only-build-2026-10-09.md`.
- MACHINE STEPS (card 156): M0–M3 done 2026-10-09; M5 is HIS and lands before this deploy (marker 1 reads `bind: lan` count: `1` at drafting, so M5 is pending); M6 (`DEPLOY-HUB.md` allow entry and reads, committed on main before the deploy hub launches) and M7 follow. The deploy hub's STEP rewrites the pinned `Uvicorn running on http://0.0.0.0:5010` line to `http://127.0.0.1:5010`.
- Marker counts: BEFORE read on main now (2026-10-09), AFTER read at `a1b99495`. Card 156 has no `## DEPLOY PROOF` section; the markers and smoke reads are built from its rows and its DEPLOY ORDER (the M5 grep).
- written by hand by the drafter `https-deploy-fixround` on the fix-round path (deploy-card.sh refuses this job: it never emits the `fix report` cell); trial merge not run by the drafter (no merge-tree allow line).
