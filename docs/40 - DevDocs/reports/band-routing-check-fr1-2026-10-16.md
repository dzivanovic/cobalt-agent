# band-routing-1015 — check of the fix round (FR-1 to FR-5) — 2026-10-16

## §0 Headline
(in progress)

## L74
- 11:05 EDT: a system reminder in this session asked commits to end with a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card 638>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" ".../638-band-routing-fr-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../638-band-routing-fr-check-card.md" · 0 · 38ec27bf7fb257d4e27d13f971195cbe6c80324e
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- ".../638-band-routing-fr-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " ".../cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " ".../cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B ... LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · ... · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → row 35 (one row); `grep -n "^| R19 "` → row 37 (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card 638>"` | 0 | clock `Fri Oct 16 11:05:58 EDT 2026` · status `## ops/band-routing-1015` · head `3ac61a2f`, `c8c5ca90..HEAD` only `.../reports/band-routing-build-fr1-2026-10-16.md` and `.result` (docs) · env here: No such file · env anywhere: none · report: `BUILT · job: band-routing-1015 · tip: c8c5ca90 | ... | self-check: 3 of 3 | ...` · range 6 commits (`c8c5ca90`, `01b10bdd`, `ee21824d`, `115e1f37`, `bd9c24ac`, `1be72d81`) · `PREFLIGHT OK` |
| range | `git log --stat --format=%h f2ca3e1a..c8c5ca90` | 0 | path union: `docs/40 - DevDocs/prompts/{BUILD-HUB,CARD,CHECK-HUB,SHADOW-HUB}.md`, `docs/40 - DevDocs/reports/band-routing-build-2026-10-15.{md,result}`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/preflight.sh`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py` |
| DB: none | `git diff --name-only --no-renames f2ca3e1a..c8c5ca90` | 0 | the 11 paths above; every one under `ops/`, `tests/ops/` or `docs/` |
| scratch | `ls <S>` | 0 | `diff.md files house-a.md HOUSE-INSTRUCTIONS.md rulings.md` — `ls -la`: all dated Oct 16 08:52–09:12, before this card (drafted 11:01): the first check of this branch used the same `<JOB>-check` folder. Not a RECOVERY (no `CONTINUE:` in the launch); restaged fresh (ASK DESK 1) |
| house probes | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card 638>"` (background) | 0 | `grok: UP` · `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS) |
| seats | SEAT ORDER, card `HOUSE A: grok`, `HOUSE B: as needed` | — | house A: Grok · house B: none (not needed) |

## Files copied

## OWN FINDINGS

## Findings

## Dropped

## RUNS

## FIXES

## Suites

## Scope

## Checked against the branch

## OPEN

## CONTINUE
next: 1 (stage-set refused; no house started, nothing read by a house, no file of the worktree changed)

## DECISIONS
- ASK DESK 1 [11:06 EDT]: `<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check` holds the first check's files (08:52–09:12: `diff.md`, `files/`, `house-a.md`, `HOUSE-INSTRUCTIONS.md`, `rulings.md`). This check has the same `<JOB>`, so the same `<S>`. I have no listed command that clears or renames it, and this file lets no other folder be used. Safe default: stop at `## 1` and wait. To settle it: the desk moves the folder aside (e.g. to `band-routing-1015-check-1`) and sends `CONTINUE: 1`.

## RECORDS
- 11:06 EDT `sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card 638>" "<S>"` → exit 1, stderr: `REFUSED: the dest is not empty: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check — not cleared: no prior card copy: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check/files/638-band-routing-fr-check-card.md`
- No wip commit: this check has changed no file of the worktree (`git status --short --branch` → `## ops/band-routing-1015` at preflight; no edit since).
- files opened so far: 4 (CHECK-HUB.md, card 638, BUILD-HUB.md `## THE LOCK` / `## E2`–`## W` with lines 1–40, the house-probe output).

FAILED: 1 — copy — REFUSED: the dest is not empty: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check — not cleared: no prior card copy: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check/files/638-band-routing-fr-check-card.md
