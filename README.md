# Cobalt

Cobalt is a local-first, multi-agent trading wingman (Python). Morning scans →
stocks in play per the trader's setups → real-time monitoring → setup alerts →
ASET grading + expected value + position size recommendation. The trader
executes trades himself, manually, always. Plus: automated research engine,
news/X monitoring, journaling, cadence reviews, coaching agents, Obsidian as
system of record, Mattermost + voice as interfaces.

## Absolute boundaries

- Cobalt never integrates with or touches a trading platform (DAS Trader Pro,
  Lightspeed, TradeStation, CenterPoint). Read-only awareness only.
- Cobalt never executes or automates a trade.
- Secrets live only in VaultManager (`COBALT_MASTER_KEY`); never in code,
  never printed or logged.
- Trading-logic changes go behind the tokenized HITL approval pattern.

## Layout

| path | what |
|---|---|
| `src/cobalt/` | the new core — Pydantic-typed, config-driven, fail-loud, tested |
| `src/cobalt_agent/` | the old tree — kept runnable, untouched, retired piece by piece (strangler rule) |
| `configs/cobalt/` | shared new-core config (jobs, radar, notify, prefill, taxonomy, …) |
| `configs/dev/` | per-component dev settings (`aset.yaml`, `vault.yaml`) |
| `configs/*.yaml` | the old loader's live top-level glob — no new-core file goes here |
| `ops/` | launchd plists (`com.cobalt.*.plist`), start scripts, role provisioning |
| `tests/` | `tests/cobalt/` + `tests/taxonomy/` (new core); top-level `test_*.py` (old tree) |
| `docs/` | the D6 documentation tree, gitignored with a carve-out per folder |

`docs/` tiers (`docs/PLACEMENT.md`, CLAUDE.md "Documentation standard"):

| folder | holds |
|---|---|
| `00 - Project` | record only: BACKLOG, COBALT-REQUIREMENTS, PROJECT-LEDGER, charter, ladder |
| `10 - Decisions` | ADRs, one per decision |
| `20 - Assessment` | the frozen pre-beta assessment + `TRIAGE.md` (authoritative) |
| `30 - Design` | design-session outputs |
| `40 - DevDocs` | per-`.py` wiki (`cobalt/`, `ops/`, `tests/`), `plans/`, `reports/`, `prompts/`, `incidents/` |
| `50 - Roles` | role packs + model fleet tiering |
| `90 - References` | input material (licensed `assets/` never committed) |
| `_archive` | superseded content — nothing under `docs/` is deleted |
| `_inflight` | README-only in git, permanently |

## How it runs

Runner is `uv`; tests are `pytest`.

```sh
uv run pytest -q tests/cobalt tests/taxonomy   # new-core suite
uv run cobalt --help                            # new-core CLI
uv run prefill {daily,drc}                      # daily-note / DRC prefill
uv run archiver [--backfill TICKER]             # Bar Archiver
./cobalt.sh {start|stop|status|restart}         # the old-tree agent process
```

`uv run cobalt --help` top-level commands (main, 2026-09-16):

```
vault       Vault write-path tools (LAW L28)
session     F1 session clock (Charter §3 F1)
cards       F7 card state machine (Charter §3 F7)
daymode     F6 two-stage day mode (Charter §3 F6)
db          Database migrations (ADR-0008 two-layer model)
taxonomy    Trade definitions, read from the vault (ADR-0008 D3)
settings    The trader's own settings (ADR-0008 D3.4)
jobs        F17 task integrity (Charter §3 F17)
heartbeat   F18 heartbeat host (Charter §3 F18)
backup      Nightly restic backup of the vault + cobalt_brain.
day-open    The morning sweep (RULED 2026-09-14, A).
notify      Outbound alert channels (F18/F19)
seat-usage  The hourly seat-usage report (L15-gated ccusage).
generated   Files in git that a job rewrites (com.cobalt.generated).
radar       Radar source, pool, and polling operations
stop        Engage the kill phrase — stop all jobs (F17d).
resume      Clear the kill phrase (F17d).
validate    Validate every config family (F16 sweep gate).
```

(`notify` leaves with the email-channel retirement on `ops/2026-09-15`.)

Scheduled and resident processes are launchd jobs registered in
`configs/cobalt/jobs.yaml` (plists in `ops/`):

- residents: `com.cobalt.aset`, `com.cobalt.mainframe`, `com.cobalt.obsidian`,
  `com.cobalt.agent`, `com.cobalt.herdr`, `com.cobalt.radar`
- one-shots: `com.cobalt.prefill-daily`, `com.cobalt.prefill-drc`,
  `com.cobalt.archiver`, `com.cobalt.cards-expire`, `com.cobalt.daymode-propose`,
  `com.cobalt.backup`, `com.cobalt.heartbeat`, `com.cobalt.seat-usage`,
  `com.cobalt.generated`

Which of them a change restarts is derived, never judged:
`uv run cobalt jobs restarts main..HEAD` → the `RESTARTS:` line.

## Dev vs prod

`COBALT_ENV` is required and has no default (`src/cobalt/env.py`):

| | `production` | `dev` |
|---|---|---|
| database | `cobalt_brain` | `cobalt_dev` |
| vault | `/Users/cobalt/Vault/Think`, set explicitly via `COBALT_VAULT_PATH` in each production process's environment | `configs/dev/vault.yaml` → `~/dev-vault-cobalt` (template skeleton, no personal notes) |

`~/cobalt` is production. All development happens in a git worktree
(`~/cobalt-wt/<branch>`) off `main`; merge = deploy, outside market hours.

## Law and memory

Start at `CLAUDE.md` (or `AGENTS.md` / `QWEN.md` for the other houses) → the
memory `INDEX.md` → the `## NOW` section of `areas/cobalt.md` → `LAWS.md`, the
only canonical current law. `docs/00 - Project/PROJECT-LEDGER.md` is the dated
record.

## Where work lands

- plans: `docs/40 - DevDocs/plans/`
- reports: `docs/40 - DevDocs/reports/`
- prompts: `docs/40 - DevDocs/prompts/<date>/`
- incidents: `docs/40 - DevDocs/incidents/<dated-slug>/`
