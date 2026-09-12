# Radar parser fix build report — 2026-09-12

## Result

Build complete on `sprint-2/radar-pool` at the pre-existing stage-2 worktree tip
`fe66fc3`. No commit, migration, database, launchd job, production process, or Vault
file was changed. The pre-existing edit to `s2-p1-2026-09-10.md` was left untouched.

The final offline suite result is:

```text
1033 passed, 238 skipped, 15 warnings in 18.19s
```

The 15 warnings are the existing LiteLLM `asyncio.iscoroutinefunction` deprecation
warning from `tests/taxonomy/test_names_rule.py`. The command ran with all common
Postgres variables and `COBALT_ENV` removed from the process environment. Skipped tests
were not counted as passes; DB-backed tests remained skipped.

## 1. Seven extraction defects

`cobalt.radar.propose.derive_screens()` now follows one bounded extraction and
reconciliation path for proposal and validation:

1. `**Sort:**` and the conventional `**Sort**:` and bare-label forms are accepted.
2. The annotated `Filters (`f=`)` label is recognized.
3. Only backticked filter codes inside the Filters field are derived. The complete
   gloss-bearing Filters line remains verbatim evidence and is rendered beside `f`.
4. Sort extracts only its leading inline-code value; explanation, columns, and preset
   commentary do not contaminate it.
5. Inline or standalone columns are accepted. `<same columns>` must resolve from an
   actual numeric declaration in the same section; there is no default column set.
6. Recognized heading/Intent `after HH:MM` or `from HH:MM` prose supplies a start.
   Conflicts refuse. Missing endpoints use the existing D13 session-span proposal and
   remain visibly marked `PROPOSED` rather than guessed.
7. An export URL without `o` is valid. Any explicit `o` in export or pasted evidence
   must agree with Sort.

Additional reconciliation refuses duplicate fields and keys, ambiguous URL parameters,
filter/sort/column contradictions, invalid times, and invalid `ScreenBlock` values.
Percent-encoded and literal commas reconcile after URL parsing. `preset`, `ar`, pasted
`v`, and English gloss semantics remain annotation/UI data.

### Defect-to-test map

| Defect | Production-shaped coverage | Supporting coverage |
|---|---|---|
| Bold colon inside markup | `test_real_shape_fixture_exercises_all_seven_extraction_defects` asserts the real `**Sort:**` evidence | `test_real_shape_supported_markup_variants_derive_equal_models` |
| Annotated Filters label | The seven-defect test derives all exact real filters from `Filters (`f=`)` | `test_real_shape_gloss_and_url_encoding_edits_do_not_change_models` |
| Filter glosses | The seven-defect test asserts exact tokens and the retained final gloss | `test_each_derived_field_has_adjacent_verbatim_source_comment` |
| Sort plus prose | The seven-defect test asserts the four exact sort codes while using real explanatory/commentary text | `test_real_shape_refusal_matrix` checks explicit URL disagreement |
| Inline columns | The seven-defect test asserts all 21 ordered columns and the inline annotated label | Refusal matrix checks unresolved, conflicting, duplicate, and out-of-range columns |
| Prose active start | The seven-defect test asserts `day_scan` and `10:00` | `test_missing_prose_window_uses_session_span_and_proposed_marker` and conflicting-time refusal |
| Export omits `o` | The seven-defect test asserts the real export evidence has no `o=` and still derives | Additional refusal test checks an explicit contradictory export `o` |

## 2. Real-shape fixture

Added `tests/fixtures/radar/radar-screens.real-shape.md` from the real Screens note.
It retains all four headings, field markup, punctuation, glosses, filter strings, export
and pasted URL parameter shapes, and ordered columns. It removes only attribution/date
metadata and replaces saved-preset identifiers with `[removed]`; those substitutions are
declared in fixture frontmatter.

The fixture-policy test now permits real filter strategy values only under the approved
`tests/fixtures/radar` path. The proposal simulation proves every original note byte is
preserved and only insertion units are added.

Failing-first focused evidence before the parser change was `10 failed, 29 passed`.
The final focused radar/account set was `68 passed in 1.19s` before the two additional
column-refusal cases were added; those final cases separately pass `9 passed in 0.18s`
as part of the final full suite.

## 3. Offline Screens validation

Added:

```text
cobalt radar screens validate --pool-block <file> [--watchlists-yaml <file>]
```

The command reads the current Screens bytes exactly once, derives the four models through
the proposal parser, validates pool references and the ruled pool budget, validates the
actual Lists note or derives prospective Lists in memory from committed watchlists, and
compares prose-derived fields with installed blocks when they exist. It prints source
hashes, derived windows, budget, drift state, and archive target count. It makes no HTTP,
DB, artifact, or Vault-write call.

The first manual invocation without an environment declaration correctly stopped at the
global environment gate. A second, explicitly production/read-only invocation against
the real Vault Screens note, stage-1 watchlists, and real pool block passed:

```text
Screens sha256: e855e919d10ae97d4658223e5824e13f96859c53def4ef7e62251aa0a146758a
Lists sha256: 89ac36444c8b0a40f81a878c77140a5fb2a8ee0a7e6678c715f0928ff125f12a
Pool sha256: ccd6c4073772ecfe19244161b795c551ce8de0ceb11a1c686e4b550f313f3a51
up_gappers: 04:00-20:00
down_gappers: 04:00-20:00
day_scan: 10:00-20:00
morning_low_float: 04:00-20:00
pool budget: 33.33/40 rpm (cap=50, scan_interval=90s)
drift: not installed
archive targets: 975
```

`Radar Lists.md` is still absent, so the displayed Lists hash is the prospective note
derived in memory. The production note was not created.

Tests: `test_screens_validate_is_offline_side_effect_free_and_hashes_current_bytes`,
`test_screens_validate_detects_installed_prose_drift`, and
`test_screens_validate_refuses_bad_pool_before_http_or_artifact`.

## 4. Truthful `radar sources`

`radar sources` now loads and validates Screens, Lists, the pool block, pool override
resolution, and budget before emitting its payload. It reports both note paths/hashes,
planned rpm, and actual archive targets. Invalid/missing source data and over-budget pools
exit nonzero. `--archiver-diff` now raises a nonzero error when it finds any archive or
backfill set difference instead of printing a successful-looking diff.

Tests: all four cases in `test_radar_sources.py`, including both-source reporting,
over-budget refusal, missing Lists refusal, and nonzero archive mismatch.

## 5. Dejan budget ruling

Committed tunables now carry:

```text
radar.scan_interval = 90
radar.poll_interval = 90
radar.finviz_max_rpm = 40
```

The validation definition implements the ruling exactly: `cap * 60 / scan_interval`.
Cap 50 therefore produces `33.33 rpm` and passes ceiling 40. A cap 61 mutation produces
`40.67 rpm` and refuses with both computed and configured values. Coverage is
`test_dejan_budget_cap_50_at_90_seconds_passes_under_40_rpm`,
`test_dejan_budget_refuses_when_ruled_pool_rate_exceeds_ceiling`, and the source/validator
budget refusal tests.

### OBJECTION — transport demand remains larger than the ruled metric

The implemented check obeys Dejan's final ruling and does not substitute Astra's cap 18.
However, the current runner's nominal total transport demand also includes four screen
requests and seven list chunks each scan. At 90 seconds that is approximately
`33.33 + 2.67 + 4.67 = 40.67 rpm`, above 40, even though the ruled pool-only validation
passes at 33.33. The 40 rpm token bucket will cap actual throughput, so the hub should
verify that the intended 90-second completion cadence is achieved before launch. This is
an objection only; it did not override the ruling.

## 6. Refusals and apply guards

The real-shape refusal suite covers export/pasted filter conflicts, explicit sort
conflicts, unresolved `<same columns>`, contradictory columns, duplicate and out-of-range
columns, duplicate fields, duplicate keys, conflicting/invalid timing, and ambiguous URL
parameters. Pool validation covers unknown overrides and budget excess.

Proposal-path refusals assert no artifact or HTTP call. Apply-path refusals assert the
writer/store call list, HTTP call list, and derivation call list all remain empty for
artifact-hash drift, target-hash drift, changed absent targets, existing blocks,
market-reset, missing token, and environment mismatch. The valid apply simulation also
proves artifact units are used without HTTP or re-derivation. Every `ProposalRefused`
message is scrubbed at construction; source-command errors and printed paths/diffs pass
through `cobalt.archiver.collector.scrub`.

`_ft_diff()` now requires parseable CSV with a `Ticker` header and refuses HTML-shaped,
missing-header, and malformed-row responses. A valid header-only CSV remains accepted.

## 7. House stubs and memory-store finding

Added root `QWEN.md` and `AGENTS.md` as thin `CLAUDE.md`-pattern pointers to the canonical,
read-only `/Users/cobalt/Vault/Think/6 - Permanent/Memory/INDEX.md`. Neither stub authorizes
Vault writes.

### Qwen Code 0.23.3

The installed version defaults both managed auto-memory and auto-dream to `true`; the
checked user settings do not override them, and a private project memory directory already
exists. Automatic saving and cleanup can be disabled globally in `~/.qwen/settings.json`
or per project in `.qwen/settings.json`:

```json
{
  "memory": {
    "enableManagedAutoMemory": false,
    "enableManagedAutoDream": false
  }
}
```

That disables automatic extraction/consolidation, not the explicit `/remember` command;
no dedicated setting that removes the private store or disables explicit manual memory
writes was found. `--safe-mode` disables memory features for a run, but also disables
context files, so it defeats the `QWEN.md` pointer.

The store is redirectable per process with `QWEN_CODE_MEMORY_BASE_DIR=<directory>`.
Qwen appends `projects/<sanitized-project>/memory` (and related generated state) below
that base, so it cannot map directly onto the existing canonical `Memory/INDEX.md`.
`QWEN_CODE_MEMORY_LOCAL=1` instead uses `.qwen/memory` inside the repository. Pointing
the base at the Vault Memory folder would create Qwen-managed subtrees there and is
therefore rejected for Cobalt. Recommended policy: disable both managed auto-memory
toggles and retain the read-only `QWEN.md` pointer; do not use `/remember` for this repo.

Sources: [Qwen memory documentation](https://github.com/QwenLM/qwen-code/blob/main/docs/users/features/memory.md)
and [Qwen settings reference](https://github.com/QwenLM/qwen-code/blob/main/docs/users/configuration/settings.md),
confirmed against the installed package's storage resolver.

### Codex CLI 0.154.0

`codex features list` reports `memories stable false`, the checked config has no memory
override, and `~/.codex/memories` is absent. Local Codex memories are therefore currently
off. To make that policy explicit:

```toml
[features]
memories = false

[memories]
generate_memories = false
use_memories = false
```

Codex documents no memory-only storage-path override. `CODEX_HOME` relocates the whole
Codex state/config/auth/log/session tree, not just memories, and must not be pointed at the
Vault. The root `AGENTS.md` pointer is the supported project instruction mechanism.
`history.persistence = "none"` controls transcript history, not the memory subsystem.

Sources: [Codex memories](https://learn.chatgpt.com/docs/customization/memories),
[Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference),
and [Codex AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

No user-level Qwen or Codex settings were edited because they are outside this build's
write scope.

## Adjacent plan items

- Lists proposal preserves the complete leading watchlists comment block as readable
  prose. Exact archive/backfill set equality is tested against the actual committed
  watchlists shape; archive targets are 975.
- Added a behavioral account-mode regression with the real checkbox/form shape: filename
  readback leaves account mode unset, store preservation keeps the existing mode, and the
  rendered form contains both fields with the expected selections. It uses a fake store
  and no DB.
- Work was performed on the already reconciled stage-2 tree; the final full suite covers
  that combined state. No migration was added or amended.
- DevDocs for each changed radar Python module were updated.
- `ruff check` on all changed Python files and `git diff --check` both pass.

## ESCALATE, cuts, and hub gates

`ESCALATE: source additions reached 431 lines across the four radar modules (341 net),`
crossing the plan's approximate 400-added-line warning. The growth is concentrated in the
required bounded parser, offline validation, and truthful source checks; no schema or new
collector/poller behavior was introduced. Mandatory scope was retained and further scope
expansion stopped.

Planned cuts retained explicitly: no structured gloss semantics, general Markdown parser,
arbitrary English scheduling, or screen-editing/regeneration workflow was built. These are
the plan's named exclusions; the real-shape fixture, budget validation, `radar sources`,
and apply guards were not cut.

Outstanding hub-only/live gates are unchanged: credentialed DB/dev-Vault proofs, the known
equity/ETF classification probe, final restart derivation from actual deployment SHAs,
review/commit, Vault proposal approval/apply, process bootstrap, and Monday session evidence.
The safe parked deployment was not touched.

DONE
