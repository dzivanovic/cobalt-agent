# Radar marker fix — 2026-09-13

## §0 Headline

- FIXED: Screens apply now emits valid, ordinal-backed marker ids instead of free-text headings.
- VERIFIED: all four L45 real-shape screens are stable across derivations and re-apply without duplicate sections.
- LISTS: the identical defect was not present; Lists is one whole-note `create_if_absent` write and never calls `upsert_unit`.
- FINISH: `1065 passed, 239 skipped, 15 warnings in 18.82s`.
- ESCALATE: 0.

## Anchor choice

| Candidate | Verdict | Reason |
|---|---|---|
| Screen number | CHOSEN | The real note carries a unique ordinal in every heading: `Screen 1` through `Screen 4`. It is structural identity, survives edits to the display prose, and requires no note edit. |
| Slug of screen name | REJECTED | The note explicitly says names are Dejan's to edit freely. A renamed `Day Scan (after 10:00)` would otherwise change marker identity and append a second owned unit. |
| Explicit id in note | NOT REQUIRED | No explicit id exists today, and the existing ordinal is sufficient. Requiring one would unnecessarily block on a production-note edit. |

The derived section ids are `radar-screen-1` through `radar-screen-4`; the corresponding unit ids are `radar-screen-1-definition` through `radar-screen-4-definition`. Both match `^[A-Za-z0-9][A-Za-z0-9._:+-]*$`. The em dash, spaces, mixed case, and the `Day Scan (after 10:00)` parenthetical remain display/source evidence only and never enter a marker id. The older accepted `## 1 — Name` shape normalizes to the same ordinal id. Missing or duplicate numeric anchors fail loudly during derivation.

Proposal artifacts are intentionally artifact-exact under D13. Any proposal generated before this fix still contains the rejected free-text section names and must be regenerated (and reviewed under its new hash/token) rather than silently rewritten during apply.

## Defect-to-test map

| Defect / law | Test evidence | Verdict |
|---|---|---|
| Free-text heading was handed to `upsert_unit` and failed marker validation | `test_all_four_real_screen_marker_ids_are_valid_and_stable` runs all four headings from `radar-screens.real-shape.md` and checks every section and unit id against the production marker regex. | PASS |
| Marker identity could follow editable display prose | `test_real_screen_marker_ids_do_not_follow_editable_display_names` changes mixed-case names, including the parenthetical screen, while asserting unchanged marker ids. | PASS |
| Re-apply could append a duplicate section/unit | `test_real_screen_reapply_targets_existing_sections_without_duplicates` runs the real `VaultWriter` merge path twice against a temporary copy of the L45 fixture; pass two is unchanged and every section marker occurs once. | PASS |
| An absent or duplicated durable anchor must not be guessed | The real-shape refusal matrix now covers a non-ordinal heading; derivation also rejects duplicate ordinal-derived section ids. | PASS |
| Lists parity | `test_lists_artifact_records_watchlists_blob_and_verbatim_bytes` proves its proposal carries no section/unit marker id; `test_lists_apply_uses_create_if_absent_and_no_section_marker_id` proves apply calls `create_if_absent` and never `upsert_unit`. | PASS — no identical defect |

## Verification

| Command | Result |
|---|---|
| Focused pre-fix regression run | `3 failed, 44 passed` — reproduced the exact invalid `Screen 1 — Up Gappers` marker path. |
| Focused post-fix run | `48 passed in 1.34s` |
| Direct read-only derivation from `/Users/cobalt/Vault/Think/1 - Trading/Radar Screens.md` | Four pairs: `radar-screen-1`…`radar-screen-4`, each with its ordinal `-definition` unit id. |
| `uv run ruff check src/cobalt/radar/propose.py tests/cobalt/test_radar_propose.py` | `All checks passed!` |
| `uv run pytest tests/cobalt tests/taxonomy -q` | `1065 passed, 239 skipped, 15 warnings in 18.82s` |
| Same suite with `-rs` to audit skips | `1065 passed, 239 skipped, 15 warnings in 18.90s`; every skip was DB-gated. |

The finish suite ran with dotenv loading disabled and all known `POSTGRES_*` variables removed from the test process. Every one of the 239 skips reported a missing Postgres environment / `requires_db` reason; no test was skipped or loosened by this patch. The worktree `.env` was not read. The 15 warnings are the existing LiteLLM Python 3.14 `asyncio.iscoroutinefunction` deprecation warnings from `tests/taxonomy/test_names_rule.py`.

## ESCALATE

None.
