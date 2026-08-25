# MODELS.md — Fleet Tiering (Human-Operated Roles)

Cobalt's agents don't exist yet as automated bots — today Dejan runs
each role as a separate manual chat session (TRIAGE.md's Operating
Rhythm: project / coach / DRC debrief / day-organizer — "the manual
prototypes of Cobalt's future agents"). This file is the single source
of truth for which model tier serves each role. Individual role packs
(`docs/roles/<role>.md`, built from TEMPLATE.md) reference this table
rather than repeating it.

## Current tiering

| Role | Model | Model ID |
|---|---|---|
| Planning | Fable 5 | `claude-fable-5` |
| Coach | Fable 5 | `claude-fable-5` |
| DRC (Daily Report Card debrief) | Sonnet 5 | `claude-sonnet-5` |
| Logistics (day-organizer) | Sonnet 5 | `claude-sonnet-5` |

## Promotion rule

**Model follows function — retier when the role's job changes.**

Not a fixed assignment and not a schedule. A role moves up a tier when
its job starts demanding more of what the higher tier buys (deeper
reasoning, broader judgment, higher-stakes calls); it moves down when
the job simplifies into something mechanical a cheaper/faster tier
handles just as well. Retiering follows from the job changing — never
from preference or a hype-driven default swap (non-negotiable: token
conservation, be honest about which tier a task needs).

## How to apply

- Before retiering a role, name what specifically changed about its job
  — not just "the new model seems better."
- Update the table above when a tier changes, and add a line to the
  retiering log below with the date and the one-line reason.
- This table is authoritative; role packs' Routing + Rationale sections
  reference it, they don't duplicate it.

## Retiering log

_(none yet — entries land here when a role's job changes and its tier
moves)_
