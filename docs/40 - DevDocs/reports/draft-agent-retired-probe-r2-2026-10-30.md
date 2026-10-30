## §0 Headline
- Card 1099 edited in place; header values `BASE`, `TIP`, `CHECK REPORT`, `HOUSE B`, `RULINGS` and the brain's RECORDS line untouched.
- FAIL 9: K1 `files` gains `tests/cobalt/test_cos_registry.py`; its `_k18` patches `RETIRED_LABELS_PATH` to an absent `tmp_path` file.
- FAIL 13: `RESTARTS: com.cobalt.cos, com.cobalt.radar`; third RECORDS line carries both import chains and the desk's `jobs restarts` run.
- Three NOTES applied (K1 FAIL gate, `enabled: false` in NOT IN THIS JOB, T1/`_k18` patch). Nothing run, nothing committed.

## DECISIONS
- ASK DESK: the card fixes `test_cos_registry.py` by patching `RETIRED_LABELS_PATH` to an absent file (the file's own pattern for the owed file), not by answering `launchctl_loaded` False for `com.cobalt.agent`. Default: the patch. [07:25]

## RECORDS
- `date` 07:18 ET at start (2026-10-30).
- Read: card 1099, preflight `## ISSUES`, `topics/writing-rules.md`.
- `git -C … show main:tests/cobalt/test_cos_registry.py`: `_k18` (`:80-110`) patches `BOOTSTRAP_OWED_PATH` only, `launchctl_loaded=lambda label: label != COS_LABEL`, so `com.cobalt.agent` reads loaded; no `RETIRED_LABELS_PATH` patch. The patch matches the file; the False-answer would rewrite its lambda.
- `git grep -n main -- src/cobalt/cos/run.py`: `:50` `from cobalt.jobs.watchdog import pidfile_alive`.
- `git grep main -- configs/cobalt/jobs.yaml`: `:203` `com.cobalt.radar` `imports: [cobalt.cli]`.
- `git grep main -- src/cobalt/cli.py`: `:72` `from cobalt.jobs import cli as jobs_cli`, `:77` `from cobalt.smoke import cli as smoke_cli`; `jobs/cli.py:27` `from .watchdog import sweep`; `smoke/cli.py:29` `from .checks import …`.
- The `restarts` derivation was not run (no `uv`; UNPROVEN until the desk runs it).

DRAFTED · decisions: 1
