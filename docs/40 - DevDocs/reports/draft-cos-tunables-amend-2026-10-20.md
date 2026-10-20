# draft-cos-tunables-amend · card 933 · 2026-10-20

## §0 Headline
Card 933 amended in place for preflight round 1 (fail 2, notes 3, 5, 7).
P1 now owns `test_cos_probes.py`: `test_disabled_row_is_unknown` rewritten as an invariant, docstring `:4`, two `bootstrap_owed` patches, file named outright.
Suites list names `test_cos_probes.py`; DEPLOY PROOF carries both marker conditions.
Fail 1, notes 4 and 6 untouched. Nothing run, nothing committed.

## DECISIONS
None.

## RECORDS
- 2026-10-20 17:51 EDT (`date`).
- Read: `prompts/2026-10-20/940-draft-cos-tunables-amend.md`, `prompts/2026-10-20/933-cos-tunables-card.md`, `reports/cos-tunables-preflight-2026-10-20.md`, `Vault/.../topics/writing-rules.md`, `src/cobalt/heartbeat/probes.py:124-190` (working tree; `git diff main --stat` over it and `tests/cobalt/test_cos_probes.py` printed nothing, so tree = main).
- `git show main:tests/cobalt/test_cos_probes.py`: `:4` docstring, `:26-34` `test_dead_session_is_red`, `:37-42` `test_disabled_row_is_unknown` (`:42` asserts `"enabled: false"`), `:45-56` `test_pending_past_ttl_and_failed_execution_are_red`.
- Edited only the card: P1 (what, red first, files), T2 (comment wording), Suites, DEPLOY PROOF.

DRAFTED · decisions: 0
