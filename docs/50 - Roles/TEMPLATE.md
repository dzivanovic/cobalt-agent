# Role Pack Template

A role pack is the standing definition for one of Dejan's operating
roles. Today these are separate manual chat sessions — TRIAGE.md's
Operating Rhythm names them: project / coach / DRC debrief /
day-organizer, "the manual prototypes of Cobalt's future agents." This
pack format is how each formalizes, ahead of the GrokBot/Hermes-agent
north star (persistent, config-driven specialist bots under one
chief-of-staff orchestrator — TRIAGE cross-cutting "Agent architecture
north star").

Copy this file to `docs/roles/<role-name>.md` per role and fill it in.
MODELS.md is the single source of truth for tier assignments — reference
it here, don't repeat the table.

---

## Charter

- **Job**: one or two sentences — what this role exists to do.
- **Boundaries**: what it explicitly does NOT do (guards against scope
  creep or overlap with another role).
- **Success signal**: how you know the role is doing its job — a
  trader/operator signal, not a vanity metric (TRIAGE Charter
  requirements: success criteria are trader metrics, not software
  metrics).

## Prompts

- **Current**: where the live prompt text lives today (ad hoc,
  hand-written per session — note it, don't leave it undocumented).
- **Target**: config path once formalized — anti-rigidity rule,
  config-driven agents, never hardcoded behavior (e.g.
  `configs/roles/<role>.yaml` or a `prompts.yaml` section).
- **Persona notes**: tone/register specifics for this role, if any (link
  to harvested Persona strings per TRIAGE 2.5's harvest rider, if
  applicable).

## Routing + Rationale

- **Current tier**: see MODELS.md — do not duplicate the table here.
- **Why this tier**: the task shape driving the choice — reasoning
  depth, stakes, cost/latency tolerance (non-negotiable: token
  conservation, be honest about which tier a task needs).
- **Retier trigger**: what would have to change about this role's job to
  justify moving tiers (promotion rule: model follows function).

## State Locations

- **Memory/context today**: where this role's history lives now (a chat
  session export, an Obsidian note, or nothing durable yet).
- **Future**: the Postgres/Hippocampus table or vault path once this
  role becomes an automated agent — gated on the Data-Model + Vault
  design session (TRIAGE 2.1/2.6).
- **Logs/artifacts**: anything durable this role produces (e.g. the DRC
  role produces daily report card notes).
