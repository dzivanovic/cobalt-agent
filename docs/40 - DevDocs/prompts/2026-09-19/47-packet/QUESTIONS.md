# QUESTIONS — house read of the APPEND-ONLY ARCHIVER's rounds 3 / 3b / DB-re-run code (`9056e73..186c9a9`)

You are reading the LAST unread code of a build that ships to production in DEPLOY 3 (Sunday). Every earlier round of this build was read by the four-house tribunal and by at least three checkers; these three commits landed after that and no house has seen them. They exist because Dejan ruled twice on two red `requires_db` tests.

`commits.txt` lists them; `folds.diff` is the complete code diff (docs excluded). `rulings.md` carries his two rulings verbatim and the design section they touch.

**Q1 — R25 (`193a2ca`), the REVOKE.** His ruling: migrations `0010`/`0011` carry an EXPLICIT `REVOKE` so `cobalt_user` cannot read `system.archive_progress` / `system.archive_incidents`, because `0001_schemas.sql`'s blanket `GRANT SELECT ON ALL TABLES IN SCHEMA system TO cobalt_user` and its `ALTER DEFAULT PRIVILEGES` would otherwise grant it. (a) Does the SQL do exactly that and nothing more? (b) Is the revoke complete — table AND its sequence AND any default-privilege path that could re-grant it on a later migration? (c) Is it idempotent: does applying `0010`/`0011` twice still end in the same state, and does the rollback SQL leave nothing behind? (d) Does the revoke break any OTHER role or any existing reader — name the role and the call site if so.

**Q2 — R26 (`ecb817c`), the dropped test.** His ruling: `test_archiver_append_store.py::test_the_own_connection_upsert_survives_another_transactions_rollback` is DROPPED because the dev harness's single-transaction fixture makes a real commit unobservable; the three OFFLINE pins of `upsert_bars`'s own connection and of the only `DO UPDATE` stay. (a) Were exactly those three pins kept, and do they actually pin what they claim — quote each assertion? (b) Did the drop remove coverage of anything ELSE that no remaining test covers? Name the behaviour and the missing test. (c) Is anything left behind — a now-unused fixture, import, helper or docstring that still describes the deleted test?

**Q3 — `d2099e1`, the advisory-lock test.** It replaces two savepoint proxies with two real sessions. (a) Does the new shape actually prove mutual exclusion, or can it pass with the lock absent? (b) Can it hang, leak a connection, or leave a lock held if it fails mid-way?

**Q4 — the whole diff, adversarially.** Read every hunk and ask: does anything here change PRODUCTION behaviour rather than test behaviour? The build ships in `upsert` mode, which is meant to be today's behaviour byte for byte. Anything in these three commits that could alter what the nightly archiver writes, when it writes it, or what it refuses, is a BLOCKER — name it with file:line.

**Q5 — anything else you would not ship**, with severity BLOCKER / MAJOR / MINOR and a one-line fix each.

Your verdict line: `VERDICT: SAFE TO DEPLOY` or `VERDICT: FIX FIRST <numbers>` or `VERDICT: DO NOT DEPLOY <numbers>`.
