## BLOCKERS

- **Correct deployment and rollback.** Brief line 8 claims `cobalt jobs register` installs plist changes; it only upserts database rows (`src/cobalt/jobs/cli.py:63`). Installed plists require separate installation (`ops/README.md:3`, `ops/README.md:152`). Specify replacement/reload steps and verify the loaded invocation; registration alone leaves the old invocation active.
- **Keep heartbeat `reads` empty.** Brief line 6 requests loader-derived `reads`, but heartbeat is a one-shot (`configs/cobalt/jobs.yaml:206`), and nonempty `reads` explicitly fails validation (`src/cobalt/jobs/config.py:290`). Document dependencies separately. Derive `RESTARTS:` for every changed configuration as required by `ops/README.md:175`; heartbeat’s interval alone does not justify “none.”
- **Define persistence ownership under F17.** Brief lines 4–6 combine early beat persistence with wrapper enrollment without addressing overwrite: the subprocess wrapper stores only `argv`/`returncode` (`src/cobalt/jobs/cli.py:137`), and wrapper completion replaces `last_result` (`src/cobalt/jobs/wrapper.py:161`, `src/cobalt/jobs/store.py:162`). Specify preservation of beat details and `green_summary_date`, which controls daily DM deduplication (`src/cobalt/heartbeat/runner.py:165`).
- **Define durable degradation and notification behavior.** Brief line 5 requires degradation after persistence and alerts. Existing persistence excludes notes (`src/cobalt/heartbeat/runner.py:279`), and notes cannot change `Beat.green` (`src/cobalt/heartbeat/render.py:43`). Require a persisted final vault outcome and explicit handling of an otherwise-green beat whose vault write fails after alert selection.
- **Supply the referenced triage report.** Brief line 2 names `docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md`, which is absent from this checkout and tracked-file listing. The unguarded write is confirmed (`src/cobalt/heartbeat/runner.py:249`), but the incident’s timing and lost-beat count cannot be checked against its cited evidence.

## RISKS

- Persistence remains upstream of out-of-band alerts; database failure can still suppress them (`src/cobalt/heartbeat/runner.py:246`). Define and test that failure path.
- F17 enrollment introduces kill-switch suppression of heartbeat (`src/cobalt/jobs/wrapper.py:137`). Confirm that monitoring should stop with other jobs.
- A forced beat does not guarantee a DM: green alerts are daily and deduplicated (`src/cobalt/heartbeat/runner.py:271`). The acceptance procedure needs a deterministic alert trigger.
- “Tonight’s 20:05 beat” is not guaranteed by the 900-second `StartInterval` (`ops/com.cobalt.heartbeat.plist:51`). Test session boundaries and use the actual scheduled firing.
- Leaving refusal counts informational matches existing intent (`src/cobalt/heartbeat/probes.py:323`). Scope “zero session_blocks” evidence to heartbeat; other writers share the counter.

## VERDICT RETHINK

The vault-last direction addresses the confirmed failure, but deployment, wrapper result ownership, and durable degradation need correction before build.
