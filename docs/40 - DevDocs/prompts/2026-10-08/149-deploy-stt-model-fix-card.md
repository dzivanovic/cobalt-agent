JOB: stt-model-fix-1008
LADDER: OFF-LADDER — his screenshot 2026-10-08 (reports/cto-2026-10-08.md R687)
BRANCH: deploy/stt-model-fix-1008
WORKTREE: deploy-stt-model-fix-1008
BASE: main
TIP: 6b4068d6
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-stt-model-fix-1008.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-08-stt-model-fix
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/stt-model-fix-1008` | `6b4068d6` | `6b4068d6` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stt-model-fix-check-2026-10-08.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "voice model READY" /Users/cobalt/cobalt/ops/fetch_voice_models.py` · before `0` · after `2` (the fetch script's ready line)

## SMOKE READS
- the fetch script's ready line present · `grep -c -F "voice model READY" /Users/cobalt/cobalt/ops/fetch_voice_models.py` · exit 0, a count of 1 or more

Card 126 (speech-to-text model fetch script, his R685). Files: `ops/fetch_voice_models.py`, `ops/fetch-voice-models.sh`, the radar restart class, tests, docs. RESTARTS: com.cobalt.radar (the check's stop line). The deploy runs when READY at any hour (L43). The check ended `held unfixed: 0 · ready: YES` at tip `6b4068d6`. POST-DEPLOY is the desk's, after the deploy's stop line, per card 126 `## RECORDS`: `COBALT_VOICE_MODEL_DIR=/Users/cobalt/.cobalt/voice-models sh /Users/cobalt/cobalt/ops/fetch-voice-models.sh --from /Users/cobalt/.cobalt-dev/voice-models`.

## RECORDS
- stt-model-fix-1008: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stt-model-fix-check-2026-10-08.md` last line: CHECK DONE · job: stt-model-fix-1008 · pass: 1 · tip: 6b4068d6 · house A: Sol FINDINGS: 3 · findings: 6 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 2 · suites: offline 3992/0 · with-DB 4876/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 188056
- stt-model-fix-1008: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/stt-model-fix-1008` → `6b4068d6`; code tip `6b4068d6`
- written by deploy-card.sh at 2026-10-08 14:48 ET (`date`); trial merge of the heads onto main in order: clean
