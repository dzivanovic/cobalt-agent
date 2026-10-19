JOB: f20-cos
LADDER: S5-P3 · F20
BRANCH: deploy/f20-cos-attempt2
WORKTREE: deploy-f20-cos-attempt2
BASE: main
TIP: 83919213
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f20-cos-attempt2.md
RULINGS: 2026-10-11 R1055, 2026-10-11 R1112, 2026-10-18 R1833
TAG: deploy-2026-10-19-f20-cos-attempt2
MIGRATIONS: none
SET: cos
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f20-cos-fr1` | `753094da` | `83919213` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f20-cos-fr1-check-2026-10-19.md` | `held unfixed: 0` and `ready: YES` | |

## LAUNCHD
com.cobalt.cos · deferred · prompts/2026-10-18/730-f20-card.md:C4a · dry run: none · gate: D14, agent stopped, X1, X13, X2, X10, X3, X14, X11, X12, X15, X17, X18, X20

## MARKERS
- `grep -c -F "label: com.cobalt.cos" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` · before `0` · after `1`
- `grep -c -F "hitl_dirs:" /Users/cobalt/cobalt/configs/cobalt/generated.yaml` · before `0` · after `1`
- `grep -c -F "claude-agent-sdk==" /Users/cobalt/cobalt/pyproject.toml` · before `0` · after `1`

## SMOKE READS
- f20 offline · `uv run pytest -q tests/cobalt/test_agents_registry.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_hitl_web.py tests/cobalt/test_hitl_executor.py tests/cobalt/test_generated_hitl_dirs.py tests/cobalt/test_cos_offline.py tests/cobalt/test_cos_listener.py tests/cobalt/test_cos_registry.py tests/cobalt/test_cos_probes.py` · green: `0 failed`
- registry · `uv run cobalt agents list` · green: lists `voice` and `cos`, exit 0

## RECORDS
- f20-cos-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f20-cos-fr1-check-2026-10-19.md` last line: CHECK DONE · job: f20-cos-fr1 · pass: 1 · tip: 753094da · house A: Grok FINDINGS: 1 · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8725/0 · with-DB 5663/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 6 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 193794
- f20-cos-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f20-cos-fr1` → `83919213`; code tip `753094da`
- written by deploy-card.sh at 2026-10-19 05:25 ET (`date`); trial merge of the heads onto main in order: clean
