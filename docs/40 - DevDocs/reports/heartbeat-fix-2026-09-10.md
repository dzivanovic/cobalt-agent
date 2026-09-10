# Heartbeat market-reset fix — 2026-09-10

## Result

The heartbeat no longer lets its daily-note write decide whether probes,
alerts, or its job row survive. `run_beat` now logs and executes one ordered
path:

1. `PROBES`
2. `COMPOSE`
3. `ALERTS`
4. `PERSIST`
5. `VAULT`
6. `FINALIZE`

Every stage records a redacted failure on the `Beat`, logs it at ERROR, and
allows the next stage to run. Alert selection precedes persistence. FINALIZE
separately attempts the database update and corrective alert, so even a final
database failure cannot suppress the out-of-band RED for a failed vault write.

The vault stage asks `cobalt.session` first. A trading-day `market_reset`
returns `deferred_market_reset` before daily-note lookup, `VaultWriteStore`
setup, or `VaultWriter` construction, so it cannot add a
`vaultwrite:heartbeat:*` refusal. Outside that window, only a successful writer
result with a non-null write id is `written`; `None`, an id-less result, or an
exception is `failed`. `Beat.green` and every renderer preserve unrelated RED
findings during deferral and turn RED on failure.

Migration `src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql` adds the
nullable `vault_outcome` and `vault_reason` text columns to the declared
system-side `cobalt_jobs` table. It is in the fixed forward list; its named
rollback is
`src/cobalt/db_migrations/0003_heartbeat_vault_outcome.rollback.sql`, first in
the reverse list. Migration digests now exclude `user_id`, `vault_outcome`, and
`vault_reason`. A database-backed test wraps a populated `cobalt_jobs` row in a
transaction, executes rollback then forward, and requires identical row counts
and digests.

`com.cobalt.heartbeat` now enters through `cobalt jobs run`. The validated
`kill_switch_exempt` flag defaults false, is rejected on every label except the
heartbeat, and is true only on the heartbeat registry row. Wrapper setup,
registration, lifecycle writes, and completion writes are best-effort only for
that exempt job; each failure is loud and the subprocess still runs. The beat
records the switch state itself. Wrapper result persistence allowlists only
`argv` and `returncode` and JSON-merges those fields, while the beat owns probe
detail, stage failures, `green_summary_date`, and vault outcome/reason.

The existing `vaultwrite_blocks` probe in `probes.py` is unchanged.

## Review blocker mapping

### Round 1

1. **Deployment and rollback — items 4(iv) and 6.** The tracked heartbeat
   plist replaces its direct invocation with the F17 invocation. LIVE below
   separates plist installation from registry row registration and names both
   deployment and rollback.
2. **Empty `reads` and restart derivation — items 4(iv) and 6.** Heartbeat
   remains a one-shot with no `reads:`. The RULE-based derivation, including
   the unknown-path investigation requested in round 3, is printed below.
3. **F17 persistence ownership — items 4(i) and 5(e).** The wrapper has a
   strict two-field result allowlist and merge update; tests retain beat detail
   and `green_summary_date` after wrapper completion.
4. **Durable degradation and notification — items 1, 2, and 5(b).** Two
   durable columns, RED rendering, final persistence, and corrective
   out-of-band notification cover late failure, including `None`.
5. **Missing triage report — item 6.** This build and report use the supplied
   `heartbeat-blackout-2026-09-10.md` as the cause record: eight scheduled
   attempts reached the unguarded write and died before alerts/persistence.

### Round 2

1. **Late-failure reporting and reason storage — items 1, 2, and 5(b).** The
   FINALIZE stage persists both fields and sends the corrective RED. The test
   also combines vault failure with final database-update failure and proves
   the alert still runs.
2. **Wrapper database failure before launch — items 4(iii) and 5(f).** A
   wrapper test makes schema setup, registration, kill-switch read,
   `mark_running`, and `mark_finished` fail and proves the heartbeat subprocess
   still executes.
3. **Migration execution and digest proof — items 3 and 5(h).** Migration 0003
   and its rollback are registered. The populated-row proof excludes both new
   columns.
4. **Restart derivation — item 6.** The plist and every changed config are
   handled below; an unknown reader result is investigated explicitly rather
   than silently treated as no readers.

Round-2 risks are also covered: missing-note `None` is failed (item 2), the
19:59/20:00/20:59/21:00 and Labor Day cases are tested (items 2/5(g)), and a
deferred vault outcome cannot mask a failed probe (items 2/5(g)).

## Round-3 disposition

The concrete unknown-path defect was fixed in this report: reader analysis is
run for `configs/cobalt/jobs.yaml`, its exit 1 is retained, and its callers are
inspected before deriving RESTARTS. The FINALIZE database-plus-alert test was
also added. The review's “exactly as 0004” concern was correct: this is a
database-wide migration, so it uses the actual fixed-list precedent and next
available number, 0003; 0004 is a feature-local vaultwrite migration and is not
copied as a false precedent.

## DISSENT

> “LIVE’s ‘no DM expected’ assumes a healthy beat with today’s green summary already sent. A forced RED beat should still notify.”

Not adopted as a LIVE redesign because item 6 explicitly defines that forced
proof as the already-deduplicated healthy path; RED notification remains
mandatory and is proven deterministically by the suite stubs.

## Tests

- `uv run pytest -q tests/cobalt/test_heartbeat.py tests/cobalt/test_heartbeat_runner.py tests/cobalt/test_jobs.py tests/cobalt/test_jobs_reads.py tests/cobalt/test_notify_email.py --disable-warnings`
  — **113 passed, 19 skipped**.
- Focused migration-registration plus heartbeat/jobs run after the final
  ownership guard — **49 passed, 18 skipped**.
- `plutil -lint ops/com.cobalt.heartbeat.plist` — **OK**.
- `python -m compileall` for the changed packages — **OK**.
- `git diff --check` — **OK**.
- Database-backed migration execution, populated-row digest, and the complete
  new-core suite could not run in this isolated worktree: no `POSTGRES_HOST`,
  `COBALT_DB_USER`, `COBALT_DB_PASSWORD`, `POSTGRES_USER`, or
  `POSTGRES_PASSWORD` is present. The attempted new-core run collected 955
  tests and failed at the first real database access with `DbConfigError`.
- `uv run cobalt validate` likewise completed its file-backed taxonomy,
  calendar, and session checks, then exited 1 when the settings validator
  reached the same absent APP credential. It did **not** exit 0 here.
- A repository-wide pytest attempt is independently blocked during collection
  by the pre-existing legacy test import
  `tests/test_finviz_extractor.py:34` (`FinvizStockData` no longer exists).

No production checkout, vault, LaunchAgent, or production database was read or
mutated to bypass those missing credentials.

## RESTARTS derivation

`git diff --stat main` contains one plist under `ops/`:

```text
ops/com.cobalt.heartbeat.plist | 9 ++
```

It contains one changed configuration file:

```text
configs/cobalt/jobs.yaml | 4 +
```

The required command was run:

```text
$ uv run cobalt jobs readers configs/cobalt/jobs.yaml
UNKNOWN PATH: no job row lists 'configs/cobalt/jobs.yaml' as re-read at runtime.
exit 1
```

That result was not treated as “no readers.” `rg 'load_job_registry\('` shows
the loader in CLI commands, the F17 one-shot wrapper, watchdog/heartbeat code,
and other one-shot entry points. No resident request/server loop loads
`jobs.yaml`; one-shots re-read it when they start and therefore must retain an
empty `reads:` list. There is no resident restart to add for this config. The
changed plist itself must be replaced.

**RESTARTS: com.cobalt.heartbeat (plist changed: bootout old, bootstrap new)**

## LIVE

Run only after an ff-only merge into `~/cobalt`, outside market hours and the
20:00–21:30 ET exclusion in `ops/README.md`.

1. **MIGRATE.** Run `uv run cobalt db migrate --allow-prod`. Confirm the two
   nullable columns exist on `system.cobalt_jobs`. The feature rollback SQL is
   `src/cobalt/db_migrations/0003_heartbeat_vault_outcome.rollback.sql`; do not
   use the database-domain-wide `--rollback` merely to remove these columns,
   because that also reverses 0002 table placement.
2. **INSTALL THE REPLACEMENT PLIST.** Follow `ops/README.md`: boot out
   `gui/$(id -u)/com.cobalt.heartbeat`, copy
   `ops/com.cobalt.heartbeat.plist` to `~/Library/LaunchAgents/`, bootstrap that
   file, and use `launchctl print` to verify the loaded invocation contains
   `cobalt jobs run com.cobalt.heartbeat ... cobalt heartbeat beat`. Never load
   the old and new invocations side by side.
3. **REGISTER ROWS ONLY.** Run `uv run cobalt jobs register`. This updates DB
   rows; it does not install or reload a plist.
4. **FORCE ONE BEAT.** Kickstart `com.cobalt.heartbeat`. Proof: the row has
   `vault_outcome=written`; `last_result` contains current `argv`/`returncode`,
   beat fields, and the intact `green_summary_date`; the log prints PROBES →
   COMPOSE → ALERTS → PERSIST → VAULT → FINALIZE. No DM is expected when the
   healthy daily summary was already deduplicated; the RED paths are proven by
   deterministic tests.
5. **TONIGHT.** Inspect the first actual beat after 20:00 ET; the 900-second
   interval does not promise an exact minute. It must show
   `vault_outcome=deferred_market_reset`, retain the colour produced by its
   probes/jobs, and leave unchanged the count of `session_blocks` rows whose
   actor matches `vaultwrite:heartbeat:*`.

## Rollback

Revert the merge, boot out the changed heartbeat plist, reinstall/bootstrap the
previous plist, and execute
`src/cobalt/db_migrations/0003_heartbeat_vault_outcome.rollback.sql` through
the approved production migration connection. Verify the two columns are gone
and force one beat on the restored direct invocation.

DONE
