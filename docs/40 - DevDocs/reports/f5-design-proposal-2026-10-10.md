# F5 Market-context checkpoints · design proposal · 2026-10-10

Proposer: Opus 5.5 drafter `f5-design` (S5 Lane B). Next: the L67 tribunal (Astra, Grok, Fable; Gemini optional), then the card. The build is based on F4's merge and launches only after it.
Code base: main `d0a5fbb8`. Every `file:line` below was read at that commit (report `f5-design-2026-10-10.md` `## RECORDS`).
Seam doc `reports/f4-f5-seam-2026-10-10.md` did not exist when this was written; F5's needs are under `## SEAM NEEDS`.

## 1. What F5 must do
- Charter:89-93: four checkpoints land on schedule with Finviz numbers (deterministic, no LLM figure) and a narrative delta vs the previous checkpoint; a missed checkpoint is loud. Test: the 08:15 block cites what changed since 07:45; a source outage shows as degraded, never blank.
- Charter:50 (M3): 07:15 / 07:45 / 08:15 / 08:45; full view by 09:00.
- LADDER:933: Finviz numbers deterministic; single-house narrative receives the filtered list only and returns the delta vs previous; missed checkpoint loud.
- LEDGER:552: single-house narrative MUST; three-house council SHOULD (not F5).

## 2. Scope (what the build delivers)
1. **One command, one slot per run:** `uv run cobalt checkpoint run --slot HHMM [--dry-run]`. It is also the manual trigger.
2. **Numbers (deterministic):**
   - SPY/QQQ/IWM price + change% through the existing `fetch_market_table` (`prefill/market.py:53`); no second Finviz client (one-path rule).
   - The 11 sector rows from Finviz Groups `g=sector&v=140` (Change, Relative Volume, Performance Week), confirmed in `DATA-SOURCE-MEMO.md:441,465`. A new fetcher `checkpoint/sources.py` reuses `resolve_token` / `scrub` exactly as `market.py` does.
   - Each source fails alone. A failed source renders `degraded: <source> — <reason>` in its lines; it is never blank (Charter:92-93).
3. **Snapshot row:** each run persists `{date, slot, figures, source_status, delta, narrative, narrative_status, model_returned, at}` to a new `market_checkpoints` table in `cobalt_brain`. The row is the stored input every delta and narrative replays from (F15 explainability, Charter:173-175).
4. **Delta (deterministic):** Python computes the delta between this slot's figures and the latest earlier slot's row for the same ET date. Fields: per-index change in price and change%, sector rank moves, sectors crossing ±1% change, and the leader/laggard set. 07:15 has no earlier slot: its delta is the baseline against the prior close (the change% Finviz already gives).
5. **Narrative (single house):** one `modelaccess.call` on a new route `checkpoint.narrative` (§5 D1). The input is the filtered delta list only, never the raw CSV. The output is JSON `{lines: [str ≤ 3]}` and the caller validates it against the schema.
   - **Number guard:** every numeral in the narrative must equal a figure in the input delta, after normalization. Any other numeral drops the narrative. The block then shows `narrative: degraded (unsourced figure)` and the numbers still land.
   - A modelaccess error (`timeout`, `think_leak`, `empty`, …) makes the narrative degraded with that kind. It never blanks the block and never retries on another lane (L25: no fallback key exists, `modelaccess/config.py` refuses one).
6. **Vault write:** one unit per slot, `checkpoint_0715` … `checkpoint_0845`, inside a new Cobalt section `market_context` placed directly under `### Market Context:` (template `configs/cobalt/templates/daily.md.j2:51`). The write goes through `VaultWriter("prefill.checkpoint")` `upsert_unit` (`vaultwrite/writer.py:673`). His `-` bullet and any text he writes under that heading stay outside the section, byte-identical. Earlier units stay, so the 09:00 view holds all four.
   - Unit body: the line `as of HH:MM · <ownership flag>` (F4's stamp, see SEAM NEEDS), the numbers, `Δ since HH:MM:` with the delta lines, and `Narrative:` with its lines or the degraded line.
7. **Missed checkpoint is loud, three ways:**
   - (a) Each run checks every earlier slot of today. A slot with no row gets a unit `MISSED HH:MM — no run recorded` and one DM (`notify/mattermost.py:130` `send_dm`).
   - (b) A heartbeat probe `checkpoint_freshness`, shaped like `archiver_freshness` (`heartbeat/probes.py:261`), turns red when a due slot has no row past `checkpoint.grace_min`.
   - (c) F17 job state per plist (below).
8. **Jobs:** four one-shot rows in `configs/cobalt/jobs.yaml`, `com.cobalt.checkpoint-0715/-0745/-0815/-0845`, each `schedule: {at: "HH:MM", weekdays: [1..5]}`. That is the shape `jobs/config.py:69` already accepts, so the schema does not change. Four plists in `ops/` carry `COBALT_ENV`. `cobalt validate` keeps its plist parity check.
9. **Non-trading day:** the run reads `TradingCalendar` (`session/calendar.py:72`). A closed day writes nothing and exits 0 with one log line.
10. **Finviz demand (L53):** each run declares itself an `extra` consumer to `check_scheduled_demand` (`radar/notes.py:384`): 2 requests in a 60 s window per slot. It takes its tokens from the shared `radar.finviz_max_rpm` bucket. A run refused by the gate renders `degraded: finviz — demand ceiling` and is loud.

## 3. Files touched
| File | Change |
|---|---|
| `src/cobalt/checkpoint/__init__.py`, `config.py`, `sources.py`, `delta.py`, `narrative.py`, `render.py`, `store.py`, `runner.py`, `cli.py` | NEW package |
| `src/cobalt/cli.py` | register `checkpoint` subcommand |
| `src/cobalt/db_migrations/<next>_market_checkpoints.sql` | NEW table (L29: Opus build) |
| `src/cobalt/heartbeat/probes.py` + runner registration | NEW probe `checkpoint_freshness` |
| `configs/cobalt/checkpoints.yaml` | NEW (§4) |
| `configs/cobalt/modelaccess.yaml` | NEW route `checkpoint.narrative` |
| `configs/cobalt/jobs.yaml` | four rows; `checkpoints.yaml` under `no_resident_reads` (readers: the four labels) |
| `configs/cobalt/templates/daily.md.j2` | empty `market_context` section markers under `### Market Context:` (SEAM) |
| `configs/cobalt/taxonomy/tunables.yaml` | `checkpoint.grace_min` (F16) |
| `ops/com.cobalt.checkpoint-{0715,0745,0815,0845}.plist` | NEW |
| `src/cobalt/prefill/daily.py` | NONE unless the seam doc assigns it (SEAM NEEDS 1, 4) |
| `configs/cobalt/prefill.yaml` | NONE (§5 D9) |
| `tests/checkpoint/…`, `tests/heartbeat/…` | NEW |

## 4. Data and config
- **Table `market_checkpoints`** (cobalt_brain and cobalt_dev): `id`, `trade_date date`, `slot text`, `figures jsonb`, `source_status jsonb`, `delta jsonb`, `narrative jsonb null`, `narrative_status text`, `model_returned text null`, `vault_write_id` (FK to `vault_writes`), `created_at`. Unique `(trade_date, slot)`; a manual re-run of a slot updates its row and its unit (same id = update in place).
- **`configs/cobalt/checkpoints.yaml`** (Pydantic, `extra="forbid"`, every key required):
  - `slots: ["07:15","07:45","08:15","08:45"]` with `source: ruling` (Charter:50; LEDGER:541).
  - `indices: [SPY, QQQ, IWM]`
  - `groups: {g: sector, v: 140}`
  - `route: checkpoint.narrative`
  - `narrative_max_lines: 3`
  - `section: market_context`
  - `heading: "### Market Context:"`
  - A test proves `slots` equals the four `jobs.yaml` `at` values and the four plists.
- **Route `checkpoint.narrative`:** `lane: local`, `kind: openai_compatible`, `api_base: http://127.0.0.1:1234/v1`, `model: mainframe`, `no_think: true`, `think_policy: forbid_nonempty`, `response_format: json_schema`, `key_name: null`.
  - `timeout_s` and `max_output_tokens` come from a build-step measure (X-E4 style, `modelaccess.yaml` comments). Each value carries its `source:` comment.
- **Tunable `checkpoint.grace_min`:** a start value of 10, marked unmeasured until his ruling (L53 covers cadences; the slot times are already ruled).

## 5. Open choices (each with its default and the reason)
| # | Choice | Default | Reason |
|---|---|---|---|
| D1 | Narrative house | Local `mainframe` through a new modelaccess route | `modelaccess/config.py:43` accepts only `lane: local`, and the validator says a non-local lane is the routing tribunal's to add. Claude-on-subscription needs the SDK chassis (L22), gated by the Lane C spike. LiteLLM→Anthropic API is paid (L22, L27). L23 local-first. The route name is stable, so a later house change is one config row. |
| D2 | Job shape | Four one-shot plists | `Schedule.at` takes one time (`jobs/config.py:69`): no schema change, per-slot F17 state, launchd exit code per slot. |
| D3 | Numbers set | SPY/QQQ/IWM + 11 sectors (`v=140`) | Both endpoints are confirmed (`market.py:53`; MEMO:441). Futures, VIX and BTC are not served by them (`market.py` docstring). |
| D4 | Delta and narrative storage | New table `market_checkpoints` | The delta needs the previous figures as data. Parsing them back from his note would read text he may edit (L28 human-wins). F15 needs stored inputs. |
| D5 | Placement | A new `market_context` section under `### Market Context:`, one unit per slot | The heading is in the template (`daily.md.j2:51`). Per-slot units keep the 07:45 block for the 08:15 cite. His bullet stays outside the markers. |
| D6 | 07:15 baseline | vs the prior close (Finviz change%) | No earlier slot exists. The figures carry the prior-close change already. |
| D7 | Missed-checkpoint loudness | MISSED unit at the next run + DM + heartbeat probe | Charter:92 "loud". The alert path is not the job's own path (F18 principle, Charter:186-190). |
| D8 | Number guard | Drop any narrative with a numeral not in the input | Charter:90-91 "no LLM figure". It is deterministic and testable. |
| D9 | Config home | New `checkpoints.yaml` | Keeps F5 out of `prefill.yaml`, which the sheet re-reads (`jobs.yaml` `com.cobalt.aset` reads), so no resident restart is derived (L42). It also shrinks the F4 seam. |
| D10 | Non-trading days | Skip via `TradingCalendar` | A holiday morning has no premarket context. Writing stale figures would mislead. |
| D11 | Note absent at slot time | F5 calls F4's ensure-note entry, if the seam names one; else the unit write is refused (`writer.py:700`), recorded FAILED in the row, and a DM goes out | F5 never creates the daily note itself (one creator, L28 create-if-absent). |
| D12 | Model-call timing | One call per slot, after the numbers are stored | The numbers land even if the model hangs. The narrative never delays the figures. |

Owner items: none. Ruling R849 needs none and no field of his changes (his bullet stays outside the markers). Only `checkpoint.grace_min` is a cadence value for him under L53, and it ships unmeasured on its default.

## 6. Tests (offline · with-DB · live-note, L68 GATE EARLY)
**Offline:**
- Delta: fixed figures at 07:45 and 08:15 give the expected rank moves and crossings.
- 08:15 render: the block contains `Δ since 07:45` and those lines (Charter test).
- Source outage: market fetch raises, so index lines read `degraded: finviz-screener — <reason>`, sectors still render, and the unit body is not empty. The same holds for the groups fetch.
- Number guard: a narrative with a numeral absent from the input is dropped and the status is `degraded (unsourced figure)`. A narrative using only input figures is kept.
- Narrative errors: `timeout` / `think_leak` / `empty` / schema-invalid each give a degraded narrative with the numbers present.
- Placement: a note with his text under `### Market Context:` keeps that text byte-identical after all four slots. The `vault_writes` diff shows only section lines.
- Idempotence: re-running the same slot with the same figures is a zero diff.
- Missed slot: a run at 08:15 with no 07:45 row writes `MISSED 07:45` and calls `send_dm` (faked).
- Schedule parity: `checkpoints.yaml` slots = `jobs.yaml` ats = plist calendar entries.
- L53: the demand gate refuses when the radar plan plus the checkpoint demand exceed the ceiling, though the checkpoint alone passes.
- Calendar: a closed day writes nothing.
- Config: an unknown key or a missing key crashes the load.

**With-DB** (cobalt_dev, L76 lock):
- Migration up, then a row round-trip.
- A unique-key re-run updates the row and keeps it at one.
- The 08:15 delta reads the 07:45 row.
- `checkpoint_freshness` goes red with no row past grace and green with one.

**Live-note:** `--dry-run` against his real notes through `COBALT_LIVE_VAULT_ROOT`, read-only. It proves the placement finds `### Market Context:` in real notes. Where a note lacks it, the section appends at the end, as daily.py's L28 rule does.

## 7. Risks
- **Mainframe contention:** voice Plan calls queued 60–72 s behind a second client (`modelaccess.yaml` X-E4 comment). A checkpoint during voice use times out, and the narrative is degraded while the numbers land. Mitigation: D12, plus the measured timeout.
- **Local narrative quality** may be thin. The number guard bounds harm; quality is not bounded. Revisit at the routing tribunal's lane extension (D1).
- **Finviz shared bucket:** 07:15–08:45 runs while the radar scans 24×5. 2 requests per slot is small, but the L53 gate is the proof, not this estimate.
- **Obsidian Sync revert** of a unit: covered by L28's sync-revert carve-out in `VaultWriter`.
- **launchd local time:** the plists fire on host-local time. The host must stay on ET, as for every existing calendar job (`jobs.yaml:211`).
- **F4 rebase:** F5 is built on F4's merge. Any F4 change to the template's Market Context lines or to the stamp helper moves F5's placement, so the seam doc must fix both before either card.

## 8. NOT in F5
- The three-house council (SHOULD, purchase gate; LEDGER:552).
- VIX/BTC "n/a (manual)" and the all-day prefill cadence and ownership flags (F4, Charter:82-88).
- The 09:00 day-mode proposal (F6).
- Prebell's full page: heatmap, expected ranges, the ranked watchlist (`docs/90 - References/INDEX.md:84-85`).
- Futures data, and the radar `context.tickers` alignment dots (`radar.yaml:40-44`, S2-P2).
- Any Claude / SDK lane (F20 chassis, Lane C spike).
- Retiring the old morning briefing or the Mattermost listener (`areas/cobalt-sprints.md:12`). They retire only when F5 and F20 have both landed, by a separate step.
- The Vital Dawn digest (M2, SHOULD).

## SEAM NEEDS
The seam doc `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-f5-seam-2026-10-10.md` (the F4 drafter writes it; LAWS:363) must settle:
1. **Template:** who adds the `market_context` section markers under `### Market Context:` in `configs/cobalt/templates/daily.md.j2`. F5's default: F5 adds them on top of F4's merge, and F4 does not touch lines 51-52.
2. **Section ownership:** F4's slot list (`prefill/daily.py:463` `SLOT_SPECS`) and its all-day refresh never write or rewrite `market_context`. F5 writes it only through writer name `prefill.checkpoint`.
3. **Stamp and flag:** the exact `as of HH:MM` line and the ownership-flag vocabulary (`cobalt` / `cobalt-degraded` / `human`, LADDER:932). F5 calls F4's helper and does not copy it.
4. **Note creation:** the public function F5 calls when the note is absent at slot time (D11). If none exists, F5 refuses and is loud.
5. **Finviz fetch:** if F4 routes `fetch_market_table` through the shared bucket or changes its signature, F5 uses that version. F5 adds no second index fetch.
6. **jobs.yaml:** F4's cadence rows and F5's four checkpoint rows are distinct labels. No shared row is edited.
7. **prefill.yaml:** F5 adds nothing (D9).
8. **Manual trigger:** F4's manual prefill trigger does not fire checkpoints. `cobalt checkpoint run --slot` is F5's own trigger.
