# `src/cobalt/jobs/restarts.py`

Derives resident restarts from changed plists, declared runtime reads, and a static Python import graph. Missing import declarations, unresolved dynamic imports, and unclassified paths are conservative and loud; worktree-ending ranges include untracked files.

Documentation paths — anything under `docs/`, or a root markdown file in `ROOT_DOCS` (`README.md`, `CLAUDE.md`, `AGENTS.md`, `QWEN.md`) — that no resident declares in `reads:` are labelled `DOCS` and derive no restart, not even the conservative set (L42 amendment O9, effective 2026-09-15). A documentation path a resident does read still derives that resident, because the reads check runs first.

A config path with no resident reader but a `no_resident_reads` declaration in `jobs.yaml` is ruled `no resident reads (one-shot: <labels>)` and derives no restart instead of `UNCLASSIFIED CONFIG` (ruled 2026-09-15; first row `configs/cobalt/notify.yaml`).

Paths under `.claude/` (the Claude Code harness settings, first committed 2026-09-15) are labelled `HARNESS; no Cobalt reader` and derive no restart.
