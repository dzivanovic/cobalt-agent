# f4-probe — build report 2026-10-26

## §0 Headline

(in progress)

## L74

## AUTHORIZATION

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → exit 0, whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1047-f4-probe-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1047-f4-probe-card.md" · 0 · 11ac13c7c7f5e232e143d799ac265193960245e5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1047-f4-probe-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:

```
clock · date · 0 · Mon Oct 26 08:14:09 EDT 2026
status · git status --short --branch · 0 · ## ops/f4-probe
head · git log --oneline -1 · 0 · 596ca32ff docs(desk): R2470 f4-gate-run done, X9 asked of the brain
diff · git diff --stat 596ca32f · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f4-probe · 0 · 596ca32ff docs(desk): R2470 f4-gate-run done, X9 asked of the brain
env here · ls /Users/cobalt/cobalt-wt/f4-probe/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 596ca32f` | 0 | `596ca32ff docs(desk): R2470 f4-gate-run done, X9 asked of the brain` · `docs/40 - DevDocs/reports/cto-2026-10-26.md | 5 +--` · `.../40 - DevDocs/reports/f4-gate-run-2026-10-26.md | 41 ++++` · `2 files changed, 44 insertions(+), 2 deletions(-)` |
| P1 main | `grep -n -F "def main" src/cobalt/prefill/cli.py` | 0 | `77:def main() -> None:` (refresh parser read at `:88-93`) |
| P2 env | `grep -n -F "def resolve_env" src/cobalt/env.py` | 0 | `60:def resolve_env() -> str:` |
| P2 clients | `grep -n -F "httpx.AsyncClient(" src/cobalt/archiver/collector.py src/cobalt/prefill/market.py src/cobalt/prefill/calendar.py` | 0 | `collector.py:222`, `market.py:68`, `calendar.py:52` (each `async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:`) |
| P2 every client | `grep -rn -F "httpx.AsyncClient(" src/cobalt` | 0 | the three above plus `prefill/checkpoints.py:232`, `aset/prefill.py:55` (not on the X15 path; the probe's client patch covers every `httpx.AsyncClient` alike) |
| X15 symbols | `grep -n -E "async def finviz_get\|async def fetch_bars\|class TokenBucket\|class StrikeDetector\|class DemandPlan\|async def tick\|def read_plan\|def poll_interval" …` | 0 | `archiver/collector.py:205 finviz_get`, `:255 fetch_bars`, `radar/collector.py:42 TokenBucket`, `strike/detector.py:80 DemandPlan`, `:103 poll_interval`, `:131 StrikeDetector`, `:238 tick`, `:313 read_plan` |
| X15 refresh | `grep -n -E "async def _gated_fetch\|def check_refresh_demand\|def refresh_demand_consumer\|async def fetch_market_table\|…" …` | 0 | `daily.py:759 refresh_demand_consumer`, `:780 check_refresh_demand`, `:800 _gated_fetch`, `market.py:55 fetch_market_table`, `calendar.py:62 fetch_economic_events`, `:83 fetch_earnings_events` |
| T2 daymode | `grep -n -E "^def render_body\|^def write\|format_stamp\(" src/cobalt/daymode/note.py` | 0 | `83:def render_body(`, `105: format_stamp(...)`, `140:def write(` |
| T2 config | `grep -rn -F "def load_daymode_config" src/cobalt/daymode` | 0 | `config.py:309:def load_daymode_config(sheet_modes=None) -> DayModeConfig:` |
| FINAL rows | `grep -n -E "…X7…X15" "docs/30 - Design/F4-FINAL-2026-10-10.md"` | 0 | `213:| X7 | Config, clock, rendering: …` · `221:| X15 | Strike loop and refresh in one minute (Opus seat, round 3) | … "dev, 5 synthetic ARMED cards, radar planned 40, ceiling 50, …"` |
| tunables | grep of `configs/cobalt/taxonomy/tunables.yaml` | 0 | `702: - key: radar.finviz_max_rpm` / `703: value: 50`; `735 strike.poll_interval_min 2`; `744 strike.max_armed 5`; `1148 prefill.refresh_window "05:45-15:45"`; `1160 prefill.refresh_interval_min 30` |
| wc | `wc -l src/cobalt/prefill/cli.py tests/cobalt/test_prefill_refresh.py "…/prefill/cli.md" "…/prefill/daily.md"` | 0 | `113`, `1268`, `42`, `160` |
| READ reports | — | — | `## READ` names no report |
| restarts | `uv run cobalt jobs restarts 596ca32f..HEAD` | 0 | `docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.md A DOCS -` (this uncommitted report, in the working tree) · `RESTARTS: none` |

Records copied from the card (`## RECORDS`):
- F4 gate 1045 — X15 load gate by probe card f4-probe (+X7 two offline tests) — brain 9b07db5a. Re-read: `grep -n -F "| R2463 " ".../reports/cto-2026-10-26.md"` → `25:| R2463 | 07:57 ET | DESK RECORD (brain 9b07db5a, L79): F4 gate 1045 — … X15 load gate by probe card f4-probe (+X7 two offline tests); … | APPROVED — pending fold |`. `git -C /Users/cobalt/cobalt log --oneline -1 9b07db5a` → exit 128 `unknown revision` (the brain's hash is not a commit of this repo; not re-readable from my list).
- DECISION 1 (in process, virtual clock, mock transport), DECISION 2 (radar stand-in at 40 rpm through `finviz_get`), DECISION 3 (BAND HIGH): the drafter's; built as written.
- ARITHMETIC (drafter, not a result): headroom 10, 5 names → `poll_interval` 30 s = 10 rpm; radar 40 + strike 10 = 50; refresh's 3 GETs fall in one minute. Re-read: `strike/detector.py:103-108` as quoted.
- RULINGS R1863: proved by `authorize.sh` above.

The with-DB strings are proven at W's first take (no with-DB red in this card).

## E0 BASELINE

## E2 RED

## E3 THE ROWS

## RESTARTS

## W THE THREE SUITES

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE

next: E0

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
