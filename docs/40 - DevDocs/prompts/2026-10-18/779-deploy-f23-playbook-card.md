JOB: f23-playbook
LADDER: S5-P5 · F23
BRANCH: deploy/f23-playbook
WORKTREE: deploy-f23-playbook
BASE: main
TIP: 65402dc9
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f23-playbook.md
RULINGS: 2026-10-11 R1055
TAG: deploy-2026-10-18-f23-playbook
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f23-playbook-1013` | `72c8a069` | `65402dc9` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f23-playbook-check-2026-10-13.md` | `held unfixed: 0` and `ready: YES` | |

## LAUNCHD
com.cobalt.playbook · deferred · prompts/2026-10-13/503-f23-card.md:P6 · dry run: none · gate: E1, E2, E4, E5, E6

## MARKERS
- `grep -c -F "playbook_cli.add_parser(sub)" /Users/cobalt/cobalt/src/cobalt/cli.py` · before `0` · after `1`
- `grep -c -F "python-pptx==" /Users/cobalt/cobalt/pyproject.toml` · before `0` · after `1`

## SMOKE READS
- playbook tests · `uv run pytest -q tests/cobalt/test_playbook_offline.py tests/cobalt/test_playbook_registry.py` · green: `0 failed`
- playbook mount · `uv run cobalt playbook render --help` · green: exit 0, usage names `--date`, `--out`, `--dry-run`

## RECORDS
- f23-playbook-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f23-playbook-check-2026-10-13.md` last line: CHECK DONE · job: f23-playbook-1013 · pass: 1 · tip: 72c8a069 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8519/0 · with-DB 5504/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 220271
- f23-playbook-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f23-playbook-1013` → `65402dc9`; code tip `72c8a069`
- written by deploy-card.sh at 2026-10-18 12:48 ET (`date`); trial merge of the heads onto main in order: clean
