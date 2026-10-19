# cobalt.agents — the generic agent registry (F20, L16)

## 2026-10-18 — f20-cos-1018
Built by card 730 (FINAL §2 `agents/registry.py`; F-10, F-21). An agent exists only as a validated `configs/cobalt/agents/<id>.yaml`; a new one is written only by the HITL executor after his approved card (T1), and committed by `com.cobalt.generated` through `hitl_dirs` (F-07).

### Schema (`registry.py`, `extra="forbid"`)
One top-level `agent:` mapping: `id` (matches the file name), `charter`, `chassis` `{kind: sdk, auth: subscription, model: <alias>}`, `tools` (each in `TOOL_CATALOG`, the CoS tool server's seven names), `schedule` (optional), `memory_namespace`, `enabled`. Refused at load: an unknown tool, and any `auth` but `subscription` (R1112).

`voice.yaml` keeps its own loader (`cobalt.voice.registry.load_agent`); `list_agents` lists it by id and never re-validates it.

`render_entry` is the one canonical form of an entry: the bytes the card hashes, the page shows and the executor writes (F-18).

### Commands
`cobalt agents list` — every entry by id (`enabled` / `disabled` / `own loader`).

### Entries
`cos.yaml` — the chief of staff, model `claude-sonnet-5-5` (UNMEASURED, X17), the seven tools.

Tests: `test_agents_registry.py` (T9).
