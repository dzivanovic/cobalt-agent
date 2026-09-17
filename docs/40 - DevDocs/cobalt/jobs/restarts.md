# `src/cobalt/jobs/restarts.py`

Derives resident restarts from changed plists, declared runtime reads, and a static Python import graph. Missing import declarations, unresolved dynamic imports, and unclassified paths are conservative and loud; worktree-ending ranges include untracked files.

Documentation paths — anything under `docs/`, or a root markdown file in `ROOT_DOCS` (`README.md`, `CLAUDE.md`, `AGENTS.md`, `QWEN.md`) — that no resident declares in `reads:` are labelled `DOCS` and derive no restart, not even the conservative set (L42 amendment O9, effective 2026-09-15). A documentation path a resident does read still derives that resident, because the reads check runs first.

A config path with no resident reader but a `no_resident_reads` declaration in `jobs.yaml` is ruled `no resident reads (one-shot: <labels>)` and derives no restart instead of `UNCLASSIFIED CONFIG` (ruled 2026-09-15; first row `configs/cobalt/notify.yaml`).

Paths under `.claude/` (the Claude Code harness settings, first committed 2026-09-15) are labelled `HARNESS; no Cobalt reader` and derive no restart.

---

## 2026-09-17 — S2-P4: a new one-shot plist says what it needs (R1-22/R2-6)

A plist ADDED (`A`) for a registered non-resident label now derives the rule
`plist in diff; new one-shot, bootstrap once: <label>` and restarts nothing.
Before this, a brand-new one-shot dropped out of the derivation silently.
The first case is `ops/com.cobalt.replay.plist`. The formation adapter in
`replay/runner.py` uses a static import on purpose: a string-named dynamic
import would mark every resident "unresolved".

## 2026-09-17 — S2-P4: smoke suite files are an operator command's input (§5, Astra R2-6)

A path under `configs/cobalt/smoke/` classifies as `operator command
(cobalt smoke); no job reads` and derives no restart. Without this rule,
`configs/cobalt/smoke/s2.yaml` fell to `UNCLASSIFIED CONFIG` and escalated
every resident.

`test_a_smoke_suite_file_derives_no_restart_and_no_job_runs_the_smoke`
checks the claim behind the rule, not only its output:
- no `ops/com.cobalt.*.plist` invokes `smoke`;
- the only source files that open a suite are `smoke/cli.py` and `smoke/config.py`.

Import reach is deliberately not the test. `com.cobalt.radar` enters
through `cobalt.cli`, which mounts every command module, so a change to
smoke's code still derives that restart by the ordinary `src/` rule.
