Reading additional input from stdin...
OpenAI Codex v0.153.4
--------
workdir: /Users/cobalt/cobalt-wt/heartbeat-mr
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a08b66-96eb-7912-bf87-14401c27d5e1
--------
user
Round 3, final. Review docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md against your rounds at _inflight/heartbeat-fix-astra.md and -r2.md, src/cobalt/heartbeat/, src/cobalt/jobs/, db_migrations/, jobs.yaml, ops/README.md and the triage report. For each round-1 and round-2 blocker: RESOLVED or OPEN with file:line. Then BLOCKERS / RISKS / VERDICT.
hook: SessionStart
hook: SessionStart Completed
codex
I’ll check the final brief against both prior reviews and the implementation, then mark each blocker RESOLVED or OPEN with file and line references.
exec
/bin/zsh -lc "pwd; rg --files -g AGENTS.md -g '*heartbeat*' -g '*triage*' -g jobs.yaml -g README.md -g '*astra*'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
/Users/cobalt/cobalt-wt/heartbeat-mr
ops/pending/README.md
ops/README.md
ops/com.cobalt.heartbeat.plist
configs/cobalt/jobs.yaml
README.md
docs/20 - Assessment/README.md
docs/_archive/README.md
docs/10 - Decisions/README.md
docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md
docs/40 - DevDocs/reports/mainframe-triage-2026-09-07.md
docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md
docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra-r3.md
docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra.md
docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra-r2.md
docs/40 - DevDocs/cobalt/vaultwrite/README.md
docs/90 - References/trade-reporter/README.md
docs/90 - References/trade-reporter/utils/README.md
docs/00 - Project/README.md
docs/30 - Design/TRADE-RADAR-CARD-MOCK-v0_1/README.md
docs/30 - Design/README.md
tests/cobalt/test_heartbeat.py

exec
/bin/zsh -lc 'for p in /AGENTS.md /Users/AGENTS.md /Users/cobalt/AGENTS.md /Users/cobalt/cobalt-wt/AGENTS.md /Users/cobalt/cobalt-wt/heartbeat-mr/AGENTS.md; do if [ -f "$p" ]; then printf '"'%s\\n' \""'$p"; cat "$p"; fi; done' in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
exec
/bin/zsh -lc "nl -ba 'docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra.md'; nl -ba 'docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra-r2.md'; nl -ba 'docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
     1	## BLOCKERS
     2	
     3	- **Correct deployment and rollback.** Brief line 8 claims `cobalt jobs register` installs plist changes; it only upserts database rows (`src/cobalt/jobs/cli.py:63`). Installed plists require separate installation (`ops/README.md:3`, `ops/README.md:152`). Specify replacement/reload steps and verify the loaded invocation; registration alone leaves the old invocation active.
     4	- **Keep heartbeat `reads` empty.** Brief line 6 requests loader-derived `reads`, but heartbeat is a one-shot (`configs/cobalt/jobs.yaml:206`), and nonempty `reads` explicitly fails validation (`src/cobalt/jobs/config.py:290`). Document dependencies separately. Derive `RESTARTS:` for every changed configuration as required by `ops/README.md:175`; heartbeat’s interval alone does not justify “none.”
     5	- **Define persistence ownership under F17.** Brief lines 4–6 combine early beat persistence with wrapper enrollment without addressing overwrite: the subprocess wrapper stores only `argv`/`returncode` (`src/cobalt/jobs/cli.py:137`), and wrapper completion replaces `last_result` (`src/cobalt/jobs/wrapper.py:161`, `src/cobalt/jobs/store.py:162`). Specify preservation of beat details and `green_summary_date`, which controls daily DM deduplication (`src/cobalt/heartbeat/runner.py:165`).
     6	- **Define durable degradation and notification behavior.** Brief line 5 requires degradation after persistence and alerts. Existing persistence excludes notes (`src/cobalt/heartbeat/runner.py:279`), and notes cannot change `Beat.green` (`src/cobalt/heartbeat/render.py:43`). Require a persisted final vault outcome and explicit handling of an otherwise-green beat whose vault write fails after alert selection.
     7	- **Supply the referenced triage report.** Brief line 2 names `docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md`, which is absent from this checkout and tracked-file listing. The unguarded write is confirmed (`src/cobalt/heartbeat/runner.py:249`), but the incident’s timing and lost-beat count cannot be checked against its cited evidence.
     8	
     9	## RISKS
    10	
    11	- Persistence remains upstream of out-of-band alerts; database failure can still suppress them (`src/cobalt/heartbeat/runner.py:246`). Define and test that failure path.
    12	- F17 enrollment introduces kill-switch suppression of heartbeat (`src/cobalt/jobs/wrapper.py:137`). Confirm that monitoring should stop with other jobs.
    13	- A forced beat does not guarantee a DM: green alerts are daily and deduplicated (`src/cobalt/heartbeat/runner.py:271`). The acceptance procedure needs a deterministic alert trigger.
    14	- “Tonight’s 20:05 beat” is not guaranteed by the 900-second `StartInterval` (`ops/com.cobalt.heartbeat.plist:51`). Test session boundaries and use the actual scheduled firing.
    15	- Leaving refusal counts informational matches existing intent (`src/cobalt/heartbeat/probes.py:323`). Scope “zero session_blocks” evidence to heartbeat; other writers share the counter.
    16	
    17	## VERDICT RETHINK
    18	
    19	The vault-last direction addresses the confirmed failure, but deployment, wrapper result ownership, and durable degradation need correction before build.
     1	Reading additional input from stdin...
     2	OpenAI Codex v0.153.4
     3	--------
     4	workdir: /Users/cobalt/cobalt-wt/heartbeat-mr
     5	model: gpt-6-astra
     6	provider: openai
     7	approval: never
     8	sandbox: read-only
     9	reasoning effort: high
    10	reasoning summaries: none
    11	session id: 01a08b5c-aa27-7fa3-818b-7231abc5a0cb
    12	--------
    13	user
    14	Round 2. Review docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md against your round-1 review at _inflight/heartbeat-fix-astra.md, src/cobalt/heartbeat/ (runner.py, render.py, probes.py), src/cobalt/jobs/ (cli.py, config.py, wrapper.py, store.py), jobs.yaml, ops/README.md and the triage report. State for each round-1 blocker RESOLVED or OPEN with file:line evidence, then BLOCKERS (new or still open) / RISKS / VERDICT SHIP or RETHINK.
    15	hook: SessionStart
    16	hook: SessionStart Completed
    17	codex
    18	I’ll check the revised brief against the round-1 blockers, implementation, and triage report, then give a verdict with file and line evidence.
    19	exec
    20	/bin/zsh -lc "pwd; rg --files -g 'AGENTS.md' -g '*heartbeat*' -g '*triage*' -g 'jobs.yaml' -g 'README.md' -g 'runner.py' -g 'render.py' -g 'probes.py' -g 'cli.py' -g 'config.py' -g 'wrapper.py' -g 'store.py'" in /Users/cobalt/cobalt-wt/heartbeat-mr
    21	 succeeded in 0ms:
    22	/Users/cobalt/cobalt-wt/heartbeat-mr
    23	src/cobalt_agent/interfaces/cli.py
    24	src/cobalt_agent/config.py
    25	src/cobalt/session/cli.py
    26	src/cobalt/session/store.py
    27	src/cobalt/seatusage/cli.py
    28	src/cobalt/seatusage/config.py
    29	src/cobalt/seatusage/runner.py
    30	src/cobalt/db_migrations/cli.py
    31	src/cobalt/aset/config.py
    32	src/cobalt/aset/store.py
    33	src/cobalt/backup/cli.py
    34	src/cobalt/backup/config.py
    35	src/cobalt/jobs/cli.py
    36	src/cobalt/jobs/config.py
    37	src/cobalt/jobs/wrapper.py
    38	src/cobalt/jobs/store.py
    39	src/cobalt/vaultwrite/store.py
    40	src/cobalt/taxonomy/cli.py
    41	src/cobalt/taxonomy/store.py
    42	src/cobalt/cli.py
    43	src/cobalt/heartbeat/probes.py
    44	src/cobalt/heartbeat/cli.py
    45	src/cobalt/heartbeat/render.py
    46	src/cobalt/heartbeat/runner.py
    47	src/cobalt/redact/config.py
    48	src/cobalt/redact/store.py
    49	src/cobalt/daymode/cli.py
    50	src/cobalt/daymode/config.py
    51	src/cobalt/daymode/store.py
    52	src/cobalt/archiver/config.py
    53	src/cobalt/archiver/runner.py
    54	src/cobalt/archiver/store.py
    55	src/cobalt/cards/cli.py
    56	src/cobalt/cards/store.py
    57	src/cobalt/prefill/cli.py
    58	src/cobalt/prefill/config.py
    59	src/cobalt/notify/cli.py
    60	src/cobalt/notify/config.py
    61	src/cobalt/notify/store.py
    62	src/cobalt/settings/cli.py
    63	src/cobalt/settings/store.py
    64	src/cobalt/generated/cli.py
    65	src/cobalt/generated/config.py
    66	ops/pending/README.md
    67	ops/README.md
    68	ops/com.cobalt.heartbeat.plist
    69	configs/cobalt/jobs.yaml
    70	README.md
    71	docs/20 - Assessment/README.md
    72	tests/cobalt/test_heartbeat.py
    73	docs/_archive/README.md
    74	docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md
    75	docs/40 - DevDocs/reports/mainframe-triage-2026-09-07.md
    76	docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md
    77	docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra.md
    78	docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra-r2.md
    79	docs/40 - DevDocs/cobalt/vaultwrite/README.md
    80	docs/10 - Decisions/README.md
    81	docs/00 - Project/README.md
    82	docs/30 - Design/TRADE-RADAR-CARD-MOCK-v0_1/README.md
    83	docs/30 - Design/README.md
    84	docs/90 - References/trade-reporter/README.md
    85	docs/90 - References/trade-reporter/utils/README.md
    86	
    87	exec
    88	/bin/zsh -lc "nl -ba 'docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra.md'; nl -ba 'docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md'" in /Users/cobalt/cobalt-wt/heartbeat-mr
    89	 succeeded in 0ms:
    90	     1	## BLOCKERS
    91	     2	
    92	     3	- **Correct deployment and rollback.** Brief line 8 claims `cobalt jobs register` installs plist changes; it only upserts database rows (`src/cobalt/jobs/cli.py:63`). Installed plists require separate installation (`ops/README.md:3`, `ops/README.md:152`). Specify replacement/reload steps and verify the loaded invocation; registration alone leaves the old invocation active.
    93	     4	- **Keep heartbeat `reads` empty.** Brief line 6 requests loader-derived `reads`, but heartbeat is a one-shot (`configs/cobalt/jobs.yaml:206`), and nonempty `reads` explicitly fails validation (`src/cobalt/jobs/config.py:290`). Document dependencies separately. Derive `RESTARTS:` for every changed configuration as required by `ops/README.md:175`; heartbeat’s interval alone does not justify “none.”
    94	     5	- **Define persistence ownership under F17.** Brief lines 4–6 combine early beat persistence with wrapper enrollment without addressing overwrite: the subprocess wrapper stores only `argv`/`returncode` (`src/cobalt/jobs/cli.py:137`), and wrapper completion replaces `last_result` (`src/cobalt/jobs/wrapper.py:161`, `src/cobalt/jobs/store.py:162`). Specify preservation of beat details and `green_summary_date`, which controls daily DM deduplication (`src/cobalt/heartbeat/runner.py:165`).
    95	     6	- **Define durable degradation and notification behavior.** Brief line 5 requires degradation after persistence and alerts. Existing persistence excludes notes (`src/cobalt/heartbeat/runner.py:279`), and notes cannot change `Beat.green` (`src/cobalt/heartbeat/render.py:43`). Require a persisted final vault outcome and explicit handling of an otherwise-green beat whose vault write fails after alert selection.
    96	     7	- **Supply the referenced triage report.** Brief line 2 names `docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md`, which is absent from this checkout and tracked-file listing. The unguarded write is confirmed (`src/cobalt/heartbeat/runner.py:249`), but the incident’s timing and lost-beat count cannot be checked against its cited evidence.
    97	     8	
    98	     9	## RISKS
    99	    10	
   100	    11	- Persistence remains upstream of out-of-band alerts; database failure can still suppress them (`src/cobalt/heartbeat/runner.py:246`). Define and test that failure path.
   101	    12	- F17 enrollment introduces kill-switch suppression of heartbeat (`src/cobalt/jobs/wrapper.py:137`). Confirm that monitoring should stop with other jobs.
   102	    13	- A forced beat does not guarantee a DM: green alerts are daily and deduplicated (`src/cobalt/heartbeat/runner.py:271`). The acceptance procedure needs a deterministic alert trigger.
   103	    14	- “Tonight’s 20:05 beat” is not guaranteed by the 900-second `StartInterval` (`ops/com.cobalt.heartbeat.plist:51`). Test session boundaries and use the actual scheduled firing.
   104	    15	- Leaving refusal counts informational matches existing intent (`src/cobalt/heartbeat/probes.py:323`). Scope “zero session_blocks” evidence to heartbeat; other writers share the counter.
   105	    16	
   106	    17	## VERDICT RETHINK
   107	    18	
   108	    19	The vault-last direction addresses the confirmed failure, but deployment, wrapper result ownership, and durable degradation need correction before build.
   109	     1	Worktree ~/cobalt-wt/heartbeat-mr, branch ops/heartbeat-market-reset. You cannot commit; leave the diff + report. No production paths (~/cobalt, ~/Vault, launchd) touched. Laws: fail loud; one path; fresh code. Inputs: docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md (cause), _inflight/heartbeat-fix-astra.md (round-1 review — every blocker there is addressed by a numbered item below; cite the item in your report).
   110	     2	Cause: run_beat writes the daily-note unit unguarded at runner.py:249, upstream of alerts (:269-270) and the beat row (:291-292); F1's market_reset block (20:00–21:00 ET) raises SessionBlocked there and the whole beat dies — 4 beats/night, traceback only in logs/heartbeat.err. The heartbeat is the one job outside the F17 wrapper. probes.py:321 (vaultwrite_blocks) stays as is.
   111	     3	Build:
   112	     4	1. Stage order in run_beat: probes → compose beat → alerts (RED out-of-band; green DM under the existing green_summary_date dedup) → persist beat row → vault unit LAST. Every stage isolated: a stage failure is logged loud, recorded in the beat (stage name + reason) and never aborts the following stages. Alerts never depend on persistence succeeding (Astra risk 1).
   113	     5	2. Vault step: consult the session clock (cobalt.session) first. market_reset → no write attempt, outcome `deferred_market_reset`. Otherwise write; any exception → outcome `failed` with the reason. Outcome is a PERSISTED column on the beat row: `vault_outcome` text nullable (`written | deferred_market_reset | failed`) — migration + placement declaration (system side) + rollback sql; render.py reads it: `deferred_market_reset` keeps GREEN, `failed` renders RED (Astra blocker 4). Human-readable reason goes in the existing notes/message field as well.
   114	     6	3. F17 wrapper enrolment for com.cobalt.heartbeat with three invariants (Astra blocker 3): (i) the wrapper writes ONLY its own fields (argv, returncode, started/finished) and never overwrites beat detail or `green_summary_date` — partial update or separate columns, your choice, one path; (ii) kill-switch EXEMPTION: the heartbeat keeps running while the switch is on and the beat reports the switch state — implement as a validated per-job flag in the JobSpec, default false, true only for the heartbeat (Astra risk 2, ruled); (iii) the wrapper replaces the current invocation — new plist in ops/ per the existing install procedure in ops/README, never side by side. NO `reads:` — the heartbeat is one-shot and the schema rejects it (Astra blocker 2).
   115	     7	4. Tests: (a) market_reset → alerts sent (stub), row persisted with `vault_outcome=deferred_market_reset`, ZERO write attempts, zero new session_blocks rows with actor `vaultwrite:heartbeat:*`; (b) SessionBlocked or any exception raised by the vault step outside the window → `vault_outcome=failed`, beat RED, alerts + row present; (c) ordering: an exception in any stage never suppresses the later stages; (d) registry/plist parity for the heartbeat + JobSpec flag validation; (e) after a wrapped run, beat detail and `green_summary_date` are unchanged by the wrapper. Full suite green (1092+); `uv run cobalt validate` exit 0.
   116	     8	5. Report docs/40 - DevDocs/reports/heartbeat-fix-2026-09-10.md: what changed, why, which Astra item each change answers, test results, and `RESTARTS: com.cobalt.heartbeat (bootout old plist, bootstrap new)` (Astra blocker 1). LIVE block as named steps: (1) after ff-only merge, `cobalt db migrate --allow-prod` (one nullable column; rollback = the rollback sql); (2) plist install per ops/README (bootout old, bootstrap new); (3) `cobalt jobs register` (rows only); (4) force one beat; proof = beat row shows `vault_outcome=written`, wrapper fields present AND beat fields + `green_summary_date` intact, log shows the stage order; no DM expected (dedup) — the RED path is proven by suite stubs; (5) tonight: the FIRST beat after 20:00 (900 s interval, exact minute not guaranteed) lands `vault_outcome=deferred_market_reset`, GREEN, and the count of session_blocks rows with actor `vaultwrite:heartbeat:*` does not grow. Rollback: `git revert`, reinstall the previous plist, migration rollback sql. Print DONE as the last line.
   117	
   118	exec
   119	/bin/zsh -lc 'nl -ba src/cobalt/heartbeat/runner.py; nl -ba src/cobalt/heartbeat/render.py; nl -ba src/cobalt/heartbeat/probes.py' in /Users/cobalt/cobalt-wt/heartbeat-mr
   120	exec
   121	/bin/zsh -lc 'for p in /AGENTS.md /Users/AGENTS.md /Users/cobalt/AGENTS.md /Users/cobalt/cobalt-wt/AGENTS.md /Users/cobalt/cobalt-wt/heartbeat-mr/AGENTS.md; do if [ -f "$p" ]; then printf '"'%s\\n' \""'$p"; cat "$p"; fi; done; rg --files --hidden -g AGENTS.md -g '"'"'!'"\\.git' docs src ops configs" in /Users/cobalt/cobalt-wt/heartbeat-mr
   122	 exited 1 in 0ms:
   123	 succeeded in 0ms:
   124	     1	"""F18 heartbeat host — the beat itself (Charter §3 F18, M10).
   125	     2	
   126	     3	    uv run cobalt heartbeat beat
   127	     4	
   128	     5	WHAT ONE BEAT DOES, in order:
   129	     6	
   130	     7	1. probes everything (`probes.py`) and sweeps every job row
   131	     8	   (`jobs.watchdog`);
   132	     9	2. writes a Cobalt-owned red/green block into TODAY'S daily note through
   133	    10	   `VaultWriter` — one L28 unit, updated in place, one diff per beat;
   134	    11	3. on red, sends the SECOND channel first (email, over Layer-B Google
   135	    12	   OAuth — `out_of_band` below), so that its outcome can appear in the
   136	    13	   DM;
   137	    14	4. DMs on any red — carrying "email channel DOWN: <reason>" when the
   138	    15	   second channel failed — plus one green summary a day at
   139	    16	   `heartbeat.green_summary_at`. The GREEN summary is DM-only: a daily
   140	    17	   all-clear in the alert inbox is how an alert inbox stops being read.
   141	    18	
   142	    19	THE ALERT PATH IS NOT THE MONITORED PATH (Charter §3 F18). The DM goes
   143	    20	over Mattermost, which is one of the things being watched — so a
   144	    21	Mattermost outage would take the alert about the Mattermost outage with
   145	    22	it. That is the whole reason F18 asks for a second channel, and since
   146	    23	S1-P4 that channel exists: `cobalt.notify.email`, whose docstring states
   147	    24	the exact dependency chain. It needs neither Mattermost, nor Postgres,
   148	    25	nor the Obsidian vault. The `email` probe watches the watcher.
   149	    26	
   150	    27	WHY THE BEAT NEVER RAISES ON A RED. A red heartbeat is the heartbeat
   151	    28	WORKING. It exits 0 and says RED loudly; it exits non-zero only when the
   152	    29	beat itself could not run, because a job row that flips to `failed` every
   153	    30	time something else is down would make the heartbeat's own history
   154	    31	useless.
   155	    32	"""
   156	    33	
   157	    34	from __future__ import annotations
   158	    35	
   159	    36	from datetime import datetime, time, timedelta
   160	    37	from typing import Optional
   161	    38	
   162	    39	from loguru import logger
   163	    40	
   164	    41	from cobalt.jobs.store import JobStore
   165	    42	from cobalt.jobs.watchdog import sweep
   166	    43	from cobalt.session import clock as clock_mod
   167	    44	from cobalt.session.clock import session_clock
   168	    45	
   169	    46	from . import probes as probe_mod
   170	    47	from .render import SECTION, UNIT, WRITER, Beat
   171	    48	
   172	    49	JOB_LABEL = "com.cobalt.heartbeat"
   173	    50	INTERVAL_KEY = "heartbeat.interval_min"
   174	    51	GREEN_SUMMARY_KEY = "heartbeat.green_summary_at"
   175	    52	
   176	    53	
   177	    54	def interval_min() -> int:
   178	    55	    from cobalt.taxonomy.loader import load_tunables
   179	    56	
   180	    57	    row = load_tunables().by_key.get(INTERVAL_KEY)
   181	    58	    if row is None:
   182	    59	        raise RuntimeError(
   183	    60	            f"tunable {INTERVAL_KEY!r} is missing from tunables.yaml — the heartbeat "
   184	    61	            "reads its own cadence from config and has no built-in default (F16). "
   185	    62	            "This is the number every 'red within one interval' claim is measured "
   186	    63	            "against."
   187	    64	        )
   188	    65	    return int(row.value)
   189	    66	
   190	    67	
   191	    68	def green_summary_at() -> time:
   192	    69	    from cobalt.taxonomy.loader import load_tunables
   193	    70	
   194	    71	    row = load_tunables().by_key.get(GREEN_SUMMARY_KEY)
   195	    72	    if row is None:
   196	    73	        raise RuntimeError(f"tunable {GREEN_SUMMARY_KEY!r} is missing from tunables.yaml (F16).")
   197	    74	    hh, _, mm = str(row.value).partition(":")
   198	    75	    return time(int(hh), int(mm))
   199	    76	
   200	    77	
   201	    78	# ---------------------------------------------------------------------
   202	    79	# 1. probe
   203	    80	# ---------------------------------------------------------------------
   204	    81	
   205	    82	
   206	    83	def take_beat(*, now: Optional[datetime] = None, probe: bool = True) -> Beat:
   207	    84	    """Every probe and every job row. Never raises on a red."""
   208	    85	    ts = now or clock_mod.now_utc()
   209	    86	    beat = Beat(at=session_clock().to_et(ts))
   210	    87	
   211	    88	    beat.probes = [
   212	    89	        probe_mod.database(),
   213	    90	        probe_mod.sheet_http(),
   214	    91	        # Right after `sheet_http`, and a separate line on purpose: "the
   215	    92	        # server is up" and "the page will take a card" are different
   216	    93	        # facts, and on 2026-09-09 they disagreed for thirteen hours
   217	    94	        # while the beat stayed green.
   218	    95	        probe_mod.sheet_daymode(),
   219	    96	        probe_mod.obsidian(),
   220	    97	        probe_mod.mainframe(),
   221	    98	        probe_mod.herdr(),
   222	    99	        probe_mod.archiver_freshness(now=ts),
   223	   100	        probe_mod.seat_usage(now=ts),
   224	   101	        probe_mod.backup_freshness(now=ts),
   225	   102	        probe_mod.vaultwrite_blocks(now=ts),
   226	   103	        probe_mod.redactions(interval_min(), now=ts),
   227	   104	        probe_mod.email(),
   228	   105	    ]
   229	   106	    try:
   230	   107	        beat.jobs = sweep(now=ts, probe=probe)
   231	   108	    except Exception as e:  # noqa: BLE001 - a broken sweep is its own red
   232	   109	        beat.probes.append(
   233	   110	            probe_mod.Probe(
   234	   111	                "job sweep", False,
   235	   112	                f"the watchdog itself FAILED ({type(e).__name__}: {e}) — every job's "
   236	   113	                "state is UNKNOWN, which is not the same as green",
   237	   114	                unknown=True,
   238	   115	            )
   239	   116	        )
   240	   117	    return beat
   241	   118	
   242	   119	
   243	   120	# ---------------------------------------------------------------------
   244	   121	# 2. the daily-note block (Output 1)
   245	   122	# ---------------------------------------------------------------------
   246	   123	
   247	   124	
   248	   125	def write_note_block(beat: Beat, *, dry_run: bool = False):
   249	   126	    """One L28 unit in today's note, updated in place — one diff a beat.
   250	   127	
   251	   128	    Returns the `WriteResult`, or None when there is no note yet. A
   252	   129	    missing note is NOT created from here (L28.1: only
   253	   130	    `create_if_absent` with a template may), and the 05:15 prefill is
   254	   131	    what creates the day's note.
   255	   132	    """
   256	   133	    from cobalt.daymode.note import daily_note_path
   257	   134	    from cobalt.vaultwrite import VaultWriter, VaultWriteStore
   258	   135	
   259	   136	    path = daily_note_path(beat.at.date())
   260	   137	    if not path.exists():
   261	   138	        logger.error(
   262	   139	            "heartbeat: {} does not exist — the status block was NOT written. The "
   263	   140	            "05:15 prefill creates the day's note; this writer never does (L28.1).",
   264	   141	            path,
   265	   142	        )
   266	   143	        return None
   267	   144	    store = VaultWriteStore()
   268	   145	    store.ensure_schema()
   269	   146	    writer = VaultWriter(WRITER, store=store, dry_run=dry_run)
   270	   147	    return writer.upsert_unit(path, SECTION, UNIT, beat.note_body())
   271	   148	
   272	   149	
   273	   150	# ---------------------------------------------------------------------
   274	   151	# 3/4. the alert channels (Outputs 2 and 3)
   275	   152	# ---------------------------------------------------------------------
   276	   153	
   277	   154	
   278	   155	def should_send_green(beat: Beat, store: JobStore) -> bool:
   279	   156	    """One green summary a day, at `heartbeat.green_summary_at`.
   280	   157	
   281	   158	    "Have we already sent today's?" is answered from the JOB ROW's own
   282	   159	    `last_result` rather than from a new table — the heartbeat is the
   283	   160	    only writer of that row, and a second table to remember one boolean a
   284	   161	    day is a table to migrate later for nothing.
   285	   162	    """
   286	   163	    if beat.at.time() < green_summary_at():
   287	   164	        return False
   288	   165	    row = store.get(JOB_LABEL) or {}
   289	   166	    last = (row.get("last_result") or {}).get("green_summary_date")
   290	   167	    return last != beat.at.date().isoformat()
   291	   168	
   292	   169	
   293	   170	def send_dm(beat: Beat) -> str:
   294	   171	    from cobalt.notify import MattermostError, send_dm as _send
   295	   172	
   296	   173	    try:
   297	   174	        result = _send(beat.dm_body())
   298	   175	    except MattermostError as e:
   299	   176	        # The alert path failing is itself worth saying, in the note and
   300	   177	        # in the log — it is the one failure the DM cannot report.
   301	   178	        logger.error("heartbeat: Mattermost DM FAILED — {}", e)
   302	   179	        return f"Mattermost DM FAILED: {e}"
   303	   180	    logger.info("heartbeat: {}", result.report())
   304	   181	    return result.report()
   305	   182	
   306	   183	
   307	   184	def out_of_band(beat: Beat) -> str:
   308	   185	    """Charter §3 F18's SECOND channel — email, over Layer-B Google OAuth.
   309	   186	
   310	   187	    Built at S1-P4 (2026-09-08). Until then this function existed only to
   311	   188	    say, loudly and on every red, that the channel did NOT exist; the
   312	   189	    honest placeholder is in the git history and its S1-P3 reasoning is
   313	   190	    unchanged — alerting that stops at Mattermost is alerting that shares
   314	   191	    a fate with one of the things it watches.
   315	   192	
   316	   193	    THIS RUNS BEFORE `send_dm`, and the order is the whole point. The DM
   317	   194	    is the channel that can carry a report ABOUT the email channel; the
   318	   195	    email channel cannot carry a report about itself. So the second
   319	   196	    channel goes first, and its outcome — including "email channel DOWN:
   320	   197	    <reason>" — is appended to the beat's notes in time for
   321	   198	    `beat.dm_body()` to render it.
   322	   199	
   323	   200	    NEVER RAISES. A failure here is a note, not a crash: a beat that died
   324	   201	    trying to send the backup alert would take the primary alert with it,
   325	   202	    which is the exact coupling this channel exists to break.
   326	   203	    """
   327	   204	    from cobalt.notify import EmailError, record_attempt, send_email
   328	   205	    from cobalt.notify.config import load_notify_config
   329	   206	
   330	   207	    try:
   331	   208	        cfg = load_notify_config().email
   332	   209	    except Exception as e:  # noqa: BLE001
   333	   210	        reason = f"notify config unreadable ({type(e).__name__}: {e})"
   334	   211	        logger.error("heartbeat: email channel DOWN — {}", reason)
   335	   212	        return f"email channel DOWN: {reason}"
   336	   213	
   337	   214	    subject = f"{beat.headline} · {beat.at:%Y-%m-%d %H:%M %Z}"
   338	   215	    try:
   339	   216	        result = send_email(cfg.to, subject, beat.dm_body())
   340	   217	    except EmailError as e:
   341	   218	        # `EmailError`'s message is redacted BY CONTRACT, so it is safe to
   342	   219	        # put straight into a Mattermost DM — which is exactly where it is
   343	   220	        # about to go.
   344	   221	        record_attempt(ok=False, caller="heartbeat", detail=str(e))
   345	   222	        logger.error("heartbeat: email channel DOWN — {}", e)
   346	   223	        return f"email channel DOWN: {e}"
   347	   224	
   348	   225	    record_attempt(
   349	   226	        ok=result.sent, caller="heartbeat", detail=result.detail, message_id=result.ref
   350	   227	    )
   351	   228	    if not result.sent:
   352	   229	        # A disabled channel is deliberate, not an outage — but the DM
   353	   230	        # still says so, because "no email arrived" must never be
   354	   231	        # ambiguous between "off" and "broken".
   355	   232	        logger.warning("heartbeat: {}", result.report())
   356	   233	        return f"email channel OFF: {result.detail}"
   357	   234	    logger.info("heartbeat: {}", result.report())
   358	   235	    return result.report()
   359	   236	
   360	   237	
   361	   238	# ---------------------------------------------------------------------
   362	   239	# the beat
   363	   240	# ---------------------------------------------------------------------
   364	   241	
   365	   242	
   366	   243	def run_beat(*, now: Optional[datetime] = None, dry_run: bool = False, probe: bool = True) -> Beat:
   367	   244	    """One whole heartbeat. Returns the Beat; never raises on a red."""
   368	   245	    store = JobStore()
   369	   246	    store.ensure_schema()
   370	   247	    beat = take_beat(now=now, probe=probe)
   371	   248	
   372	   249	    write = write_note_block(beat, dry_run=dry_run)
   373	   250	    if write is None:
   374	   251	        beat.notes.append("Daily note: NOT WRITTEN — today's note does not exist yet.")
   375	   252	    else:
   376	   253	        # L28.4: the unified diff goes in the RUN REPORT, every time. The
   377	   254	        # heartbeat writes to the live vault every 15 minutes; a write
   378	   255	        # path that reported only "updated" would be the one write path
   379	   256	        # in this codebase whose changes nobody could read back.
   380	   257	        beat.notes.append(write.report())
   381	   258	
   382	   259	    sent_green = False
   383	   260	    if dry_run:
   384	   261	        beat.notes.append("DRY RUN — no DM sent, nothing written.")
   385	   262	    elif not beat.green:
   386	   263	        # OUT-OF-BAND FIRST. The DM's body is rendered from `beat.notes`,
   387	   264	        # so the email outcome has to be in the list before `send_dm`
   388	   265	        # reads it — that is what puts "email channel DOWN: <reason>" in
   389	   266	        # the red DM. The reverse order would report the email result
   390	   267	        # only to the log, where a failed second channel would be
   391	   268	        # discovered by whoever went looking, which is nobody.
   392	   269	        beat.notes.append(out_of_band(beat))
   393	   270	        beat.notes.append(send_dm(beat))
   394	   271	    elif should_send_green(beat, store):
   395	   272	        beat.notes.append(send_dm(beat))
   396	   273	        sent_green = True
   397	   274	
   398	   275	    if not dry_run:
   399	   276	        # The heartbeat records ITS OWN run like any other job — it is the
   400	   277	        # one job nobody else is watching, so it watches itself and a
   401	   278	        # stalled heartbeat shows up as its own MISSED row.
   402	   279	        result = {
   403	   280	            "green": beat.green,
   404	   281	            "red_jobs": [j.label for j in beat.red_jobs],
   405	   282	            "red_probes": [p.name for p in beat.red_probes],
   406	   283	        }
   407	   284	        prior = (store.get(JOB_LABEL) or {}).get("last_result") or {}
   408	   285	        result["green_summary_date"] = (
   409	   286	            beat.at.date().isoformat() if sent_green else prior.get("green_summary_date")
   410	   287	        )
   411	   288	        store.register_all(__import__(
   412	   289	            "cobalt.jobs.config", fromlist=["load_job_registry"]
   413	   290	        ).load_job_registry())
   414	   291	        store.mark_running(JOB_LABEL, now=now or clock_mod.now_utc())
   415	   292	        store.mark_finished(JOB_LABEL, exit_code=0, result=result, now=now or clock_mod.now_utc())
   416	   293	
   417	   294	    (logger.info if beat.green else logger.error)("heartbeat: {}", beat.headline)
   418	   295	    return beat
   419	   296	
   420	   297	
   421	   298	__all__ = [
   422	   299	    "GREEN_SUMMARY_KEY",
   423	   300	    "INTERVAL_KEY",
   424	   301	    "JOB_LABEL",
   425	   302	    "green_summary_at",
   426	   303	    "interval_min",
   427	   304	    "out_of_band",
   428	   305	    "run_beat",
   429	   306	    "take_beat",
   430	   307	    "write_note_block",
   431	   308	]
   432	     1	"""F18's block — what he reads, in the note and in the DM.
   433	     2	
   434	     3	ONE RENDERER, two destinations. The daily-note block and the Mattermost
   435	     4	DM are the same text: a heartbeat whose two channels could disagree is a
   436	     5	heartbeat you have to check twice.
   437	     6	"""
   438	     7	
   439	     8	from __future__ import annotations
   440	     9	
   441	    10	from dataclasses import dataclass, field
   442	    11	from datetime import datetime
   443	    12	from typing import Optional
   444	    13	
   445	    14	from cobalt.jobs.watchdog import Finding
   446	    15	
   447	    16	from .probes import Probe
   448	    17	
   449	    18	#: The L28 unit this writes. Section + stable id: same id every beat, so
   450	    19	#: it updates in place and the note never accumulates 96 blocks a day.
   451	    20	SECTION = "heartbeat"
   452	    21	UNIT = "status"
   453	    22	WRITER = "heartbeat"
   454	    23	
   455	    24	
   456	    25	@dataclass
   457	    26	class Beat:
   458	    27	    """One heartbeat's whole result."""
   459	    28	
   460	    29	    at: datetime
   461	    30	    probes: list[Probe] = field(default_factory=list)
   462	    31	    jobs: list[Finding] = field(default_factory=list)
   463	    32	    notes: list[str] = field(default_factory=list)
   464	    33	
   465	    34	    @property
   466	    35	    def red_probes(self) -> list[Probe]:
   467	    36	        return [p for p in self.probes if not p.ok]
   468	    37	
   469	    38	    @property
   470	    39	    def red_jobs(self) -> list[Finding]:
   471	    40	        return [j for j in self.jobs if not j.ok]
   472	    41	
   473	    42	    @property
   474	    43	    def green(self) -> bool:
   475	    44	        return not self.red_probes and not self.red_jobs
   476	    45	
   477	    46	    @property
   478	    47	    def headline(self) -> str:
   479	    48	        if self.green:
   480	    49	            return (
   481	    50	                f"GREEN — {len(self.jobs)} job(s), {len(self.probes)} probe(s), "
   482	    51	                "nothing red"
   483	    52	            )
   484	    53	        parts = []
   485	    54	        if self.red_jobs:
   486	    55	            parts.append(f"{len(self.red_jobs)} job(s)")
   487	    56	        if self.red_probes:
   488	    57	            parts.append(f"{len(self.red_probes)} probe(s)")
   489	    58	        return f"RED — {' and '.join(parts)}"
   490	    59	
   491	    60	    # -- the two renderings -------------------------------------------
   492	    61	
   493	    62	    def note_body(self) -> str:
   494	    63	        """The daily-note unit. Markdown, deterministic, no LLM (L28)."""
   495	    64	        mark = "🟢" if self.green else "🔴"
   496	    65	        lines = [
   497	    66	            f"{mark} **HEARTBEAT {self.headline}** · {self.at:%Y-%m-%d %H:%M:%S %Z}",
   498	    67	            "",
   499	    68	            "| | check | detail |",
   500	    69	            "|---|---|---|",
   501	    70	        ]
   502	    71	        for probe in self.probes:
   503	    72	            icon = "🟢" if probe.ok else ("⚪" if probe.unknown else "🔴")
   504	    73	            lines.append(f"| {icon} | {probe.name} | {_cell(probe.detail)} |")
   505	    74	        for job in self.jobs:
   506	    75	            icon = "🟢" if job.ok else "🔴"
   507	    76	            lines.append(f"| {icon} | `{job.label}` | {job.state} — {_cell(job.detail)} |")
   508	    77	        for note in self.notes:
   509	    78	            lines += ["", f"> {note}"]
   510	    79	        return "\n".join(lines)
   511	    80	
   512	    81	    def dm_body(self) -> str:
   513	    82	        """The Mattermost DM. Plain lines — a table in a DM is unreadable
   514	    83	        on a phone, and the phone is where a red alert is actually read."""
   515	    84	        head = ("🟢 " if self.green else "🔴 ") + f"COBALT HEARTBEAT {self.headline}"
   516	    85	        lines = [head, f"{self.at:%Y-%m-%d %H:%M:%S %Z}", ""]
   517	    86	        if self.green:
   518	    87	            lines.append(
   519	    88	                f"{len(self.jobs)} jobs and {len(self.probes)} probes all green."
   520	    89	            )
   521	    90	        else:
   522	    91	            lines.append("RED:")
   523	    92	            for item in [*self.red_jobs, *self.red_probes]:
   524	    93	                name = getattr(item, "label", None) or item.name
   525	    94	                detail = item.detail
   526	    95	                lines.append(f"  • {name}: {detail}")
   527	    96	            lines.append("")
   528	    97	            lines.append("Green:")
   529	    98	            for probe in self.probes:
   530	    99	                if probe.ok:
   531	   100	                    lines.append(f"  • {probe.name}: {probe.detail}")
   532	   101	        for note in self.notes:
   533	   102	            lines += ["", note]
   534	   103	        return "\n".join(lines)
   535	   104	
   536	   105	    def console(self) -> str:
   537	   106	        lines = [f"HEARTBEAT {self.headline}  ({self.at:%Y-%m-%d %H:%M:%S %Z})", ""]
   538	   107	        lines += [p.line() for p in self.probes]
   539	   108	        lines += [j.line() for j in self.jobs]
   540	   109	        lines += ["", *self.notes]
   541	   110	        return "\n".join(lines)
   542	   111	
   543	   112	
   544	   113	def _cell(text: str) -> str:
   545	   114	    """A markdown table cell cannot contain a raw pipe or a newline."""
   546	   115	    return text.replace("|", "\\|").replace("\n", " ").strip()
   547	   116	
   548	   117	
   549	   118	__all__ = ["SECTION", "UNIT", "WRITER", "Beat"]
   550	     1	"""F18's probes — one function per question, each answering honestly.
   551	     2	
   552	     3	Charter §3 F18: "services alive · archiver freshness · every ops plist
   553	     4	loaded + last exit code · Obsidian running; red/green to daily note + DM;
   554	     5	red also out-of-band."
   555	     6	
   556	     7	THE RULE EVERY PROBE HERE KEEPS. "The probe broke" and "the thing is
   557	     8	down" are different facts, and collapsing them is how a red condition
   558	     9	becomes invisible. A probe that cannot run returns UNKNOWN, and UNKNOWN
   559	    10	is RED — because a heartbeat that says green when it did not look is
   560	    11	worse than no heartbeat at all.
   561	    12	"""
   562	    13	
   563	    14	from __future__ import annotations
   564	    15	
   565	    16	import json
   566	    17	import os
   567	    18	import socket
   568	    19	import subprocess
   569	    20	from dataclasses import dataclass
   570	    21	from datetime import datetime, timedelta
   571	    22	from pathlib import Path
   572	    23	from typing import Optional
   573	    24	from urllib import request as urlrequest
   574	    25	
   575	    26	from cobalt.session import clock as clock_mod
   576	    27	
   577	    28	
   578	    29	@dataclass
   579	    30	class Probe:
   580	    31	    """One answered question."""
   581	    32	
   582	    33	    name: str
   583	    34	    ok: bool
   584	    35	    detail: str
   585	    36	    #: True when the probe could not run. Still red — but an operator
   586	    37	    #: needs to know they are looking at ignorance, not at a diagnosis.
   587	    38	    unknown: bool = False
   588	    39	
   589	    40	    def line(self) -> str:
   590	    41	        mark = "OK  " if self.ok else ("??  " if self.unknown else "RED ")
   591	    42	        return f"{mark} {self.name:<24} {self.detail}"
   592	    43	
   593	    44	
   594	    45	def _tunable(key: str):
   595	    46	    from cobalt.taxonomy.loader import load_tunables
   596	    47	
   597	    48	    row = load_tunables().by_key.get(key)
   598	    49	    if row is None:
   599	    50	        raise RuntimeError(
   600	    51	            f"tunable {key!r} is missing from tunables.yaml — the heartbeat reads "
   601	    52	            "its thresholds from config and has no built-in defaults (F16)."
   602	    53	        )
   603	    54	    return row.value
   604	    55	
   605	    56	
   606	    57	def probe_timeout_s() -> float:
   607	    58	    return float(_tunable("heartbeat.probe_timeout_s"))
   608	    59	
   609	    60	
   610	    61	# ---------------------------------------------------------------------
   611	    62	
   612	    63	
   613	    64	def sheet_http(url: str = "http://127.0.0.1:5010/") -> Probe:
   614	    65	    """The ASET sheet answers 200.
   615	    66	
   616	    67	    NOT the same question as "the process exists", and S1-P2 is why this
   617	    68	    is a separate probe: reshaping `configs/cobalt/aset.yaml` took the
   618	    69	    running sheet to HTTP 500 while the process stayed perfectly alive
   619	    70	    and launchd stayed perfectly happy. The thing he trades beside is the
   620	    71	    PAGE, not the PID.
   621	    72	    """
   622	    73	    try:
   623	    74	        with urlrequest.urlopen(url, timeout=probe_timeout_s()) as resp:
   624	    75	            code = resp.status
   625	    76	        if code == 200:
   626	    77	            return Probe("sheet HTTP", True, f"{url} -> 200")
   627	    78	        return Probe("sheet HTTP", False, f"{url} -> {code} (expected 200)")
   628	    79	    except Exception as e:  # noqa: BLE001
   629	    80	        return Probe("sheet HTTP", False, f"{url} unreachable: {type(e).__name__}: {e}")
   630	    81	
   631	    82	
   632	    83	#: How much of a config error's own message reaches the beat line. A
   633	    84	#: `TaxonomyConfigError` runs to several hundred characters; the first
   634	    85	#: 160 carry the name of the thing that broke, which is what a reader
   635	    86	#: needs at 06:09 — the whole text is on the page itself.
   636	    87	DAYMODE_ERROR_CHARS = 160
   637	    88	
   638	    89	
   639	    90	def sheet_daymode(url: str = "http://127.0.0.1:5010/api/health") -> Probe:
   640	    91	    """The sheet is not just SERVING — it is WORKING.
   641	    92	
   642	    93	    THE THIRTEEN-HOUR GREEN. On 2026-09-09 the ASET sheet answered HTTP
   643	    94	    200 from roughly 19:00 the previous evening until 07:06, while the
   644	    95	    page carried "⚠ DAY MODE UNRESOLVED — cards are refused until this
   645	    96	    is fixed". `sheet_http` was green the whole time and it was telling
   646	    97	    the truth: the server was up. It was answering the wrong question.
   647	    98	
   648	    99	    The cause is worth keeping next to the probe, because it is the
   649	   100	    shape of the failure this watches for. The 09-08 seat-usage deploy
   650	   101	    added a `TunableUnit.WINDOW` row to `tunables.yaml`; the sheet
   651	   102	    process re-reads that file per request through code that predated
   652	   103	    the enum value, so every render raised `TaxonomyConfigError` — and
   653	   104	    `_daymode_state()` catches everything and renders a banner, exactly
   654	   105	    so the page paints rather than 500s. A page that refuses cards
   655	   106	    politely looks identical, from the outside, to one that is working.
   656	   107	
   657	   108	    So this reads the banner. `/api/health` reports what
   658	   109	    `_daymode_state()` resolved, and a false `ok` is red with the sheet's
   659	   110	    own words.
   660	   111	
   661	   112	    NOT A REPLACEMENT FOR `sheet_http`, which stays exactly as it was.
   662	   113	    Two questions: is it up, and is it usable. A dead server fails both,
   663	   114	    and the first one's message is the one that says what to restart.
   664	   115	    """
   665	   116	    try:
   666	   117	        with urlrequest.urlopen(url, timeout=probe_timeout_s()) as resp:
   667	   118	            code = resp.status
   668	   119	            payload = json.loads(resp.read().decode("utf-8"))
   669	   120	    except Exception as e:  # noqa: BLE001
   670	   121	        return Probe(
   671	   122	            "sheet daymode", False,
   672	   123	            f"{url} unreachable: {type(e).__name__}: {e}",
   673	   124	            unknown=True,
   674	   125	        )
   675	   126	
   676	   127	    if code != 200 or not isinstance(payload, dict) or "ok" not in payload:
   677	   128	        return Probe(
   678	   129	            "sheet daymode", False,
   679	   130	            f"{url} -> {code}, payload {str(payload)[:120]!r} — the health endpoint "
   680	   131	            "is not answering the shape this probe reads. UNKNOWN, which is red.",
   681	   132	            unknown=True,
   682	   133	        )
   683	   134	
   684	   135	    if payload.get("ok"):
   685	   136	        return Probe(
   686	   137	            "sheet daymode", True,
   687	   138	            f"day mode {payload.get('mode')} · {payload.get('stage')} · "
   688	   139	            f"{payload.get('sheet_mode')} sheet — cards are accepted",
   689	   140	        )
   690	   141	
   691	   142	    reason = payload.get("error") or (
   692	   143	        f"no day mode resolved (stage {payload.get('stage')})"
   693	   144	    )
   694	   145	    return Probe(
   695	   146	        "sheet daymode", False,
   696	   147	        "THE SHEET IS SERVING BUT REFUSING CARDS — "
   697	   148	        + str(reason)[:DAYMODE_ERROR_CHARS],
   698	   149	    )
   699	   150	
   700	   151	
   701	   152	def database(db_name: Optional[str] = None) -> Probe:
   702	   153	    """`cobalt_brain` (or whatever COBALT_ENV resolves) answers a query."""
   703	   154	    from cobalt import db, env
   704	   155	
   705	   156	    name = db_name or env.resolve_db_name()
   706	   157	    try:
   707	   158	        # ADR-0008: the probe names no table, but a connection still has
   708	   159	        # to declare a side. SYSTEM — the heartbeat is system-side, and a
   709	   160	        # liveness probe must never be the thing that opens user data.
   710	   161	        with db.connect(name, side=db.Side.SYSTEM) as conn:
   711	   162	            row = conn.execute("SELECT 1").fetchone()
   712	   163	        if row and row[0] == 1:
   713	   164	            return Probe("database", True, f"{name} reachable")
   714	   165	        return Probe("database", False, f"{name} answered {row!r} to SELECT 1")
   715	   166	    except Exception as e:  # noqa: BLE001
   716	   167	        return Probe("database", False, f"{name} unreachable: {type(e).__name__}: {e}")
   717	   168	
   718	   169	
   719	   170	def obsidian() -> Probe:
   720	   171	    """Obsidian is running — RULING 6, and not a cosmetic check.
   721	   172	
   722	   173	    The vault reaches his other devices only through a RUNNING Obsidian
   723	   174	    on this Mac. On 2026-09-04 a correct 05:15 write was silently
   724	   175	    overwritten by the trading PC's template because none was running
   725	   176	    here. This reads the SAME `cobalt.obsidian.sync_status()` the vault
   726	   177	    writer reads, so the two can never disagree about the wording.
   727	   178	    """
   728	   179	    from cobalt import obsidian as obsidian_mod
   729	   180	
   730	   181	    try:
   731	   182	        running, message = obsidian_mod.sync_status()
   732	   183	    except obsidian_mod.ObsidianProbeError as e:
   733	   184	        return Probe("obsidian", False, f"PROBE FAILED — sync state UNKNOWN: {e}", unknown=True)
   734	   185	    return Probe("obsidian", running, message)
   735	   186	
   736	   187	
   737	   188	def mainframe(host: str = "127.0.0.1", port: int = 1234) -> Probe:
   738	   189	    """The local model server accepts a connection (L23's local lane)."""
   739	   190	    try:
   740	   191	        with socket.create_connection((host, port), timeout=probe_timeout_s()):
   741	   192	            return Probe("mainframe", True, f"{host}:{port} accepting connections")
   742	   193	    except Exception as e:  # noqa: BLE001
   743	   194	        return Probe("mainframe", False, f"{host}:{port} refused: {type(e).__name__}")
   744	   195	
   745	   196	
   746	   197	def archiver_freshness(store=None, now: Optional[datetime] = None) -> Probe:
   747	   198	    """Last run + rows written, checked against the archiver's own
   748	   199	    Mon-Fri cadence via the same `is_missed` arithmetic F17's watchdog
   749	   200	    uses — not a flat age window.
   750	   201	
   751	   202	    A flat `now - last_run > N hours` window cannot tell a genuine miss
   752	   203	    from an ordinary Friday-to-Monday gap: whatever N is, it either
   753	   204	    fires every weekend (too small) or hides a multi-day outage (too
   754	   205	    big). 2026-09-06 is why this changed: the F17 wrapper was registered
   755	   206	    at 22:19 ET Friday, AFTER that evening's 20:30 run had already
   756	   207	    completed via the pre-wrapper code path, so the row's `finished_at`
   757	   208	    stayed NULL forever with nothing wrong — and the old flat
   758	   209	    `registered_at + heartbeat.archiver_max_age_min` grace expired
   759	   210	    Saturday just after midnight, painting the whole weekend red for a
   760	   211	    job that was never actually due again until Monday evening.
   761	   212	    `is_missed` already gets this right, including the exact "cannot
   762	   213	    miss a run it was not watching for" case above — reusing it here is
   763	   214	    the one-path rule, not a nicety.
   764	   215	
   765	   216	    Rows written still matters once a run HAS completed — a nightly run
   766	   217	    that exits 0 having written zero rows looks green in every state
   767	   218	    column and is quietly not collecting the corpus every later feature
   768	   219	    depends on. That check is cadence-independent and unchanged.
   769	   220	    """
   770	   221	    from cobalt.jobs.config import load_job_registry
   771	   222	    from cobalt.jobs.store import JobStore
   772	   223	    from cobalt.jobs.watchdog import MISSED_GRACE_KEY, is_missed
   773	   224	    from cobalt.session.clock import session_clock
   774	   225	
   775	   226	    store = store or JobStore()
   776	   227	    ts = now or clock_mod.now_utc()
   777	   228	    row = store.get("com.cobalt.archiver")
   778	   229	    if row is None:
   779	   230	        return Probe("archiver", False, "no jobs row — not registered")
   780	   231	
   781	   232	    spec = load_job_registry().spec("com.cobalt.archiver")
   782	   233	    now_et = session_clock().to_et(ts)
   783	   234	    grace = timedelta(minutes=int(_tunable(MISSED_GRACE_KEY)))
   784	   235	    missed, missed_detail = is_missed(spec, row, now_et=now_et, grace=grace)
   785	   236	
   786	   237	    finished = row["finished_at"]
   787	   238	    if finished is None:
   788	   239	        if missed:
   789	   240	            return Probe("archiver", False, missed_detail)
   790	   241	        return Probe(
   791	   242	            "archiver", True,
   792	   243	            f"no run OBSERVED yet — none due since registration "
   793	   244	            f"({row['registered_at']:%Y-%m-%d %H:%M} UTC)",
   794	   245	        )
   795	   246	    age = ts - finished
   796	   247	    result = row["last_result"] or {}
   797	   248	    rows_written = result.get("rows_written")
   798	   249	    detail = (
   799	   250	        f"last run {finished:%Y-%m-%d %H:%M} UTC ({age.total_seconds() / 3600:.1f} h ago)"
   800	   251	        f", rows written {rows_written if rows_written is not None else 'UNRECORDED'}"
   801	   252	        f", exit {row['exit_code']}"
   802	   253	    )
   803	   254	    if missed:
   804	   255	        return Probe("archiver", False, f"STALE — {detail} — {missed_detail}")
   805	   256	    if row["exit_code"] not in (0, None):
   806	   257	        return Probe("archiver", False, f"last run FAILED — {detail}")
   807	   258	    if rows_written == 0:
   808	   259	        return Probe(
   809	   260	            "archiver", False,
   810	   261	            f"ran and wrote NOTHING — {detail}. Exit 0 with zero rows is the "
   811	   262	            "failure that looks green in every state column.",
   812	   263	        )
   813	   264	    return Probe("archiver", True, detail)
   814	   265	
   815	   266	
   816	   267	def backup_freshness(now: Optional[datetime] = None) -> Probe:
   817	   268	    """Age of the newest nightly snapshot, against
   818	   269	    `heartbeat.backup_max_age_min` (26 h).
   819	   270	
   820	   271	    THE UNARMED CASE IS RED, AND SAYS SO. Both legs of the backup ruling
   821	   272	    (external SSD, Backblaze B2) are off until their inputs exist, and
   822	   273	    the honest report of that is "there is no backup", not `??` and not
   823	   274	    a green tick. `unknown` is reserved for a probe that could not RUN;
   824	   275	    a config that declares no destination ran fine and the answer is bad.
   825	   276	    """
   826	   277	    from cobalt.backup.config import BackupConfigError, load_backup_config
   827	   278	    from cobalt.backup.restic import BackupError, latest_snapshot_age
   828	   279	
   829	   280	    ts = now or clock_mod.now_utc()
   830	   281	    try:
   831	   282	        cfg = load_backup_config()
   832	   283	    except BackupConfigError as e:
   833	   284	        return Probe("backup", False, f"config unreadable: {e}", unknown=True)
   834	   285	
   835	   286	    if not cfg.armed:
   836	   287	        off = ", ".join(d.name for d in cfg.destinations)
   837	   288	        return Probe(
   838	   289	            "backup", False,
   839	   290	            f"NO DESTINATION ARMED ({off} all off) — there is no backup. "
   840	   291	            "configs/cobalt/backup.yaml says what each leg is missing.",
   841	   292	        )
   842	   293	
   843	   294	    max_age = timedelta(minutes=int(_tunable("heartbeat.backup_max_age_min")))
   844	   295	    try:
   845	   296	        age = latest_snapshot_age(cfg)
   846	   297	    except BackupError as e:
   847	   298	        # BackupError's text is credential-free BY CONTRACT (see
   848	   299	        # backup/restic.py), and it is the one carrying the actionable
   849	   300	        # sentence — "/Volumes/COBALT-BACKUP is NOT MOUNTED". A beat that
   850	   301	        # said only `BackupError` would send someone to read the log to
   851	   302	        # learn they need to plug a disk in.
   852	   303	        return Probe("backup", False, str(e).split(". ")[0], unknown=True)
   853	   304	    except Exception as e:  # noqa: BLE001 — a repo we cannot reach is not a diagnosis
   854	   305	        return Probe("backup", False, f"could not read the repository: {type(e).__name__}",
   855	   306	                     unknown=True)
   856	   307	    if age is None:
   857	   308	        return Probe("backup", False,
   858	   309	                     f"armed ({', '.join(d.name for d in cfg.armed)}) but the repository "
   859	   310	                     "holds NO snapshot yet")
   860	   311	    hours = age.total_seconds() / 3600
   861	   312	    detail = (f"newest snapshot {hours:.1f} h old across "
   862	   313	              f"{', '.join(d.name for d in cfg.armed)}")
   863	   314	    if age > max_age:
   864	   315	        return Probe("backup", False,
   865	   316	                     f"STALE — {detail} (limit {max_age.total_seconds()/3600:.0f} h)")
   866	   317	    return Probe("backup", True, detail)
   867	   318	
   868	   319	
   869	   320	def vaultwrite_blocks(now: Optional[datetime] = None) -> Probe:
   870	   321	    """market_reset refusals + ungated migration runs since the last beat.
   871	   322	
   872	   323	    NOT RED ON ITS OWN. A refusal is the guard WORKING — F1 turning away
   873	   324	    a write inside 20:00-21:00 is the system doing its job. The number is
   874	   325	    reported because a spike means something is retrying blind, and
   875	   326	    because the RULING on migration tooling (S1-P3, decided-with-veto)
   876	   327	    says every ungated repair run inside the block increments this same
   877	   328	    counter so it can never happen quietly.
   878	   329	    """
   879	   330	    from cobalt.session.store import SessionBlockStore
   880	   331	
   881	   332	    try:
   882	   333	        store = SessionBlockStore()
   883	   334	        counts = store.counts_over_window(now=now)
   884	   335	    except Exception as e:  # noqa: BLE001
   885	   336	        return Probe("vault blocks", False, f"counter unreadable: {type(e).__name__}: {e}",
   886	   337	                     unknown=True)
   887	   338	    refused = counts.get(SessionBlockStore.REFUSED, 0)
   888	   339	    ungated = counts.get(SessionBlockStore.UNGATED_RUN, 0)
   889	   340	    # BOTH numbers, always, and never summed into one. They share a
   890	   341	    # counter because they are both "a write met the market_reset window"
   891	   342	    # — but a refusal is the guard working and an ungated run is the
   892	   343	    # carve-out being used, and reading five repairs as five refusals
   893	   344	    # would send someone hunting a bug that is not there.
   894	   345	    return Probe(
   895	   346	        "vault blocks", True,
   896	   347	        f"{refused} refused, {ungated} ungated repair run(s) in the counter window",
   897	   348	    )
   898	   349	
   899	   350	
   900	   351	def redactions(minutes: int, now: Optional[datetime] = None) -> Probe:
   901	   352	    """F19 hits since the last beat.
   902	   353	
   903	   354	    Also not red on its own — the guard firing is the guard working. It
   904	   355	    is on the block because a redaction count that suddenly climbs means
   905	   356	    something started putting credentials into outbound text, and that is
   906	   357	    worth seeing the day it starts rather than at the next audit.
   907	   358	    """
   908	   359	    from cobalt.redact.store import RedactionStore
   909	   360	
   910	   361	    try:
   911	   362	        store = RedactionStore()
   912	   363	        store.ensure_schema()
   913	   364	        count = store.count_over_minutes(minutes, now=now)
   914	   365	        by_pattern = store.by_pattern_since(
   915	   366	            (now or clock_mod.now_utc()) - timedelta(minutes=minutes)
   916	   367	        )
   917	   368	    except Exception as e:  # noqa: BLE001
   918	   369	        return Probe("redactions", False, f"counter unreadable: {type(e).__name__}: {e}",
   919	   370	                     unknown=True)
   920	   371	    if not count:
   921	   372	        return Probe("redactions", True, "0 since the last beat")
   922	   373	    kinds = ", ".join(f"{p} on {c} x{n}" for c, p, n in by_pattern[:5])
   923	   374	    return Probe("redactions", True, f"{count} since the last beat ({kinds})")
   924	   375	
   925	   376	
   926	   377	# ---------------------------------------------------------------------
   927	   378	# herdr — the terminal workspace every agent seat lives in
   928	   379	# ---------------------------------------------------------------------
   929	   380	
   930	   381	HERDR_LABEL = "com.cobalt.herdr"
   931	   382	
   932	   383	#: Where herdr puts its API socket. Not a tunable: F16 governs
   933	   384	#: THRESHOLDS, and this is an address — a number you might tune versus a
   934	   385	#: path that is either right or wrong. `herdr status server` prints it,
   935	   386	#: and it has been this since 0.8.x.
   936	   387	HERDR_SOCKET = Path("~/.config/herdr/herdr.sock")
   937	   388	
   938	   389	#: Absolute, for the same reason every plist's ProgramArguments is: a
   939	   390	#: probe that resolved a binary off PATH would answer a different
   940	   391	#: question under launchd than it answers in a shell.
   941	   392	HERDR_BINARY = Path("/opt/homebrew/bin/herdr")
   942	   393	
   943	   394	#: Claude Code's settings file, and the harness-aware hook it must point
   944	   395	#: at. Addresses, not thresholds — same reasoning as `HERDR_SOCKET`.
   945	   396	CLAUDE_SETTINGS = Path("~/.claude/settings.json")
   946	   397	HOOK_GUARD = Path("~/.claude/hooks/herdr-harness-guard.sh")
   947	   398	
   948	   399	
   949	   400	class HookGuardDrift(RuntimeError):
   950	   401	    """The SessionStart hook is not exactly the one guard entry."""
   951	   402	
   952	   403	
   953	   404	def _check_hook_guard(
   954	   405	    settings_path: Optional[Path] = None, guard_path: Optional[Path] = None
   955	   406	) -> str:
   956	   407	    """`hooks.SessionStart` is EXACTLY one entry pointing at the guard.
   957	   408	
   958	   409	    WHY THIS IS A HERDR QUESTION AND NOT A HOUSEKEEPING ONE. The `herdr`
   959	   410	    probe's second question is `herdr agent list`, and that list is what
   960	   411	    tells one seat from another. herdr's own Claude integration hardcodes
   961	   412	    the agent name `herdr:claude` with no harness detection, so a Grok or
   962	   413	    Codex session started under it reports itself as `claude`. The guard
   963	   414	    script is what makes the report honest, and this probe reads the list
   964	   415	    the guard protects — so the two belong in one answer.
   965	   416	
   966	   417	    IT IS NOT ENOUGH TO ASK WHETHER THE GUARD IS PRESENT. On 2026-09-09
   967	   418	    at 08:33 `herdr integration install claude` (v8 -> v9) did NOT replace
   968	   419	    the pointer, which a presence check would have called fine: it
   969	   420	    APPENDED A SECOND SessionStart ENTRY aimed at herdr's own script, so
   970	   421	    both would have fired and the last writer would have won. That is why
   971	   422	    the assertion is EXACTLY ONE — an integration update is expected to
   972	   423	    keep trying, and the count is the thing it changes.
   973	   424	
   974	   425	    Raises `HookGuardDrift` naming the drift; returns a one-line summary
   975	   426	    when everything is as it should be.
   976	   427	    """
   977	   428	    settings = Path(settings_path or CLAUDE_SETTINGS).expanduser()
   978	   429	    guard = Path(guard_path or HOOK_GUARD).expanduser()
   979	   430	
   980	   431	    if not settings.exists():
   981	   432	        raise HookGuardDrift(f"{settings} does not exist — no SessionStart hook at all")
   982	   433	    try:
   983	   434	        data = json.loads(settings.read_text())
   984	   435	    except Exception as e:  # noqa: BLE001
   985	   436	        raise HookGuardDrift(
   986	   437	            f"{settings} does not parse as JSON ({type(e).__name__}) — the hook "
   987	   438	            "configuration is UNKNOWN, which is not the same as correct"
   988	   439	        ) from None
   989	   440	
   990	   441	    entries = ((data.get("hooks") or {}).get("SessionStart")) or []
   991	   442	    if not isinstance(entries, list):
   992	   443	        raise HookGuardDrift(
   993	   444	            f"hooks.SessionStart is a {type(entries).__name__}, not a list of entries"
   994	   445	        )
   995	   446	    if len(entries) != 1:
   996	   447	        raise HookGuardDrift(
   997	   448	            f"hooks.SessionStart has {len(entries)} entries, expected exactly 1 — "
   998	   449	            "a herdr integration update appended/replaced the SessionStart hook. "
   999	   450	            "Grok sessions will report as claude; restore the single guard entry "
  1000	   451	            f"({guard})"
  1001	   452	        )
  1002	   453	
  1003	   454	    hooks = entries[0].get("hooks") or []
  1004	   455	    commands = [h for h in hooks if isinstance(h, dict) and h.get("type") == "command"]
  1005	   456	    if len(commands) != 1:
  1006	   457	        raise HookGuardDrift(
  1007	   458	            f"the SessionStart entry carries {len(commands)} command hook(s), "
  1008	   459	            "expected exactly 1 — a herdr integration update appended/replaced the "
  1009	   460	            "SessionStart hook. Grok sessions will report as claude; restore the "
  1010	   461	            f"single guard entry ({guard})"
  1011	   462	        )
  1012	   463	
  1013	   464	    command = str(commands[0].get("command") or "")
  1014	   465	    if str(guard) not in command:
  1015	   466	        raise HookGuardDrift(
  1016	   467	            f"the SessionStart hook does not run {guard} — a herdr integration "
  1017	   468	            "update appended/replaced the SessionStart hook. Grok sessions will "
  1018	   469	            "report as claude; restore the single guard entry"
  1019	   470	        )
  1020	   471	    if not guard.exists():
  1021	   472	        raise HookGuardDrift(
  1022	   473	            f"the SessionStart hook points at {guard}, which DOES NOT EXIST — "
  1023	   474	            "every session starts with a failing hook and no harness detection. "
  1024	   475	            "Restore the guard script"
  1025	   476	        )
  1026	   477	    if not os.access(guard, os.X_OK):
  1027	   478	        raise HookGuardDrift(
  1028	   479	            f"{guard} exists but is NOT EXECUTABLE — the hook cannot run it, so "
  1029	   480	            "no harness detection happens. `chmod +x` it"
  1030	   481	        )
  1031	   482	    return f"hook guard: 1 SessionStart entry -> {guard.name}, executable"
  1032	   483	
  1033	   484	
  1034	   485	def _herdr_enabled() -> tuple[bool, str]:
  1035	   486	    """Is `com.cobalt.herdr` supposed to be up yet?
  1036	   487	
  1037	   488	    The registry row answers, and until the handover it says no. This is
  1038	   489	    read every beat rather than baked in, so flipping one flag in
  1039	   490	    `configs/cobalt/jobs.yaml` is the whole of the last handover step.
  1040	   491	    """
  1041	   492	    from cobalt.jobs.config import load_job_registry
  1042	   493	
  1043	   494	    spec = load_job_registry().by_label.get(HERDR_LABEL)
  1044	   495	    if spec is None:
  1045	   496	        return False, f"{HERDR_LABEL} is not in the job registry"
  1046	   497	    return spec.enabled, ""
  1047	   498	
  1048	   499	
  1049	   500	def _herdr_agent_list(binary: Path, timeout: float) -> list:
  1050	   501	    """`herdr agent list` -> the agents array. Raises on anything else."""
  1051	   502	    proc = subprocess.run(
  1052	   503	        [str(binary), "agent", "list"], capture_output=True, text=True, timeout=timeout
  1053	   504	    )
  1054	   505	    if proc.returncode != 0:
  1055	   506	        raise RuntimeError(
  1056	   507	            f"`herdr agent list` exited {proc.returncode}: "
  1057	   508	            f"{proc.stderr.strip()[:200] or '(no stderr)'}"
  1058	   509	        )
  1059	   510	    payload = json.loads(proc.stdout)
  1060	   511	    agents = (payload.get("result") or {}).get("agents")
  1061	   512	    if not isinstance(agents, list):
  1062	   513	        raise RuntimeError("`herdr agent list` returned no `result.agents` array")
  1063	   514	    return agents
  1064	   515	
  1065	   516	
  1066	   517	def herdr(
  1067	   518	    *,
  1068	   519	    socket_path: Optional[Path] = None,
  1069	   520	    binary: Optional[Path] = None,
  1070	   521	    list_agents=None,
  1071	   522	    settings_path: Optional[Path] = None,
  1072	   523	    guard_path: Optional[Path] = None,
  1073	   524	) -> Probe:
  1074	   525	    """The herdr server is up, answering, AND honestly labelled — three
  1075	   526	    questions, all asked.
  1076	   527	
  1077	   528	    THE SOCKET EXISTING IS NOT THE SERVER WORKING, which is the same
  1078	   529	    lesson the ASET sheet's HTTP probe carries: a stale socket file
  1079	   530	    outlives the process that made it, and a server that has wedged
  1080	   531	    still holds its socket open. So this connects to the socket (does it
  1081	   532	    accept?) and then asks it something real (`herdr agent list`, which
  1082	   533	    has to traverse the server's live pane state to answer). Either half
  1083	   534	    failing is red, and the message names the launchd label so a reader
  1084	   535	    knows what to bootstrap.
  1085	   536	
  1086	   537	    THE THIRD QUESTION, added 2026-09-09: is the SessionStart hook still
  1087	   538	    exactly the harness-aware guard? See `_check_hook_guard` — the short
  1088	   539	    version is that `agent list` is what this probe asserts on, and a
  1089	   540	    herdr integration update that appends a second hook makes every Grok
  1090	   541	    session report itself as `claude` IN THAT LIST. Asking the first two
  1091	   542	    questions of a list that has quietly stopped meaning what it says is
  1092	   543	    asking nothing.
  1093	   544	
  1094	   545	    WHEN THE ROW IS DISABLED IT IS GREEN AND SAYS WHY. `enabled: false`
  1095	   546	    is the declared state of a job that is built and deliberately not
  1096	   547	    loaded — see ops/README.md. A red every 15 minutes for a state
  1097	   548	    somebody chose on purpose is how a heartbeat stops being read. The
  1098	   549	    hook check is skipped there too: with no server under launchd there
  1099	   550	    is no `agent list` for a mislabelled seat to corrupt.
  1100	   551	    """
  1101	   552	    enabled, why = _herdr_enabled()
  1102	   553	    if not enabled:
  1103	   554	        return Probe(
  1104	   555	            "herdr", True,
  1105	   556	            (why or f"{HERDR_LABEL} is registered with `enabled: false`")
  1106	   557	            + " — NOT PROBED. The plist is built and deliberately not loaded; the "
  1107	   558	            "server is running under a manual start. ops/README.md 'herdr handover' "
  1108	   559	            "is the procedure, and flipping that flag is its last step.",
  1109	   560	        )
  1110	   561	
  1111	   562	    path = Path(socket_path or HERDR_SOCKET).expanduser()
  1112	   563	    timeout = probe_timeout_s()
  1113	   564	    if not path.exists():
  1114	   565	        return Probe(
  1115	   566	            "herdr", False,
  1116	   567	            f"no API socket at {path} — the server is not running. "
  1117	   568	            f"`launchctl kickstart -k gui/$(id -u)/{HERDR_LABEL}`",
  1118	   569	        )
  1119	   570	    try:
  1120	   571	        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
  1121	   572	            sock.settimeout(timeout)
  1122	   573	            sock.connect(str(path))
  1123	   574	    except OSError as e:
  1124	   575	        return Probe(
  1125	   576	            "herdr", False,
  1126	   577	            f"the socket at {path} exists but REFUSED a connection "
  1127	   578	            f"({type(e).__name__}) — a stale socket file outlives the process that "
  1128	   579	            f"made it. {HERDR_LABEL} needs a kickstart.",
  1129	   580	        )
  1130	   581	
  1131	   582	    caller = list_agents or _herdr_agent_list
  1132	   583	    try:
  1133	   584	        agents = caller(Path(binary or HERDR_BINARY), timeout)
  1134	   585	    except Exception as e:  # noqa: BLE001
  1135	   586	        return Probe(
  1136	   587	            "herdr", False,
  1137	   588	            f"socket accepted but the server did not answer `agent list` "
  1138	   589	            f"({type(e).__name__}: {e}) — {HERDR_LABEL} is up and not serving",
  1139	   590	        )
  1140	   591	    # THIRD QUESTION. Asked last, because a drifted hook is a fact about
  1141	   592	    # what the answer above MEANS, and the two answers above are worth
  1142	   593	    # having either way.
  1143	   594	    try:
  1144	   595	        guard_line = _check_hook_guard(settings_path, guard_path)
  1145	   596	    except HookGuardDrift as e:
  1146	   597	        return Probe(
  1147	   598	            "herdr", False,
  1148	   599	            f"socket and `agent list` are fine, but the SEAT LABELS ARE NOT "
  1149	   600	            f"TRUSTWORTHY: {e}",
  1150	   601	        )
  1151	   602	
  1152	   603	    seats = ", ".join(sorted({str(a.get("agent")) for a in agents if a.get("agent")}))
  1153	   604	    return Probe(
  1154	   605	        "herdr", True,
  1155	   606	        f"socket accepting at {path}; {len(agents)} pane(s)"
  1156	   607	        + (f", seats: {seats}" if seats else "")
  1157	   608	        + f"; {guard_line}",
  1158	   609	    )
  1159	   610	
  1160	   611	
  1161	   612	# ---------------------------------------------------------------------
  1162	   613	# seat-usage report freshness
  1163	   614	# ---------------------------------------------------------------------
  1164	   615	
  1165	   616	
  1166	   617	def seat_usage(store=None, now: Optional[datetime] = None) -> Probe:
  1167	   618	    """Has the seat-usage report been refreshed recently ENOUGH, and is
  1168	   619	    it even due right now?
  1169	   620	
  1170	   621	    ASKED ONLY INSIDE THE WINDOW. The job runs hourly between 06:00 and
  1171	   622	    23:00 ET; at 03:00 the last run is four hours old and everything is
  1172	   623	    exactly as it should be. A flat age check would be red all night for
  1173	   624	    a schedule working as written — the same mistake the archiver's
  1174	   625	    freshness probe made against weekends, and fixed on 2026-09-06 by
  1175	   626	    asking the schedule instead of guessing a number.
  1176	   627	
  1177	   628	    Inside the window, the limit is `seat_usage.max_age_min` (two
  1178	   629	    intervals): one missed run is a hiccup nobody needs to be told
  1179	   630	    about, two in a row means the number Dejan reads at the close is
  1180	   631	    wrong.
  1181	   632	    """
  1182	   633	    from cobalt.jobs.config import load_job_registry
  1183	   634	    from cobalt.jobs.store import JobStore
  1184	   635	    from cobalt.session.clock import session_clock
  1185	   636	    from cobalt.seatusage.runner import JOB_LABEL
  1186	   637	
  1187	   638	    ts = now or clock_mod.now_utc()
  1188	   639	    now_et = session_clock().to_et(ts)
  1189	   640	    spec = load_job_registry().by_label.get(JOB_LABEL)
  1190	   641	    if spec is None or spec.schedule is None:
  1191	   642	        return Probe("seat usage", False, f"{JOB_LABEL} is not in the job registry")
  1192	   643	    if not spec.enabled:
  1193	   644	        return Probe(
  1194	   645	            "seat usage", True,
  1195	   646	            f"{JOB_LABEL} is registered with `enabled: false` — NOT PROBED",
  1196	   647	        )
  1197	   648	    cadence = spec.cadence or "(no cadence)"
  1198	   649	    if not spec.schedule.due_now(now_et):
  1199	   650	        return Probe(
  1200	   651	            "seat usage", True,
  1201	   652	            f"outside its window — not due ({cadence}). The report holds "
  1202	   653	            "yesterday's last run until the window opens again.",
  1203	   654	        )
  1204	   655	
  1205	   656	    store = store or JobStore()
  1206	   657	    try:
  1207	   658	        row = store.get(JOB_LABEL)
  1208	   659	    except Exception as e:  # noqa: BLE001
  1209	   660	        return Probe("seat usage", False,
  1210	   661	                     f"jobs row unreadable: {type(e).__name__}: {e}", unknown=True)
  1211	   662	    if row is None:
  1212	   663	        return Probe("seat usage", False, f"no jobs row for {JOB_LABEL} — not registered")
  1213	   664	
  1214	   665	    limit = timedelta(minutes=int(_tunable("seat_usage.max_age_min")))
  1215	   666	    finished = row["finished_at"]
  1216	   667	    if finished is None:
  1217	   668	        opened = spec.schedule.window_opened_at(now_et)
  1218	   669	        reference = max(
  1219	   670	            [d for d in (opened, session_clock().to_et(row["registered_at"])) if d]
  1220	   671	        )
  1221	   672	        if now_et - reference <= limit:
  1222	   673	            return Probe(
  1223	   674	                "seat usage", True,
  1224	   675	                f"no run OBSERVED yet — none due since {reference:%Y-%m-%d %H:%M} ET "
  1225	   676	                f"({cadence})",
  1226	   677	            )
  1227	   678	        return Probe(
  1228	   679	            "seat usage", False,
  1229	   680	            f"NEVER RUN inside its window — nothing since "
  1230	   681	            f"{reference:%Y-%m-%d %H:%M} ET ({cadence})",
  1231	   682	        )
  1232	   683	
  1233	   684	    age = ts - finished
  1234	   685	    result = row["last_result"] or {}
  1235	   686	    unpriced = result.get("unpriced") or []
  1236	   687	    detail = (
  1237	   688	        f"last run {session_clock().to_et(finished):%Y-%m-%d %H:%M} ET "
  1238	   689	        f"({age.total_seconds() / 60:.0f} min ago), exit {row['exit_code']}"
  1239	   690	    )
  1240	   691	    if unpriced:
  1241	   692	        # NOT RED. An unpriced model is loud in the report itself, every
  1242	   693	        # hour, where the number it distorts is. Repeating it as a red
  1243	   694	        # beat would put a permanent alert on a condition that is fixed
  1244	   695	        # by a deliberate version bump, not by anything at 03:00.
  1245	   696	        detail += f"; UNPRICED in the report: {', '.join(unpriced)}"
  1246	   697	    if row["exit_code"] not in (0, None):
  1247	   698	        return Probe("seat usage", False, f"last run FAILED — {detail}")
  1248	   699	    if age > limit:
  1249	   700	        return Probe(
  1250	   701	            "seat usage", False,
  1251	   702	            f"STALE — {detail}, limit {limit.total_seconds() / 60:.0f} min "
  1252	   703	            f"({cadence}). The report is no longer today's.",
  1253	   704	        )
  1254	   705	    return Probe("seat usage", True, detail)
  1255	   706	
  1256	   707	
  1257	   708	def email() -> Probe:
  1258	   709	    """The out-of-band alert channel is armed — token present + last send.
  1259	   710	
  1260	   711	    THE ONE PROBE THAT WATCHES THE ALERT PATH ITSELF. Every other probe
  1261	   712	    here answers "is a monitored thing up?"; this one answers "could we
  1262	   713	    still tell him if it were not?". An email channel that quietly lost
  1263	   714	    its refresh token would take every red with it and leave the beat
  1264	   715	    looking exactly as green as before — which is the failure this row
  1265	   716	    exists to make impossible.
  1266	   717	
  1267	   718	    It NEVER SENDS. A probe that mailed a test every 15 minutes would put
  1268	   719	    96 messages a day in the inbox and train its reader to filter the
  1269	   720	    channel, defeating the thing it was checking. Presence of the
  1270	   721	    credential is read from the vault (names only, no values, no
  1271	   722	    network); the last real send is read from `cobalt_email_sends`,
  1272	   723	    written by whoever actually sent one.
  1273	   724	
  1274	   725	    A FAILED LAST SEND IS RED, and stays red until a later send succeeds.
  1275	   726	    "It worked in July" is not an answer about an alert path.
  1276	   727	    """
  1277	   728	    from cobalt.notify.email import channel_status
  1278	   729	    from cobalt.notify.store import EmailSendStore
  1279	   730	
  1280	   731	    try:
  1281	   732	        armed, detail = channel_status()
  1282	   733	    except Exception as e:  # noqa: BLE001
  1283	   734	        return Probe("email", False, f"PROBE FAILED — channel state UNKNOWN: {e}", unknown=True)
  1284	   735	    if not armed:
  1285	   736	        return Probe("email", False, detail)
  1286	   737	
  1287	   738	    try:
  1288	   739	        last = EmailSendStore().last()
  1289	   740	    except Exception as e:  # noqa: BLE001
  1290	   741	        # The credential IS there; only the history is unreadable. That
  1291	   742	        # is ignorance about half the question, not a dead channel — and
  1292	   743	        # `unknown` is what says so.
  1293	   744	        return Probe("email", False, f"{detail}; last send UNKNOWN ({type(e).__name__})",
  1294	   745	                     unknown=True)
  1295	   746	
  1296	   747	    if last is None:
  1297	   748	        # Never sent is not "broken", but it is not proven either, and
  1298	   749	        # F18's whole claim is that this path works. `cobalt notify
  1299	   750	        # email-test` is one command.
  1300	   751	        return Probe("email", False,
  1301	   752	                     f"{detail}, but NO SEND HAS EVER BEEN MADE from this host — the "
  1302	   753	                     "out-of-band path is unproven. Run `cobalt notify email-test`.")
  1303	   754	    when = f"{last['ts']:%Y-%m-%d %H:%M} UTC"
  1304	   755	    if not last["ok"]:
  1305	   756	        return Probe("email", False,
  1306	   757	                     f"{detail}; LAST SEND FAILED at {when} ({last['caller']}) — "
  1307	   758	                     f"{last['detail']}")
  1308	   759	    return Probe("email", True, f"{detail}; last send OK {when} ({last['caller']})")
  1309	   760	
  1310	   761	
  1311	   762	__all__ = [
  1312	   763	    "Probe",
  1313	   764	    "archiver_freshness",
  1314	   765	    "database",
  1315	   766	    "email",
  1316	   767	    "herdr",
  1317	   768	    "mainframe",
  1318	   769	    "obsidian",
  1319	   770	    "probe_timeout_s",
  1320	   771	    "redactions",
  1321	   772	    "seat_usage",
  1322	   773	    "sheet_http",
  1323	   774	    "vaultwrite_blocks",
  1324	   775	]
  1325	
  1326	exec
  1327	/bin/zsh -lc "nl -ba src/cobalt/heartbeat/runner.py | sed -n '240,330p'; nl -ba src/cobalt/heartbeat/render.py; nl -ba src/cobalt/heartbeat/probes.py | sed -n '285,365p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
  1328	 succeeded in 0ms:
  1329	   240	# ---------------------------------------------------------------------
  1330	   241	
  1331	   242	
  1332	   243	def run_beat(*, now: Optional[datetime] = None, dry_run: bool = False, probe: bool = True) -> Beat:
  1333	   244	    """One whole heartbeat. Returns the Beat; never raises on a red."""
  1334	   245	    store = JobStore()
  1335	   246	    store.ensure_schema()
  1336	   247	    beat = take_beat(now=now, probe=probe)
  1337	   248	
  1338	   249	    write = write_note_block(beat, dry_run=dry_run)
  1339	   250	    if write is None:
  1340	   251	        beat.notes.append("Daily note: NOT WRITTEN — today's note does not exist yet.")
  1341	   252	    else:
  1342	   253	        # L28.4: the unified diff goes in the RUN REPORT, every time. The
  1343	   254	        # heartbeat writes to the live vault every 15 minutes; a write
  1344	   255	        # path that reported only "updated" would be the one write path
  1345	   256	        # in this codebase whose changes nobody could read back.
  1346	   257	        beat.notes.append(write.report())
  1347	   258	
  1348	   259	    sent_green = False
  1349	   260	    if dry_run:
  1350	   261	        beat.notes.append("DRY RUN — no DM sent, nothing written.")
  1351	   262	    elif not beat.green:
  1352	   263	        # OUT-OF-BAND FIRST. The DM's body is rendered from `beat.notes`,
  1353	   264	        # so the email outcome has to be in the list before `send_dm`
  1354	   265	        # reads it — that is what puts "email channel DOWN: <reason>" in
  1355	   266	        # the red DM. The reverse order would report the email result
  1356	   267	        # only to the log, where a failed second channel would be
  1357	   268	        # discovered by whoever went looking, which is nobody.
  1358	   269	        beat.notes.append(out_of_band(beat))
  1359	   270	        beat.notes.append(send_dm(beat))
  1360	   271	    elif should_send_green(beat, store):
  1361	   272	        beat.notes.append(send_dm(beat))
  1362	   273	        sent_green = True
  1363	   274	
  1364	   275	    if not dry_run:
  1365	   276	        # The heartbeat records ITS OWN run like any other job — it is the
  1366	   277	        # one job nobody else is watching, so it watches itself and a
  1367	   278	        # stalled heartbeat shows up as its own MISSED row.
  1368	   279	        result = {
  1369	   280	            "green": beat.green,
  1370	   281	            "red_jobs": [j.label for j in beat.red_jobs],
  1371	   282	            "red_probes": [p.name for p in beat.red_probes],
  1372	   283	        }
  1373	   284	        prior = (store.get(JOB_LABEL) or {}).get("last_result") or {}
  1374	   285	        result["green_summary_date"] = (
  1375	   286	            beat.at.date().isoformat() if sent_green else prior.get("green_summary_date")
  1376	   287	        )
  1377	   288	        store.register_all(__import__(
  1378	   289	            "cobalt.jobs.config", fromlist=["load_job_registry"]
  1379	   290	        ).load_job_registry())
  1380	   291	        store.mark_running(JOB_LABEL, now=now or clock_mod.now_utc())
  1381	   292	        store.mark_finished(JOB_LABEL, exit_code=0, result=result, now=now or clock_mod.now_utc())
  1382	   293	
  1383	   294	    (logger.info if beat.green else logger.error)("heartbeat: {}", beat.headline)
  1384	   295	    return beat
  1385	   296	
  1386	   297	
  1387	   298	__all__ = [
  1388	   299	    "GREEN_SUMMARY_KEY",
  1389	   300	    "INTERVAL_KEY",
  1390	   301	    "JOB_LABEL",
  1391	   302	    "green_summary_at",
  1392	   303	    "interval_min",
  1393	   304	    "out_of_band",
  1394	   305	    "run_beat",
  1395	   306	    "take_beat",
  1396	   307	    "write_note_block",
  1397	   308	]
  1398	     1	"""F18's block — what he reads, in the note and in the DM.
  1399	     2	
  1400	     3	ONE RENDERER, two destinations. The daily-note block and the Mattermost
  1401	     4	DM are the same text: a heartbeat whose two channels could disagree is a
  1402	     5	heartbeat you have to check twice.
  1403	     6	"""
  1404	     7	
  1405	     8	from __future__ import annotations
  1406	     9	
  1407	    10	from dataclasses import dataclass, field
  1408	    11	from datetime import datetime
  1409	    12	from typing import Optional
  1410	    13	
  1411	    14	from cobalt.jobs.watchdog import Finding
  1412	    15	
  1413	    16	from .probes import Probe
  1414	    17	
  1415	    18	#: The L28 unit this writes. Section + stable id: same id every beat, so
  1416	    19	#: it updates in place and the note never accumulates 96 blocks a day.
  1417	    20	SECTION = "heartbeat"
  1418	    21	UNIT = "status"
  1419	    22	WRITER = "heartbeat"
  1420	    23	
  1421	    24	
  1422	    25	@dataclass
  1423	    26	class Beat:
  1424	    27	    """One heartbeat's whole result."""
  1425	    28	
  1426	    29	    at: datetime
  1427	    30	    probes: list[Probe] = field(default_factory=list)
  1428	    31	    jobs: list[Finding] = field(default_factory=list)
  1429	    32	    notes: list[str] = field(default_factory=list)
  1430	    33	
  1431	    34	    @property
  1432	    35	    def red_probes(self) -> list[Probe]:
  1433	    36	        return [p for p in self.probes if not p.ok]
  1434	    37	
  1435	    38	    @property
  1436	    39	    def red_jobs(self) -> list[Finding]:
  1437	    40	        return [j for j in self.jobs if not j.ok]
  1438	    41	
  1439	    42	    @property
  1440	    43	    def green(self) -> bool:
  1441	    44	        return not self.red_probes and not self.red_jobs
  1442	    45	
  1443	    46	    @property
  1444	    47	    def headline(self) -> str:
  1445	    48	        if self.green:
  1446	    49	            return (
  1447	    50	                f"GREEN — {len(self.jobs)} job(s), {len(self.probes)} probe(s), "
  1448	    51	                "nothing red"
  1449	    52	            )
  1450	    53	        parts = []
  1451	    54	        if self.red_jobs:
  1452	    55	            parts.append(f"{len(self.red_jobs)} job(s)")
  1453	    56	        if self.red_probes:
  1454	    57	            parts.append(f"{len(self.red_probes)} probe(s)")
  1455	    58	        return f"RED — {' and '.join(parts)}"
  1456	    59	
  1457	    60	    # -- the two renderings -------------------------------------------
  1458	    61	
  1459	    62	    def note_body(self) -> str:
  1460	    63	        """The daily-note unit. Markdown, deterministic, no LLM (L28)."""
  1461	    64	        mark = "🟢" if self.green else "🔴"
  1462	    65	        lines = [
  1463	    66	            f"{mark} **HEARTBEAT {self.headline}** · {self.at:%Y-%m-%d %H:%M:%S %Z}",
  1464	    67	            "",
  1465	    68	            "| | check | detail |",
  1466	    69	            "|---|---|---|",
  1467	    70	        ]
  1468	    71	        for probe in self.probes:
  1469	    72	            icon = "🟢" if probe.ok else ("⚪" if probe.unknown else "🔴")
  1470	    73	            lines.append(f"| {icon} | {probe.name} | {_cell(probe.detail)} |")
  1471	    74	        for job in self.jobs:
  1472	    75	            icon = "🟢" if job.ok else "🔴"
  1473	    76	            lines.append(f"| {icon} | `{job.label}` | {job.state} — {_cell(job.detail)} |")
  1474	    77	        for note in self.notes:
  1475	    78	            lines += ["", f"> {note}"]
  1476	    79	        return "\n".join(lines)
  1477	    80	
  1478	    81	    def dm_body(self) -> str:
  1479	    82	        """The Mattermost DM. Plain lines — a table in a DM is unreadable
  1480	    83	        on a phone, and the phone is where a red alert is actually read."""
  1481	    84	        head = ("🟢 " if self.green else "🔴 ") + f"COBALT HEARTBEAT {self.headline}"
  1482	    85	        lines = [head, f"{self.at:%Y-%m-%d %H:%M:%S %Z}", ""]
  1483	    86	        if self.green:
  1484	    87	            lines.append(
  1485	    88	                f"{len(self.jobs)} jobs and {len(self.probes)} probes all green."
  1486	    89	            )
  1487	    90	        else:
  1488	    91	            lines.append("RED:")
  1489	    92	            for item in [*self.red_jobs, *self.red_probes]:
  1490	    93	                name = getattr(item, "label", None) or item.name
  1491	    94	                detail = item.detail
  1492	    95	                lines.append(f"  • {name}: {detail}")
  1493	    96	            lines.append("")
  1494	    97	            lines.append("Green:")
  1495	    98	            for probe in self.probes:
  1496	    99	                if probe.ok:
  1497	   100	                    lines.append(f"  • {probe.name}: {probe.detail}")
  1498	   101	        for note in self.notes:
  1499	   102	            lines += ["", note]
  1500	   103	        return "\n".join(lines)
  1501	   104	
  1502	   105	    def console(self) -> str:
  1503	   106	        lines = [f"HEARTBEAT {self.headline}  ({self.at:%Y-%m-%d %H:%M:%S %Z})", ""]
  1504	   107	        lines += [p.line() for p in self.probes]
  1505	   108	        lines += [j.line() for j in self.jobs]
  1506	   109	        lines += ["", *self.notes]
  1507	   110	        return "\n".join(lines)
  1508	   111	
  1509	   112	
  1510	   113	def _cell(text: str) -> str:
  1511	   114	    """A markdown table cell cannot contain a raw pipe or a newline."""
  1512	   115	    return text.replace("|", "\\|").replace("\n", " ").strip()
  1513	   116	
  1514	   117	
  1515	   118	__all__ = ["SECTION", "UNIT", "WRITER", "Beat"]
  1516	   285	
  1517	   286	    if not cfg.armed:
  1518	   287	        off = ", ".join(d.name for d in cfg.destinations)
  1519	   288	        return Probe(
  1520	   289	            "backup", False,
  1521	   290	            f"NO DESTINATION ARMED ({off} all off) — there is no backup. "
  1522	   291	            "configs/cobalt/backup.yaml says what each leg is missing.",
  1523	   292	        )
  1524	   293	
  1525	   294	    max_age = timedelta(minutes=int(_tunable("heartbeat.backup_max_age_min")))
  1526	   295	    try:
  1527	   296	        age = latest_snapshot_age(cfg)
  1528	   297	    except BackupError as e:
  1529	   298	        # BackupError's text is credential-free BY CONTRACT (see
  1530	   299	        # backup/restic.py), and it is the one carrying the actionable
  1531	   300	        # sentence — "/Volumes/COBALT-BACKUP is NOT MOUNTED". A beat that
  1532	   301	        # said only `BackupError` would send someone to read the log to
  1533	   302	        # learn they need to plug a disk in.
  1534	   303	        return Probe("backup", False, str(e).split(". ")[0], unknown=True)
  1535	   304	    except Exception as e:  # noqa: BLE001 — a repo we cannot reach is not a diagnosis
  1536	   305	        return Probe("backup", False, f"could not read the repository: {type(e).__name__}",
  1537	   306	                     unknown=True)
  1538	   307	    if age is None:
  1539	   308	        return Probe("backup", False,
  1540	   309	                     f"armed ({', '.join(d.name for d in cfg.armed)}) but the repository "
  1541	   310	                     "holds NO snapshot yet")
  1542	   311	    hours = age.total_seconds() / 3600
  1543	   312	    detail = (f"newest snapshot {hours:.1f} h old across "
  1544	   313	              f"{', '.join(d.name for d in cfg.armed)}")
  1545	   314	    if age > max_age:
  1546	   315	        return Probe("backup", False,
  1547	   316	                     f"STALE — {detail} (limit {max_age.total_seconds()/3600:.0f} h)")
  1548	   317	    return Probe("backup", True, detail)
  1549	   318	
  1550	   319	
  1551	   320	def vaultwrite_blocks(now: Optional[datetime] = None) -> Probe:
  1552	   321	    """market_reset refusals + ungated migration runs since the last beat.
  1553	   322	
  1554	   323	    NOT RED ON ITS OWN. A refusal is the guard WORKING — F1 turning away
  1555	   324	    a write inside 20:00-21:00 is the system doing its job. The number is
  1556	   325	    reported because a spike means something is retrying blind, and
  1557	   326	    because the RULING on migration tooling (S1-P3, decided-with-veto)
  1558	   327	    says every ungated repair run inside the block increments this same
  1559	   328	    counter so it can never happen quietly.
  1560	   329	    """
  1561	   330	    from cobalt.session.store import SessionBlockStore
  1562	   331	
  1563	   332	    try:
  1564	   333	        store = SessionBlockStore()
  1565	   334	        counts = store.counts_over_window(now=now)
  1566	   335	    except Exception as e:  # noqa: BLE001
  1567	   336	        return Probe("vault blocks", False, f"counter unreadable: {type(e).__name__}: {e}",
  1568	   337	                     unknown=True)
  1569	   338	    refused = counts.get(SessionBlockStore.REFUSED, 0)
  1570	   339	    ungated = counts.get(SessionBlockStore.UNGATED_RUN, 0)
  1571	   340	    # BOTH numbers, always, and never summed into one. They share a
  1572	   341	    # counter because they are both "a write met the market_reset window"
  1573	   342	    # — but a refusal is the guard working and an ungated run is the
  1574	   343	    # carve-out being used, and reading five repairs as five refusals
  1575	   344	    # would send someone hunting a bug that is not there.
  1576	   345	    return Probe(
  1577	   346	        "vault blocks", True,
  1578	   347	        f"{refused} refused, {ungated} ungated repair run(s) in the counter window",
  1579	   348	    )
  1580	   349	
  1581	   350	
  1582	   351	def redactions(minutes: int, now: Optional[datetime] = None) -> Probe:
  1583	   352	    """F19 hits since the last beat.
  1584	   353	
  1585	   354	    Also not red on its own — the guard firing is the guard working. It
  1586	   355	    is on the block because a redaction count that suddenly climbs means
  1587	   356	    something started putting credentials into outbound text, and that is
  1588	   357	    worth seeing the day it starts rather than at the next audit.
  1589	   358	    """
  1590	   359	    from cobalt.redact.store import RedactionStore
  1591	   360	
  1592	   361	    try:
  1593	   362	        store = RedactionStore()
  1594	   363	        store.ensure_schema()
  1595	   364	        count = store.count_over_minutes(minutes, now=now)
  1596	   365	        by_pattern = store.by_pattern_since(
  1597	
  1598	exec
  1599	/bin/zsh -lc "nl -ba src/cobalt/jobs/cli.py | sed -n '1,180p'; nl -ba src/cobalt/jobs/wrapper.py; nl -ba src/cobalt/jobs/store.py | sed -n '1,240p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
  1600	 succeeded in 0ms:
  1601	     1	"""`cobalt jobs` — F17's command surface, plus `cobalt stop` / `resume`.
  1602	     2	
  1603	     3	    cobalt jobs list                     the table, as F18 reads it
  1604	     4	    cobalt jobs register                 upsert every row from jobs.yaml
  1605	     5	    cobalt jobs check                    run the watchdog, print findings
  1606	     6	    cobalt jobs run LABEL -- CMD ARGS    wrap any command as that job
  1607	     7	    cobalt stop  [--phrase "COBALT STOP"]
  1608	     8	    cobalt resume
  1609	     9	
  1610	    10	`jobs run` is the plist-facing half of the wrapper: a launchd job whose
  1611	    11	program is not Python (or is a `uv run` of something else) gets its row,
  1612	    12	its heartbeat and its exit code by being launched through this.
  1613	    13	"""
  1614	    14	
  1615	    15	from __future__ import annotations
  1616	    16	
  1617	    17	import argparse
  1618	    18	import subprocess
  1619	    19	import sys
  1620	    20	
  1621	    21	from cobalt import env
  1622	    22	
  1623	    23	from . import killswitch
  1624	    24	from .config import load_job_registry
  1625	    25	from .models import RED_STATES
  1626	    26	from .store import JobStore
  1627	    27	from .watchdog import sweep
  1628	    28	from .wrapper import JobStopped, job_run
  1629	    29	
  1630	    30	
  1631	    31	def _store() -> JobStore:
  1632	    32	    store = JobStore()
  1633	    33	    store.ensure_schema()
  1634	    34	    return store
  1635	    35	
  1636	    36	
  1637	    37	def cmd_list(args: argparse.Namespace) -> None:
  1638	    38	    store = _store()
  1639	    39	    print(f"database: {store.db_name}  (COBALT_ENV={env.resolve_env()})")
  1640	    40	    print(killswitch.read(store).describe())
  1641	    41	    rows = store.all()
  1642	    42	    if not rows:
  1643	    43	        print("\nno jobs registered — run `cobalt jobs register`")
  1644	    44	        return
  1645	    45	    red_values = {s.value for s in RED_STATES}
  1646	    46	    print(
  1647	    47	        f"\n{'LABEL':<28} {'KIND':<9} {'STATE':<9} {'SRC':<8} {'LAST FINISH':<20} "
  1648	    48	        f"{'EXIT':<5} CADENCE"
  1649	    49	    )
  1650	    50	    for r in rows:
  1651	    51	        finish = f"{r['finished_at']:%Y-%m-%d %H:%M:%S}" if r["finished_at"] else "-"
  1652	    52	        mark = " !" if r["state"] in red_values else "  "
  1653	    53	        print(
  1654	    54	            f"{r['label']:<28} {r['kind']:<9} {r['state']:<9}{mark[1]} "
  1655	    55	            f"{r['heartbeat_source']:<8} {finish:<20} "
  1656	    56	            f"{'-' if r['exit_code'] is None else r['exit_code']:<5} "
  1657	    57	            f"{r['expected_cadence'] or '(resident)'}"
  1658	    58	        )
  1659	    59	        if r["last_error"]:
  1660	    60	            print(f"{'':>28}   last_error: {r['last_error'][:160]}")
  1661	    61	
  1662	    62	
  1663	    63	def cmd_register(args: argparse.Namespace) -> None:
  1664	    64	    store = _store()
  1665	    65	    registry = load_job_registry()
  1666	    66	    labels = store.register_all(registry)
  1667	    67	    print(f"database: {store.db_name}  (COBALT_ENV={env.resolve_env()})")
  1668	    68	    print(f"registered {len(labels)} job(s):")
  1669	    69	    for label in labels:
  1670	    70	        spec = registry.spec(label)
  1671	    71	        print(f"  {label:<28} {spec.kind!s:<9} supervisor={spec.supervisor!s:<8} "
  1672	    72	              f"timeout={spec.timeout_s}s  {spec.cadence or '(resident)'}")
  1673	    73	
  1674	    74	
  1675	    75	def cmd_readers(args: argparse.Namespace) -> None:
  1676	    76	    """`cobalt jobs readers <path>` — who must be restarted for this file.
  1677	    77	
  1678	    78	    THE COMMAND THAT PRODUCES A DEPLOY PLAN'S `RESTARTS:` LINE. The law
  1679	    79	    has been ruled three times (2026-09-04, 09-08 on aset.yaml, 09-09 on
  1680	    80	    tunables.yaml): a config-shape change and the restart of every
  1681	    81	    resident that reads that file are ONE ACTION. Re-deriving that list
  1682	    82	    from memory at deploy time is what failed on 09-08, when a plan that
  1683	    83	    said "nothing else is restarted" left the ASET sheet answering 200s
  1684	    84	    and refusing every card for thirteen hours.
  1685	    85	
  1686	    86	    EXIT 1 ON AN UNKNOWN PATH, and that is the useful half. "No resident
  1687	    87	    re-reads this" and "nobody has written down who reads this" are
  1688	    88	    different answers, and only one of them means it is safe to deploy
  1689	    89	    without a restart. A path no row mentions gets a non-zero exit and
  1690	    90	    the list of paths that ARE covered, so the operator knows they are
  1691	    91	    looking at a gap rather than an all-clear.
  1692	    92	    """
  1693	    93	    from pathlib import Path
  1694	    94	
  1695	    95	    registry = load_job_registry()
  1696	    96	    path = args.path
  1697	    97	    readers = registry.readers_of(path)
  1698	    98	
  1699	    99	    if not readers:
  1700	   100	        known = registry.read_paths
  1701	   101	        print(
  1702	   102	            f"UNKNOWN PATH: no job row lists {path!r} as re-read at runtime.\n"
  1703	   103	            "\n"
  1704	   104	            "That is NOT the same as 'nothing reads it'. `reads` is derived by hand\n"
  1705	   105	            "from the code, so an unlisted path means nobody has worked out its\n"
  1706	   106	            "readers yet — check before deploying a change to it, and add the row.\n"
  1707	   107	            "\n"
  1708	   108	            "Paths that ARE covered:\n  " + ("\n  ".join(known) or "(none)"),
  1709	   109	            file=sys.stderr,
  1710	   110	        )
  1711	   111	        sys.exit(1)
  1712	   112	
  1713	   113	    print(f"{path} is re-read at runtime by {len(readers)} resident(s):")
  1714	   114	    for spec in readers:
  1715	   115	        print(f"  {spec.label:<28} {spec.what.strip().splitlines()[0]}")
  1716	   116	    print("\nRESTARTS: " + " ".join(s.label for s in readers))
  1717	   117	    print("  launchctl kickstart -k gui/$(id -u)/<label>")
  1718	   118	
  1719	   119	
  1720	   120	def cmd_check(args: argparse.Namespace) -> None:
  1721	   121	    findings = sweep()
  1722	   122	    for f in findings:
  1723	   123	        print(f.line())
  1724	   124	    bad = [f for f in findings if not f.ok]
  1725	   125	    print(f"\n{len(findings)} job(s) checked, {len(bad)} RED.")
  1726	   126	    if bad:
  1727	   127	        sys.exit(1)
  1728	   128	
  1729	   129	
  1730	   130	def cmd_run(args: argparse.Namespace) -> None:
  1731	   131	    """Wrap an arbitrary command as `label`. Its exit code is ours."""
  1732	   132	    if not args.command:
  1733	   133	        raise SystemExit("nothing to run — pass the command after `--`")
  1734	   134	    try:
  1735	   135	        with job_run(args.label) as run:
  1736	   136	            proc = subprocess.run(args.command)
  1737	   137	            run.result = {"argv": args.command, "returncode": proc.returncode}
  1738	   138	            if proc.returncode != 0:
  1739	   139	                raise RuntimeError(
  1740	   140	                    f"{args.label}: `{' '.join(args.command)}` exited "
  1741	   141	                    f"{proc.returncode}"
  1742	   142	                )
  1743	   143	    except JobStopped as e:
  1744	   144	        # Exit 0: a deliberate stop is not a failure and must not paint
  1745	   145	        # F18 red for a state the operator caused on purpose.
  1746	   146	        print(f"NOT RUN — {e}")
  1747	   147	        return
  1748	   148	    print(f"{args.label}: exit 0")
  1749	   149	
  1750	   150	
  1751	   151	def cmd_stop(args: argparse.Namespace) -> None:
  1752	   152	    state = killswitch.engage(by=args.by, phrase=args.phrase)
  1753	   153	    print(state.describe())
  1754	   154	
  1755	   155	
  1756	   156	def cmd_resume(args: argparse.Namespace) -> None:
  1757	   157	    state = killswitch.clear(by=args.by)
  1758	   158	    print(state.describe())
  1759	   159	
  1760	   160	
  1761	   161	def add_parser(sub) -> None:
  1762	   162	    jobs = sub.add_parser("jobs", help="F17 task integrity (Charter §3 F17)")
  1763	   163	    jsub = jobs.add_subparsers(dest="command", required=True)
  1764	   164	
  1765	   165	    lst = jsub.add_parser("list", help="Every job row, as F18 reads it.")
  1766	   166	    lst.set_defaults(func=cmd_list)
  1767	   167	
  1768	   168	    reg = jsub.add_parser("register", help="Upsert every row from configs/cobalt/jobs.yaml.")
  1769	   169	    reg.set_defaults(func=cmd_register)
  1770	   170	
  1771	   171	    check = jsub.add_parser("check", help="Run the watchdog (zombie / missed).")
  1772	   172	    check.set_defaults(func=cmd_check)
  1773	   173	
  1774	   174	    readers = jsub.add_parser(
  1775	   175	        "readers",
  1776	   176	        help="Which residents re-read a config file — the deploy plan's RESTARTS line.",
  1777	   177	    )
  1778	   178	    readers.add_argument("path", help="Repo-relative config path, e.g. configs/cobalt/taxonomy/tunables.yaml")
  1779	   179	    readers.set_defaults(func=cmd_readers)
  1780	   180	
  1781	     1	"""F17b: the wrapper every scheduled job runs inside.
  1782	     2	
  1783	     3	Charter §3 F17: "marks running/done/failed with exit code and stamps
  1784	     4	heartbeat_at at least every timeout_s/3 for long jobs."
  1785	     5	
  1786	     6	TWO WAYS IN, one implementation:
  1787	     7	
  1788	     8	    # a Python entry point (prefill, archiver, cards-expire, …)
  1789	     9	    with job_run("com.cobalt.archiver") as run:
  1790	    10	        summary = do_the_work()
  1791	    11	        run.result = {"rows_written": summary.rows_written}
  1792	    12	
  1793	    13	    # anything else, from a plist
  1794	    14	    uv run cobalt jobs run com.cobalt.prefill-daily -- uv run prefill daily
  1795	    15	
  1796	    16	WHAT IT GUARANTEES, in order:
  1797	    17	
  1798	    18	1. THE KILL SWITCH IS CHECKED FIRST. A stopped Cobalt does not start a
  1799	    19	   one-shot at all — and it exits 0, not 1, because a deliberate stop is
  1800	    20	   not a failure and must not paint F18 red.
  1801	    21	2. `running` is marked before the work, with `started_at`.
  1802	    22	3. A BEATER THREAD stamps `heartbeat_at` every `timeout_s /
  1803	    23	   jobs.heartbeat_fraction` (5 min for the 15-min archiver window). This
  1804	    24	   is the ONLY thing that distinguishes a long job from a hung one — the
  1805	    25	   archiver legitimately runs 23 minutes, so "started and did not
  1806	    26	   finish" cannot be the zombie test.
  1807	    27	4. `done` (exit 0) or `failed` (exit code + the exception, redacted
  1808	    28	   through F19 on the way into the column) — and `failed` is LOUD.
  1809	    29	5. The exception is RE-RAISED. The wrapper reports; it never swallows.
  1810	    30	
  1811	    31	The beater thread is a daemon: if the job process dies hard, the thread
  1812	    32	dies with it, `heartbeat_at` stops advancing, and the watchdog draws the
  1813	    33	right conclusion. A thread that outlived its job would keep a dead job
  1814	    34	looking alive, which is the exact failure this feature exists to catch.
  1815	    35	"""
  1816	    36	
  1817	    37	from __future__ import annotations
  1818	    38	
  1819	    39	import threading
  1820	    40	import traceback
  1821	    41	from contextlib import contextmanager
  1822	    42	from typing import Any, Optional
  1823	    43	
  1824	    44	from loguru import logger
  1825	    45	
  1826	    46	from . import killswitch
  1827	    47	from .config import JobSpec, load_job_registry
  1828	    48	from .store import JobStore
  1829	    49	
  1830	    50	#: The tunables row governing how often a long job stamps (F16).
  1831	    51	HEARTBEAT_FRACTION_KEY = "jobs.heartbeat_fraction"
  1832	    52	
  1833	    53	#: Exit code a job uses when the kill switch turned it away. ZERO, on
  1834	    54	#: purpose — see guarantee 1.
  1835	    55	STOPPED_EXIT_CODE = 0
  1836	    56	
  1837	    57	
  1838	    58	class JobStopped(RuntimeError):
  1839	    59	    """The kill switch is engaged; this run did not happen."""
  1840	    60	
  1841	    61	
  1842	    62	def heartbeat_fraction() -> int:
  1843	    63	    from cobalt.taxonomy.loader import load_tunables
  1844	    64	
  1845	    65	    row = load_tunables().by_key.get(HEARTBEAT_FRACTION_KEY)
  1846	    66	    if row is None:
  1847	    67	        raise RuntimeError(
  1848	    68	            f"tunable {HEARTBEAT_FRACTION_KEY!r} is missing from tunables.yaml — the "
  1849	    69	            "wrapper reads its stamp interval from config and has no built-in "
  1850	    70	            "default (F16)."
  1851	    71	        )
  1852	    72	    return int(row.value)
  1853	    73	
  1854	    74	
  1855	    75	class _Beater:
  1856	    76	    """Stamps `heartbeat_at` on a timer until the run ends."""
  1857	    77	
  1858	    78	    def __init__(self, store: JobStore, label: str, every_s: float):
  1859	    79	        self.store = store
  1860	    80	        self.label = label
  1861	    81	        self.every_s = max(1.0, every_s)
  1862	    82	        self._stop = threading.Event()
  1863	    83	        self._thread = threading.Thread(
  1864	    84	            target=self._loop, name=f"beat:{label}", daemon=True
  1865	    85	        )
  1866	    86	
  1867	    87	    def _loop(self) -> None:
  1868	    88	        while not self._stop.wait(self.every_s):
  1869	    89	            try:
  1870	    90	                self.store.beat(self.label)
  1871	    91	            except Exception as e:  # noqa: BLE001
  1872	    92	                # A missed stamp is not a reason to kill the job. It IS a
  1873	    93	                # reason to say so: the watchdog may conclude ZOMBIE from
  1874	    94	                # this, and an operator needs the other half of the story.
  1875	    95	                logger.error(
  1876	    96	                    "F17: heartbeat stamp FAILED for {} ({}: {}) — the job is still "
  1877	    97	                    "running; the watchdog may see a stale heartbeat.",
  1878	    98	                    self.label, type(e).__name__, e,
  1879	    99	                )
  1880	   100	
  1881	   101	    def __enter__(self) -> "_Beater":
  1882	   102	        self._thread.start()
  1883	   103	        return self
  1884	   104	
  1885	   105	    def __exit__(self, *exc) -> None:
  1886	   106	        self._stop.set()
  1887	   107	
  1888	   108	
  1889	   109	class JobRun:
  1890	   110	    """Handle a wrapped job can hang its result on."""
  1891	   111	
  1892	   112	    def __init__(self, spec: JobSpec):
  1893	   113	        self.spec = spec
  1894	   114	        self.label = spec.label
  1895	   115	        #: Whatever the run wants F18 to be able to report — the
  1896	   116	        #: archiver's `rows_written` is what makes "archiver freshness
  1897	   117	        #: (last run + rows written)" answerable.
  1898	   118	        self.result: Optional[dict[str, Any]] = None
  1899	   119	
  1900	   120	
  1901	   121	@contextmanager
  1902	   122	def job_run(
  1903	   123	    label: str,
  1904	   124	    *,
  1905	   125	    store: Optional[JobStore] = None,
  1906	   126	    register: bool = True,
  1907	   127	    allow_prod: bool = False,
  1908	   128	):
  1909	   129	    """Run a block as a registered job. See the module docstring."""
  1910	   130	    registry = load_job_registry()
  1911	   131	    spec = registry.spec(label)
  1912	   132	    store = store or JobStore()
  1913	   133	    store.ensure_schema(allow_prod=allow_prod)
  1914	   134	    if register:
  1915	   135	        store.register(spec, allow_prod=allow_prod)
  1916	   136	
  1917	   137	    if killswitch.is_active(store):
  1918	   138	        state = killswitch.read(store)
  1919	   139	        logger.error("F17: {} REFUSED TO START — {}", label, state.describe())
  1920	   140	        raise JobStopped(state.describe())
  1921	   141	
  1922	   142	    store.mark_running(label)
  1923	   143	    run = JobRun(spec)
  1924	   144	    every_s = spec.timeout_s / heartbeat_fraction()
  1925	   145	    logger.info(
  1926	   146	        "F17: {} RUNNING (timeout {}s, heartbeat every {:.0f}s)",
  1927	   147	        label, spec.timeout_s, every_s,
  1928	   148	    )
  1929	   149	    try:
  1930	   150	        with _Beater(store, label, every_s):
  1931	   151	            yield run
  1932	   152	    except BaseException as e:
  1933	   153	        store.mark_finished(
  1934	   154	            label,
  1935	   155	            exit_code=1,
  1936	   156	            error=f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=8)}",
  1937	   157	            result=run.result,
  1938	   158	        )
  1939	   159	        logger.error("F17: {} FAILED — {}: {}", label, type(e).__name__, e)
  1940	   160	        raise            # the wrapper reports; it never swallows
  1941	   161	    store.mark_finished(label, exit_code=0, result=run.result)
  1942	   162	    logger.info("F17: {} DONE", label)
  1943	   163	
  1944	   164	
  1945	   165	def should_keep_running(label: str, *, store: Optional[JobStore] = None) -> bool:
  1946	   166	    """A RESIDENT's own loop check. `False` means exit cleanly now.
  1947	   167	
  1948	   168	    Residents call this where they can stop without tearing out of a
  1949	   169	    write. Cobalt's residents today are supervised by launchd rather than
  1950	   170	    wrapped (see jobs.yaml), so this exists for the first new-core
  1951	   171	    resident — the S2 radar poller — and for anything the chief of staff
  1952	   172	    grows into.
  1953	   173	    """
  1954	   174	    if killswitch.is_active(store):
  1955	   175	        logger.error(
  1956	   176	            "F17: kill switch engaged — {} is exiting cleanly at its next safe point.",
  1957	   177	            label,
  1958	   178	        )
  1959	   179	        return False
  1960	   180	    return True
  1961	   181	
  1962	   182	
  1963	   183	__all__ = [
  1964	   184	    "HEARTBEAT_FRACTION_KEY",
  1965	   185	    "STOPPED_EXIT_CODE",
  1966	   186	    "JobRun",
  1967	   187	    "JobStopped",
  1968	   188	    "heartbeat_fraction",
  1969	   189	    "job_run",
  1970	   190	    "should_keep_running",
  1971	   191	]
  1972	     1	"""F17 persistence: the `cobalt_jobs` row, and the kill switch behind it.
  1973	     2	
  1974	     3	THE TABLE IS `cobalt_jobs`, NOT `jobs`. `cobalt_brain` is the same
  1975	     4	Postgres database Mattermost runs in, and Mattermost owns a `jobs` table
  1976	     5	with 164,320 rows — see the note at the head of
  1977	     6	`migrations/0001_cobalt_jobs.sql` for how that was found and why only the
  1978	     7	tables introduced by this prompt carry the prefix.
  1979	     8	
  1980	     9	Database from `COBALT_ENV` via `env.resolve_db_name()` (RULING 7/9);
  1981	    10	`db_name` is the test/tooling seam only.
  1982	    11	
  1983	    12	NOT SESSION-GATED, and this one is deliberate. `cobalt.session`'s
  1984	    13	market_reset hard block exists to stop Cobalt WRITING TRADING RECORD in
  1985	    14	the 20:00-21:00 window. A job's own state is not trading record — and the
  1986	    15	archiver, the one job that runs squarely inside that window by design
  1987	    16	(20:30, its own carve-out in L28), is exactly the job whose failure the
  1988	    17	heartbeat most needs to see. A `jobs` table that went blind for an hour
  1989	    18	every evening would go blind for the hour it matters most.
  1990	    19	"""
  1991	    20	
  1992	    21	from __future__ import annotations
  1993	    22	
  1994	    23	import json
  1995	    24	from datetime import datetime, timedelta
  1996	    25	from pathlib import Path
  1997	    26	from typing import Any, Optional
  1998	    27	
  1999	    28	from cobalt import db, env
  2000	    29	from cobalt.db import Side
  2001	    30	from cobalt.session import clock as clock_mod
  2002	    31	
  2003	    32	from .config import JobSpec
  2004	    33	from .models import JobState, Supervisor
  2005	    34	
  2006	    35	MIGRATIONS_DIR = Path(__file__).parent / "migrations"
  2007	    36	
  2008	    37	
  2009	    38	class JobStoreError(RuntimeError):
  2010	    39	    """A job operation was refused."""
  2011	    40	
  2012	    41	
  2013	    42	class JobStore:
  2014	    43	    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
  2015	    44	    #: The scheduler's own bookkeeping: one row per launchd label, plus
  2016	    45	    #: the kill switch. Engine state, identical on every install.
  2017	    46	    SIDE = Side.SYSTEM
  2018	    47	
  2019	    48	    def __init__(self, db_name: Optional[str] = None):
  2020	    49	        self.db_name = db_name or env.resolve_db_name()
  2021	    50	
  2022	    51	    def _connect(self, *, allow_prod: bool = False):
  2023	    52	        return db.connect(self.db_name, side=self.SIDE, allow_prod=allow_prod)
  2024	    53	
  2025	    54	    def ensure_schema(self, *, allow_prod: bool = False) -> None:
  2026	    55	        with self._connect(allow_prod=allow_prod) as conn:
  2027	    56	            db.assert_schemas_exist(conn)
  2028	    57	            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
  2029	    58	                lines = migration.read_text().splitlines()
  2030	    59	                sql = "\n".join(l for l in lines if not l.strip().startswith("--"))
  2031	    60	                for statement in sql.split(";"):
  2032	    61	                    statement = statement.strip()
  2033	    62	                    if statement:
  2034	    63	                        conn.execute(statement)
  2035	    64	
  2036	    65	    # -- registration -------------------------------------------------
  2037	    66	
  2038	    67	    def register(self, spec: JobSpec, *, allow_prod: bool = False) -> None:
  2039	    68	        """Upsert one row from its config spec. IDEMPOTENT, and it does
  2040	    69	        NOT touch runtime columns: re-registering after a config edit
  2041	    70	        must never erase the last run's exit code, which is the one thing
  2042	    71	        an operator looks at first."""
  2043	    72	        with self._connect(allow_prod=allow_prod) as conn:
  2044	    73	            conn.execute(
  2045	    74	                "INSERT INTO cobalt_jobs (label, kind, expected_cadence, timeout_s, "
  2046	    75	                "heartbeat_source) VALUES (%s, %s, %s, %s, %s) "
  2047	    76	                "ON CONFLICT (label) DO UPDATE SET kind = EXCLUDED.kind, "
  2048	    77	                "expected_cadence = EXCLUDED.expected_cadence, "
  2049	    78	                "timeout_s = EXCLUDED.timeout_s, "
  2050	    79	                "heartbeat_source = EXCLUDED.heartbeat_source, updated_at = now()",
  2051	    80	                (
  2052	    81	                    spec.label,
  2053	    82	                    spec.kind.value,
  2054	    83	                    spec.cadence,
  2055	    84	                    spec.timeout_s,
  2056	    85	                    spec.supervisor.value,
  2057	    86	                ),
  2058	    87	            )
  2059	    88	
  2060	    89	    def register_all(self, registry, *, allow_prod: bool = False) -> list[str]:
  2061	    90	        self.ensure_schema(allow_prod=allow_prod)
  2062	    91	        for spec in registry.jobs:
  2063	    92	            self.register(spec, allow_prod=allow_prod)
  2064	    93	        return [s.label for s in registry.jobs]
  2065	    94	
  2066	    95	    # -- reads --------------------------------------------------------
  2067	    96	
  2068	    97	    def get(self, label: str) -> Optional[dict[str, Any]]:
  2069	    98	        with self._connect() as conn:
  2070	    99	            cur = conn.execute("SELECT * FROM cobalt_jobs WHERE label = %s", (label,))
  2071	   100	            row = cur.fetchone()
  2072	   101	            if row is None:
  2073	   102	                return None
  2074	   103	            return dict(zip([d.name for d in cur.description], row))
  2075	   104	
  2076	   105	    def all(self) -> list[dict[str, Any]]:
  2077	   106	        with self._connect() as conn:
  2078	   107	            cur = conn.execute("SELECT * FROM cobalt_jobs ORDER BY kind DESC, label")
  2079	   108	            columns = [d.name for d in cur.description]
  2080	   109	            return [dict(zip(columns, r)) for r in cur.fetchall()]
  2081	   110	
  2082	   111	    # -- the run lifecycle (the wrapper's three calls) -----------------
  2083	   112	
  2084	   113	    def mark_running(self, label: str, *, now: Optional[datetime] = None) -> None:
  2085	   114	        ts = now or clock_mod.now_utc()
  2086	   115	        with self._connect() as conn:
  2087	   116	            cur = conn.execute(
  2088	   117	                "UPDATE cobalt_jobs SET state = %s, started_at = %s, heartbeat_at = %s, "
  2089	   118	                "finished_at = NULL, exit_code = NULL, last_error = NULL, "
  2090	   119	                "updated_at = now() WHERE label = %s",
  2091	   120	                (JobState.RUNNING.value, ts, ts, label),
  2092	   121	            )
  2093	   122	            if cur.rowcount != 1:
  2094	   123	                raise JobStoreError(
  2095	   124	                    f"no jobs row for {label!r} — register it first "
  2096	   125	                    "(`cobalt jobs register`). F17 refuses to run a job it cannot "
  2097	   126	                    "report on: an unregistered job that hangs is invisible."
  2098	   127	                )
  2099	   128	
  2100	   129	    def beat(self, label: str, *, now: Optional[datetime] = None) -> None:
  2101	   130	        """Stamp `heartbeat_at`. The only thing separating a long job
  2102	   131	        from a hung one."""
  2103	   132	        with self._connect() as conn:
  2104	   133	            conn.execute(
  2105	   134	                "UPDATE cobalt_jobs SET heartbeat_at = %s, updated_at = now() WHERE label = %s",
  2106	   135	                (now or clock_mod.now_utc(), label),
  2107	   136	            )
  2108	   137	
  2109	   138	    def mark_finished(
  2110	   139	        self,
  2111	   140	        label: str,
  2112	   141	        *,
  2113	   142	        exit_code: int,
  2114	   143	        error: Optional[str] = None,
  2115	   144	        result: Optional[dict[str, Any]] = None,
  2116	   145	        now: Optional[datetime] = None,
  2117	   146	    ) -> None:
  2118	   147	        """`done` on 0, `failed` on anything else. Failed is LOUD: F18
  2119	   148	        turns red on this column, and the error text goes with it."""
  2120	   149	        ts = now or clock_mod.now_utc()
  2121	   150	        state = JobState.DONE if exit_code == 0 else JobState.FAILED
  2122	   151	        # F19: a job's own error text is outbound the moment F18 puts it
  2123	   152	        # in a DM. Redacting at the point of STORAGE means a traceback
  2124	   153	        # carrying a DSN never becomes a row that later leaks.
  2125	   154	        safe_error = None
  2126	   155	        if error:
  2127	   156	            from cobalt.redact import redact
  2128	   157	
  2129	   158	            safe_error = redact(error, channel="jobs.last_error").text
  2130	   159	        with self._connect() as conn:
  2131	   160	            conn.execute(
  2132	   161	                "UPDATE cobalt_jobs SET state = %s, finished_at = %s, heartbeat_at = %s, "
  2133	   162	                "exit_code = %s, last_error = %s, last_result = %s, updated_at = now() "
  2134	   163	                "WHERE label = %s",
  2135	   164	                (
  2136	   165	                    state.value,
  2137	   166	                    ts,
  2138	   167	                    ts,
  2139	   168	                    exit_code,
  2140	   169	                    safe_error,
  2141	   170	                    json.dumps(result, default=str) if result is not None else None,
  2142	   171	                    label,
  2143	   172	                ),
  2144	   173	            )
  2145	   174	
  2146	   175	    def mark_zombie(self, label: str, *, reason: str) -> None:
  2147	   176	        """The watchdog's conclusion. Nothing else may write this state."""
  2148	   177	        from cobalt.redact import redact
  2149	   178	
  2150	   179	        with self._connect() as conn:
  2151	   180	            conn.execute(
  2152	   181	                "UPDATE cobalt_jobs SET state = %s, last_error = %s, updated_at = now() "
  2153	   182	                "WHERE label = %s",
  2154	   183	                (JobState.ZOMBIE.value, redact(reason, channel="jobs.last_error").text, label),
  2155	   184	            )
  2156	   185	
  2157	   186	    def mark_probe(
  2158	   187	        self,
  2159	   188	        label: str,
  2160	   189	        *,
  2161	   190	        alive: bool,
  2162	   191	        detail: str,
  2163	   192	        now: Optional[datetime] = None,
  2164	   193	    ) -> None:
  2165	   194	        """Stamp a resident whose heartbeat comes from a PROBE, not from
  2166	   195	        itself (`supervisor: launchd | pidfile`).
  2167	   196	
  2168	   197	        A probe says "the process exists". That is a weaker claim than a
  2169	   198	        wrapper's "I am running and past my gates", which is why
  2170	   199	        `heartbeat_source` is a column: the two must never be read as the
  2171	   200	        same evidence.
  2172	   201	        """
  2173	   202	        from cobalt.redact import redact
  2174	   203	
  2175	   204	        ts = now or clock_mod.now_utc()
  2176	   205	        safe = redact(detail, channel="jobs.last_error").text
  2177	   206	        with self._connect() as conn:
  2178	   207	            if alive:
  2179	   208	                conn.execute(
  2180	   209	                    "UPDATE cobalt_jobs SET state = %s, heartbeat_at = %s, last_error = NULL, "
  2181	   210	                    "updated_at = now() WHERE label = %s",
  2182	   211	                    (JobState.RUNNING.value, ts, label),
  2183	   212	                )
  2184	   213	            else:
  2185	   214	                conn.execute(
  2186	   215	                    "UPDATE cobalt_jobs SET state = %s, last_error = %s, updated_at = now() "
  2187	   216	                    "WHERE label = %s",
  2188	   217	                    (JobState.FAILED.value, safe, label),
  2189	   218	                )
  2190	   219	
  2191	   220	    # -- the kill switch (F17d) ---------------------------------------
  2192	   221	
  2193	   222	    def kill_switch(self) -> dict[str, Any]:
  2194	   223	        with self._connect() as conn:
  2195	   224	            cur = conn.execute("SELECT * FROM cobalt_kill_switch WHERE id = TRUE")
  2196	   225	            row = cur.fetchone()
  2197	   226	            if row is None:
  2198	   227	                return {"active": False}
  2199	   228	            return dict(zip([d.name for d in cur.description], row))
  2200	   229	
  2201	   230	    def set_kill_switch(
  2202	   231	        self, *, active: bool, phrase: Optional[str], by: str,
  2203	   232	        now: Optional[datetime] = None,
  2204	   233	    ) -> dict[str, Any]:
  2205	   234	        ts = now or clock_mod.now_utc()
  2206	   235	        with self._connect() as conn:
  2207	   236	            if active:
  2208	   237	                conn.execute(
  2209	   238	                    "UPDATE cobalt_kill_switch SET active = TRUE, phrase = %s, set_by = %s, "
  2210	   239	                    "set_at = %s, cleared_by = NULL, cleared_at = NULL WHERE id = TRUE",
  2211	   240	                    (phrase, by, ts),
  2212	
  2213	exec
  2214	/bin/zsh -lc "nl -ba src/cobalt/jobs/config.py | sed -n '200,355p'; nl -ba configs/cobalt/jobs.yaml | sed -n '175,240p'; nl -ba ops/README.md; nl -ba 'docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md'; git status --short" in /Users/cobalt/cobalt-wt/heartbeat-mr
  2215	 succeeded in 0ms:
  2216	   200	
  2217	   201	        launchd has no "every N minutes between 06:00 and 23:00": it has
  2218	   202	        `StartInterval` (which never stops) and `StartCalendarInterval`
  2219	   203	        (which is a list of moments). A window is therefore EXPANDED into
  2220	   204	        moments here, and the test suite compares this list against the
  2221	   205	        plist's own array so the two can never drift.
  2222	   206	        """
  2223	   207	        minutes = self.interval_minutes()
  2224	   208	        span = self.window()
  2225	   209	        if minutes is None or span is None:
  2226	   210	            return []
  2227	   211	        opens, closes = span
  2228	   212	        entries: list[dict[str, int]] = []
  2229	   213	        for day in sorted(self.weekdays):
  2230	   214	            cursor = opens.hour * 60 + opens.minute
  2231	   215	            last = closes.hour * 60 + closes.minute
  2232	   216	            while cursor <= last:
  2233	   217	                entries.append(
  2234	   218	                    {"Weekday": day, "Hour": cursor // 60, "Minute": cursor % 60}
  2235	   219	                )
  2236	   220	                cursor += minutes
  2237	   221	        return entries
  2238	   222	
  2239	   223	
  2240	   224	class JobSpec(BaseModel):
  2241	   225	    model_config = ConfigDict(extra="forbid")
  2242	   226	
  2243	   227	    label: str = Field(min_length=1)
  2244	   228	    kind: JobKind
  2245	   229	    supervisor: Supervisor
  2246	   230	    timeout_s: int = Field(gt=0)
  2247	   231	    what: str = Field(min_length=1)
  2248	   232	    schedule: Optional[Schedule] = None
  2249	   233	    pidfile: Optional[str] = None
  2250	   234	    #: Is this job's plist supposed to be LOADED in launchd right now?
  2251	   235	    #:
  2252	   236	    #: Default True, because that is what every job in this registry has
  2253	   237	    #: always meant. `enabled: false` is the narrow, declared case of a
  2254	   238	    #: job that is BUILT, registered and reviewable but deliberately not
  2255	   239	    #: yet handed over to launchd — `com.cobalt.herdr` is the first, and
  2256	   240	    #: it exists because the handover has to happen at the keyboard (the
  2257	   241	    #: server being registered is the one hosting the session that would
  2258	   242	    #: register it).
  2259	   243	    #:
  2260	   244	    #: THE FLAG SUPPRESSES THE PROBE, NOT THE ROW. A disabled job is
  2261	   245	    #: still in the registry, still has to have a plist in ops/, still
  2262	   246	    #: has its schedule cross-checked by the suite. What it does not get
  2263	   247	    #: is a red "NOT LOADED in launchd" every 15 minutes for a state
  2264	   248	    #: somebody chose on purpose — which is exactly the kind of standing
  2265	   249	    #: red that teaches a reader to scroll past the heartbeat.
  2266	   250	    #:
  2267	   251	    #: Flipping it to true is the LAST step of a handover, after the
  2268	   252	    #: bootstrap: true means "launchd should hold this, tell me if it
  2269	   253	    #: does not".
  2270	   254	    enabled: bool = True
  2271	   255	
  2272	   256	    #: Repo-relative config files this RESIDENT RE-READS AT RUNTIME.
  2273	   257	    #:
  2274	   258	    #: THE LAW THIS SERVES, ruled three times (2026-09-04, 2026-09-08 on
  2275	   259	    #: aset.yaml, 2026-09-09 on tunables.yaml): a config-shape change and
  2276	   260	    #: the restart of every resident that reads that file are ONE ACTION.
  2277	   261	    #: The 09-09 case is the one to remember — the 09-08 seat-usage deploy
  2278	   262	    #: added a `TunableUnit.WINDOW` row to tunables.yaml and its plan said
  2279	   263	    #: "nothing else is restarted". The ASET sheet re-reads that file on
  2280	   264	    #: every request, through code that predated the enum value, so from
  2281	   265	    #: roughly 19:00 to 07:06 the page he trades beside answered HTTP 200
  2282	   266	    #: and refused every card. The deploy was right about its own job and
  2283	   267	    #: wrong about everybody else's.
  2284	   268	    #:
  2285	   269	    #: EVERY ENTRY IS DERIVED FROM THE CODE, never guessed: a row here
  2286	   270	    #: claims that a specific loader call reads a specific file on a
  2287	   271	    #: request path, and the 2026-09-09 ops report cites file:line for
  2288	   272	    #: each one. A guessed row is worse than an empty list, because
  2289	   273	    #: `cobalt jobs readers` is trusted to be complete.
  2290	   274	    #:
  2291	   275	    #: ONE-SHOTS LEAVE IT EMPTY, and `cobalt validate` enforces that: a
  2292	   276	    #: one-shot re-reads everything every time it runs, by definition —
  2293	   277	    #: it starts, reads, exits. There is no stale process to restart, so
  2294	   278	    #: rows here would be noise diluting the ones that mean something.
  2295	   279	    #:
  2296	   280	    #: KNOWN GAP, deliberately not papered over: this is RE-READS, not
  2297	   281	    #: reads. A resident that loads a config ONCE AT STARTUP also needs a
  2298	   282	    #: restart when it changes, and `com.cobalt.agent` (the old tree) is
  2299	   283	    #: exactly that shape — it caches settings in a singleton at first
  2300	   284	    #: construction (`cobalt_agent/config.py:410`). That wants its own
  2301	   285	    #: field; see the 09-09 report's ESCALATE.
  2302	   286	    reads: list[str] = Field(default_factory=list)
  2303	   287	
  2304	   288	    @model_validator(mode="after")
  2305	   289	    def _shape_matches_kind(self) -> "JobSpec":
  2306	   290	        if self.kind is JobKind.ONE_SHOT and self.reads:
  2307	   291	            raise ValueError(
  2308	   292	                f"{self.label}: `reads` belongs to a RESIDENT. A one-shot re-reads "
  2309	   293	                "everything every time it runs — there is no stale process to "
  2310	   294	                "restart, so naming files here dilutes the rows that do mean "
  2311	   295	                "something."
  2312	   296	            )
  2313	   297	        bad = [p for p in self.reads if Path(p).is_absolute() or ".." in Path(p).parts]
  2314	   298	        if bad:
  2315	   299	            raise ValueError(
  2316	   300	                f"{self.label}: `reads` entries are REPO-RELATIVE with no `..`: {bad}"
  2317	   301	            )
  2318	   302	        if self.kind is JobKind.ONE_SHOT and self.schedule is None:
  2319	   303	            raise ValueError(
  2320	   304	                f"{self.label}: a one-shot needs a `schedule` — the MISSED probe "
  2321	   305	                "asks 'should this have run by now', and without a schedule there "
  2322	   306	                "is no answer, only silence."
  2323	   307	            )
  2324	   308	        if self.supervisor is Supervisor.PIDFILE and not self.pidfile:
  2325	   309	            raise ValueError(f"{self.label}: supervisor `pidfile` needs a `pidfile` path")
  2326	   310	        if self.supervisor is not Supervisor.PIDFILE and self.pidfile:
  2327	   311	            raise ValueError(
  2328	   312	                f"{self.label}: `pidfile` is set but the supervisor is "
  2329	   313	                f"{self.supervisor} — nothing would read it."
  2330	   314	            )
  2331	   315	        return self
  2332	   316	
  2333	   317	    @property
  2334	   318	    def cadence(self) -> Optional[str]:
  2335	   319	        return self.schedule.describe() if self.schedule else None
  2336	   320	
  2337	   321	    @property
  2338	   322	    def pidfile_path(self) -> Optional[Path]:
  2339	   323	        return (REPO_ROOT / self.pidfile) if self.pidfile else None
  2340	   324	
  2341	   325	    @property
  2342	   326	    def plist_path(self) -> Path:
  2343	   327	        return OPS_DIR / f"{self.label}.plist"
  2344	   328	
  2345	   329	
  2346	   330	class JobRegistry(BaseModel):
  2347	   331	    model_config = ConfigDict(extra="forbid")
  2348	   332	
  2349	   333	    jobs: list[JobSpec] = Field(min_length=1)
  2350	   334	    kill_phrase: str = Field(min_length=1)
  2351	   335	    resume_phrase: str = Field(min_length=1)
  2352	   336	
  2353	   337	    @model_validator(mode="after")
  2354	   338	    def _unique_labels(self) -> "JobRegistry":
  2355	   339	        labels = [j.label for j in self.jobs]
  2356	   340	        dupes = sorted({l for l in labels if labels.count(l) > 1})
  2357	   341	        if dupes:
  2358	   342	            raise ValueError(f"duplicate job label(s): {dupes}")
  2359	   343	        if self.kill_phrase.strip().upper() == self.resume_phrase.strip().upper():
  2360	   344	            raise ValueError("kill_phrase and resume_phrase must differ")
  2361	   345	        return self
  2362	   346	
  2363	   347	    @property
  2364	   348	    def by_label(self) -> dict[str, JobSpec]:
  2365	   349	        return {j.label: j for j in self.jobs}
  2366	   350	
  2367	   351	    def readers_of(self, path: str) -> list[JobSpec]:
  2368	   352	        """Every RESIDENT that re-reads `path` at runtime — the jobs a
  2369	   353	        change to that file must restart, in one action with the change.
  2370	   354	
  2371	   355	        Normalised through `Path` so `./configs/cobalt/x.yaml` and
  2372	   175	
  2373	   176	  - label: com.cobalt.cards-expire
  2374	   177	    kind: one-shot
  2375	   178	    supervisor: self
  2376	   179	    timeout_s: 300
  2377	   180	    schedule: {at: "16:05", weekdays: [1, 2, 3, 4, 5]}
  2378	   181	    what: "expire cards whose window closed (uv run cobalt cards expire)"
  2379	   182	
  2380	   183	  - label: com.cobalt.daymode-propose
  2381	   184	    kind: one-shot
  2382	   185	    supervisor: self
  2383	   186	    timeout_s: 300
  2384	   187	    schedule: {at: "09:00", weekdays: [1, 2, 3, 4, 5]}
  2385	   188	    what: "the 09:00 day-mode proposal (uv run cobalt daymode propose)"
  2386	   189	
  2387	   190	  - label: com.cobalt.backup
  2388	   191	    kind: one-shot
  2389	   192	    supervisor: self
  2390	   193	    # An hour. The first real snapshot took minutes, but the number that
  2391	   194	    # matters is the one a FULL re-read takes on a bad night — restic
  2392	   195	    # rescans every source file when its cache is cold, and the dump
  2393	   196	    # alone is 360 MB.
  2394	   197	    timeout_s: 3600
  2395	   198	    # EVERY day including weekends, and after the archiver's 20:30 (which
  2396	   199	    # takes ~23 min) so the snapshot contains that night's bars rather
  2397	   200	    # than racing them. A vault edit on a Saturday is exactly as
  2398	   201	    # unrecoverable as one on a Tuesday.
  2399	   202	    schedule: {at: "21:40", weekdays: [0, 1, 2, 3, 4, 5, 6]}
  2400	   203	    what: "the nightly restic snapshot — vault + a fresh cobalt_brain dump, to the SSD"
  2401	   204	
  2402	   205	  - label: com.cobalt.heartbeat
  2403	   206	    kind: one-shot
  2404	   207	    supervisor: self
  2405	   208	    timeout_s: 300
  2406	   209	    # EVERY interval, all week. The heartbeat is the thing that notices a
  2407	   210	    # weekend failure before Monday morning needs it.
  2408	   211	    schedule: {every_min_tunable: heartbeat.interval_min}
  2409	   212	    what: "the F18 heartbeat host — probes everything above and says so out loud"
  2410	   213	
  2411	   214	  - label: com.cobalt.seat-usage
  2412	   215	    kind: one-shot
  2413	   216	    supervisor: self
  2414	   217	    timeout_s: 300
  2415	   218	    # An INTERVAL inside a WINDOW, both from tunables rows (F16). launchd
  2416	   219	    # has no such shape natively, so the plist carries the window expanded
  2417	   220	    # into one StartCalendarInterval entry per firing and the suite
  2418	   221	    # compares the two — see Schedule.calendar_entries().
  2419	   222	    schedule:
  2420	   223	      every_min_tunable: seat_usage.interval_min
  2421	   224	      window_tunable: seat_usage.window
  2422	   225	      weekdays: [0, 1, 2, 3, 4, 5, 6]
  2423	   226	    what: "the hourly seat-usage report (uv run cobalt seat-usage run) — what the seats cost today"
  2424	   227	
  2425	   228	  - label: com.cobalt.generated
  2426	   229	    kind: one-shot
  2427	   230	    supervisor: self
  2428	   231	    timeout_s: 300
  2429	   232	    # 23:37 ET, EVERY DAY. After the last seat-usage run (23:00) and well
  2430	   233	    # after the archiver's 20:30 + the backup's 21:40, so the day's
  2431	   234	    # rewrites are all on disk before this looks. Not on the hour, and
  2432	   235	    # not on a round five: a scheduled `git add` should not share its
  2433	   236	    # minute with anything, and an odd minute is the cheapest way to say
  2434	   237	    # so. Weekends included — the seat-usage report is rewritten on a
  2435	   238	    # Saturday exactly as it is on a Tuesday.
  2436	   239	    schedule: {at: "23:37", weekdays: [0, 1, 2, 3, 4, 5, 6]}
  2437	   240	    what: >
  2438	     1	# ops/ — LaunchAgents & wrapper scripts
  2439	     2	
  2440	     3	Everything here is captured in git as the SOURCE for what's installed
  2441	     4	to `~/Library/LaunchAgents/` — that install directory itself is outside
  2442	     5	the repo and not tracked. When you add or change a plist, re-copy it
  2443	     6	(see "Install / reload" below); the copy in `~/Library/LaunchAgents/`
  2444	     7	does not auto-update from git.
  2445	     8	
  2446	     9	## Inventory
  2447	    10	
  2448	    11	**Nine plists below, all of them loaded, as of 2026-09-09**
  2449	    12	(`launchctl list | grep com.cobalt`). `com.cobalt.herdr` was the one
  2450	    13	exception until the handover on 2026-09-08 at 19:21 ET; it is live now —
  2451	    14	see "herdr under launchd (0.9.0)" further down. `com.cobalt.generated`
  2452	    15	is new on 2026-09-09.
  2453	    16	
  2454	    17	This table is not the whole of `ops/`, and never was: `com.cobalt.backup`,
  2455	    18	`cards-expire`, `daymode-propose`, `heartbeat` and `obsidian` have
  2456	    19	plists and rows without a row here. **`configs/cobalt/jobs.yaml` is the
  2457	    20	authoritative list** — fourteen labels, cross-checked against `ops/`
  2458	    21	by `uv run cobalt validate` on every run of the gate. Read this table as
  2459	    22	prose about the ones with a story attached, not as an inventory.
  2460	    23	
  2461	    24	| Plist | Runs | Schedule | Wrapper | Installed |
  2462	    25	|---|---|---|---|---|
  2463	    26	| `com.cobalt.agent.plist` | `cobalt.sh start` (the Mattermost chief-of-staff agent) | RunAtLoad only, no KeepAlive | — | yes |
  2464	    27	| `com.cobalt.mainframe.plist` | `ops/start_mainframe.sh` (local LLM — the L23 local lane) | RunAtLoad only | `ops/start_mainframe.sh` | yes |
  2465	    28	| `com.cobalt.archiver.plist` | `/Users/cobalt/.local/bin/uv run archiver` (nightly bar archiver) | Mon-Fri 20:30 ET | — | yes (2026-09-03 — was not loaded before this) |
  2466	    29	| `com.cobalt.prefill-daily.plist` | `/Users/cobalt/.local/bin/uv run prefill daily` | Mon-Fri 05:15 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
  2467	    30	| `com.cobalt.prefill-drc.plist` | `/Users/cobalt/.local/bin/uv run prefill drc` | Mon-Fri 15:40 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
  2468	    31	| `com.cobalt.aset.plist` | `ops/start_aset.sh` → `uv run python -m cobalt.aset` (ASET sizing widget, :5010) | RunAtLoad + KeepAlive (persistent) | `ops/start_aset.sh` | yes |
  2469	    32	| `com.cobalt.herdr.plist` | `/opt/homebrew/bin/herdr server` (the terminal workspace every agent seat lives in) | RunAtLoad + KeepAlive on crash only | — | **yes (2026-09-08 19:21 — the handover)** |
  2470	    33	| `com.cobalt.generated.plist` | `/Users/cobalt/.local/bin/uv run cobalt generated commit` (commits the files a job rewrote today) | daily 23:37 ET | F17 wrapper | new 2026-09-09 |
  2471	    34	| `com.cobalt.seat-usage.plist` | `/Users/cobalt/.local/bin/uv run cobalt seat-usage run` (the hourly seat-usage report) | hourly 06:00-23:00 ET, every day | F17 wrapper (`cobalt seat-usage run`) | yes (2026-09-08) |
  2472	    35	
  2473	    36	The table above says which plists are *supposed* to be loaded.
  2474	    37	`configs/cobalt/jobs.yaml` is the machine-readable version of the same
  2475	    38	claim, and `uv run cobalt validate` compares the two: it fails on a job
  2476	    39	in one and not the other, and prints a `NOT LOADED BY DESIGN` line for
  2477	    40	every row carrying `enabled: false`.
  2478	    41	
  2479	    42	## com.cobalt.aset — persistence fix (2026-08-31)
  2480	    43	
  2481	    44	**Incident:** the ASET widget had no LaunchAgent at all — it was only
  2482	    45	ever started by hand (`uv run python -m cobalt.aset`, bare `nohup`, no
  2483	    46	supervision) and died silently at the Aug 29 10:35 reboot. Nobody
  2484	    47	noticed until the trading PC got connection-refused on `:5010`. It was
  2485	    48	restarted by hand at least twice since (2026-08-31 sessions) with no
  2486	    49	persistence fix until now.
  2487	    50	
  2488	    51	**Fix:** `com.cobalt.aset.plist` + `ops/start_aset.sh`.
  2489	    52	- `RunAtLoad: true` — starts on login/boot.
  2490	    53	- `KeepAlive: true` — unconditional restart on any exit (crash, kill,
  2491	    54	  even a clean 0 exit) — this is meant to be a persistent widget, not a
  2492	    55	  scheduled batch job like the archiver/prefill jobs above.
  2493	    56	- **Secret-free plist:** `COBALT_MASTER_KEY` is sourced inside
  2494	    57	  `ops/start_aset.sh` from `~/.cobalt_key` (the same key file
  2495	    58	  `cobalt.sh start` uses) — never written into the plist's
  2496	    59	  `EnvironmentVariables`. Without it, the sheet's pages still serve,
  2497	    60	  but `/api/prefill` (Finviz last-price fetch) fails every call because
  2498	    61	  VaultManager can't unlock.
  2499	    62	- **Logs with rotation:** `logs/aset.log` / `logs/aset.err`
  2500	    63	  (gitignored). Rotation is **best-effort, on-restart only**: launchd
  2501	    64	  binds stdout/stderr to those paths once at process spawn with no
  2502	    65	  SIGHUP/reopen support, and per this session's scope `ops/start_aset.sh`
  2503	    66	  does not touch `src/cobalt/aset`'s own Python — so true live rotation
  2504	    67	  would need either app-level logging changes (out of scope here) or a
  2505	    68	  root-owned `newsyslog.d` entry (not installed — avoided sudo). The
  2506	    69	  wrapper instead rotates each log to a timestamped `.YYYYMMDDHHMMSS`
  2507	    70	  suffix on every (re)start if it's grown past 5MB, keeping the 5 most
  2508	    71	  recent rotated files. For a KeepAlive service that's expected to stay
  2509	    72	  up for days/weeks at a stretch, this bounds worst-case growth but
  2510	    73	  does not guarantee any particular rotation cadence — if `aset.log`
  2511	    74	  grows unbounded between restarts, check it by hand.
  2512	    75	
  2513	    76	## NN#16 dev/prod vault split (2026-08-31)
  2514	    77	
  2515	    78	`configs/dev/vault.yaml`'s committed default no longer points at the
  2516	    79	real vault — it now points at `~/dev-vault-cobalt` (a skeleton copy:
  2517	    80	templates + Rules.md, no personal notes — see `docs/40 - DevDocs/cobalt/
  2518	    81	vault.md`). Every PRODUCTION consumer of `cobalt.vault.resolve_vault_path()`
  2519	    82	must therefore set `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`
  2520	    83	explicitly in its own environment, or it silently starts writing into
  2521	    84	the dev vault instead. All three plists that touch the vault do this:
  2522	    85	`com.cobalt.aset.plist` (via `ops/start_aset.sh`, so the plist itself
  2523	    86	stays free of it too) and both `com.cobalt.prefill-*.plist` (directly
  2524	    87	in `EnvironmentVariables`, since they have no wrapper script).
  2525	    88	
  2526	    89	**Action required (not done by this change):** `com.cobalt.aset` is
  2527	    90	already installed and running — its CURRENT process started before
  2528	    91	this fix and does not have `COBALT_VAULT_PATH` set. It needs
  2529	    92	`launchctl kickstart -k gui/$(id -u)/com.cobalt.aset` to pick it up;
  2530	    93	until then any card it saves would resolve the vault via the new dev
  2531	    94	default and land in `~/dev-vault-cobalt`, not the real vault. Not run
  2532	    95	automatically here — restarting a live production process during
  2533	    96	market hours needs a human go-ahead, not an agent's own judgment call.
  2534	    97	The two prefill plists are still not installed at all, so they carry
  2535	    98	no such risk yet.
  2536	    99	
  2537	   100	## uv path in ProgramArguments — FIXED 2026-09-03 (was the 09-03 prefill-silence root cause)
  2538	   101	
  2539	   102	**Rule: every `ops/*.plist` that invokes a binary directly in
  2540	   103	`ProgramArguments` (not through a wrapper script's own shebang) must use
  2541	   104	an ABSOLUTE path to that binary.** `uv` on this machine is a standalone
  2542	   105	install at `~/.local/bin/uv` (confirmed: `which uv` →
  2543	   106	`/Users/cobalt/.local/bin/uv`; `/opt/homebrew/bin/uv` → no such file;
  2544	   107	`brew list uv` → no such keg).
  2545	   108	
  2546	   109	Two different-looking bugs, same rule, found/fixed together:
  2547	   110	- `com.cobalt.archiver.plist` hardcoded the WRONG absolute path
  2548	   111	  (`/opt/homebrew/bin/uv`, doesn't exist here) — and was also simply not
  2549	   112	  loaded at all (`launchctl print` found no service). Its job had
  2550	   113	  therefore never run since 08-27 (`docs/30 - Design/archiver-runs.md`
  2551	   114	  has no nightly rows 08-28 onward) despite the Ledger's 08-29/31 claim
  2552	   115	  it was "verified running unattended" — that check evidently only
  2553	   116	  confirmed the plist file existed/looked right, not that launchd had
  2554	   117	  it loaded.
  2555	   118	- `com.cobalt.prefill-daily.plist` / `com.cobalt.prefill-drc.plist` used
  2556	   119	  a BARE `uv` (the 08-31 fix for the above bug, modeled on
  2557	   120	  `ops/start_aset.sh`'s pattern — see BACKLOG.md's 08-31 slice-2 entry).
  2558	   121	  This looked right but is itself wrong for a plist with no wrapper
  2559	   122	  script: `start_aset.sh`'s bare `uv` works because bash's own shebang
  2560	   123	  does a real PATH search before `exec`ing it; a bare name directly in
  2561	   124	  `ProgramArguments[0]` has no shell in front of it, and launchd's
  2562	   125	  posix_spawn does not reliably search the job's own
  2563	   126	  `EnvironmentVariables.PATH` the way a shell does. Confirmed by an
  2564	   127	  isolated diagnostic LaunchAgent: bare `uv` → `last exit code = 78:
  2565	   128	  EX_CONFIG`, empty stdout+stderr; absolute path → exit 0. This is
  2566	   129	  exactly what happened when `com.cobalt.prefill-daily` fired for real
  2567	   130	  at 05:15 on 09-03 (and `com.cobalt.prefill-drc` the evening before) —
  2568	   131	  loaded, fired, failed instantly, zero output, no alert. Full
  2569	   132	  root-cause writeup: `docs/00 - Project/BACKLOG.md`'s INCIDENT LOG,
  2570	   133	  2026-09-03 entry.
  2571	   134	
  2572	   135	**Fix (this session):** all three now use the absolute
  2573	   136	`/Users/cobalt/.local/bin/uv` in `ProgramArguments`; all three
  2574	   137	installed/reloaded and confirmed exit 0 on a manual `kickstart`.
  2575	   138	`com.cobalt.mainframe.plist` does not actually invoke `uv` at all (its
  2576	   139	`ProgramArguments` is `/Users/cobalt/cobalt/ops/start_mainframe.sh`,
  2577	   140	which uses `lms` — the earlier note above conflated it with the archiver
  2578	   141	bug; left uninvestigated further since it isn't broken).
  2579	   142	
  2580	   143	*(Path corrected 2026-09-09: this paragraph and the Inventory row both
  2581	   144	said `~/.lmstudio/start_mainframe.sh`. The wrapper is in the repo, where
  2582	   145	it is reviewed in a diff; `~/.lmstudio/` is where the 09-04 note put it
  2583	   146	and the plist never agreed.)*
  2584	   147	
  2585	   148	## Install / reload
  2586	   149	
  2587	   150	```sh
  2588	   151	# first install
  2589	   152	cp ops/com.cobalt.<name>.plist ~/Library/LaunchAgents/
  2590	   153	launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.<name>.plist
  2591	   154	
  2592	   155	# after editing the plist or its wrapper script
  2593	   156	cp ops/com.cobalt.<name>.plist ~/Library/LaunchAgents/   # only if the plist itself changed
  2594	   157	launchctl kickstart -k gui/$(id -u)/com.cobalt.<name>
  2595	   158	
  2596	   159	# status / logs
  2597	   160	launchctl list | grep com.cobalt.<name>
  2598	   161	tail -f logs/<name>.log logs/<name>.err
  2599	   162	
  2600	   163	# stop + unload
  2601	   164	launchctl bootout gui/$(id -u)/com.cobalt.<name>
  2602	   165	```
  2603	   166	
  2604	   167	## Deploy checklist
  2605	   168	
  2606	   169	**THE LAW, ruled three times — 2026-09-04, 2026-09-08 (`aset.yaml`) and
  2607	   170	2026-09-09 (`tunables.yaml`): a config-shape change and the restart of
  2608	   171	EVERY resident that reads that file are ONE ACTION.** Not two steps, not
  2609	   172	a follow-up. A deploy plan that changes a config and does not name the
  2610	   173	processes it restarts is an incomplete plan.
  2611	   174	
  2612	   175	**Every deploy plan carries a `RESTARTS:` line, and it is produced by a
  2613	   176	command, not by memory:**
  2614	   177	
  2615	   178	```sh
  2616	   179	# for every config file the merge touches
  2617	   180	uv run cobalt jobs readers configs/cobalt/taxonomy/tunables.yaml
  2618	   181	#   -> RESTARTS: com.cobalt.aset
  2619	   182	
  2620	   183	launchctl kickstart -k gui/$(id -u)/com.cobalt.aset
  2621	   184	```
  2622	   185	
  2623	   186	`cobalt jobs readers` reads `reads:` in `configs/cobalt/jobs.yaml` —
  2624	   187	per-resident, derived from the code, one row per config file the process
  2625	   188	re-reads at runtime. **An unknown path exits 1**, deliberately: "no
  2626	   189	resident re-reads this" and "nobody has worked out who reads this" are
  2627	   190	different answers, and only one of them makes it safe to deploy without
  2628	   191	a restart. `uv run cobalt validate` prints the whole map and fails if a
  2629	   192	listed path has gone missing.
  2630	   193	
  2631	   194	### Why this is a law and not a habit
  2632	   195	
  2633	   196	On 2026-09-08 at ~19:00 the seat-usage deploy added a
  2634	   197	`TunableUnit.WINDOW` row to `configs/cobalt/taxonomy/tunables.yaml`. Its
  2635	   198	plan said *"nothing else is loaded or restarted"* — true of its own job,
  2636	   199	and wrong about the sheet. `com.cobalt.aset` had been running since
  2637	   200	17:50 and **re-reads `tunables.yaml` on every request**, so it read the
  2638	   201	new row through code that predated the enum value and raised
  2639	   202	`TaxonomyConfigError` on every render. From then until the kickstart at
  2640	   203	**07:06 on 09-09** — about thirteen hours, including the premarket — the
  2641	   204	page he trades beside served HTTP 200 with
  2642	   205	
  2643	   206	> ⚠ DAY MODE UNRESOLVED — cards are refused until this is fixed
  2644	   207	
  2645	   208	and every card write was refused. `sheet_http` was green throughout and
  2646	   209	was telling the truth: the server was up.
  2647	   210	
  2648	   211	Two things came out of it, and both are in place now: this checklist,
  2649	   212	and the `sheet daymode` probe (F18) that reads the banner instead of the
  2650	   213	status line, so the same failure is red within one heartbeat interval
  2651	   214	rather than at whatever hour somebody happens to look.
  2652	   215	
  2653	   216	### The order
  2654	   217	
  2655	   218	1. `uv run cobalt validate` — the config gate, on the branch, before merging.
  2656	   219	2. In the worktree, `git rebase main` first — after the nightly generated commit
  2657	   220	   (`com.cobalt.generated`, 23:37) every branch older than a day is behind `main`.
  2658	   221	   Then `git merge --ff-only <branch>` from `~/cobalt`. **Merge is deploy** (R4).
  2659	   222	   If the merge carries a NEW credential, its `.env` lines land BEFORE the merge:
  2660	   223	   between merge and `.env` a starting job fails loud (heartbeat, seat-usage).
  2661	   224	3. **Migrations**, if any, as their own step with their own rollback.
  2662	   225	4. **`RESTARTS:`** — kickstart every resident named by `cobalt jobs
  2663	   226	   readers` for every config file the merge touched.
  2664	   227	5. **Registry** — `uv run cobalt jobs register` if `jobs.yaml` changed;
  2665	   228	   `cp` + `launchctl bootstrap` for a new plist.
  2666	   229	6. **Force a beat** and read it:
  2667	   230	   `launchctl kickstart -k gui/$(id -u)/com.cobalt.heartbeat`.
  2668	   231	7. Deploys go **outside market hours** (NN#16) and outside 20:00-21:30 ET
  2669	   232	   (F1's market-reset window).
  2670	   233	8. **Vault delivery snapshots:** a report written on an unmerged branch is copied
  2671	   234	   to `docs/_inflight/` (git-ignored, visible in Obsidian at
  2672	   235	   `0 - Projects/Cobalt/_inflight/`) so Dejan can read it before the merge; delete
  2673	   236	   the copy when the report lands in `40 - DevDocs/reports/` at merge.
  2674	   237	
  2675	   238	## herdr under launchd (0.9.0)
  2676	   239	
  2677	   240	**STATUS: LIVE since 2026-09-08 19:21 ET.** `com.cobalt.herdr` is
  2678	   241	bootstrapped, `configs/cobalt/jobs.yaml` carries `enabled: true`, and the
  2679	   242	F18 `herdr` probe is a real probe. On 2026-09-09 the server is **pid
  2680	   243	72998, run 3, herdr 0.9.0**, on the Mac and on Fedora.
  2681	   244	
  2682	   245	**launchd owns the server.** That is the whole change, and everything
  2683	   246	below follows from it.
  2684	   247	
  2685	   248	```sh
  2686	   249	launchctl list | grep com.cobalt.herdr            # the truth about who is running
  2687	   250	launchctl kickstart -k gui/$(id -u)/com.cobalt.herdr   # restart
  2688	   251	herdr server stop                                  # a DELIBERATE stop; nothing fights you
  2689	   252	```
  2690	   253	
  2691	   254	`KeepAlive` is `SuccessfulExit: false`, not `true`, and that is why
  2692	   255	`herdr server stop` works: a clean exit is a human decision and launchd
  2693	   256	leaves it alone. **A crash is the only case it restarts**, which is the
  2694	   257	only case worth restarting.
  2695	   258	
  2696	   259	### Attaching — the rules, not just the commands
  2697	   260	
  2698	   261	| From | Command | The rule |
  2699	   262	|---|---|---|
  2700	   263	| The Mac | `herdr` | Attaches to the persistent session. `herdr session attach default` names it explicitly. |
  2701	   264	| Fedora | `herdr --remote cobalt@cobalt` | **Only from a 0.9.0 client**, and **answer No to any replace prompt.** |
  2702	   265	| The phone | `ssh cobalt@cobalt` then `herdr` | **NEVER `--remote`.** There is no phone client; the phone is a terminal onto the Mac. |
  2703	   266	
  2704	   267	**WHY `--remote` HAS A RULE ATTACHED.** On the morning of 2026-09-09 the
  2705	   268	server was replaced twice — 06:03 and 07:26, both from Fedora, the second
  2706	   269	27 seconds after launchd had started it. A `herdr --remote` from a
  2707	   270	**0.8.2** client replaces the running server. 0.8.2 does prompt, and
  2708	   271	Dejan answered Yes without reading it, so this was partly procedure and
  2709	   272	not only version — which is why the rule is written as a rule and not as
  2710	   273	"upgrade and forget".
  2711	   274	
  2712	   275	**The fix was forward, not back.** Mac and Fedora went 0.8.2 → 0.9.0
  2713	   276	("client updates leave compatible servers untouched … replacing a remote
  2714	   277	server asks, default **No**"), and the server was restarted under launchd
  2715	   278	**from the Mac keyboard in Terminal.app — not from a herdr pane** — at
  2716	   279	08:17. Result: pid 72998, `endpoint_compatible yes`, heartbeat GREEN at
  2717	   280	08:19:57 (13 jobs / 11 probes).
  2718	   281	
  2719	   282	**The phone is still 0.8.2 and must not `--remote`.** `ssh` then `herdr`
  2720	   283	costs nothing and cannot replace anything.
  2721	   284	
  2722	   285	### Acceptance, 2026-09-09
  2723	   286	
  2724	   287	Dejan attached from Fedora over `--remote` on 0.9.0. **The client
  2725	   288	prompted before replacing; he answered No; `launchctl list | grep
  2726	   289	com.cobalt.herdr` still showed pid 72998 after four attaches.** The
  2727	   290	version fix and the procedure both hold. Recorded as PASSED.
  2728	   291	
  2729	   292	### What a restart brings back, and what it does not
  2730	   293	
  2731	   294	0.9.0's native agent restore is better than 0.8.2's, measured on the
  2732	   295	08:17 restart:
  2733	   296	
  2734	   297	* **Restored** — the session, workspace, tabs, panes and working
  2735	   298	  directories, **and** `claude`, `grok` and `qwen` were relaunched in
  2736	   299	  their panes with their sessions. The Claude1 conversation continued
  2737	   300	  without `claude --resume`.
  2738	   301	* **Not restored** — panes that were **empty shells**. Codex1 and
  2739	   302	  Gemini1 held no agent before the restart, so there was nothing for
  2740	   303	  restore to name; they were relaunched by hand.
  2741	   304	* **The standing rule is unchanged, and 0.9.0 does not soften it: never
  2742	   305	  rely on restore.** State goes to the vault or to Postgres **before** a
  2743	   306	  `/clear`, a restart or an update. An agent that reports a session
  2744	   307	  reference can be brought back; a conversation nobody wrote down cannot.
  2745	   308	
  2746	   309	### Integration updates append hooks — the probe watches for it
  2747	   310	
  2748	   311	`herdr integration install claude` rewrites Claude Code's hook config,
  2749	   312	and on **2026-09-09 at 08:33** the v8 → v9 update did **not** replace the
  2750	   313	guard pointer — it **APPENDED A SECOND `SessionStart` ENTRY** aimed at
  2751	   314	herdr's own script, so both would have fired. The duplicate was removed
  2752	   315	by hand and `~/.claude/settings.json` restored byte-identical to the
  2753	   316	pre-install backup (`~/.claude/settings.json.pre-herdr-v9`).
  2754	   317	
  2755	   318	This matters to this job, not just to the seats: v9 still hardcodes the
  2756	   319	agent name `herdr:claude` with **no harness detection**, so without
  2757	   320	`~/.claude/hooks/herdr-harness-guard.sh` every Grok session reports
  2758	   321	itself as `claude` in `herdr agent list` — **and that is the list the F18
  2759	   322	`herdr` probe asserts on**.
  2760	   323	
  2761	   324	Since 2026-09-09 **the probe checks the pointer as its third question**:
  2762	   325	`hooks.SessionStart` must be **exactly one entry with exactly one command
  2763	   326	hook** running the guard, and the guard must exist and be executable.
  2764	   327	Anything else is red, naming the drift. Counting is the check because a
  2765	   328	presence check would have called the 08:33 state fine.
  2766	   329	
  2767	   330	After any `brew upgrade herdr` or `herdr integration install`, force a
  2768	   331	beat rather than eyeballing the file:
  2769	   332	
  2770	   333	```sh
  2771	   334	launchctl kickstart -k gui/$(id -u)/com.cobalt.heartbeat
  2772	   335	tail -40 logs/heartbeat.log | grep herdr
  2773	   336	```
  2774	   337	
  2775	   338	### Where things live
  2776	   339	
  2777	   340	The socket is `/Users/cobalt/.config/herdr/herdr.sock` and the config
  2778	   341	`/Users/cobalt/.config/herdr/config.toml` — `herdr server reload-config`
  2779	   342	re-reads it without a restart, which is preferable to a restart for a
  2780	   343	config change. Server logs sit in the same directory
  2781	   344	(`herdr-server.log`); the launchd job's own stdout/stderr go to
  2782	   345	`ops/logs/herdr.log` and `ops/logs/herdr.err`.
  2783	   346	
  2784	   347	Nothing in `configs/` reaches this process, which is why its registry row
  2785	   348	carries `reads: []` — no deploy of ours can require restarting it.
  2786	   349	
  2787	   350	### Rolling it back
  2788	   351	
  2789	   352	Rolling back means **handing the server back to a manual start**, which
  2790	   353	is a downgrade from where it is now — do it only if launchd supervision
  2791	   354	is itself the problem.
  2792	   355	
  2793	   356	```sh
  2794	   357	launchctl bootout gui/$(id -u)/com.cobalt.herdr    # this STOPS the server; every pane goes
  2795	   358	# set `enabled: false` on com.cobalt.herdr in configs/cobalt/jobs.yaml, then:
  2796	   359	uv run cobalt jobs register                        # the probe goes quiet and says why
  2797	   360	/opt/homebrew/bin/herdr server &                   # back to the manual start
  2798	   361	```
  2799	   362	
  2800	   363	The order matters: `bootout` takes the terminal workspace down with it,
  2801	   364	so **run it from Terminal.app, not from a herdr pane** — the same reason
  2802	   365	the original handover had to happen at the keyboard. Land everything
  2803	   366	first; assume every conversation is lost.
  2804	   367	
  2805	   368	## Email OAuth token clock (F18 / S1-P4)
  2806	   369	
  2807	   370	The Google project behind `gmail.send` is still in **Testing** status, so a refresh token
  2808	   371	expires **7 days after consent**. Dejan retries **Publish** (from another browser); if it
  2809	   372	fails again, a fresh `uv run cobalt notify email-auth` consent resets the 7-day clock —
  2810	   373	repeat every **≤6 days** until Publish lands. After each consent: send a test alert and read
  2811	   374	the token date back (`cobalt notify` status / the heartbeat `email` probe line) — proof, not
  2812	   375	assumption. Ruled 09-09 (chat second opinion, item 10).
  2813	     1	# Heartbeat blackout — 2026-09-08 & 09-09, 20:00–21:00 ET
  2814	     2	
  2815	     3	*Read-only diagnosis. No fix applied, nothing committed. Hub: Opus 5. Worker: Codex `gpt-5.6-terra`, `-s read-only`.*
  2816	     4	
  2817	     5	## §0 Headline
  2818	     6	
  2819	     7	Both blackouts are **one cause, fully in the log**: every "missing" beat ran, and
  2820	     8	died at the F1 `market_reset` gate on its own daily-note write. `write_note_block()`
  2821	     9	is called unguarded at `runner.py:249`, and the heartbeat's own DB row is not stamped
  2822	    10	until `runner.py:291-292` — so the refusal kills the beat before it records itself,
  2823	    11	alerts, or DMs. **H1 SUPPORTED · H2 REFUTED · H3 REFUTED.** ESCALATE: 4.
  2824	    12	
  2825	    13	## The two windows, side by side
  2826	    14	
  2827	    15	| | 2026-09-08 | 2026-09-09 |
  2828	    16	|---|---|---|
  2829	    17	| Last beat before gap | 19:52:20 ET (`vault_writes` id 2103) | 19:59:01 ET (id 2216) |
  2830	    18	| Beats attempted in gap | 20:07:23, 20:22:26, 20:37:28, 20:52:31 | 20:14:04, 20:29:07, 20:44:10, 20:59:13 |
  2831	    19	| Each attempt's outcome | `SessionBlocked` → process exit non-zero | `SessionBlocked` → process exit non-zero |
  2832	    20	| First beat back | 21:07:31 ET, **RED — 1 job(s)** (id 2106) | 21:14:16 ET, **RED — 1 job(s)** (id 2219) |
  2833	    21	| Gap length | 75 min 13 s | 75 min 15 s |
  2834	    22	| Archiver 20:30 run | 20:30:05 → 20:53:26, 3,166,696 rows, exit 0, 23m20s | 20:30:05 → 20:53:25, 3,167,272 rows, exit 0, 23m19s |
  2835	    23	
  2836	    24	The gap is not approximately the block window — it **is** the block window, snapped to
  2837	    25	the 15-min phase: every scheduled tick whose clock fell inside 20:00–21:00 ET died,
  2838	    26	and the phase is unbroken across the gap (19:52→21:07, 19:59→21:14). launchd never
  2839	    27	missed a beat; the beat missed itself.
  2840	    28	
  2841	    29	## Verdicts
  2842	    30	
  2843	    31	| H | Verdict | Evidence |
  2844	    32	|---|---|---|
  2845	    33	| **H1** write-block collision | **SUPPORTED** | `system.session_blocks` ids 1–8, actor `vaultwrite:heartbeat:upsert_unit`, one row per missing tick, target = that day's daily note. Each is paired in `logs/heartbeat.err` with `FAILED: SessionBlocked: …` — the CLI's top-level fail-loud exit. 8 rows, 8 `FAILED` lines, whole-file totals, no other cause anywhere. |
  2846	    34	| **H2** job never launched | **REFUTED** | The job launched at all four ticks each night — the refusal rows carry its own wall clock (20:07:23, 20:22:26, …). `launchctl print gui/501/com.cobalt.heartbeat`: `run interval = 900 seconds`, `runs = 518`, `last exit code = 0`, no throttle field, `runatload`. `pmset -g log` shows `caffeinate PreventUserIdleSystemSleep` held through both windows and no sleep/wake transition. |
  2847	    35	| **H3** launched, hung or killed | **REFUTED** | Every attempt died **fast** and by name: `SessionBlocked`, ~3 s after launch, after all 12 probes had already run. The archiver completed cleanly both nights (exit 0, 0 failures, 23m). No hang, no SIGKILL, no timeout. |
  2848	    36	
  2849	    37	## The code path (item 1.6)
  2850	    38	
  2851	    39	`src/cobalt/heartbeat/runner.py:243-292` — the order is the defect:
  2852	    40	
  2853	    41	```python
  2854	    42	243  def run_beat(*, now=None, dry_run=False, probe=True) -> Beat:
  2855	    43	247      beat = take_beat(now=now, probe=probe)      # all 12 probes + job sweep — succeeded every time
  2856	    44	249      write = write_note_block(beat, dry_run=dry_run)   # ← raises here, unguarded
  2857	    45	250      if write is None:                                  # only handles "note does not exist"
  2858	    46	...
  2859	    47	291      store.mark_running(JOB_LABEL,  now=...)     # ← never reached
  2860	    48	292      store.mark_finished(JOB_LABEL, exit_code=0, result=result, now=...)
  2861	    49	```
  2862	    50	
  2863	    51	`write_note_block` → `runner.py:147` `writer.upsert_unit(...)` → `vaultwrite/writer.py:664`
  2864	    52	`self._session_gate("upsert_unit", path)` → `writer.py:411` `assert_writable(...)` →
  2865	    53	`session/guard.py:150` **raises `SessionBlocked`** (a `RuntimeError`; the ERROR line is `guard.py:146`).
  2866	    54	
  2867	    55	Nothing catches it. `write_note_block` guards only "the note does not exist"
  2868	    56	(`runner.py:136-142`); `cmd_beat` (`heartbeat/cli.py:27`) has no handler either. The
  2869	    57	exception unwinds to the CLI's fail-loud top level, which prints `FAILED: SessionBlocked: …`
  2870	    58	to stderr and exits non-zero.
  2871	    59	
  2872	    60	Consequences of dying at :249, all four of them:
  2873	    61	1. **No DB row** — `system.cobalt_jobs` is a single upsert row per label, so the heartbeat's
  2874	    62	   row simply stays at 19:52 and goes stale. There is no beat history to lose; there is no
  2875	    63	   beat history at all.
  2876	    64	2. **No alert** — `out_of_band()` (email) and `send_dm()` are at `runner.py:269-270`, after
  2877	    65	   the write. A beat that has something to say is silenced by the fact that it cannot write
  2878	    66	   the note.
  2879	    67	3. **No F17 wrapper to catch it** — the plist runs `uv run cobalt heartbeat beat` directly.
  2880	    68	   Unlike the archiver (`jobs.wrapper` logs `F17: … RUNNING` / `DONE`), the heartbeat
  2881	    69	   self-records inside `run_beat`, so a crash before :291 leaves no `failed` row — just silence.
  2882	    70	4. **Nothing degrades** — probes, sweep, and rendered beat were all in hand at :249 and were
  2883	    71	   thrown away with the exception.
  2884	    72	
  2885	    73	## Why it self-detects, and why that took 75 minutes
  2886	    74	
  2887	    75	The 21:07 / 21:14 beat is the first one whose clock is outside the block. Its own watchdog
  2888	    76	sweep reads its own stale `cobalt_jobs` row and reports:
  2889	    77	
  2890	    78	```
  2891	    79	RED  com.cobalt.heartbeat  done (MISSED) every 15 min; last finish 2026-09-08 19:52 ET,
  2892	    80	     measured from 2026-09-08 19:52 ET — more than two intervals (30 min) ago.
  2893	    81	```
  2894	    82	
  2895	    83	Correct, and it names the symptom without the cause. The cause was in `heartbeat.err` the
  2896	    84	whole time — Dejan's "not in the log" is `heartbeat.log` (stdout, the rendered beat), which
  2897	    85	by construction contains only beats that survived to be rendered.
  2898	    86	
  2899	    87	## The probe that watched it happen and called it green
  2900	    88	
  2901	    89	`probes.py:320-348` `vaultwrite_blocks` reported, in the very RED beat that noticed the gap:
  2902	    90	
  2903	    91	```
  2904	    92	OK   vault blocks   4 refused, 0 ungated repair run(s) in the counter window
  2905	    93	```
  2906	    94	
  2907	    95	Four refusals — the exact four dead beats — rated **OK by design**: *"NOT RED ON ITS OWN. A
  2908	    96	refusal is the guard WORKING"* (`probes.py:321-324`). True of every other actor; false when
  2909	    97	the refused writer is the heartbeat itself. `system.session_blocks` has **8 rows total,
  2910	    98	all 8 `vaultwrite:heartbeat:upsert_unit`** — to date, the only thing F1 has ever turned away
  2911	    99	is the heartbeat.
  2912	   100	
  2913	   101	## The control case: 2026-09-07 proves causation
  2914	   102	
  2915	   103	| Date | Trading day? | Heartbeat writes inside 20:00–21:00 |
  2916	   104	|---|---|---|
  2917	   105	| 2026-09-07 | **No — Labor Day** (`configs/cobalt/calendar/nyse-2026.yaml:45`) | **4** (20:02, 20:17, 20:32, 20:47) — no gap |
  2918	   106	| 2026-09-08 | Yes | 0 |
  2919	   107	| 2026-09-09 | Yes | 0 |
  2920	   108	
  2921	   109	On a market holiday the whole day is `overnight` (`clock.py:196-198`), no `market_reset`
  2922	   110	window exists, the gate never fires, and the beats went through — same code, same archiver
  2923	   111	run at 20:30 (also exit 0, 23m21s), same machine. This also dates the defect: the gate landed
  2924	   112	2026-09-04 19:03 (`e2acd20`), and **09-08 was the first trading-day 20:00–21:00 window with
  2925	   113	both the gate and the heartbeat live**. It is not a regression from 09-08's deploy; it is the
  2926	   114	first night the two met. It will recur tonight and every trading night until fixed.
  2927	   115	
  2928	   116	## ESCALATE
  2929	   117	
  2930	   118	- **Fix class (not applied):** *persistence ordering + vault-write degradation.* The beat must
  2931	   119	  persist itself (DB row) and run its alert channels **before**, or independently of, the vault
  2932	   120	  write; the `market_reset` refusal of the heartbeat's own status unit must be a caught,
  2933	   121	  degraded, reported condition — not an exception that ends the beat. Whether the correct shape
  2934	   122	  is (a) reorder + `try/except SessionBlocked` around `write_note_block`, (b) a repo-owned-style
  2935	   123	  carve-out for the heartbeat's status unit, or (c) writing the block at 21:00 as a catch-up, is
  2936	   124	  a **trading-logic-adjacent design call** — F1's window is a Charter rule and any carve-out in it
  2937	   125	  needs its own ruling. Not decided here.
  2938	   126	- **`log show` unavailable.** Terra's Unified Log queries returned `log: Cannot run while sandboxed`;
  2939	   127	  launchd's own spawn/throttle/kill messages are unread. Moot for these verdicts — the refusal rows
  2940	   128	  timestamp the launches directly — but it means no independent launchd-side confirmation exists,
  2941	   129	  and this tool will be unavailable to the next sandboxed forensics run too.
  2942	   130	- **Per-run exit codes are not retained.** `heartbeat.err` carries no per-run exit code or duration,
  2943	   131	  and `launchctl` keeps only the most recent (`last exit code = 0`). Eight non-zero exits left no
  2944	   132	  durable trace outside the log text. The heartbeat is the one job with no F17 wrapper.
  2945	   133	- **Second failure mode, unrelated to the gap:** `vaultwrite_blocks` cannot distinguish "F1 turned
  2946	   134	  away someone else" from "F1 killed the watcher". As written it will stay green through every
  2947	   135	  future recurrence of this exact outage.
  2948	   136	- **Also observed, not investigated:** an off-phase beat at 2026-09-08 19:22:14, 62 s after the
  2949	   137	  19:21:12 beat. Out of scope here; flagging it rather than dropping it.
  2950	?? "docs/40 - DevDocs/reports/_inflight/"
  2951	?? "docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md"
  2952	
  2953	exec
  2954	/bin/zsh -lc "nl -ba src/cobalt/jobs/wrapper.py | sed -n '85,210p'; nl -ba src/cobalt/jobs/store.py | sed -n '20,205p'; nl -ba src/cobalt/jobs/cli.py | sed -n '130,155p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
  2955	 succeeded in 0ms:
  2956	    85	        )
  2957	    86	
  2958	    87	    def _loop(self) -> None:
  2959	    88	        while not self._stop.wait(self.every_s):
  2960	    89	            try:
  2961	    90	                self.store.beat(self.label)
  2962	    91	            except Exception as e:  # noqa: BLE001
  2963	    92	                # A missed stamp is not a reason to kill the job. It IS a
  2964	    93	                # reason to say so: the watchdog may conclude ZOMBIE from
  2965	    94	                # this, and an operator needs the other half of the story.
  2966	    95	                logger.error(
  2967	    96	                    "F17: heartbeat stamp FAILED for {} ({}: {}) — the job is still "
  2968	    97	                    "running; the watchdog may see a stale heartbeat.",
  2969	    98	                    self.label, type(e).__name__, e,
  2970	    99	                )
  2971	   100	
  2972	   101	    def __enter__(self) -> "_Beater":
  2973	   102	        self._thread.start()
  2974	   103	        return self
  2975	   104	
  2976	   105	    def __exit__(self, *exc) -> None:
  2977	   106	        self._stop.set()
  2978	   107	
  2979	   108	
  2980	   109	class JobRun:
  2981	   110	    """Handle a wrapped job can hang its result on."""
  2982	   111	
  2983	   112	    def __init__(self, spec: JobSpec):
  2984	   113	        self.spec = spec
  2985	   114	        self.label = spec.label
  2986	   115	        #: Whatever the run wants F18 to be able to report — the
  2987	   116	        #: archiver's `rows_written` is what makes "archiver freshness
  2988	   117	        #: (last run + rows written)" answerable.
  2989	   118	        self.result: Optional[dict[str, Any]] = None
  2990	   119	
  2991	   120	
  2992	   121	@contextmanager
  2993	   122	def job_run(
  2994	   123	    label: str,
  2995	   124	    *,
  2996	   125	    store: Optional[JobStore] = None,
  2997	   126	    register: bool = True,
  2998	   127	    allow_prod: bool = False,
  2999	   128	):
  3000	   129	    """Run a block as a registered job. See the module docstring."""
  3001	   130	    registry = load_job_registry()
  3002	   131	    spec = registry.spec(label)
  3003	   132	    store = store or JobStore()
  3004	   133	    store.ensure_schema(allow_prod=allow_prod)
  3005	   134	    if register:
  3006	   135	        store.register(spec, allow_prod=allow_prod)
  3007	   136	
  3008	   137	    if killswitch.is_active(store):
  3009	   138	        state = killswitch.read(store)
  3010	   139	        logger.error("F17: {} REFUSED TO START — {}", label, state.describe())
  3011	   140	        raise JobStopped(state.describe())
  3012	   141	
  3013	   142	    store.mark_running(label)
  3014	   143	    run = JobRun(spec)
  3015	   144	    every_s = spec.timeout_s / heartbeat_fraction()
  3016	   145	    logger.info(
  3017	   146	        "F17: {} RUNNING (timeout {}s, heartbeat every {:.0f}s)",
  3018	   147	        label, spec.timeout_s, every_s,
  3019	   148	    )
  3020	   149	    try:
  3021	   150	        with _Beater(store, label, every_s):
  3022	   151	            yield run
  3023	   152	    except BaseException as e:
  3024	   153	        store.mark_finished(
  3025	   154	            label,
  3026	   155	            exit_code=1,
  3027	   156	            error=f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=8)}",
  3028	   157	            result=run.result,
  3029	   158	        )
  3030	   159	        logger.error("F17: {} FAILED — {}: {}", label, type(e).__name__, e)
  3031	   160	        raise            # the wrapper reports; it never swallows
  3032	   161	    store.mark_finished(label, exit_code=0, result=run.result)
  3033	   162	    logger.info("F17: {} DONE", label)
  3034	   163	
  3035	   164	
  3036	   165	def should_keep_running(label: str, *, store: Optional[JobStore] = None) -> bool:
  3037	   166	    """A RESIDENT's own loop check. `False` means exit cleanly now.
  3038	   167	
  3039	   168	    Residents call this where they can stop without tearing out of a
  3040	   169	    write. Cobalt's residents today are supervised by launchd rather than
  3041	   170	    wrapped (see jobs.yaml), so this exists for the first new-core
  3042	   171	    resident — the S2 radar poller — and for anything the chief of staff
  3043	   172	    grows into.
  3044	   173	    """
  3045	   174	    if killswitch.is_active(store):
  3046	   175	        logger.error(
  3047	   176	            "F17: kill switch engaged — {} is exiting cleanly at its next safe point.",
  3048	   177	            label,
  3049	   178	        )
  3050	   179	        return False
  3051	   180	    return True
  3052	   181	
  3053	   182	
  3054	   183	__all__ = [
  3055	   184	    "HEARTBEAT_FRACTION_KEY",
  3056	   185	    "STOPPED_EXIT_CODE",
  3057	   186	    "JobRun",
  3058	   187	    "JobStopped",
  3059	   188	    "heartbeat_fraction",
  3060	   189	    "job_run",
  3061	   190	    "should_keep_running",
  3062	   191	]
  3063	    20	
  3064	    21	from __future__ import annotations
  3065	    22	
  3066	    23	import json
  3067	    24	from datetime import datetime, timedelta
  3068	    25	from pathlib import Path
  3069	    26	from typing import Any, Optional
  3070	    27	
  3071	    28	from cobalt import db, env
  3072	    29	from cobalt.db import Side
  3073	    30	from cobalt.session import clock as clock_mod
  3074	    31	
  3075	    32	from .config import JobSpec
  3076	    33	from .models import JobState, Supervisor
  3077	    34	
  3078	    35	MIGRATIONS_DIR = Path(__file__).parent / "migrations"
  3079	    36	
  3080	    37	
  3081	    38	class JobStoreError(RuntimeError):
  3082	    39	    """A job operation was refused."""
  3083	    40	
  3084	    41	
  3085	    42	class JobStore:
  3086	    43	    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
  3087	    44	    #: The scheduler's own bookkeeping: one row per launchd label, plus
  3088	    45	    #: the kill switch. Engine state, identical on every install.
  3089	    46	    SIDE = Side.SYSTEM
  3090	    47	
  3091	    48	    def __init__(self, db_name: Optional[str] = None):
  3092	    49	        self.db_name = db_name or env.resolve_db_name()
  3093	    50	
  3094	    51	    def _connect(self, *, allow_prod: bool = False):
  3095	    52	        return db.connect(self.db_name, side=self.SIDE, allow_prod=allow_prod)
  3096	    53	
  3097	    54	    def ensure_schema(self, *, allow_prod: bool = False) -> None:
  3098	    55	        with self._connect(allow_prod=allow_prod) as conn:
  3099	    56	            db.assert_schemas_exist(conn)
  3100	    57	            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
  3101	    58	                lines = migration.read_text().splitlines()
  3102	    59	                sql = "\n".join(l for l in lines if not l.strip().startswith("--"))
  3103	    60	                for statement in sql.split(";"):
  3104	    61	                    statement = statement.strip()
  3105	    62	                    if statement:
  3106	    63	                        conn.execute(statement)
  3107	    64	
  3108	    65	    # -- registration -------------------------------------------------
  3109	    66	
  3110	    67	    def register(self, spec: JobSpec, *, allow_prod: bool = False) -> None:
  3111	    68	        """Upsert one row from its config spec. IDEMPOTENT, and it does
  3112	    69	        NOT touch runtime columns: re-registering after a config edit
  3113	    70	        must never erase the last run's exit code, which is the one thing
  3114	    71	        an operator looks at first."""
  3115	    72	        with self._connect(allow_prod=allow_prod) as conn:
  3116	    73	            conn.execute(
  3117	    74	                "INSERT INTO cobalt_jobs (label, kind, expected_cadence, timeout_s, "
  3118	    75	                "heartbeat_source) VALUES (%s, %s, %s, %s, %s) "
  3119	    76	                "ON CONFLICT (label) DO UPDATE SET kind = EXCLUDED.kind, "
  3120	    77	                "expected_cadence = EXCLUDED.expected_cadence, "
  3121	    78	                "timeout_s = EXCLUDED.timeout_s, "
  3122	    79	                "heartbeat_source = EXCLUDED.heartbeat_source, updated_at = now()",
  3123	    80	                (
  3124	    81	                    spec.label,
  3125	    82	                    spec.kind.value,
  3126	    83	                    spec.cadence,
  3127	    84	                    spec.timeout_s,
  3128	    85	                    spec.supervisor.value,
  3129	    86	                ),
  3130	    87	            )
  3131	    88	
  3132	    89	    def register_all(self, registry, *, allow_prod: bool = False) -> list[str]:
  3133	    90	        self.ensure_schema(allow_prod=allow_prod)
  3134	    91	        for spec in registry.jobs:
  3135	    92	            self.register(spec, allow_prod=allow_prod)
  3136	    93	        return [s.label for s in registry.jobs]
  3137	    94	
  3138	    95	    # -- reads --------------------------------------------------------
  3139	    96	
  3140	    97	    def get(self, label: str) -> Optional[dict[str, Any]]:
  3141	    98	        with self._connect() as conn:
  3142	    99	            cur = conn.execute("SELECT * FROM cobalt_jobs WHERE label = %s", (label,))
  3143	   100	            row = cur.fetchone()
  3144	   101	            if row is None:
  3145	   102	                return None
  3146	   103	            return dict(zip([d.name for d in cur.description], row))
  3147	   104	
  3148	   105	    def all(self) -> list[dict[str, Any]]:
  3149	   106	        with self._connect() as conn:
  3150	   107	            cur = conn.execute("SELECT * FROM cobalt_jobs ORDER BY kind DESC, label")
  3151	   108	            columns = [d.name for d in cur.description]
  3152	   109	            return [dict(zip(columns, r)) for r in cur.fetchall()]
  3153	   110	
  3154	   111	    # -- the run lifecycle (the wrapper's three calls) -----------------
  3155	   112	
  3156	   113	    def mark_running(self, label: str, *, now: Optional[datetime] = None) -> None:
  3157	   114	        ts = now or clock_mod.now_utc()
  3158	   115	        with self._connect() as conn:
  3159	   116	            cur = conn.execute(
  3160	   117	                "UPDATE cobalt_jobs SET state = %s, started_at = %s, heartbeat_at = %s, "
  3161	   118	                "finished_at = NULL, exit_code = NULL, last_error = NULL, "
  3162	   119	                "updated_at = now() WHERE label = %s",
  3163	   120	                (JobState.RUNNING.value, ts, ts, label),
  3164	   121	            )
  3165	   122	            if cur.rowcount != 1:
  3166	   123	                raise JobStoreError(
  3167	   124	                    f"no jobs row for {label!r} — register it first "
  3168	   125	                    "(`cobalt jobs register`). F17 refuses to run a job it cannot "
  3169	   126	                    "report on: an unregistered job that hangs is invisible."
  3170	   127	                )
  3171	   128	
  3172	   129	    def beat(self, label: str, *, now: Optional[datetime] = None) -> None:
  3173	   130	        """Stamp `heartbeat_at`. The only thing separating a long job
  3174	   131	        from a hung one."""
  3175	   132	        with self._connect() as conn:
  3176	   133	            conn.execute(
  3177	   134	                "UPDATE cobalt_jobs SET heartbeat_at = %s, updated_at = now() WHERE label = %s",
  3178	   135	                (now or clock_mod.now_utc(), label),
  3179	   136	            )
  3180	   137	
  3181	   138	    def mark_finished(
  3182	   139	        self,
  3183	   140	        label: str,
  3184	   141	        *,
  3185	   142	        exit_code: int,
  3186	   143	        error: Optional[str] = None,
  3187	   144	        result: Optional[dict[str, Any]] = None,
  3188	   145	        now: Optional[datetime] = None,
  3189	   146	    ) -> None:
  3190	   147	        """`done` on 0, `failed` on anything else. Failed is LOUD: F18
  3191	   148	        turns red on this column, and the error text goes with it."""
  3192	   149	        ts = now or clock_mod.now_utc()
  3193	   150	        state = JobState.DONE if exit_code == 0 else JobState.FAILED
  3194	   151	        # F19: a job's own error text is outbound the moment F18 puts it
  3195	   152	        # in a DM. Redacting at the point of STORAGE means a traceback
  3196	   153	        # carrying a DSN never becomes a row that later leaks.
  3197	   154	        safe_error = None
  3198	   155	        if error:
  3199	   156	            from cobalt.redact import redact
  3200	   157	
  3201	   158	            safe_error = redact(error, channel="jobs.last_error").text
  3202	   159	        with self._connect() as conn:
  3203	   160	            conn.execute(
  3204	   161	                "UPDATE cobalt_jobs SET state = %s, finished_at = %s, heartbeat_at = %s, "
  3205	   162	                "exit_code = %s, last_error = %s, last_result = %s, updated_at = now() "
  3206	   163	                "WHERE label = %s",
  3207	   164	                (
  3208	   165	                    state.value,
  3209	   166	                    ts,
  3210	   167	                    ts,
  3211	   168	                    exit_code,
  3212	   169	                    safe_error,
  3213	   170	                    json.dumps(result, default=str) if result is not None else None,
  3214	   171	                    label,
  3215	   172	                ),
  3216	   173	            )
  3217	   174	
  3218	   175	    def mark_zombie(self, label: str, *, reason: str) -> None:
  3219	   176	        """The watchdog's conclusion. Nothing else may write this state."""
  3220	   177	        from cobalt.redact import redact
  3221	   178	
  3222	   179	        with self._connect() as conn:
  3223	   180	            conn.execute(
  3224	   181	                "UPDATE cobalt_jobs SET state = %s, last_error = %s, updated_at = now() "
  3225	   182	                "WHERE label = %s",
  3226	   183	                (JobState.ZOMBIE.value, redact(reason, channel="jobs.last_error").text, label),
  3227	   184	            )
  3228	   185	
  3229	   186	    def mark_probe(
  3230	   187	        self,
  3231	   188	        label: str,
  3232	   189	        *,
  3233	   190	        alive: bool,
  3234	   191	        detail: str,
  3235	   192	        now: Optional[datetime] = None,
  3236	   193	    ) -> None:
  3237	   194	        """Stamp a resident whose heartbeat comes from a PROBE, not from
  3238	   195	        itself (`supervisor: launchd | pidfile`).
  3239	   196	
  3240	   197	        A probe says "the process exists". That is a weaker claim than a
  3241	   198	        wrapper's "I am running and past my gates", which is why
  3242	   199	        `heartbeat_source` is a column: the two must never be read as the
  3243	   200	        same evidence.
  3244	   201	        """
  3245	   202	        from cobalt.redact import redact
  3246	   203	
  3247	   204	        ts = now or clock_mod.now_utc()
  3248	   205	        safe = redact(detail, channel="jobs.last_error").text
  3249	   130	def cmd_run(args: argparse.Namespace) -> None:
  3250	   131	    """Wrap an arbitrary command as `label`. Its exit code is ours."""
  3251	   132	    if not args.command:
  3252	   133	        raise SystemExit("nothing to run — pass the command after `--`")
  3253	   134	    try:
  3254	   135	        with job_run(args.label) as run:
  3255	   136	            proc = subprocess.run(args.command)
  3256	   137	            run.result = {"argv": args.command, "returncode": proc.returncode}
  3257	   138	            if proc.returncode != 0:
  3258	   139	                raise RuntimeError(
  3259	   140	                    f"{args.label}: `{' '.join(args.command)}` exited "
  3260	   141	                    f"{proc.returncode}"
  3261	   142	                )
  3262	   143	    except JobStopped as e:
  3263	   144	        # Exit 0: a deliberate stop is not a failure and must not paint
  3264	   145	        # F18 red for a state the operator caused on purpose.
  3265	   146	        print(f"NOT RUN — {e}")
  3266	   147	        return
  3267	   148	    print(f"{args.label}: exit 0")
  3268	   149	
  3269	   150	
  3270	   151	def cmd_stop(args: argparse.Namespace) -> None:
  3271	   152	    state = killswitch.engage(by=args.by, phrase=args.phrase)
  3272	   153	    print(state.describe())
  3273	   154	
  3274	   155	
  3275	
  3276	codex
  3277	The brief now specifies result preservation, empty `reads`, and plist replacement, and the triage report is present. Two gaps remain: alert selection happens before a vault failure can turn the beat RED, and F17’s database-dependent startup can prevent the beat from reaching its isolated stages.
  3278	exec
  3279	/bin/zsh -lc "nl -ba src/cobalt/jobs/config.py | sed -n '223,325p'; nl -ba configs/cobalt/jobs.yaml | sed -n '1,105p'; nl -ba configs/cobalt/jobs.yaml | sed -n '195,230p'; nl -ba ops/README.md | sed -n '1,38p'; nl -ba ops/README.md | sed -n '140,202p'; nl -ba ops/com.cobalt.heartbeat.plist | sed -n '1,82p'; rg -n 'jobs.yaml|load_job_registry|vault_outcome|notes|message' src/cobalt/jobs/migrations src/cobalt/aset src/cobalt/db_migrations configs/cobalt/db*" in /Users/cobalt/cobalt-wt/heartbeat-mr
  3280	 exited 1 in 0ms:
  3281	   223	
  3282	   224	class JobSpec(BaseModel):
  3283	   225	    model_config = ConfigDict(extra="forbid")
  3284	   226	
  3285	   227	    label: str = Field(min_length=1)
  3286	   228	    kind: JobKind
  3287	   229	    supervisor: Supervisor
  3288	   230	    timeout_s: int = Field(gt=0)
  3289	   231	    what: str = Field(min_length=1)
  3290	   232	    schedule: Optional[Schedule] = None
  3291	   233	    pidfile: Optional[str] = None
  3292	   234	    #: Is this job's plist supposed to be LOADED in launchd right now?
  3293	   235	    #:
  3294	   236	    #: Default True, because that is what every job in this registry has
  3295	   237	    #: always meant. `enabled: false` is the narrow, declared case of a
  3296	   238	    #: job that is BUILT, registered and reviewable but deliberately not
  3297	   239	    #: yet handed over to launchd — `com.cobalt.herdr` is the first, and
  3298	   240	    #: it exists because the handover has to happen at the keyboard (the
  3299	   241	    #: server being registered is the one hosting the session that would
  3300	   242	    #: register it).
  3301	   243	    #:
  3302	   244	    #: THE FLAG SUPPRESSES THE PROBE, NOT THE ROW. A disabled job is
  3303	   245	    #: still in the registry, still has to have a plist in ops/, still
  3304	   246	    #: has its schedule cross-checked by the suite. What it does not get
  3305	   247	    #: is a red "NOT LOADED in launchd" every 15 minutes for a state
  3306	   248	    #: somebody chose on purpose — which is exactly the kind of standing
  3307	   249	    #: red that teaches a reader to scroll past the heartbeat.
  3308	   250	    #:
  3309	   251	    #: Flipping it to true is the LAST step of a handover, after the
  3310	   252	    #: bootstrap: true means "launchd should hold this, tell me if it
  3311	   253	    #: does not".
  3312	   254	    enabled: bool = True
  3313	   255	
  3314	   256	    #: Repo-relative config files this RESIDENT RE-READS AT RUNTIME.
  3315	   257	    #:
  3316	   258	    #: THE LAW THIS SERVES, ruled three times (2026-09-04, 2026-09-08 on
  3317	   259	    #: aset.yaml, 2026-09-09 on tunables.yaml): a config-shape change and
  3318	   260	    #: the restart of every resident that reads that file are ONE ACTION.
  3319	   261	    #: The 09-09 case is the one to remember — the 09-08 seat-usage deploy
  3320	   262	    #: added a `TunableUnit.WINDOW` row to tunables.yaml and its plan said
  3321	   263	    #: "nothing else is restarted". The ASET sheet re-reads that file on
  3322	   264	    #: every request, through code that predated the enum value, so from
  3323	   265	    #: roughly 19:00 to 07:06 the page he trades beside answered HTTP 200
  3324	   266	    #: and refused every card. The deploy was right about its own job and
  3325	   267	    #: wrong about everybody else's.
  3326	   268	    #:
  3327	   269	    #: EVERY ENTRY IS DERIVED FROM THE CODE, never guessed: a row here
  3328	   270	    #: claims that a specific loader call reads a specific file on a
  3329	   271	    #: request path, and the 2026-09-09 ops report cites file:line for
  3330	   272	    #: each one. A guessed row is worse than an empty list, because
  3331	   273	    #: `cobalt jobs readers` is trusted to be complete.
  3332	   274	    #:
  3333	   275	    #: ONE-SHOTS LEAVE IT EMPTY, and `cobalt validate` enforces that: a
  3334	   276	    #: one-shot re-reads everything every time it runs, by definition —
  3335	   277	    #: it starts, reads, exits. There is no stale process to restart, so
  3336	   278	    #: rows here would be noise diluting the ones that mean something.
  3337	   279	    #:
  3338	   280	    #: KNOWN GAP, deliberately not papered over: this is RE-READS, not
  3339	   281	    #: reads. A resident that loads a config ONCE AT STARTUP also needs a
  3340	   282	    #: restart when it changes, and `com.cobalt.agent` (the old tree) is
  3341	   283	    #: exactly that shape — it caches settings in a singleton at first
  3342	   284	    #: construction (`cobalt_agent/config.py:410`). That wants its own
  3343	   285	    #: field; see the 09-09 report's ESCALATE.
  3344	   286	    reads: list[str] = Field(default_factory=list)
  3345	   287	
  3346	   288	    @model_validator(mode="after")
  3347	   289	    def _shape_matches_kind(self) -> "JobSpec":
  3348	   290	        if self.kind is JobKind.ONE_SHOT and self.reads:
  3349	   291	            raise ValueError(
  3350	   292	                f"{self.label}: `reads` belongs to a RESIDENT. A one-shot re-reads "
  3351	   293	                "everything every time it runs — there is no stale process to "
  3352	   294	                "restart, so naming files here dilutes the rows that do mean "
  3353	   295	                "something."
  3354	   296	            )
  3355	   297	        bad = [p for p in self.reads if Path(p).is_absolute() or ".." in Path(p).parts]
  3356	   298	        if bad:
  3357	   299	            raise ValueError(
  3358	   300	                f"{self.label}: `reads` entries are REPO-RELATIVE with no `..`: {bad}"
  3359	   301	            )
  3360	   302	        if self.kind is JobKind.ONE_SHOT and self.schedule is None:
  3361	   303	            raise ValueError(
  3362	   304	                f"{self.label}: a one-shot needs a `schedule` — the MISSED probe "
  3363	   305	                "asks 'should this have run by now', and without a schedule there "
  3364	   306	                "is no answer, only silence."
  3365	   307	            )
  3366	   308	        if self.supervisor is Supervisor.PIDFILE and not self.pidfile:
  3367	   309	            raise ValueError(f"{self.label}: supervisor `pidfile` needs a `pidfile` path")
  3368	   310	        if self.supervisor is not Supervisor.PIDFILE and self.pidfile:
  3369	   311	            raise ValueError(
  3370	   312	                f"{self.label}: `pidfile` is set but the supervisor is "
  3371	   313	                f"{self.supervisor} — nothing would read it."
  3372	   314	            )
  3373	   315	        return self
  3374	   316	
  3375	   317	    @property
  3376	   318	    def cadence(self) -> Optional[str]:
  3377	   319	        return self.schedule.describe() if self.schedule else None
  3378	   320	
  3379	   321	    @property
  3380	   322	    def pidfile_path(self) -> Optional[Path]:
  3381	   323	        return (REPO_ROOT / self.pidfile) if self.pidfile else None
  3382	   324	
  3383	   325	    @property
  3384	     1	# F17 TASK INTEGRITY — the job registry (Charter §3 F17, L18).
  3385	     2	#
  3386	     3	# Schema: src/cobalt/jobs/config.py. Pydantic-validated on load; a bad
  3387	     4	# row CRASHES with its label. `cobalt validate` cross-checks this file
  3388	     5	# against ops/*.plist and fails on a job in one and not the other —
  3389	     6	# a registry that has drifted from launchd is a registry that reports
  3390	     7	# green for a job that no longer exists.
  3391	     8	#
  3392	     9	# ---------------------------------------------------------------------
  3393	    10	# WHAT A ROW MEANS
  3394	    11	# ---------------------------------------------------------------------
  3395	    12	# label     : the launchd label, exactly. It is the join key everywhere.
  3396	    13	# kind      : resident (runs continuously) | one-shot (runs and exits).
  3397	    14	# supervisor: WHO stamps `heartbeat_at`, and this is the honest part —
  3398	    15	#             `self`    Cobalt's own code, through the wrapper
  3399	    16	#                       (src/cobalt/jobs/wrapper.py). The process says it
  3400	    17	#                       is alive because it IS alive and running our code.
  3401	    18	#             `launchd` launchd holds a live PID for it. Cobalt does not
  3402	    19	#                       run inside it (Obsidian, the LM Studio server) or
  3403	    20	#                       does not want a heartbeat thread in it (the ASET
  3404	    21	#                       sheet). The WATCHDOG stamps from a real
  3405	    22	#                       `launchctl` probe, and the row says so, so nothing
  3406	    23	#                       pretends the process reported in itself.
  3407	    24	#             `pidfile` the process is not launchd's own child — see
  3408	    25	#                       com.cobalt.agent below.
  3409	    26	# enabled   : is this plist supposed to be LOADED in launchd right now?
  3410	    27	#             Defaults true, which is what every row has always meant.
  3411	    28	#             `false` is the declared case of a job that is built,
  3412	    29	#             registered and reviewable but NOT yet handed over — the
  3413	    30	#             sweep reports it and probes nothing, so a deliberate state
  3414	    31	#             never shows up as a standing red.
  3415	    32	# timeout_s : how long a run may take before a stale heartbeat means
  3416	    33	#             ZOMBIE. The wrapper stamps at least every timeout_s/3.
  3417	    34	# schedule  : mirrors the plist. launchd cannot read this file and this
  3418	    35	#             file cannot read launchd, so `cobalt validate` compares
  3419	    36	#             them and a drift is loud.
  3420	    37	jobs:
  3421	    38	  # ---------------- residents ----------------
  3422	    39	  - label: com.cobalt.aset
  3423	    40	    kind: resident
  3424	    41	    supervisor: launchd
  3425	    42	    # The ASET sheet (ops/start_aset.sh -> uvicorn). It is Cobalt's own
  3426	    43	    # code, but it is a request-driven server: a heartbeat thread inside
  3427	    44	    # it would report "the process exists", which is exactly what the
  3428	    45	    # launchd probe already reports, and F18 additionally probes the
  3429	    46	    # sheet's HTTP 200 — which is the thing that actually matters and
  3430	    47	    # that a thread could not tell us (S1-P2 watched this process serve
  3431	    48	    # 500s while perfectly alive).
  3432	    49	    timeout_s: 300
  3433	    50	    # WHAT THIS PROCESS RE-READS ON EVERY REQUEST — derived by measuring
  3434	    51	    # the request path (instrumented `open`/`read_text` over GET / and
  3435	    52	    # GET /api/health), not by reading config names off a shelf. Each
  3436	    53	    # entry cites its loader call in the 2026-09-09 ops report.
  3437	    54	    #
  3438	    55	    # It is the reason the field exists. On 09-08 a deploy added a
  3439	    56	    # `TunableUnit.WINDOW` row to tunables.yaml and said "nothing else is
  3440	    57	    # restarted"; this process re-read the new file through code that
  3441	    58	    # predated the enum value, and from ~19:00 to 07:06 the page he
  3442	    59	    # trades beside answered HTTP 200 and refused every card.
  3443	    60	    #
  3444	    61	    # NOT LISTED, and the omission is the point: `configs/dev/vault.yaml`
  3445	    62	    # IS re-read per request in dev (cobalt/vault.py:167) but NOT in
  3446	    63	    # production, where COBALT_VAULT_PATH is set in this job's own plist
  3447	    64	    # and the resolver returns before it reads the file. A row here that
  3448	    65	    # is only true in dev would send an operator to restart the sheet for
  3449	    66	    # a file production never opens.
  3450	    67	    reads:
  3451	    68	      - "configs/dev/aset.yaml"                    # aset/config.py:134 (load_config); the name says dev, but there is no configs/cobalt/aset.yaml — this IS the production sheet's config
  3452	    69	      - "configs/cobalt/taxonomy/tunables.yaml"    # taxonomy/loader.py:79 (load_tunables); the 09-09 R1 case
  3453	    70	    what: "the ASET semi-auto sheet on :5010 — the surface he trades beside"
  3454	    71	
  3455	    72	  - label: com.cobalt.mainframe
  3456	    73	    kind: resident
  3457	    74	    supervisor: launchd
  3458	    75	    timeout_s: 600
  3459	    76	    # EMPTY, derived: LM Studio is not Cobalt code and reads its own
  3460	    77	    # `~/.lmstudio/` config, which is not repo-relative. Nothing in
  3461	    78	    # configs/ reaches this process.
  3462	    79	    reads: []
  3463	    80	    what: "the LM Studio local-model server (ops/start_mainframe.sh), the L23 local lane"
  3464	    81	
  3465	    82	  - label: com.cobalt.obsidian
  3466	    83	    kind: resident
  3467	    84	    supervisor: launchd
  3468	    85	    timeout_s: 300
  3469	    86	    what: >
  3470	    87	      Obsidian as a supervised service (RULING 6). Not decoration: the
  3471	    88	      vault reaches his other devices only through a RUNNING Obsidian on
  3472	    89	      this Mac, and on 09-04 a correct 05:15 write was silently
  3473	    90	      overwritten because none was running.
  3474	    91	    # EMPTY, derived: Obsidian is a third-party app. It reads the vault's
  3475	    92	    # own .obsidian/ directory, never configs/.
  3476	    93	    reads: []
  3477	    94	
  3478	    95	  - label: com.cobalt.agent
  3479	    96	    kind: resident
  3480	    97	    supervisor: pidfile
  3481	    98	    pidfile: logs/cobalt.pid
  3482	    99	    timeout_s: 600
  3483	   100	    # WHAT com.cobalt.agent IS (S1-P3 answer to the prompt's question).
  3484	   101	    # It is the OLD TREE's agent: the plist runs `cobalt.sh start`, which
  3485	   102	    # pre-flight-checks LM Studio/Postgres/Mattermost and then
  3486	   103	    # `nohup uv run src/cobalt_agent/main.py &` — the Mattermost
  3487	   104	    # websocket listener, the scheduler, the Scribe, the memory layer.
  3488	   105	    #
  3489	   195	    # rescans every source file when its cache is cold, and the dump
  3490	   196	    # alone is 360 MB.
  3491	   197	    timeout_s: 3600
  3492	   198	    # EVERY day including weekends, and after the archiver's 20:30 (which
  3493	   199	    # takes ~23 min) so the snapshot contains that night's bars rather
  3494	   200	    # than racing them. A vault edit on a Saturday is exactly as
  3495	   201	    # unrecoverable as one on a Tuesday.
  3496	   202	    schedule: {at: "21:40", weekdays: [0, 1, 2, 3, 4, 5, 6]}
  3497	   203	    what: "the nightly restic snapshot — vault + a fresh cobalt_brain dump, to the SSD"
  3498	   204	
  3499	   205	  - label: com.cobalt.heartbeat
  3500	   206	    kind: one-shot
  3501	   207	    supervisor: self
  3502	   208	    timeout_s: 300
  3503	   209	    # EVERY interval, all week. The heartbeat is the thing that notices a
  3504	   210	    # weekend failure before Monday morning needs it.
  3505	   211	    schedule: {every_min_tunable: heartbeat.interval_min}
  3506	   212	    what: "the F18 heartbeat host — probes everything above and says so out loud"
  3507	   213	
  3508	   214	  - label: com.cobalt.seat-usage
  3509	   215	    kind: one-shot
  3510	   216	    supervisor: self
  3511	   217	    timeout_s: 300
  3512	   218	    # An INTERVAL inside a WINDOW, both from tunables rows (F16). launchd
  3513	   219	    # has no such shape natively, so the plist carries the window expanded
  3514	   220	    # into one StartCalendarInterval entry per firing and the suite
  3515	   221	    # compares the two — see Schedule.calendar_entries().
  3516	   222	    schedule:
  3517	   223	      every_min_tunable: seat_usage.interval_min
  3518	   224	      window_tunable: seat_usage.window
  3519	   225	      weekdays: [0, 1, 2, 3, 4, 5, 6]
  3520	   226	    what: "the hourly seat-usage report (uv run cobalt seat-usage run) — what the seats cost today"
  3521	   227	
  3522	   228	  - label: com.cobalt.generated
  3523	   229	    kind: one-shot
  3524	   230	    supervisor: self
  3525	     1	# ops/ — LaunchAgents & wrapper scripts
  3526	     2	
  3527	     3	Everything here is captured in git as the SOURCE for what's installed
  3528	     4	to `~/Library/LaunchAgents/` — that install directory itself is outside
  3529	     5	the repo and not tracked. When you add or change a plist, re-copy it
  3530	     6	(see "Install / reload" below); the copy in `~/Library/LaunchAgents/`
  3531	     7	does not auto-update from git.
  3532	     8	
  3533	     9	## Inventory
  3534	    10	
  3535	    11	**Nine plists below, all of them loaded, as of 2026-09-09**
  3536	    12	(`launchctl list | grep com.cobalt`). `com.cobalt.herdr` was the one
  3537	    13	exception until the handover on 2026-09-08 at 19:21 ET; it is live now —
  3538	    14	see "herdr under launchd (0.9.0)" further down. `com.cobalt.generated`
  3539	    15	is new on 2026-09-09.
  3540	    16	
  3541	    17	This table is not the whole of `ops/`, and never was: `com.cobalt.backup`,
  3542	    18	`cards-expire`, `daymode-propose`, `heartbeat` and `obsidian` have
  3543	    19	plists and rows without a row here. **`configs/cobalt/jobs.yaml` is the
  3544	    20	authoritative list** — fourteen labels, cross-checked against `ops/`
  3545	    21	by `uv run cobalt validate` on every run of the gate. Read this table as
  3546	    22	prose about the ones with a story attached, not as an inventory.
  3547	    23	
  3548	    24	| Plist | Runs | Schedule | Wrapper | Installed |
  3549	    25	|---|---|---|---|---|
  3550	    26	| `com.cobalt.agent.plist` | `cobalt.sh start` (the Mattermost chief-of-staff agent) | RunAtLoad only, no KeepAlive | — | yes |
  3551	    27	| `com.cobalt.mainframe.plist` | `ops/start_mainframe.sh` (local LLM — the L23 local lane) | RunAtLoad only | `ops/start_mainframe.sh` | yes |
  3552	    28	| `com.cobalt.archiver.plist` | `/Users/cobalt/.local/bin/uv run archiver` (nightly bar archiver) | Mon-Fri 20:30 ET | — | yes (2026-09-03 — was not loaded before this) |
  3553	    29	| `com.cobalt.prefill-daily.plist` | `/Users/cobalt/.local/bin/uv run prefill daily` | Mon-Fri 05:15 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
  3554	    30	| `com.cobalt.prefill-drc.plist` | `/Users/cobalt/.local/bin/uv run prefill drc` | Mon-Fri 15:40 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
  3555	    31	| `com.cobalt.aset.plist` | `ops/start_aset.sh` → `uv run python -m cobalt.aset` (ASET sizing widget, :5010) | RunAtLoad + KeepAlive (persistent) | `ops/start_aset.sh` | yes |
  3556	    32	| `com.cobalt.herdr.plist` | `/opt/homebrew/bin/herdr server` (the terminal workspace every agent seat lives in) | RunAtLoad + KeepAlive on crash only | — | **yes (2026-09-08 19:21 — the handover)** |
  3557	    33	| `com.cobalt.generated.plist` | `/Users/cobalt/.local/bin/uv run cobalt generated commit` (commits the files a job rewrote today) | daily 23:37 ET | F17 wrapper | new 2026-09-09 |
  3558	    34	| `com.cobalt.seat-usage.plist` | `/Users/cobalt/.local/bin/uv run cobalt seat-usage run` (the hourly seat-usage report) | hourly 06:00-23:00 ET, every day | F17 wrapper (`cobalt seat-usage run`) | yes (2026-09-08) |
  3559	    35	
  3560	    36	The table above says which plists are *supposed* to be loaded.
  3561	    37	`configs/cobalt/jobs.yaml` is the machine-readable version of the same
  3562	    38	claim, and `uv run cobalt validate` compares the two: it fails on a job
  3563	   140	which uses `lms` — the earlier note above conflated it with the archiver
  3564	   141	bug; left uninvestigated further since it isn't broken).
  3565	   142	
  3566	   143	*(Path corrected 2026-09-09: this paragraph and the Inventory row both
  3567	   144	said `~/.lmstudio/start_mainframe.sh`. The wrapper is in the repo, where
  3568	   145	it is reviewed in a diff; `~/.lmstudio/` is where the 09-04 note put it
  3569	   146	and the plist never agreed.)*
  3570	   147	
  3571	   148	## Install / reload
  3572	   149	
  3573	   150	```sh
  3574	   151	# first install
  3575	   152	cp ops/com.cobalt.<name>.plist ~/Library/LaunchAgents/
  3576	   153	launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.<name>.plist
  3577	   154	
  3578	   155	# after editing the plist or its wrapper script
  3579	   156	cp ops/com.cobalt.<name>.plist ~/Library/LaunchAgents/   # only if the plist itself changed
  3580	   157	launchctl kickstart -k gui/$(id -u)/com.cobalt.<name>
  3581	   158	
  3582	   159	# status / logs
  3583	   160	launchctl list | grep com.cobalt.<name>
  3584	   161	tail -f logs/<name>.log logs/<name>.err
  3585	   162	
  3586	   163	# stop + unload
  3587	   164	launchctl bootout gui/$(id -u)/com.cobalt.<name>
  3588	   165	```
  3589	   166	
  3590	   167	## Deploy checklist
  3591	   168	
  3592	   169	**THE LAW, ruled three times — 2026-09-04, 2026-09-08 (`aset.yaml`) and
  3593	   170	2026-09-09 (`tunables.yaml`): a config-shape change and the restart of
  3594	   171	EVERY resident that reads that file are ONE ACTION.** Not two steps, not
  3595	   172	a follow-up. A deploy plan that changes a config and does not name the
  3596	   173	processes it restarts is an incomplete plan.
  3597	   174	
  3598	   175	**Every deploy plan carries a `RESTARTS:` line, and it is produced by a
  3599	   176	command, not by memory:**
  3600	   177	
  3601	   178	```sh
  3602	   179	# for every config file the merge touches
  3603	   180	uv run cobalt jobs readers configs/cobalt/taxonomy/tunables.yaml
  3604	   181	#   -> RESTARTS: com.cobalt.aset
  3605	   182	
  3606	   183	launchctl kickstart -k gui/$(id -u)/com.cobalt.aset
  3607	   184	```
  3608	   185	
  3609	   186	`cobalt jobs readers` reads `reads:` in `configs/cobalt/jobs.yaml` —
  3610	   187	per-resident, derived from the code, one row per config file the process
  3611	   188	re-reads at runtime. **An unknown path exits 1**, deliberately: "no
  3612	   189	resident re-reads this" and "nobody has worked out who reads this" are
  3613	   190	different answers, and only one of them makes it safe to deploy without
  3614	   191	a restart. `uv run cobalt validate` prints the whole map and fails if a
  3615	   192	listed path has gone missing.
  3616	   193	
  3617	   194	### Why this is a law and not a habit
  3618	   195	
  3619	   196	On 2026-09-08 at ~19:00 the seat-usage deploy added a
  3620	   197	`TunableUnit.WINDOW` row to `configs/cobalt/taxonomy/tunables.yaml`. Its
  3621	   198	plan said *"nothing else is loaded or restarted"* — true of its own job,
  3622	   199	and wrong about the sheet. `com.cobalt.aset` had been running since
  3623	   200	17:50 and **re-reads `tunables.yaml` on every request**, so it read the
  3624	   201	new row through code that predated the enum value and raised
  3625	   202	`TaxonomyConfigError` on every render. From then until the kickstart at
  3626	     1	<?xml version="1.0" encoding="UTF-8"?>
  3627	     2	<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  3628	     3	<plist version="1.0">
  3629	     4	<dict>
  3630	     5	    <key>Label</key>
  3631	     6	    <string>com.cobalt.heartbeat</string>
  3632	     7	    <key>EnvironmentVariables</key>
  3633	     8	    <dict>
  3634	     9	        <key>PATH</key>
  3635	    10	        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/cobalt/.local/bin</string>
  3636	    11	        <!-- RULING 7 / Charter §8.4: every plist carries COBALT_ENV. The
  3637	    12	             heartbeat reads the LIVE jobs table and writes the LIVE daily
  3638	    13	             note, so it declares production. Without this the store would
  3639	    14	             refuse to resolve a database at all rather than quietly
  3640	    15	             defaulting to dev. -->
  3641	    16	        <key>COBALT_ENV</key>
  3642	    17	        <string>production</string>
  3643	    18	        <!-- Output 1 is a Cobalt-owned block in TODAY'S daily note (L28
  3644	    19	             unit, in-place update). That has to be the real vault. -->
  3645	    20	        <key>COBALT_VAULT_PATH</key>
  3646	    21	        <string>/Users/cobalt/Vault/Think</string>
  3647	    22	    </dict>
  3648	    23	    <key>ProgramArguments</key>
  3649	    24	    <array>
  3650	    25	        <!-- ABSOLUTE PATH, deliberately: launchd posix_spawn()s
  3651	    26	             ProgramArguments[0] and does NOT search the job's own PATH
  3652	    27	             the way a shell does. A bare "uv" here produces exit 78
  3653	    28	             (EX_CONFIG) with empty stdout and stderr, which is exactly
  3654	    29	             how the 05:15 prefill failed silently on 2026-09-03. -->
  3655	    30	        <string>/Users/cobalt/.local/bin/uv</string>
  3656	    31	        <string>run</string>
  3657	    32	        <string>cobalt</string>
  3658	    33	        <string>heartbeat</string>
  3659	    34	        <string>beat</string>
  3660	    35	    </array>
  3661	    36	    <key>WorkingDirectory</key>
  3662	    37	    <string>/Users/cobalt/cobalt</string>
  3663	    38	    <key>AbandonProcessGroup</key>
  3664	    39	    <true/>
  3665	    40	    <!-- StartInterval, NOT StartCalendarInterval, and every day of the
  3666	    41	         week. The heartbeat is the thing that notices a Saturday failure
  3667	    42	         before Monday morning needs it, and every "red within one
  3668	    43	         interval" claim in Charter §3 F18 is measured against THIS
  3669	    44	         number.
  3670	    45	
  3671	    46	         900 s = 15 min = the `heartbeat.interval_min` tunable. launchd
  3672	    47	         cannot read a tunables row, so this is a mirror; `cobalt
  3673	    48	         validate` prints both and fails if they disagree, which is the
  3674	    49	         only thing standing between the schedule and the code that
  3675	    50	         believes it. -->
  3676	    51	    <key>StartInterval</key>
  3677	    52	    <integer>900</integer>
  3678	    53	    <!-- RunAtLoad: the first beat happens when the machine comes up,
  3679	    54	         rather than up to 15 minutes later. A reboot is precisely when
  3680	    55	         something is most likely to be down (09-04: the 15.7.9 reboot
  3681	    56	         left Obsidian dead and a whole day's writes unsynced). -->
  3682	    57	    <key>RunAtLoad</key>
  3683	    58	    <true/>
  3684	    59	    <key>StandardOutPath</key>
  3685	    60	    <string>/Users/cobalt/cobalt/logs/heartbeat.log</string>
  3686	    61	    <key>StandardErrorPath</key>
  3687	    62	    <string>/Users/cobalt/cobalt/logs/heartbeat.err</string>
  3688	    63	</dict>
  3689	    64	</plist>
  3690	zsh:1: no matches found: configs/cobalt/db*
  3691	
  3692	exec
  3693	/bin/zsh -lc "rg --files src/cobalt/jobs/migrations src/cobalt/db_migrations configs | rg 'migration|placement'; rg -n 'load_job_registry|cobalt.jobs' src/cobalt/aset src/cobalt_agent; nl -ba src/cobalt/jobs/migrations/001_jobs.sql; nl -ba src/cobalt/jobs/killswitch.py | sed -n '50,110p'; nl -ba src/cobalt/jobs/watchdog.py | sed -n '90,205p'; nl -ba src/cobalt/db_migrations/cli.py | sed -n '1,135p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
  3694	 succeeded in 0ms:
  3695	src/cobalt/db_migrations/placement.py
  3696	src/cobalt/db_migrations/cli.py
  3697	src/cobalt/db_migrations/0001_schemas.sql
  3698	src/cobalt/db_migrations/__init__.py
  3699	src/cobalt/db_migrations/0002_move_tables.rollback.sql
  3700	src/cobalt/db_migrations/0002_move_tables.sql
  3701	src/cobalt/jobs/migrations/0001_cobalt_jobs.sql
  3702	nl: src/cobalt/jobs/migrations/001_jobs.sql: No such file or directory
  3703	    50	            f"KILL SWITCH ACTIVE — set by {self.set_by or 'unknown'}{when} "
  3704	    51	            f"(phrase: {self.phrase!r}). One-shots refuse to start; residents exit "
  3705	    52	            "cleanly at their next heartbeat. Clear it with `cobalt resume`."
  3706	    53	        )
  3707	    54	
  3708	    55	
  3709	    56	def read(store: Optional[JobStore] = None) -> KillState:
  3710	    57	    store = store or JobStore()
  3711	    58	    row = store.kill_switch()
  3712	    59	    return KillState(
  3713	    60	        active=bool(row.get("active")),
  3714	    61	        phrase=row.get("phrase"),
  3715	    62	        set_by=row.get("set_by"),
  3716	    63	        set_at=row.get("set_at"),
  3717	    64	    )
  3718	    65	
  3719	    66	
  3720	    67	def is_active(store: Optional[JobStore] = None) -> bool:
  3721	    68	    """Fail OPEN, deliberately, and loudly.
  3722	    69	
  3723	    70	    If the database cannot be reached the answer is "not stopped". The
  3724	    71	    alternative — a database blip silently stopping every scheduled job
  3725	    72	    on the host — is a far worse failure than one run happening after a
  3726	    73	    stop was requested, and it would look exactly like the kill switch
  3727	    74	    working correctly.
  3728	    75	    """
  3729	    76	    try:
  3730	    77	        return read(store).active
  3731	    78	    except Exception as e:  # noqa: BLE001
  3732	    79	        logger.error(
  3733	    80	            "F17: could not read the kill switch ({}: {}) — treating it as CLEAR. "
  3734	    81	            "A database blip must not silently stop every job on this host.",
  3735	    82	            type(e).__name__, e,
  3736	    83	        )
  3737	    84	        return False
  3738	    85	
  3739	    86	
  3740	    87	def engage(*, by: str, phrase: Optional[str] = None, store: Optional[JobStore] = None) -> KillState:
  3741	    88	    store = store or JobStore()
  3742	    89	    store.ensure_schema()
  3743	    90	    registry = load_job_registry()
  3744	    91	    store.set_kill_switch(active=True, phrase=phrase or registry.kill_phrase, by=by)
  3745	    92	    state = read(store)
  3746	    93	    logger.error(state.describe())      # ERROR: this is a loud, visible act
  3747	    94	    return state
  3748	    95	
  3749	    96	
  3750	    97	def clear(*, by: str, store: Optional[JobStore] = None) -> KillState:
  3751	    98	    store = store or JobStore()
  3752	    99	    store.ensure_schema()
  3753	   100	    store.set_kill_switch(active=False, phrase=None, by=by)
  3754	   101	    state = read(store)
  3755	   102	    logger.warning("F17: kill switch CLEARED by {} — jobs run normally again.", by)
  3756	   103	    return state
  3757	   104	
  3758	   105	
  3759	   106	def matches_kill_phrase(text: str) -> bool:
  3760	   107	    """Does an inbound message carry the kill phrase?
  3761	   108	
  3762	   109	    Exists for the Mattermost DM listener the moment one lands in the new
  3763	   110	    core. The phrase is CONFIG (`configs/cobalt/jobs.yaml`), compared
  3764	    90	      fire again. Charter §3 F18's acceptance test is exactly this
  3765	    91	      ("unload a plist -> red within one interval").
  3766	    92	    * `loaded=True, pid=None` — registered with launchd, not currently
  3767	    93	      running. Correct and healthy for a one-shot between runs; a
  3768	    94	      FAILURE for a resident.
  3769	    95	    * `last_exit` — launchd's own record of how the last run ended,
  3770	    96	      which is the other half of what the Charter asks for ("every ops
  3771	    97	      plist loaded + last exit code").
  3772	    98	    """
  3773	    99	
  3774	   100	    label: str
  3775	   101	    loaded: bool
  3776	   102	    pid: Optional[int]
  3777	   103	    last_exit: Optional[int]
  3778	   104	    detail: str
  3779	   105	
  3780	   106	
  3781	   107	def launchctl_status(label: str, *, timeout: float = 5.0) -> LaunchdStatus:
  3782	   108	    """Ask launchd about one label. Fail-loud: a `launchctl` that cannot
  3783	   109	    be run RAISES rather than reporting "not loaded" — "the probe is
  3784	   110	    broken" and "the job is gone" are different facts, and collapsing
  3785	   111	    them is how a red condition becomes invisible (the same rule
  3786	   112	    `cobalt.obsidian` keeps)."""
  3787	   113	    binary = shutil.which("launchctl") or "/bin/launchctl"
  3788	   114	    if not os.path.exists(binary):
  3789	   115	        raise RuntimeError("launchctl not found — cannot probe launchd jobs.")
  3790	   116	    proc = subprocess.run(
  3791	   117	        [binary, "list"], capture_output=True, text=True, timeout=timeout
  3792	   118	    )
  3793	   119	    if proc.returncode != 0:
  3794	   120	        raise RuntimeError(
  3795	   121	            f"`launchctl list` exited {proc.returncode}: "
  3796	   122	            f"{proc.stderr.strip() or '(no stderr)'}"
  3797	   123	        )
  3798	   124	    for line in proc.stdout.splitlines():
  3799	   125	        parts = line.split("\t")
  3800	   126	        if len(parts) == 3 and parts[2].strip() == label:
  3801	   127	            pid_raw, status_raw = parts[0].strip(), parts[1].strip()
  3802	   128	            pid = int(pid_raw) if pid_raw.lstrip("-").isdigit() and pid_raw != "-" else None
  3803	   129	            try:
  3804	   130	                last_exit = int(status_raw)
  3805	   131	            except ValueError:
  3806	   132	                last_exit = None
  3807	   133	            detail = (
  3808	   134	                f"loaded, pid {pid}" if pid is not None
  3809	   135	                else f"loaded, not running (last exit {status_raw})"
  3810	   136	            )
  3811	   137	            return LaunchdStatus(label, True, pid, last_exit, detail)
  3812	   138	    return LaunchdStatus(
  3813	   139	        label, False, None, None,
  3814	   140	        "NOT LOADED in launchd — `launchctl list` does not know this label, so it "
  3815	   141	        "will never fire again. Reload it: "
  3816	   142	        f"launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/{label}.plist",
  3817	   143	    )
  3818	   144	
  3819	   145	
  3820	   146	def launchctl_pid(label: str, *, timeout: float = 5.0) -> tuple[Optional[int], str]:
  3821	   147	    """(pid, detail). Kept as the narrow question residents ask."""
  3822	   148	    status = launchctl_status(label, timeout=timeout)
  3823	   149	    if status.pid is not None:
  3824	   150	        return status.pid, f"launchd pid {status.pid}"
  3825	   151	    return None, status.detail
  3826	   152	
  3827	   153	
  3828	   154	def pidfile_alive(spec: JobSpec) -> tuple[bool, str]:
  3829	   155	    """(alive, detail) for a detached resident tracked by a PID file."""
  3830	   156	    path = spec.pidfile_path
  3831	   157	    if path is None or not path.exists():
  3832	   158	        return False, f"no pid file at {path} — the process was never started, or it cleaned up"
  3833	   159	    raw = path.read_text().strip()
  3834	   160	    if not raw.isdigit():
  3835	   161	        return False, f"pid file {path} does not contain a pid ({raw[:40]!r})"
  3836	   162	    pid = int(raw)
  3837	   163	    try:
  3838	   164	        os.kill(pid, 0)          # signal 0: existence check, changes nothing
  3839	   165	    except ProcessLookupError:
  3840	   166	        return False, f"pid {pid} from {path} is GONE — stale pid file, process is dead"
  3841	   167	    except PermissionError:
  3842	   168	        return True, f"pid {pid} exists (owned by another user)"
  3843	   169	    return True, f"pid {pid} alive (from {path})"
  3844	   170	
  3845	   171	
  3846	   172	# ---------------------------------------------------------------------
  3847	   173	# schedule arithmetic — "should this have run by now?"
  3848	   174	# ---------------------------------------------------------------------
  3849	   175	
  3850	   176	
  3851	   177	def last_due(spec: JobSpec, now_et: datetime) -> Optional[datetime]:
  3852	   178	    """The most recent CALENDAR moment this one-shot was scheduled to
  3853	   179	    fire, at or before `now_et`. `None` for an interval job (which has no
  3854	   180	    calendar moments — see `is_missed`) and for a resident.
  3855	   181	
  3856	   182	    Weekday numbering is launchd's (1 = Monday), matching the plists this
  3857	   183	    mirrors.
  3858	   184	    """
  3859	   185	    schedule = spec.schedule
  3860	   186	    if schedule is None or schedule.interval_minutes() is not None:
  3861	   187	        return None
  3862	   188	
  3863	   189	    hh, _, mm = schedule.at.partition(":")
  3864	   190	    hour, minute = int(hh), int(mm)
  3865	   191	    # launchd: Sunday is 0 and 7; python's isoweekday() is Mon=1..Sun=7.
  3866	   192	    wanted = {0 if d == 7 else d for d in schedule.weekdays}
  3867	   193	    probe: date = now_et.date()
  3868	   194	    for _ in range(14):
  3869	   195	        iso = probe.isoweekday()
  3870	   196	        launchd_day = 0 if iso == 7 else iso
  3871	   197	        if launchd_day in wanted:
  3872	   198	            due = datetime(
  3873	   199	                probe.year, probe.month, probe.day, hour, minute, tzinfo=ET
  3874	   200	            )
  3875	   201	            if due <= now_et:
  3876	   202	                return due
  3877	   203	        probe -= timedelta(days=1)
  3878	   204	    return None
  3879	   205	
  3880	     1	"""`cobalt db migrate [--allow-prod] [--rollback]` — ADR-0008's harness.
  3881	     2	
  3882	     3	WHAT IT PRINTS IS THE POINT. A migration that moves twelve tables between
  3883	     4	schemas and adds a column to six of them is a migration whose claim
  3884	     5	("nothing was lost") has to be checkable by looking, not by trusting. So
  3885	     6	every run captures, per table, BEFORE and AFTER:
  3886	     7	
  3887	     8	  * where it lives (`public` / `system` / `"user"`),
  3888	     9	  * `count(*)`,
  3889	    10	  * a content digest: `md5(string_agg(row::text, '|' ORDER BY <pk>))`.
  3890	    11	
  3891	    12	THE DIGEST EXCLUDES `user_id`. The forward migration ADDS that column to
  3892	    13	the six user-side tables, so a digest over the whole row would differ
  3893	    14	before and after by construction and would prove nothing. Taking it over
  3894	    15	`to_jsonb(t) - 'user_id'` means the two digests are comparable and an
  3895	    16	inequality is a real finding: the rows themselves changed. `to_jsonb`
  3896	    17	serialises keys in a stable order, so the digest does not depend on
  3897	    18	column order either — which matters, because `SET SCHEMA` and `ADD
  3898	    19	COLUMN` both touch the catalog the naive `row::text` reads.
  3899	    20	
  3900	    21	ORDERED BY THE PRIMARY KEY, read from the catalog per table rather than
  3901	    22	hard-coded: `bars` is keyed `(ticker, interval, ts)`, `day_modes` by
  3902	    23	`trade_date`, `cobalt_jobs` by `label`, the rest by `id`.
  3903	    24	
  3904	    25	`--rollback` runs `0002_move_tables.rollback.sql` (catalog-only reverse)
  3905	    26	and prints the same proof table. Running `migrate`, then `--rollback`,
  3906	    27	then `migrate` again must land on the same digests — the suite asserts
  3907	    28	exactly that round-trip on `cobalt_dev`.
  3908	    29	
  3909	    30	`--allow-prod` reaches `cobalt_brain` without flipping the process into
  3910	    31	production mode (RULING 7's one-off-tooling seam). Without it the target
  3911	    32	is whatever `COBALT_ENV` resolves.
  3912	    33	"""
  3913	    34	
  3914	    35	from __future__ import annotations
  3915	    36	
  3916	    37	import argparse
  3917	    38	from typing import Optional
  3918	    39	
  3919	    40	from psycopg import sql
  3920	    41	
  3921	    42	from cobalt import db, env
  3922	    43	
  3923	    44	from . import FORWARD, REVERSE
  3924	    45	from .placement import MOVED_TABLES, SEEDED_TABLES
  3925	    46	
  3926	    47	#: The tenancy column the digest ignores — see the module docstring.
  3927	    48	TENANCY_COLUMN = "user_id"
  3928	    49	
  3929	    50	#: Where a new-core table may legitimately be found, in look-up order.
  3930	    51	SEARCHED_SCHEMAS = ("public", "user", "system")
  3931	    52	
  3932	    53	
  3933	    54	class MigrationError(RuntimeError):
  3934	    55	    """The migration could not be run or could not be proven."""
  3935	    56	
  3936	    57	
  3937	    58	def _schema_of(conn, table: str) -> Optional[str]:
  3938	    59	    row = conn.execute(
  3939	    60	        "SELECT schemaname FROM pg_tables "
  3940	    61	        "WHERE tablename = %s AND schemaname = ANY(%s) LIMIT 1",
  3941	    62	        (table, list(SEARCHED_SCHEMAS)),
  3942	    63	    ).fetchone()
  3943	    64	    return row[0] if row else None
  3944	    65	
  3945	    66	
  3946	    67	def _pk_columns(conn, schema: str, table: str) -> list[str]:
  3947	    68	    rows = conn.execute(
  3948	    69	        """
  3949	    70	        SELECT a.attname
  3950	    71	        FROM pg_index i
  3951	    72	        JOIN pg_attribute a
  3952	    73	          ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
  3953	    74	        WHERE i.indrelid = (quote_ident(%s) || '.' || quote_ident(%s))::regclass
  3954	    75	          AND i.indisprimary
  3955	    76	        ORDER BY array_position(i.indkey::int2[], a.attnum)
  3956	    77	        """,
  3957	    78	        (schema, table),
  3958	    79	    ).fetchall()
  3959	    80	    if not rows:
  3960	    81	        raise MigrationError(
  3961	    82	            f"{schema}.{table} has no primary key, so its rows cannot be put in a "
  3962	    83	            "deterministic order and no content digest can be taken. Every "
  3963	    84	            "new-core table has one; this is a real finding, not a tooling gap."
  3964	    85	        )
  3965	    86	    return [r[0] for r in rows]
  3966	    87	
  3967	    88	
  3968	    89	def _probe(conn, table: str) -> dict:
  3969	    90	    """(schema, rows, digest) for `table`, wherever it currently lives."""
  3970	    91	    schema = _schema_of(conn, table)
  3971	    92	    if schema is None:
  3972	    93	        return {"schema": None, "rows": None, "digest": None}
  3973	    94	    pk = _pk_columns(conn, schema, table)
  3974	    95	    query = sql.SQL(
  3975	    96	        "SELECT count(*), "
  3976	    97	        "md5(coalesce(string_agg((to_jsonb(t) - {tenancy})::text, '|' ORDER BY {order}), '')) "
  3977	    98	        "FROM {rel} AS t"
  3978	    99	    ).format(
  3979	   100	        tenancy=sql.Literal(TENANCY_COLUMN),
  3980	   101	        order=sql.SQL(", ").join(sql.Identifier("t", c) for c in pk),
  3981	   102	        rel=sql.Identifier(schema, table),
  3982	   103	    )
  3983	   104	    rows, digest = conn.execute(query).fetchone()
  3984	   105	    return {"schema": schema, "rows": int(rows), "digest": digest}
  3985	   106	
  3986	   107	
  3987	   108	def _probe_all(conn) -> dict[str, dict]:
  3988	   109	    tables = {**MOVED_TABLES, **SEEDED_TABLES}
  3989	   110	    return {t: _probe(conn, t) for t in sorted(tables)}
  3990	   111	
  3991	   112	
  3992	   113	def _print_proof(before: dict[str, dict], after: dict[str, dict]) -> int:
  3993	   114	    """Render the proof table. Returns the number of CHANGED digests."""
  3994	   115	    tables = {**MOVED_TABLES, **SEEDED_TABLES}
  3995	   116	    header = (
  3996	   117	        f"{'table':<20} {'side':<7} {'schema before -> after':<26} "
  3997	   118	        f"{'rows':<15} {'digest before -> after':<21} verdict"
  3998	   119	    )
  3999	   120	    print(header)
  4000	   121	    print("-" * len(header))
  4001	   122	    changed = 0
  4002	   123	    for name in sorted(tables):
  4003	   124	        b, a = before[name], after[name]
  4004	   125	        where = f"{b['schema'] or '-'} -> {a['schema'] or '-'}"
  4005	   126	        rows = f"{'-' if b['rows'] is None else b['rows']} -> " \
  4006	   127	               f"{'-' if a['rows'] is None else a['rows']}"
  4007	   128	        dig = f"{(b['digest'] or '-')[:8]} -> {(a['digest'] or '-')[:8]}"
  4008	   129	        if b["schema"] is None and a["schema"] is None:
  4009	   130	            verdict = "ABSENT"
  4010	   131	        elif b["digest"] == a["digest"] and b["rows"] == a["rows"]:
  4011	   132	            verdict = "OK"
  4012	   133	        elif b["schema"] is None:
  4013	   134	            verdict = "CREATED"
  4014	   135	        else:
  4015	
  4016	exec
  4017	/bin/zsh -lc "nl -ba src/cobalt/db_migrations/__init__.py; nl -ba src/cobalt/db_migrations/cli.py | sed -n '148,230p'; nl -ba src/cobalt/jobs/migrations/0001_cobalt_jobs.sql; rg -n 'def upsert_unit|class WriteResult|return WriteResult|changed|dry_run' src/cobalt/vaultwrite/writer.py | head -45; nl -ba src/cobalt/session/clock.py | sed -n '179,222p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
  4018	 succeeded in 0ms:
  4019	     1	"""The two-layer data model's migrations (ADR-0008).
  4020	     2	
  4021	     3	`0001_schemas.sql`  — schemas, roles, grants, ownership, `"user".traders`,
  4022	     4	                      the `cobalt.trader_id` GUC convention.
  4023	     5	`0002_move_tables.sql` — every new-core table onto its side, plus
  4024	     6	                      `user_id` on the user side.
  4025	     7	`0002_move_tables.rollback.sql` — the reverse, catalog-only.
  4026	     8	
  4027	     9	These are the DATABASE-WIDE migrations and they are the only ones that
  4028	    10	live outside a feature module. A module's own DDL still lives in its own
  4029	    11	`migrations/` directory and is still executed by its store's
  4030	    12	`ensure_schema()`; those files create tables UNQUALIFIED and land them in
  4031	    13	whichever schema the factory pinned on the connection.
  4032	    14	
  4033	    15	Run them with `cobalt db migrate` (`--allow-prod` from ~/cobalt only,
  4034	    16	`--rollback` to reverse 0002). Nothing runs them implicitly: a store's
  4035	    17	`ensure_schema()` asserts the schemas exist and tells you to run the CLI.
  4036	    18	"""
  4037	    19	
  4038	    20	from pathlib import Path
  4039	    21	
  4040	    22	MIGRATIONS_DIR = Path(__file__).parent
  4041	    23	
  4042	    24	#: Applied in this order, every time, both idempotent.
  4043	    25	FORWARD = (
  4044	    26	    MIGRATIONS_DIR / "0001_schemas.sql",
  4045	    27	    MIGRATIONS_DIR / "0002_move_tables.sql",
  4046	    28	)
  4047	    29	
  4048	    30	#: `--rollback`. 0001 is deliberately NOT reversed — see the file header.
  4049	    31	REVERSE = (MIGRATIONS_DIR / "0002_move_tables.rollback.sql",)
  4050	    32	
  4051	    33	__all__ = ["FORWARD", "MIGRATIONS_DIR", "REVERSE"]
  4052	   148	           else f"{changed} table(s) CHANGED — investigate before proceeding.")
  4053	   149	    )
  4054	   150	    return changed
  4055	   151	
  4056	   152	
  4057	   153	def _apply(conn, paths) -> None:
  4058	   154	    """Run whole .sql files, one transaction for the lot.
  4059	   155	
  4060	   156	    Each file is handed to the server ENTIRE rather than split on ';':
  4061	   157	    these migrations are DO blocks, and a splitter would cut them at the
  4062	   158	    first semicolon inside the body. psycopg uses the simple query
  4063	   159	    protocol when there are no parameters, which accepts multiple
  4064	   160	    statements — and the migrations take no parameters by design.
  4065	   161	    """
  4066	   162	    for path in paths:
  4067	   163	        print(f"-- applying {path.name}")
  4068	   164	        conn.execute(path.read_text())
  4069	   165	
  4070	   166	
  4071	   167	def cmd_migrate(args: argparse.Namespace) -> None:
  4072	   168	    dbname = db.PROD_DB_NAME if args.allow_prod else env.resolve_db_name()
  4073	   169	    direction = "ROLLBACK" if args.rollback else "FORWARD"
  4074	   170	    paths = REVERSE if args.rollback else FORWARD
  4075	   171	
  4076	   172	    print(f"cobalt db migrate — {direction} on {dbname}")
  4077	   173	    conn = db.connect_migration(dbname, allow_prod=args.allow_prod)
  4078	   174	    conn.autocommit = False
  4079	   175	    try:
  4080	   176	        before = _probe_all(conn)
  4081	   177	        _apply(conn, paths)
  4082	   178	        after = _probe_all(conn)
  4083	   179	        conn.commit()
  4084	   180	    except BaseException:
  4085	   181	        conn.rollback()
  4086	   182	        raise
  4087	   183	    finally:
  4088	   184	        conn.close()
  4089	   185	
  4090	   186	    print()
  4091	   187	    changed = _print_proof(before, after)
  4092	   188	    if changed:
  4093	   189	        raise MigrationError(
  4094	   190	            f"{changed} table(s) changed content across the migration. The "
  4095	   191	            "migration is committed; the proof is not clean — compare against the "
  4096	   192	            "pg_dump taken before this run."
  4097	   193	        )
  4098	   194	
  4099	   195	
  4100	   196	def add_parser(sub) -> None:
  4101	   197	    group = sub.add_parser("db", help="Database migrations (ADR-0008 two-layer model)")
  4102	   198	    gsub = group.add_subparsers(dest="command", required=True)
  4103	   199	
  4104	   200	    migrate = gsub.add_parser(
  4105	   201	        "migrate",
  4106	   202	        help="Create the system/\"user\" schemas and move every new-core table.",
  4107	   203	    )
  4108	   204	    migrate.add_argument(
  4109	   205	        "--allow-prod",
  4110	   206	        action="store_true",
  4111	   207	        help="Target cobalt_brain (run from ~/cobalt only, outside market hours).",
  4112	   208	    )
  4113	   209	    migrate.add_argument(
  4114	   210	        "--rollback",
  4115	   211	        action="store_true",
  4116	   212	        help="Reverse 0002: every table back to public, user_id dropped.",
  4117	   213	    )
  4118	   214	    migrate.set_defaults(func=cmd_migrate)
  4119	   215	
  4120	   216	
  4121	   217	__all__ = ["MigrationError", "add_parser", "cmd_migrate"]
  4122	     1	-- 0001: cobalt_jobs — F17's persisted row per scheduled job (Charter §3, L18).
  4123	     2	--
  4124	     3	-- WHY THE `cobalt_` PREFIX, when no other new-core table has one.
  4125	     4	-- `cobalt_brain` is the SAME Postgres database Mattermost uses: 129
  4126	     5	-- tables, of which 103 were Mattermost's (they moved to their own
  4127	     6	-- database on 2026-09-04, ADR-0006) — and one of them was called
  4128	     7	-- `jobs`, with 164,320 rows of `expiry_notify` / `delete_expired_posts`
  4129	     8	-- work items in it. `CREATE TABLE IF NOT EXISTS jobs` therefore did
  4130	     9	-- NOTHING, silently, and the first query failed with `column "label"
  4131	    10	-- does not exist` (found 2026-09-04 by the first production dry run —
  4132	    11	-- the fail-loud discipline is what surfaced it in seconds rather than
  4133	    12	-- in a week of green heartbeats reporting on Mattermost's table).
  4134	    13	--
  4135	    14	-- `jobs` and `kill_switch` are generic enough that a collision was
  4136	    15	-- always going to happen; the existing new-core tables (aset_sizings,
  4137	    16	-- vault_writes, card_transitions, day_modes, bars) are specific enough
  4138	    17	-- that none has one, and they are NOT renamed here — they hold live
  4139	    18	-- trading record and a rename is a migration, not a naming preference.
  4140	    19	-- New tables from this prompt take the prefix.
  4141	    20	--
  4142	    21	-- ONE ROW PER LAUNCHD LABEL, and the label is the join key everywhere:
  4143	    22	-- configs/cobalt/jobs.yaml, ops/*.plist, `launchctl list`, and the F18
  4144	    23	-- heartbeat all name the same string.
  4145	    24	--
  4146	    25	-- WHY THE COLUMNS ARE THESE COLUMNS:
  4147	    26	--   state/started_at/finished_at/exit_code/last_error  — what happened.
  4148	    27	--   heartbeat_at  — the ONLY thing that distinguishes a long job from a
  4149	    28	--                   hung one. Without it `running` means "started and did
  4150	    29	--                   not finish", which is true of both.
  4151	    30	--   expected_cadence — rendered from the schedule in jobs.yaml, so the
  4152	    31	--                   MISSED probe reads one place and an operator reading
  4153	    32	--                   this table sees when the job should have run.
  4154	    33	--   heartbeat_source — `self` | `launchd` | `pidfile`. Cobalt cannot run
  4155	    34	--                   a heartbeat thread inside Obsidian or LM Studio, so
  4156	    35	--                   the watchdog stamps for them from a real probe. The
  4157	    36	--                   column exists so that is VISIBLE rather than implied:
  4158	    37	--                   a probe saying "the process exists" and a process
  4159	    38	--                   saying "I am working" are different claims.
  4160	    39	--   last_result   — the run's own numbers, JSON. The archiver's rows
  4161	    40	--                   written land here, which is what makes F18's
  4162	    41	--                   "archiver freshness (last run + rows written)"
  4163	    42	--                   answerable without a second table.
  4164	    43	CREATE TABLE IF NOT EXISTS cobalt_jobs (
  4165	    44	    label TEXT PRIMARY KEY,
  4166	    45	    kind TEXT NOT NULL CHECK (kind IN ('resident', 'one-shot')),
  4167	    46	    expected_cadence TEXT,
  4168	    47	    timeout_s INTEGER NOT NULL CHECK (timeout_s > 0),
  4169	    48	    state TEXT NOT NULL DEFAULT 'pending'
  4170	    49	        CHECK (state IN ('pending', 'running', 'done', 'failed', 'zombie')),
  4171	    50	    heartbeat_source TEXT NOT NULL DEFAULT 'self'
  4172	    51	        CHECK (heartbeat_source IN ('self', 'launchd', 'pidfile')),
  4173	    52	    started_at TIMESTAMPTZ,
  4174	    53	    heartbeat_at TIMESTAMPTZ,
  4175	    54	    finished_at TIMESTAMPTZ,
  4176	    55	    exit_code INTEGER,
  4177	    56	    last_error TEXT,
  4178	    57	    last_result JSONB,
  4179	    58	    registered_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  4180	    59	    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
  4181	    60	);
  4182	    61	
  4183	    62	-- The kill switch (F17d). ONE row, id = TRUE, so there is exactly one
  4184	    63	-- answer to "is Cobalt stopped" and no way to have two.
  4185	    64	CREATE TABLE IF NOT EXISTS cobalt_kill_switch (
  4186	    65	    id BOOLEAN PRIMARY KEY DEFAULT TRUE CHECK (id),
  4187	    66	    active BOOLEAN NOT NULL DEFAULT FALSE,
  4188	    67	    phrase TEXT,
  4189	    68	    set_by TEXT,
  4190	    69	    set_at TIMESTAMPTZ,
  4191	    70	    cleared_by TEXT,
  4192	    71	    cleared_at TIMESTAMPTZ
  4193	    72	);
  4194	    73	
  4195	    74	INSERT INTO cobalt_kill_switch (id, active) VALUES (TRUE, FALSE) ON CONFLICT (id) DO NOTHING;
  4196	25:   same directory) behind an mtime+hash guard: if the file changed since
  4197	124:    """The note changed between the read this edit was computed from and
  4198	246:class WriteResult:
  4199	248:    action: str  # created | updated | unchanged | skipped_exists | skipped | restored
  4200	252:    dry_run: bool = False
  4201	266:    def changed(self) -> bool:
  4202	271:        head = f"[{'DRY-RUN' if self.dry_run else 'WRITE'}] {self.action}: {self.path}"
  4203	290:        parts.append(self.diff if self.diff else "  (no diff — nothing changed)")
  4204	326:# Actions that put (or would put) bytes on disk. "unchanged", "skipped"
  4205	335:    entry points rather than the ten `return WriteResult(...)` sites, so
  4206	357:        dry_run: bool = False,
  4207	364:        self.dry_run = dry_run
  4208	398:        if self.dry_run:
  4209	447:        if self._purged or self.store is None or self.dry_run:
  4210	466:                f"ABORT: {path} changed on disk between this run's read and its "
  4211	541:            if self.dry_run:
  4212	570:            return WriteResult(
  4213	573:                dry_run=self.dry_run,
  4214	588:        if self.dry_run:
  4215	589:            return WriteResult(
  4216	593:                dry_run=True,
  4217	612:        return WriteResult(
  4218	644:    def upsert_unit(
  4219	757:                state["unchanged"] = True
  4220	776:            return WriteResult(
  4221	778:                dry_run=self.dry_run, hash_before=snapshot.sha256,
  4222	783:            return WriteResult(
  4223	784:                path=path, action="unchanged", section=section, unit=unit_id,
  4224	785:                dry_run=self.dry_run, hash_before=snapshot.sha256,
  4225	791:        changed = new_text != (snapshot.text or "")
  4226	792:        return WriteResult(
  4227	794:            action="updated" if changed else "unchanged",
  4228	798:            dry_run=self.dry_run,
  4229	912:        Everything else L28 asks for still applies, unchanged: the same
  4230	976:            return WriteResult(
  4231	977:                path=path, action="unchanged", section=section_label, unit=region_id,
  4232	978:                dry_run=self.dry_run, hash_before=snapshot.sha256, hash_after=snapshot.sha256,
  4233	983:        changed = new_text != (snapshot.text or "")
  4234	984:        return WriteResult(
  4235	986:            action="updated" if changed else "unchanged",
  4236	990:            dry_run=self.dry_run,
  4237	1055:                f"written — {row['note']} has changed since. Restoring would "
  4238	1094:          the original whole-section replace, unchanged. Rows written
  4239	1255:            return WriteResult(
  4240	1256:                path=path, action="unchanged", section=section_name, unit=row["unit"],
  4241	   179	                    + ", ".join(f"{k}={self._b[k]:%H:%M}" for k in keys)
  4242	   180	                )
  4243	   181	        if self._b["session.market_reset_open"] != self._b["session.aftermarket_close"]:
  4244	   182	            # Not fatal — an early close already opens such a gap on
  4245	   183	            # purpose — but on a FULL day these two are the same instant
  4246	   184	            # by design, and a silent divergence would put an unnamed
  4247	   185	            # overnight sliver in the middle of the trading evening.
  4248	   186	            raise SessionError(
  4249	   187	                "session.market_reset_open "
  4250	   188	                f"({self._b['session.market_reset_open']:%H:%M}) must equal "
  4251	   189	                "session.aftermarket_close "
  4252	   190	                f"({self._b['session.aftermarket_close']:%H:%M}) — on a full "
  4253	   191	                "day market_reset begins the moment aftermarket ends"
  4254	   192	            )
  4255	   193	
  4256	   194	    # -- the day's shape ---------------------------------------------
  4257	   195	
  4258	   196	    def windows_for(self, day: date) -> list[Window]:
  4259	   197	        """The ordered [start, end) ET windows of `day`. Empty list = the
  4260	   198	        whole day is overnight (weekend or holiday)."""
  4261	   199	        if not self.calendar.is_trading_day(day):
  4262	   200	            return []
  4263	   201	
  4264	   202	        early = self.calendar.is_early_close(day)
  4265	   203	        rth_close = self._b[
  4266	   204	            "session.early_close.rth_close" if early else "session.rth_close"
  4267	   205	        ]
  4268	   206	        am_close = self._b[
  4269	   207	            "session.early_close.aftermarket_close" if early else "session.aftermarket_close"
  4270	   208	        ]
  4271	   209	        return [
  4272	   210	            Window(Session.PREMARKET, self._b["session.premarket_open"], self._b["session.rth_open"]),
  4273	   211	            Window(Session.RTH, self._b["session.rth_open"], rth_close),
  4274	   212	            Window(Session.AFTERMARKET, rth_close, am_close),
  4275	   213	            Window(
  4276	   214	                Session.MARKET_RESET,
  4277	   215	                self._b["session.market_reset_open"],
  4278	   216	                self._b["session.market_reset_close"],
  4279	   217	            ),
  4280	   218	        ]
  4281	   219	
  4282	   220	    # -- the two questions -------------------------------------------
  4283	   221	
  4284	   222	    def session(self, ts: datetime) -> Session:
  4285	
  4286	codex
  4287	Reviewed as a **build brief**: RESOLVED means the revised requirements address the finding; implementation is still pending.
  4288	
  4289	**Round-1 blockers**
  4290	
  4291	1. **RESOLVED — deployment and rollback.** Items 3 and 5 require replacing the invocation, bootout/bootstrap, registry updates explicitly described as “rows only,” and restoration of the previous plist. This addresses the registration/install confusion. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:8](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:8), [cli.py:63](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:63), [ops/README.md:3](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:3). The new migration procedure has a separate blocker below.
  4292	
  4293	2. **OPEN — empty `reads` fixed; restart derivation missing.** Item 3 correctly prohibits heartbeat `reads`, matching its one-shot declaration and validation. But item 5 hard-codes heartbeat’s reload without requiring reader analysis for every changed configuration or resolving unknown paths. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:8](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:8), [jobs.yaml:206](/Users/cobalt/cobalt-wt/heartbeat-mr/configs/cobalt/jobs.yaml:206), [config.py:290](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/config.py:290), [ops/README.md:175](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:175).
  4294	
  4295	3. **RESOLVED — result ownership.** Item 3 explicitly protects beat details and `green_summary_date`; item 4(e) requires verification after wrapper completion. Those requirements directly address subprocess result replacement. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:7](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:7), [cli.py:137](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:137), [store.py:162](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/store.py:162).
  4296	
  4297	4. **OPEN — durable degradation specified, late-failure notification unresolved.** Item 2 requires persisted outcomes and RED on failure, but item 1 selects alerts before the vault operation. An otherwise-green beat can send an all-clear—or nothing—then fail its vault write without sending a RED alert. Item 4(b)’s “alerts + row present” does not require an alert reporting that failure. Evidence: [brief:4](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:4), [brief:5](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:5), [brief:7](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:7), [runner.py:262](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:262).
  4298	
  4299	5. **RESOLVED — triage report supplied.** The input named at brief line 1 now exists. It documents four attempts each night, eight refusal records, and the unguarded write preceding alerts and persistence. Evidence: [triage:18](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/heartbeat-blackout-2026-09-10.md:18), [triage:33](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/heartbeat-blackout-2026-09-10.md:33), [runner.py:249](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:249). Incident evidence was reviewed from the report; production logs were not rechecked.
  4300	
  4301	**BLOCKERS**
  4302	
  4303	- **Still open: restart derivation and late-failure reporting**, above. Specify a post-vault finalization step that persists the final outcome, severity, and reason, and sends corrective RED notifications when needed. There is no existing persisted `notes/message` column: `Beat.notes` is in memory, and current result serialization omits it ([render.py:32](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/render.py:32), [runner.py:279](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:279)). Name its storage location explicitly.
  4304	- **New: F17 can prevent database-outage alerts before `run_beat` starts.** The wrapper performs schema setup, registration, and `mark_running` before yielding to the subprocess ([wrapper.py:133](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:133), [wrapper.py:142](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:142)). Isolating stages inside `run_beat` cannot catch these failures. Define heartbeat-specific behavior and test the wrapped entry point with database access failing before launch.
  4305	- **New: the migration command does not execute the proposed feature migration.** `cobalt db migrate` runs a fixed two-file list; feature migrations run through their stores ([db_migrations/__init__.py:9](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:9), [db_migrations/__init__.py:25](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:25)). Specify the actual forward/rollback execution path. Simply extending that list also needs proof handling: its digest excludes only `user_id`, so adding `vault_outcome` changes populated-row digests and produces an error **after commit** ([cli.py:96](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:96), [cli.py:187](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:187)).
  4306	
  4307	**RISKS**
  4308	
  4309	- Define missing-note behavior: `write_note_block` returns `None` without raising, so exception handling alone cannot justify `written` ([runner.py:137](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:137)).
  4310	- Add session-boundary and holiday coverage; market reset is calendar-dependent ([clock.py:196](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/session/clock.py:196)).
  4311	- LIVE acceptance should require GREEN **when other checks are healthy**. Deferral must preserve unrelated RED findings; refusal counts remain informational by design ([render.py:43](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/render.py:43), [probes.py:323](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/probes.py:323)).
  4312	
  4313	**VERDICT: RETHINK.** Close the notification, wrapper-startup, migration, and restart-analysis gaps before build. This was a static review; no tests or production actions were run.
  4314	tokens used
  4315	54,827
  4316	Reviewed as a **build brief**: RESOLVED means the revised requirements address the finding; implementation is still pending.
  4317	
  4318	**Round-1 blockers**
  4319	
  4320	1. **RESOLVED — deployment and rollback.** Items 3 and 5 require replacing the invocation, bootout/bootstrap, registry updates explicitly described as “rows only,” and restoration of the previous plist. This addresses the registration/install confusion. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:8](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:8), [cli.py:63](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:63), [ops/README.md:3](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:3). The new migration procedure has a separate blocker below.
  4321	
  4322	2. **OPEN — empty `reads` fixed; restart derivation missing.** Item 3 correctly prohibits heartbeat `reads`, matching its one-shot declaration and validation. But item 5 hard-codes heartbeat’s reload without requiring reader analysis for every changed configuration or resolving unknown paths. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:8](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:8), [jobs.yaml:206](/Users/cobalt/cobalt-wt/heartbeat-mr/configs/cobalt/jobs.yaml:206), [config.py:290](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/config.py:290), [ops/README.md:175](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:175).
  4323	
  4324	3. **RESOLVED — result ownership.** Item 3 explicitly protects beat details and `green_summary_date`; item 4(e) requires verification after wrapper completion. Those requirements directly address subprocess result replacement. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:7](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:7), [cli.py:137](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:137), [store.py:162](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/store.py:162).
  4325	
  4326	4. **OPEN — durable degradation specified, late-failure notification unresolved.** Item 2 requires persisted outcomes and RED on failure, but item 1 selects alerts before the vault operation. An otherwise-green beat can send an all-clear—or nothing—then fail its vault write without sending a RED alert. Item 4(b)’s “alerts + row present” does not require an alert reporting that failure. Evidence: [brief:4](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:4), [brief:5](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:5), [brief:7](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:7), [runner.py:262](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:262).
  4327	
  4328	5. **RESOLVED — triage report supplied.** The input named at brief line 1 now exists. It documents four attempts each night, eight refusal records, and the unguarded write preceding alerts and persistence. Evidence: [triage:18](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/heartbeat-blackout-2026-09-10.md:18), [triage:33](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/heartbeat-blackout-2026-09-10.md:33), [runner.py:249](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:249). Incident evidence was reviewed from the report; production logs were not rechecked.
  4329	
  4330	**BLOCKERS**
  4331	
  4332	- **Still open: restart derivation and late-failure reporting**, above. Specify a post-vault finalization step that persists the final outcome, severity, and reason, and sends corrective RED notifications when needed. There is no existing persisted `notes/message` column: `Beat.notes` is in memory, and current result serialization omits it ([render.py:32](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/render.py:32), [runner.py:279](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:279)). Name its storage location explicitly.
  4333	- **New: F17 can prevent database-outage alerts before `run_beat` starts.** The wrapper performs schema setup, registration, and `mark_running` before yielding to the subprocess ([wrapper.py:133](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:133), [wrapper.py:142](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:142)). Isolating stages inside `run_beat` cannot catch these failures. Define heartbeat-specific behavior and test the wrapped entry point with database access failing before launch.
  4334	- **New: the migration command does not execute the proposed feature migration.** `cobalt db migrate` runs a fixed two-file list; feature migrations run through their stores ([db_migrations/__init__.py:9](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:9), [db_migrations/__init__.py:25](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:25)). Specify the actual forward/rollback execution path. Simply extending that list also needs proof handling: its digest excludes only `user_id`, so adding `vault_outcome` changes populated-row digests and produces an error **after commit** ([cli.py:96](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:96), [cli.py:187](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:187)).
  4335	
  4336	**RISKS**
  4337	
  4338	- Define missing-note behavior: `write_note_block` returns `None` without raising, so exception handling alone cannot justify `written` ([runner.py:137](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:137)).
  4339	- Add session-boundary and holiday coverage; market reset is calendar-dependent ([clock.py:196](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/session/clock.py:196)).
  4340	- LIVE acceptance should require GREEN **when other checks are healthy**. Deferral must preserve unrelated RED findings; refusal counts remain informational by design ([render.py:43](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/render.py:43), [probes.py:323](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/probes.py:323)).
  4341	
  4342	**VERDICT: RETHINK.** Close the notification, wrapper-startup, migration, and restart-analysis gaps before build. This was a static review; no tests or production actions were run.
     1	=== BRIEF v3 (Sol) ===
     2	Worktree ~/cobalt-wt/heartbeat-mr, branch ops/heartbeat-market-reset. You cannot commit; leave the diff + report. No production paths (~/cobalt, ~/Vault, launchd) touched. Laws: fail loud; one path; fresh code. Inputs: the triage report heartbeat-blackout-2026-09-10.md (cause), _inflight/heartbeat-fix-astra.md, -r2.md and -r3.md (reviews). Every round-1/2 blocker maps to a numbered item below — cite the item per blocker in your report. Round 3 (-r3.md) is dissent: if it names a concrete file:line defect in this brief, fix it in the build and say so; otherwise record it as dissent, do not redesign.
     3	Cause: run_beat writes the daily-note unit unguarded at runner.py:249, upstream of alerts (:269-270) and the beat row (:291-292); F1's market_reset block (20:00–21:00 ET) raises SessionBlocked there and the whole beat dies — 4 beats/night, traceback only in logs/heartbeat.err. The heartbeat is the one job outside the F17 wrapper. probes.py:321 stays as is.
     4	Build:
     5	1. Stage order in run_beat: probes → compose → alerts (RED out-of-band; green DM under the existing green_summary_date dedup) → persist beat row → vault unit → FINALIZE. Every stage isolated: a failure is logged loud, recorded in the beat and never aborts later stages; alerts never depend on persistence. FINALIZE (r2 blocker 1): updates the persisted row with the vault result and, if the vault outcome is `failed`, sends a corrective RED alert out-of-band naming the reason — a beat can never end all-clear with a failed vault write.
     6	2. Vault step: session clock first (cobalt.session; boundary tests at 19:59/20:00/20:59/21:00 ET and a holiday — r2 risk). market_reset → no write attempt, outcome `deferred_market_reset`. Otherwise write; `written` ONLY when the writer returns a success result with a write id — a `None` return or any exception → `failed` with the reason (r2 risk). Persisted on the beat row as two nullable text columns: `vault_outcome` (`written | deferred_market_reset | failed`) and `vault_reason`. render.py reads them: `deferred_market_reset` leaves the beat's colour to the probes (never masks an unrelated RED — r2 risk); `failed` renders RED.
     7	3. Migration (r2 blocker 3): a new numbered file in db_migrations/ REGISTERED in the fixed list in db_migrations/__init__.py exactly as 0004 was, placement declared system side, rollback sql; the row digest in db_migrations/cli.py excludes the two new columns (or the digest scheme is versioned) — test proves populated-row digests are unchanged after the migration.
     8	4. F17 wrapper enrolment for com.cobalt.heartbeat: (i) wrapper writes ONLY its own fields, never beat detail or green_summary_date (r1 blocker 3); (ii) kill-switch exemption via a validated per-job JobSpec flag, default false, true only for the heartbeat; the beat reports the switch state; (iii) heartbeat-only rule (r2 blocker 2): wrapper bookkeeping (schema setup, registration, mark_running) is best-effort for this job — any failure there is logged loud and the beat subprocess STILL runs; its own DB probe then reports the outage out-of-band; (iv) the new plist in ops/ replaces the current invocation per ops/README, never side by side; NO `reads:` (one-shot).
     9	5. Tests: (a) market_reset → alerts, row with `deferred_market_reset`, ZERO write attempts, zero new session_blocks rows for actor `vaultwrite:heartbeat:*`; (b) vault exception or None outside the window → `failed`, RED, corrective RED alert sent, row present; (c) any stage's exception never suppresses later stages; (d) registry/plist parity + flag validation; (e) wrapped run leaves beat detail + green_summary_date intact; (f) wrapper bookkeeping failure → beat subprocess still runs; (g) boundary + holiday clock cases; (h) migration registered, rollback works, digests unchanged. Full suite green; `uv run cobalt validate` exit 0.
    10	6. Report docs/40 - DevDocs/reports/heartbeat-fix-2026-09-10.md: changes, which review item each answers, DISSENT section quoting anything from -r3.md not adopted with one line why, test results, and RESTARTS derived by RULE (r2 blocker 4): every plist under ops/ present in `git diff --stat main` + every resident whose `reads:` names a changed file — print the derivation, expected result `RESTARTS: com.cobalt.heartbeat (plist changed: bootout old, bootstrap new)`. LIVE block as named steps: (1) after ff-only merge, `cobalt db migrate --allow-prod` (two nullable columns; rollback sql named); (2) plist install per ops/README; (3) `cobalt jobs register` (rows only); (4) force one beat; proof = row shows `vault_outcome=written`, wrapper fields present, beat fields + green_summary_date intact, log shows the stage order incl. FINALIZE; no DM expected (dedup); (5) tonight: the FIRST beat after 20:00 (900 s interval, minute not guaranteed) shows `deferred_market_reset`, colour from probes, and the count of session_blocks rows for actor `vaultwrite:heartbeat:*` does not grow. Rollback: `git revert`, reinstall the previous plist, migration rollback sql. Print DONE as the last line.
    11	=== END BRIEF ===

exec
/bin/zsh -lc 'rg --files src/cobalt/heartbeat src/cobalt/jobs db_migrations; git status --short; rg --files --hidden -g AGENTS.md docs src db_migrations configs ops' in /Users/cobalt/cobalt-wt/heartbeat-mr
 exited 2 in 0ms:
rg: db_migrations: No such file or directory (os error 2)
src/cobalt/jobs/cli.py
src/cobalt/jobs/entrypoint.py
src/cobalt/jobs/__init__.py
src/cobalt/jobs/watchdog.py
src/cobalt/jobs/models.py
src/cobalt/jobs/config.py
src/cobalt/jobs/wrapper.py
src/cobalt/heartbeat/probes.py
src/cobalt/heartbeat/cli.py
src/cobalt/heartbeat/__init__.py
src/cobalt/heartbeat/render.py
src/cobalt/heartbeat/runner.py
src/cobalt/jobs/killswitch.py
src/cobalt/jobs/store.py
src/cobalt/jobs/migrations/0001_cobalt_jobs.sql
?? "docs/40 - DevDocs/reports/_inflight/"
?? "docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md"
rg: db_migrations: No such file or directory (os error 2)

exec
/bin/zsh -lc 'nl -ba src/cobalt/heartbeat/runner.py; nl -ba src/cobalt/heartbeat/render.py; nl -ba src/cobalt/heartbeat/cli.py' in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
     1	"""F18 heartbeat host — the beat itself (Charter §3 F18, M10).
     2	
     3	    uv run cobalt heartbeat beat
     4	
     5	WHAT ONE BEAT DOES, in order:
     6	
     7	1. probes everything (`probes.py`) and sweeps every job row
     8	   (`jobs.watchdog`);
     9	2. writes a Cobalt-owned red/green block into TODAY'S daily note through
    10	   `VaultWriter` — one L28 unit, updated in place, one diff per beat;
    11	3. on red, sends the SECOND channel first (email, over Layer-B Google
    12	   OAuth — `out_of_band` below), so that its outcome can appear in the
    13	   DM;
    14	4. DMs on any red — carrying "email channel DOWN: <reason>" when the
    15	   second channel failed — plus one green summary a day at
    16	   `heartbeat.green_summary_at`. The GREEN summary is DM-only: a daily
    17	   all-clear in the alert inbox is how an alert inbox stops being read.
    18	
    19	THE ALERT PATH IS NOT THE MONITORED PATH (Charter §3 F18). The DM goes
    20	over Mattermost, which is one of the things being watched — so a
    21	Mattermost outage would take the alert about the Mattermost outage with
    22	it. That is the whole reason F18 asks for a second channel, and since
    23	S1-P4 that channel exists: `cobalt.notify.email`, whose docstring states
    24	the exact dependency chain. It needs neither Mattermost, nor Postgres,
    25	nor the Obsidian vault. The `email` probe watches the watcher.
    26	
    27	WHY THE BEAT NEVER RAISES ON A RED. A red heartbeat is the heartbeat
    28	WORKING. It exits 0 and says RED loudly; it exits non-zero only when the
    29	beat itself could not run, because a job row that flips to `failed` every
    30	time something else is down would make the heartbeat's own history
    31	useless.
    32	"""
    33	
    34	from __future__ import annotations
    35	
    36	from datetime import datetime, time, timedelta
    37	from typing import Optional
    38	
    39	from loguru import logger
    40	
    41	from cobalt.jobs.store import JobStore
    42	from cobalt.jobs.watchdog import sweep
    43	from cobalt.session import clock as clock_mod
    44	from cobalt.session.clock import session_clock
    45	
    46	from . import probes as probe_mod
    47	from .render import SECTION, UNIT, WRITER, Beat
    48	
    49	JOB_LABEL = "com.cobalt.heartbeat"
    50	INTERVAL_KEY = "heartbeat.interval_min"
    51	GREEN_SUMMARY_KEY = "heartbeat.green_summary_at"
    52	
    53	
    54	def interval_min() -> int:
    55	    from cobalt.taxonomy.loader import load_tunables
    56	
    57	    row = load_tunables().by_key.get(INTERVAL_KEY)
    58	    if row is None:
    59	        raise RuntimeError(
    60	            f"tunable {INTERVAL_KEY!r} is missing from tunables.yaml — the heartbeat "
    61	            "reads its own cadence from config and has no built-in default (F16). "
    62	            "This is the number every 'red within one interval' claim is measured "
    63	            "against."
    64	        )
    65	    return int(row.value)
    66	
    67	
    68	def green_summary_at() -> time:
    69	    from cobalt.taxonomy.loader import load_tunables
    70	
    71	    row = load_tunables().by_key.get(GREEN_SUMMARY_KEY)
    72	    if row is None:
    73	        raise RuntimeError(f"tunable {GREEN_SUMMARY_KEY!r} is missing from tunables.yaml (F16).")
    74	    hh, _, mm = str(row.value).partition(":")
    75	    return time(int(hh), int(mm))
    76	
    77	
    78	# ---------------------------------------------------------------------
    79	# 1. probe
    80	# ---------------------------------------------------------------------
    81	
    82	
    83	def take_beat(*, now: Optional[datetime] = None, probe: bool = True) -> Beat:
    84	    """Every probe and every job row. Never raises on a red."""
    85	    ts = now or clock_mod.now_utc()
    86	    beat = Beat(at=session_clock().to_et(ts))
    87	
    88	    beat.probes = [
    89	        probe_mod.database(),
    90	        probe_mod.sheet_http(),
    91	        # Right after `sheet_http`, and a separate line on purpose: "the
    92	        # server is up" and "the page will take a card" are different
    93	        # facts, and on 2026-09-09 they disagreed for thirteen hours
    94	        # while the beat stayed green.
    95	        probe_mod.sheet_daymode(),
    96	        probe_mod.obsidian(),
    97	        probe_mod.mainframe(),
    98	        probe_mod.herdr(),
    99	        probe_mod.archiver_freshness(now=ts),
   100	        probe_mod.seat_usage(now=ts),
   101	        probe_mod.backup_freshness(now=ts),
   102	        probe_mod.vaultwrite_blocks(now=ts),
   103	        probe_mod.redactions(interval_min(), now=ts),
   104	        probe_mod.email(),
   105	    ]
   106	    try:
   107	        beat.jobs = sweep(now=ts, probe=probe)
   108	    except Exception as e:  # noqa: BLE001 - a broken sweep is its own red
   109	        beat.probes.append(
   110	            probe_mod.Probe(
   111	                "job sweep", False,
   112	                f"the watchdog itself FAILED ({type(e).__name__}: {e}) — every job's "
   113	                "state is UNKNOWN, which is not the same as green",
   114	                unknown=True,
   115	            )
   116	        )
   117	    return beat
   118	
   119	
   120	# ---------------------------------------------------------------------
   121	# 2. the daily-note block (Output 1)
   122	# ---------------------------------------------------------------------
   123	
   124	
   125	def write_note_block(beat: Beat, *, dry_run: bool = False):
   126	    """One L28 unit in today's note, updated in place — one diff a beat.
   127	
   128	    Returns the `WriteResult`, or None when there is no note yet. A
   129	    missing note is NOT created from here (L28.1: only
   130	    `create_if_absent` with a template may), and the 05:15 prefill is
   131	    what creates the day's note.
   132	    """
   133	    from cobalt.daymode.note import daily_note_path
   134	    from cobalt.vaultwrite import VaultWriter, VaultWriteStore
   135	
   136	    path = daily_note_path(beat.at.date())
   137	    if not path.exists():
   138	        logger.error(
   139	            "heartbeat: {} does not exist — the status block was NOT written. The "
   140	            "05:15 prefill creates the day's note; this writer never does (L28.1).",
   141	            path,
   142	        )
   143	        return None
   144	    store = VaultWriteStore()
   145	    store.ensure_schema()
   146	    writer = VaultWriter(WRITER, store=store, dry_run=dry_run)
   147	    return writer.upsert_unit(path, SECTION, UNIT, beat.note_body())
   148	
   149	
   150	# ---------------------------------------------------------------------
   151	# 3/4. the alert channels (Outputs 2 and 3)
   152	# ---------------------------------------------------------------------
   153	
   154	
   155	def should_send_green(beat: Beat, store: JobStore) -> bool:
   156	    """One green summary a day, at `heartbeat.green_summary_at`.
   157	
   158	    "Have we already sent today's?" is answered from the JOB ROW's own
   159	    `last_result` rather than from a new table — the heartbeat is the
   160	    only writer of that row, and a second table to remember one boolean a
   161	    day is a table to migrate later for nothing.
   162	    """
   163	    if beat.at.time() < green_summary_at():
   164	        return False
   165	    row = store.get(JOB_LABEL) or {}
   166	    last = (row.get("last_result") or {}).get("green_summary_date")
   167	    return last != beat.at.date().isoformat()
   168	
   169	
   170	def send_dm(beat: Beat) -> str:
   171	    from cobalt.notify import MattermostError, send_dm as _send
   172	
   173	    try:
   174	        result = _send(beat.dm_body())
   175	    except MattermostError as e:
   176	        # The alert path failing is itself worth saying, in the note and
   177	        # in the log — it is the one failure the DM cannot report.
   178	        logger.error("heartbeat: Mattermost DM FAILED — {}", e)
   179	        return f"Mattermost DM FAILED: {e}"
   180	    logger.info("heartbeat: {}", result.report())
   181	    return result.report()
   182	
   183	
   184	def out_of_band(beat: Beat) -> str:
   185	    """Charter §3 F18's SECOND channel — email, over Layer-B Google OAuth.
   186	
   187	    Built at S1-P4 (2026-09-08). Until then this function existed only to
   188	    say, loudly and on every red, that the channel did NOT exist; the
   189	    honest placeholder is in the git history and its S1-P3 reasoning is
   190	    unchanged — alerting that stops at Mattermost is alerting that shares
   191	    a fate with one of the things it watches.
   192	
   193	    THIS RUNS BEFORE `send_dm`, and the order is the whole point. The DM
   194	    is the channel that can carry a report ABOUT the email channel; the
   195	    email channel cannot carry a report about itself. So the second
   196	    channel goes first, and its outcome — including "email channel DOWN:
   197	    <reason>" — is appended to the beat's notes in time for
   198	    `beat.dm_body()` to render it.
   199	
   200	    NEVER RAISES. A failure here is a note, not a crash: a beat that died
   201	    trying to send the backup alert would take the primary alert with it,
   202	    which is the exact coupling this channel exists to break.
   203	    """
   204	    from cobalt.notify import EmailError, record_attempt, send_email
   205	    from cobalt.notify.config import load_notify_config
   206	
   207	    try:
   208	        cfg = load_notify_config().email
   209	    except Exception as e:  # noqa: BLE001
   210	        reason = f"notify config unreadable ({type(e).__name__}: {e})"
   211	        logger.error("heartbeat: email channel DOWN — {}", reason)
   212	        return f"email channel DOWN: {reason}"
   213	
   214	    subject = f"{beat.headline} · {beat.at:%Y-%m-%d %H:%M %Z}"
   215	    try:
   216	        result = send_email(cfg.to, subject, beat.dm_body())
   217	    except EmailError as e:
   218	        # `EmailError`'s message is redacted BY CONTRACT, so it is safe to
   219	        # put straight into a Mattermost DM — which is exactly where it is
   220	        # about to go.
   221	        record_attempt(ok=False, caller="heartbeat", detail=str(e))
   222	        logger.error("heartbeat: email channel DOWN — {}", e)
   223	        return f"email channel DOWN: {e}"
   224	
   225	    record_attempt(
   226	        ok=result.sent, caller="heartbeat", detail=result.detail, message_id=result.ref
   227	    )
   228	    if not result.sent:
   229	        # A disabled channel is deliberate, not an outage — but the DM
   230	        # still says so, because "no email arrived" must never be
   231	        # ambiguous between "off" and "broken".
   232	        logger.warning("heartbeat: {}", result.report())
   233	        return f"email channel OFF: {result.detail}"
   234	    logger.info("heartbeat: {}", result.report())
   235	    return result.report()
   236	
   237	
   238	# ---------------------------------------------------------------------
   239	# the beat
   240	# ---------------------------------------------------------------------
   241	
   242	
   243	def run_beat(*, now: Optional[datetime] = None, dry_run: bool = False, probe: bool = True) -> Beat:
   244	    """One whole heartbeat. Returns the Beat; never raises on a red."""
   245	    store = JobStore()
   246	    store.ensure_schema()
   247	    beat = take_beat(now=now, probe=probe)
   248	
   249	    write = write_note_block(beat, dry_run=dry_run)
   250	    if write is None:
   251	        beat.notes.append("Daily note: NOT WRITTEN — today's note does not exist yet.")
   252	    else:
   253	        # L28.4: the unified diff goes in the RUN REPORT, every time. The
   254	        # heartbeat writes to the live vault every 15 minutes; a write
   255	        # path that reported only "updated" would be the one write path
   256	        # in this codebase whose changes nobody could read back.
   257	        beat.notes.append(write.report())
   258	
   259	    sent_green = False
   260	    if dry_run:
   261	        beat.notes.append("DRY RUN — no DM sent, nothing written.")
   262	    elif not beat.green:
   263	        # OUT-OF-BAND FIRST. The DM's body is rendered from `beat.notes`,
   264	        # so the email outcome has to be in the list before `send_dm`
   265	        # reads it — that is what puts "email channel DOWN: <reason>" in
   266	        # the red DM. The reverse order would report the email result
   267	        # only to the log, where a failed second channel would be
   268	        # discovered by whoever went looking, which is nobody.
   269	        beat.notes.append(out_of_band(beat))
   270	        beat.notes.append(send_dm(beat))
   271	    elif should_send_green(beat, store):
   272	        beat.notes.append(send_dm(beat))
   273	        sent_green = True
   274	
   275	    if not dry_run:
   276	        # The heartbeat records ITS OWN run like any other job — it is the
   277	        # one job nobody else is watching, so it watches itself and a
   278	        # stalled heartbeat shows up as its own MISSED row.
   279	        result = {
   280	            "green": beat.green,
   281	            "red_jobs": [j.label for j in beat.red_jobs],
   282	            "red_probes": [p.name for p in beat.red_probes],
   283	        }
   284	        prior = (store.get(JOB_LABEL) or {}).get("last_result") or {}
   285	        result["green_summary_date"] = (
   286	            beat.at.date().isoformat() if sent_green else prior.get("green_summary_date")
   287	        )
   288	        store.register_all(__import__(
   289	            "cobalt.jobs.config", fromlist=["load_job_registry"]
   290	        ).load_job_registry())
   291	        store.mark_running(JOB_LABEL, now=now or clock_mod.now_utc())
   292	        store.mark_finished(JOB_LABEL, exit_code=0, result=result, now=now or clock_mod.now_utc())
   293	
   294	    (logger.info if beat.green else logger.error)("heartbeat: {}", beat.headline)
   295	    return beat
   296	
   297	
   298	__all__ = [
   299	    "GREEN_SUMMARY_KEY",
   300	    "INTERVAL_KEY",
   301	    "JOB_LABEL",
   302	    "green_summary_at",
   303	    "interval_min",
   304	    "out_of_band",
   305	    "run_beat",
   306	    "take_beat",
   307	    "write_note_block",
   308	]
     1	"""F18's block — what he reads, in the note and in the DM.
     2	
     3	ONE RENDERER, two destinations. The daily-note block and the Mattermost
     4	DM are the same text: a heartbeat whose two channels could disagree is a
     5	heartbeat you have to check twice.
     6	"""
     7	
     8	from __future__ import annotations
     9	
    10	from dataclasses import dataclass, field
    11	from datetime import datetime
    12	from typing import Optional
    13	
    14	from cobalt.jobs.watchdog import Finding
    15	
    16	from .probes import Probe
    17	
    18	#: The L28 unit this writes. Section + stable id: same id every beat, so
    19	#: it updates in place and the note never accumulates 96 blocks a day.
    20	SECTION = "heartbeat"
    21	UNIT = "status"
    22	WRITER = "heartbeat"
    23	
    24	
    25	@dataclass
    26	class Beat:
    27	    """One heartbeat's whole result."""
    28	
    29	    at: datetime
    30	    probes: list[Probe] = field(default_factory=list)
    31	    jobs: list[Finding] = field(default_factory=list)
    32	    notes: list[str] = field(default_factory=list)
    33	
    34	    @property
    35	    def red_probes(self) -> list[Probe]:
    36	        return [p for p in self.probes if not p.ok]
    37	
    38	    @property
    39	    def red_jobs(self) -> list[Finding]:
    40	        return [j for j in self.jobs if not j.ok]
    41	
    42	    @property
    43	    def green(self) -> bool:
    44	        return not self.red_probes and not self.red_jobs
    45	
    46	    @property
    47	    def headline(self) -> str:
    48	        if self.green:
    49	            return (
    50	                f"GREEN — {len(self.jobs)} job(s), {len(self.probes)} probe(s), "
    51	                "nothing red"
    52	            )
    53	        parts = []
    54	        if self.red_jobs:
    55	            parts.append(f"{len(self.red_jobs)} job(s)")
    56	        if self.red_probes:
    57	            parts.append(f"{len(self.red_probes)} probe(s)")
    58	        return f"RED — {' and '.join(parts)}"
    59	
    60	    # -- the two renderings -------------------------------------------
    61	
    62	    def note_body(self) -> str:
    63	        """The daily-note unit. Markdown, deterministic, no LLM (L28)."""
    64	        mark = "🟢" if self.green else "🔴"
    65	        lines = [
    66	            f"{mark} **HEARTBEAT {self.headline}** · {self.at:%Y-%m-%d %H:%M:%S %Z}",
    67	            "",
    68	            "| | check | detail |",
    69	            "|---|---|---|",
    70	        ]
    71	        for probe in self.probes:
    72	            icon = "🟢" if probe.ok else ("⚪" if probe.unknown else "🔴")
    73	            lines.append(f"| {icon} | {probe.name} | {_cell(probe.detail)} |")
    74	        for job in self.jobs:
    75	            icon = "🟢" if job.ok else "🔴"
    76	            lines.append(f"| {icon} | `{job.label}` | {job.state} — {_cell(job.detail)} |")
    77	        for note in self.notes:
    78	            lines += ["", f"> {note}"]
    79	        return "\n".join(lines)
    80	
    81	    def dm_body(self) -> str:
    82	        """The Mattermost DM. Plain lines — a table in a DM is unreadable
    83	        on a phone, and the phone is where a red alert is actually read."""
    84	        head = ("🟢 " if self.green else "🔴 ") + f"COBALT HEARTBEAT {self.headline}"
    85	        lines = [head, f"{self.at:%Y-%m-%d %H:%M:%S %Z}", ""]
    86	        if self.green:
    87	            lines.append(
    88	                f"{len(self.jobs)} jobs and {len(self.probes)} probes all green."
    89	            )
    90	        else:
    91	            lines.append("RED:")
    92	            for item in [*self.red_jobs, *self.red_probes]:
    93	                name = getattr(item, "label", None) or item.name
    94	                detail = item.detail
    95	                lines.append(f"  • {name}: {detail}")
    96	            lines.append("")
    97	            lines.append("Green:")
    98	            for probe in self.probes:
    99	                if probe.ok:
   100	                    lines.append(f"  • {probe.name}: {probe.detail}")
   101	        for note in self.notes:
   102	            lines += ["", note]
   103	        return "\n".join(lines)
   104	
   105	    def console(self) -> str:
   106	        lines = [f"HEARTBEAT {self.headline}  ({self.at:%Y-%m-%d %H:%M:%S %Z})", ""]
   107	        lines += [p.line() for p in self.probes]
   108	        lines += [j.line() for j in self.jobs]
   109	        lines += ["", *self.notes]
   110	        return "\n".join(lines)
   111	
   112	
   113	def _cell(text: str) -> str:
   114	    """A markdown table cell cannot contain a raw pipe or a newline."""
   115	    return text.replace("|", "\\|").replace("\n", " ").strip()
   116	
   117	
   118	__all__ = ["SECTION", "UNIT", "WRITER", "Beat"]
     1	"""`cobalt heartbeat` — F18's command surface.
     2	
     3	    cobalt heartbeat beat [--dry-run]     one beat (launchd runs this)
     4	    cobalt heartbeat show                 probe and print, send nothing
     5	
     6	`beat` is what `com.cobalt.heartbeat` runs every `heartbeat.interval_min`
     7	minutes. It EXITS 0 on a red: a red heartbeat is the heartbeat working,
     8	and a job row that flipped to `failed` every time something else was down
     9	would make the heartbeat's own history useless. It exits non-zero only
    10	when the beat itself could not run.
    11	"""
    12	
    13	from __future__ import annotations
    14	
    15	import argparse
    16	import sys
    17	
    18	from cobalt import env
    19	
    20	from .runner import run_beat, take_beat
    21	
    22	
    23	def cmd_beat(args: argparse.Namespace) -> None:
    24	    from cobalt.redact import install_log_guard
    25	
    26	    install_log_guard()
    27	    beat = run_beat(dry_run=args.dry_run)
    28	    print(f"database: {env.resolve_db_name()}  (COBALT_ENV={env.resolve_env()})")
    29	    print(beat.console())
    30	
    31	
    32	def cmd_show(args: argparse.Namespace) -> None:
    33	    """Probe and print. Writes nothing, sends nothing."""
    34	    print(take_beat().console())
    35	
    36	
    37	def add_parser(sub) -> None:
    38	    hb = sub.add_parser("heartbeat", help="F18 heartbeat host (Charter §3 F18)")
    39	    hsub = hb.add_subparsers(dest="command", required=True)
    40	
    41	    beat = hsub.add_parser("beat", help="One beat: probe, write the note block, alert.")
    42	    beat.add_argument("--dry-run", action="store_true", help="Probe and print; send/write nothing.")
    43	    beat.set_defaults(func=cmd_beat)
    44	
    45	    show = hsub.add_parser("show", help="Probe and print. Writes nothing, sends nothing.")
    46	    show.set_defaults(func=cmd_show)
    47	
    48	
    49	__all__ = ["add_parser"]

exec
/bin/zsh -lc 'nl -ba src/cobalt/jobs/wrapper.py; nl -ba src/cobalt/jobs/cli.py; nl -ba src/cobalt/jobs/store.py' in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
     1	"""F17b: the wrapper every scheduled job runs inside.
     2	
     3	Charter §3 F17: "marks running/done/failed with exit code and stamps
     4	heartbeat_at at least every timeout_s/3 for long jobs."
     5	
     6	TWO WAYS IN, one implementation:
     7	
     8	    # a Python entry point (prefill, archiver, cards-expire, …)
     9	    with job_run("com.cobalt.archiver") as run:
    10	        summary = do_the_work()
    11	        run.result = {"rows_written": summary.rows_written}
    12	
    13	    # anything else, from a plist
    14	    uv run cobalt jobs run com.cobalt.prefill-daily -- uv run prefill daily
    15	
    16	WHAT IT GUARANTEES, in order:
    17	
    18	1. THE KILL SWITCH IS CHECKED FIRST. A stopped Cobalt does not start a
    19	   one-shot at all — and it exits 0, not 1, because a deliberate stop is
    20	   not a failure and must not paint F18 red.
    21	2. `running` is marked before the work, with `started_at`.
    22	3. A BEATER THREAD stamps `heartbeat_at` every `timeout_s /
    23	   jobs.heartbeat_fraction` (5 min for the 15-min archiver window). This
    24	   is the ONLY thing that distinguishes a long job from a hung one — the
    25	   archiver legitimately runs 23 minutes, so "started and did not
    26	   finish" cannot be the zombie test.
    27	4. `done` (exit 0) or `failed` (exit code + the exception, redacted
    28	   through F19 on the way into the column) — and `failed` is LOUD.
    29	5. The exception is RE-RAISED. The wrapper reports; it never swallows.
    30	
    31	The beater thread is a daemon: if the job process dies hard, the thread
    32	dies with it, `heartbeat_at` stops advancing, and the watchdog draws the
    33	right conclusion. A thread that outlived its job would keep a dead job
    34	looking alive, which is the exact failure this feature exists to catch.
    35	"""
    36	
    37	from __future__ import annotations
    38	
    39	import threading
    40	import traceback
    41	from contextlib import contextmanager
    42	from typing import Any, Optional
    43	
    44	from loguru import logger
    45	
    46	from . import killswitch
    47	from .config import JobSpec, load_job_registry
    48	from .store import JobStore
    49	
    50	#: The tunables row governing how often a long job stamps (F16).
    51	HEARTBEAT_FRACTION_KEY = "jobs.heartbeat_fraction"
    52	
    53	#: Exit code a job uses when the kill switch turned it away. ZERO, on
    54	#: purpose — see guarantee 1.
    55	STOPPED_EXIT_CODE = 0
    56	
    57	
    58	class JobStopped(RuntimeError):
    59	    """The kill switch is engaged; this run did not happen."""
    60	
    61	
    62	def heartbeat_fraction() -> int:
    63	    from cobalt.taxonomy.loader import load_tunables
    64	
    65	    row = load_tunables().by_key.get(HEARTBEAT_FRACTION_KEY)
    66	    if row is None:
    67	        raise RuntimeError(
    68	            f"tunable {HEARTBEAT_FRACTION_KEY!r} is missing from tunables.yaml — the "
    69	            "wrapper reads its stamp interval from config and has no built-in "
    70	            "default (F16)."
    71	        )
    72	    return int(row.value)
    73	
    74	
    75	class _Beater:
    76	    """Stamps `heartbeat_at` on a timer until the run ends."""
    77	
    78	    def __init__(self, store: JobStore, label: str, every_s: float):
    79	        self.store = store
    80	        self.label = label
    81	        self.every_s = max(1.0, every_s)
    82	        self._stop = threading.Event()
    83	        self._thread = threading.Thread(
    84	            target=self._loop, name=f"beat:{label}", daemon=True
    85	        )
    86	
    87	    def _loop(self) -> None:
    88	        while not self._stop.wait(self.every_s):
    89	            try:
    90	                self.store.beat(self.label)
    91	            except Exception as e:  # noqa: BLE001
    92	                # A missed stamp is not a reason to kill the job. It IS a
    93	                # reason to say so: the watchdog may conclude ZOMBIE from
    94	                # this, and an operator needs the other half of the story.
    95	                logger.error(
    96	                    "F17: heartbeat stamp FAILED for {} ({}: {}) — the job is still "
    97	                    "running; the watchdog may see a stale heartbeat.",
    98	                    self.label, type(e).__name__, e,
    99	                )
   100	
   101	    def __enter__(self) -> "_Beater":
   102	        self._thread.start()
   103	        return self
   104	
   105	    def __exit__(self, *exc) -> None:
   106	        self._stop.set()
   107	
   108	
   109	class JobRun:
   110	    """Handle a wrapped job can hang its result on."""
   111	
   112	    def __init__(self, spec: JobSpec):
   113	        self.spec = spec
   114	        self.label = spec.label
   115	        #: Whatever the run wants F18 to be able to report — the
   116	        #: archiver's `rows_written` is what makes "archiver freshness
   117	        #: (last run + rows written)" answerable.
   118	        self.result: Optional[dict[str, Any]] = None
   119	
   120	
   121	@contextmanager
   122	def job_run(
   123	    label: str,
   124	    *,
   125	    store: Optional[JobStore] = None,
   126	    register: bool = True,
   127	    allow_prod: bool = False,
   128	):
   129	    """Run a block as a registered job. See the module docstring."""
   130	    registry = load_job_registry()
   131	    spec = registry.spec(label)
   132	    store = store or JobStore()
   133	    store.ensure_schema(allow_prod=allow_prod)
   134	    if register:
   135	        store.register(spec, allow_prod=allow_prod)
   136	
   137	    if killswitch.is_active(store):
   138	        state = killswitch.read(store)
   139	        logger.error("F17: {} REFUSED TO START — {}", label, state.describe())
   140	        raise JobStopped(state.describe())
   141	
   142	    store.mark_running(label)
   143	    run = JobRun(spec)
   144	    every_s = spec.timeout_s / heartbeat_fraction()
   145	    logger.info(
   146	        "F17: {} RUNNING (timeout {}s, heartbeat every {:.0f}s)",
   147	        label, spec.timeout_s, every_s,
   148	    )
   149	    try:
   150	        with _Beater(store, label, every_s):
   151	            yield run
   152	    except BaseException as e:
   153	        store.mark_finished(
   154	            label,
   155	            exit_code=1,
   156	            error=f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=8)}",
   157	            result=run.result,
   158	        )
   159	        logger.error("F17: {} FAILED — {}: {}", label, type(e).__name__, e)
   160	        raise            # the wrapper reports; it never swallows
   161	    store.mark_finished(label, exit_code=0, result=run.result)
   162	    logger.info("F17: {} DONE", label)
   163	
   164	
   165	def should_keep_running(label: str, *, store: Optional[JobStore] = None) -> bool:
   166	    """A RESIDENT's own loop check. `False` means exit cleanly now.
   167	
   168	    Residents call this where they can stop without tearing out of a
   169	    write. Cobalt's residents today are supervised by launchd rather than
   170	    wrapped (see jobs.yaml), so this exists for the first new-core
   171	    resident — the S2 radar poller — and for anything the chief of staff
   172	    grows into.
   173	    """
   174	    if killswitch.is_active(store):
   175	        logger.error(
   176	            "F17: kill switch engaged — {} is exiting cleanly at its next safe point.",
   177	            label,
   178	        )
   179	        return False
   180	    return True
   181	
   182	
   183	__all__ = [
   184	    "HEARTBEAT_FRACTION_KEY",
   185	    "STOPPED_EXIT_CODE",
   186	    "JobRun",
   187	    "JobStopped",
   188	    "heartbeat_fraction",
   189	    "job_run",
   190	    "should_keep_running",
   191	]
     1	"""`cobalt jobs` — F17's command surface, plus `cobalt stop` / `resume`.
     2	
     3	    cobalt jobs list                     the table, as F18 reads it
     4	    cobalt jobs register                 upsert every row from jobs.yaml
     5	    cobalt jobs check                    run the watchdog, print findings
     6	    cobalt jobs run LABEL -- CMD ARGS    wrap any command as that job
     7	    cobalt stop  [--phrase "COBALT STOP"]
     8	    cobalt resume
     9	
    10	`jobs run` is the plist-facing half of the wrapper: a launchd job whose
    11	program is not Python (or is a `uv run` of something else) gets its row,
    12	its heartbeat and its exit code by being launched through this.
    13	"""
    14	
    15	from __future__ import annotations
    16	
    17	import argparse
    18	import subprocess
    19	import sys
    20	
    21	from cobalt import env
    22	
    23	from . import killswitch
    24	from .config import load_job_registry
    25	from .models import RED_STATES
    26	from .store import JobStore
    27	from .watchdog import sweep
    28	from .wrapper import JobStopped, job_run
    29	
    30	
    31	def _store() -> JobStore:
    32	    store = JobStore()
    33	    store.ensure_schema()
    34	    return store
    35	
    36	
    37	def cmd_list(args: argparse.Namespace) -> None:
    38	    store = _store()
    39	    print(f"database: {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    40	    print(killswitch.read(store).describe())
    41	    rows = store.all()
    42	    if not rows:
    43	        print("\nno jobs registered — run `cobalt jobs register`")
    44	        return
    45	    red_values = {s.value for s in RED_STATES}
    46	    print(
    47	        f"\n{'LABEL':<28} {'KIND':<9} {'STATE':<9} {'SRC':<8} {'LAST FINISH':<20} "
    48	        f"{'EXIT':<5} CADENCE"
    49	    )
    50	    for r in rows:
    51	        finish = f"{r['finished_at']:%Y-%m-%d %H:%M:%S}" if r["finished_at"] else "-"
    52	        mark = " !" if r["state"] in red_values else "  "
    53	        print(
    54	            f"{r['label']:<28} {r['kind']:<9} {r['state']:<9}{mark[1]} "
    55	            f"{r['heartbeat_source']:<8} {finish:<20} "
    56	            f"{'-' if r['exit_code'] is None else r['exit_code']:<5} "
    57	            f"{r['expected_cadence'] or '(resident)'}"
    58	        )
    59	        if r["last_error"]:
    60	            print(f"{'':>28}   last_error: {r['last_error'][:160]}")
    61	
    62	
    63	def cmd_register(args: argparse.Namespace) -> None:
    64	    store = _store()
    65	    registry = load_job_registry()
    66	    labels = store.register_all(registry)
    67	    print(f"database: {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    68	    print(f"registered {len(labels)} job(s):")
    69	    for label in labels:
    70	        spec = registry.spec(label)
    71	        print(f"  {label:<28} {spec.kind!s:<9} supervisor={spec.supervisor!s:<8} "
    72	              f"timeout={spec.timeout_s}s  {spec.cadence or '(resident)'}")
    73	
    74	
    75	def cmd_readers(args: argparse.Namespace) -> None:
    76	    """`cobalt jobs readers <path>` — who must be restarted for this file.
    77	
    78	    THE COMMAND THAT PRODUCES A DEPLOY PLAN'S `RESTARTS:` LINE. The law
    79	    has been ruled three times (2026-09-04, 09-08 on aset.yaml, 09-09 on
    80	    tunables.yaml): a config-shape change and the restart of every
    81	    resident that reads that file are ONE ACTION. Re-deriving that list
    82	    from memory at deploy time is what failed on 09-08, when a plan that
    83	    said "nothing else is restarted" left the ASET sheet answering 200s
    84	    and refusing every card for thirteen hours.
    85	
    86	    EXIT 1 ON AN UNKNOWN PATH, and that is the useful half. "No resident
    87	    re-reads this" and "nobody has written down who reads this" are
    88	    different answers, and only one of them means it is safe to deploy
    89	    without a restart. A path no row mentions gets a non-zero exit and
    90	    the list of paths that ARE covered, so the operator knows they are
    91	    looking at a gap rather than an all-clear.
    92	    """
    93	    from pathlib import Path
    94	
    95	    registry = load_job_registry()
    96	    path = args.path
    97	    readers = registry.readers_of(path)
    98	
    99	    if not readers:
   100	        known = registry.read_paths
   101	        print(
   102	            f"UNKNOWN PATH: no job row lists {path!r} as re-read at runtime.\n"
   103	            "\n"
   104	            "That is NOT the same as 'nothing reads it'. `reads` is derived by hand\n"
   105	            "from the code, so an unlisted path means nobody has worked out its\n"
   106	            "readers yet — check before deploying a change to it, and add the row.\n"
   107	            "\n"
   108	            "Paths that ARE covered:\n  " + ("\n  ".join(known) or "(none)"),
   109	            file=sys.stderr,
   110	        )
   111	        sys.exit(1)
   112	
   113	    print(f"{path} is re-read at runtime by {len(readers)} resident(s):")
   114	    for spec in readers:
   115	        print(f"  {spec.label:<28} {spec.what.strip().splitlines()[0]}")
   116	    print("\nRESTARTS: " + " ".join(s.label for s in readers))
   117	    print("  launchctl kickstart -k gui/$(id -u)/<label>")
   118	
   119	
   120	def cmd_check(args: argparse.Namespace) -> None:
   121	    findings = sweep()
   122	    for f in findings:
   123	        print(f.line())
   124	    bad = [f for f in findings if not f.ok]
   125	    print(f"\n{len(findings)} job(s) checked, {len(bad)} RED.")
   126	    if bad:
   127	        sys.exit(1)
   128	
   129	
   130	def cmd_run(args: argparse.Namespace) -> None:
   131	    """Wrap an arbitrary command as `label`. Its exit code is ours."""
   132	    if not args.command:
   133	        raise SystemExit("nothing to run — pass the command after `--`")
   134	    try:
   135	        with job_run(args.label) as run:
   136	            proc = subprocess.run(args.command)
   137	            run.result = {"argv": args.command, "returncode": proc.returncode}
   138	            if proc.returncode != 0:
   139	                raise RuntimeError(
   140	                    f"{args.label}: `{' '.join(args.command)}` exited "
   141	                    f"{proc.returncode}"
   142	                )
   143	    except JobStopped as e:
   144	        # Exit 0: a deliberate stop is not a failure and must not paint
   145	        # F18 red for a state the operator caused on purpose.
   146	        print(f"NOT RUN — {e}")
   147	        return
   148	    print(f"{args.label}: exit 0")
   149	
   150	
   151	def cmd_stop(args: argparse.Namespace) -> None:
   152	    state = killswitch.engage(by=args.by, phrase=args.phrase)
   153	    print(state.describe())
   154	
   155	
   156	def cmd_resume(args: argparse.Namespace) -> None:
   157	    state = killswitch.clear(by=args.by)
   158	    print(state.describe())
   159	
   160	
   161	def add_parser(sub) -> None:
   162	    jobs = sub.add_parser("jobs", help="F17 task integrity (Charter §3 F17)")
   163	    jsub = jobs.add_subparsers(dest="command", required=True)
   164	
   165	    lst = jsub.add_parser("list", help="Every job row, as F18 reads it.")
   166	    lst.set_defaults(func=cmd_list)
   167	
   168	    reg = jsub.add_parser("register", help="Upsert every row from configs/cobalt/jobs.yaml.")
   169	    reg.set_defaults(func=cmd_register)
   170	
   171	    check = jsub.add_parser("check", help="Run the watchdog (zombie / missed).")
   172	    check.set_defaults(func=cmd_check)
   173	
   174	    readers = jsub.add_parser(
   175	        "readers",
   176	        help="Which residents re-read a config file — the deploy plan's RESTARTS line.",
   177	    )
   178	    readers.add_argument("path", help="Repo-relative config path, e.g. configs/cobalt/taxonomy/tunables.yaml")
   179	    readers.set_defaults(func=cmd_readers)
   180	
   181	    run = jsub.add_parser("run", help="Run a command wrapped as a registered job.")
   182	    run.add_argument("label")
   183	    run.add_argument("command", nargs=argparse.REMAINDER)
   184	    run.set_defaults(func=cmd_run)
   185	
   186	
   187	def add_stop_parsers(sub) -> None:
   188	    """`cobalt stop` / `cobalt resume` — top-level, not under `jobs`.
   189	
   190	    Deliberately: the kill phrase is the thing you reach for when
   191	    something is wrong, and `cobalt jobs killswitch engage` is not what
   192	    anyone types at that moment.
   193	    """
   194	    stop = sub.add_parser("stop", help="Engage the kill phrase — stop all jobs (F17d).")
   195	    stop.add_argument("--phrase", default=None, help="Defaults to jobs.yaml's kill_phrase.")
   196	    stop.add_argument("--by", default="cli", help="Who is stopping (recorded).")
   197	    stop.set_defaults(func=cmd_stop)
   198	
   199	    resume = sub.add_parser("resume", help="Clear the kill phrase (F17d).")
   200	    resume.add_argument("--by", default="cli", help="Who is resuming (recorded).")
   201	    resume.set_defaults(func=cmd_resume)
   202	
   203	
   204	__all__ = ["add_parser", "add_stop_parsers"]
     1	"""F17 persistence: the `cobalt_jobs` row, and the kill switch behind it.
     2	
     3	THE TABLE IS `cobalt_jobs`, NOT `jobs`. `cobalt_brain` is the same
     4	Postgres database Mattermost runs in, and Mattermost owns a `jobs` table
     5	with 164,320 rows — see the note at the head of
     6	`migrations/0001_cobalt_jobs.sql` for how that was found and why only the
     7	tables introduced by this prompt carry the prefix.
     8	
     9	Database from `COBALT_ENV` via `env.resolve_db_name()` (RULING 7/9);
    10	`db_name` is the test/tooling seam only.
    11	
    12	NOT SESSION-GATED, and this one is deliberate. `cobalt.session`'s
    13	market_reset hard block exists to stop Cobalt WRITING TRADING RECORD in
    14	the 20:00-21:00 window. A job's own state is not trading record — and the
    15	archiver, the one job that runs squarely inside that window by design
    16	(20:30, its own carve-out in L28), is exactly the job whose failure the
    17	heartbeat most needs to see. A `jobs` table that went blind for an hour
    18	every evening would go blind for the hour it matters most.
    19	"""
    20	
    21	from __future__ import annotations
    22	
    23	import json
    24	from datetime import datetime, timedelta
    25	from pathlib import Path
    26	from typing import Any, Optional
    27	
    28	from cobalt import db, env
    29	from cobalt.db import Side
    30	from cobalt.session import clock as clock_mod
    31	
    32	from .config import JobSpec
    33	from .models import JobState, Supervisor
    34	
    35	MIGRATIONS_DIR = Path(__file__).parent / "migrations"
    36	
    37	
    38	class JobStoreError(RuntimeError):
    39	    """A job operation was refused."""
    40	
    41	
    42	class JobStore:
    43	    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
    44	    #: The scheduler's own bookkeeping: one row per launchd label, plus
    45	    #: the kill switch. Engine state, identical on every install.
    46	    SIDE = Side.SYSTEM
    47	
    48	    def __init__(self, db_name: Optional[str] = None):
    49	        self.db_name = db_name or env.resolve_db_name()
    50	
    51	    def _connect(self, *, allow_prod: bool = False):
    52	        return db.connect(self.db_name, side=self.SIDE, allow_prod=allow_prod)
    53	
    54	    def ensure_schema(self, *, allow_prod: bool = False) -> None:
    55	        with self._connect(allow_prod=allow_prod) as conn:
    56	            db.assert_schemas_exist(conn)
    57	            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
    58	                lines = migration.read_text().splitlines()
    59	                sql = "\n".join(l for l in lines if not l.strip().startswith("--"))
    60	                for statement in sql.split(";"):
    61	                    statement = statement.strip()
    62	                    if statement:
    63	                        conn.execute(statement)
    64	
    65	    # -- registration -------------------------------------------------
    66	
    67	    def register(self, spec: JobSpec, *, allow_prod: bool = False) -> None:
    68	        """Upsert one row from its config spec. IDEMPOTENT, and it does
    69	        NOT touch runtime columns: re-registering after a config edit
    70	        must never erase the last run's exit code, which is the one thing
    71	        an operator looks at first."""
    72	        with self._connect(allow_prod=allow_prod) as conn:
    73	            conn.execute(
    74	                "INSERT INTO cobalt_jobs (label, kind, expected_cadence, timeout_s, "
    75	                "heartbeat_source) VALUES (%s, %s, %s, %s, %s) "
    76	                "ON CONFLICT (label) DO UPDATE SET kind = EXCLUDED.kind, "
    77	                "expected_cadence = EXCLUDED.expected_cadence, "
    78	                "timeout_s = EXCLUDED.timeout_s, "
    79	                "heartbeat_source = EXCLUDED.heartbeat_source, updated_at = now()",
    80	                (
    81	                    spec.label,
    82	                    spec.kind.value,
    83	                    spec.cadence,
    84	                    spec.timeout_s,
    85	                    spec.supervisor.value,
    86	                ),
    87	            )
    88	
    89	    def register_all(self, registry, *, allow_prod: bool = False) -> list[str]:
    90	        self.ensure_schema(allow_prod=allow_prod)
    91	        for spec in registry.jobs:
    92	            self.register(spec, allow_prod=allow_prod)
    93	        return [s.label for s in registry.jobs]
    94	
    95	    # -- reads --------------------------------------------------------
    96	
    97	    def get(self, label: str) -> Optional[dict[str, Any]]:
    98	        with self._connect() as conn:
    99	            cur = conn.execute("SELECT * FROM cobalt_jobs WHERE label = %s", (label,))
   100	            row = cur.fetchone()
   101	            if row is None:
   102	                return None
   103	            return dict(zip([d.name for d in cur.description], row))
   104	
   105	    def all(self) -> list[dict[str, Any]]:
   106	        with self._connect() as conn:
   107	            cur = conn.execute("SELECT * FROM cobalt_jobs ORDER BY kind DESC, label")
   108	            columns = [d.name for d in cur.description]
   109	            return [dict(zip(columns, r)) for r in cur.fetchall()]
   110	
   111	    # -- the run lifecycle (the wrapper's three calls) -----------------
   112	
   113	    def mark_running(self, label: str, *, now: Optional[datetime] = None) -> None:
   114	        ts = now or clock_mod.now_utc()
   115	        with self._connect() as conn:
   116	            cur = conn.execute(
   117	                "UPDATE cobalt_jobs SET state = %s, started_at = %s, heartbeat_at = %s, "
   118	                "finished_at = NULL, exit_code = NULL, last_error = NULL, "
   119	                "updated_at = now() WHERE label = %s",
   120	                (JobState.RUNNING.value, ts, ts, label),
   121	            )
   122	            if cur.rowcount != 1:
   123	                raise JobStoreError(
   124	                    f"no jobs row for {label!r} — register it first "
   125	                    "(`cobalt jobs register`). F17 refuses to run a job it cannot "
   126	                    "report on: an unregistered job that hangs is invisible."
   127	                )
   128	
   129	    def beat(self, label: str, *, now: Optional[datetime] = None) -> None:
   130	        """Stamp `heartbeat_at`. The only thing separating a long job
   131	        from a hung one."""
   132	        with self._connect() as conn:
   133	            conn.execute(
   134	                "UPDATE cobalt_jobs SET heartbeat_at = %s, updated_at = now() WHERE label = %s",
   135	                (now or clock_mod.now_utc(), label),
   136	            )
   137	
   138	    def mark_finished(
   139	        self,
   140	        label: str,
   141	        *,
   142	        exit_code: int,
   143	        error: Optional[str] = None,
   144	        result: Optional[dict[str, Any]] = None,
   145	        now: Optional[datetime] = None,
   146	    ) -> None:
   147	        """`done` on 0, `failed` on anything else. Failed is LOUD: F18
   148	        turns red on this column, and the error text goes with it."""
   149	        ts = now or clock_mod.now_utc()
   150	        state = JobState.DONE if exit_code == 0 else JobState.FAILED
   151	        # F19: a job's own error text is outbound the moment F18 puts it
   152	        # in a DM. Redacting at the point of STORAGE means a traceback
   153	        # carrying a DSN never becomes a row that later leaks.
   154	        safe_error = None
   155	        if error:
   156	            from cobalt.redact import redact
   157	
   158	            safe_error = redact(error, channel="jobs.last_error").text
   159	        with self._connect() as conn:
   160	            conn.execute(
   161	                "UPDATE cobalt_jobs SET state = %s, finished_at = %s, heartbeat_at = %s, "
   162	                "exit_code = %s, last_error = %s, last_result = %s, updated_at = now() "
   163	                "WHERE label = %s",
   164	                (
   165	                    state.value,
   166	                    ts,
   167	                    ts,
   168	                    exit_code,
   169	                    safe_error,
   170	                    json.dumps(result, default=str) if result is not None else None,
   171	                    label,
   172	                ),
   173	            )
   174	
   175	    def mark_zombie(self, label: str, *, reason: str) -> None:
   176	        """The watchdog's conclusion. Nothing else may write this state."""
   177	        from cobalt.redact import redact
   178	
   179	        with self._connect() as conn:
   180	            conn.execute(
   181	                "UPDATE cobalt_jobs SET state = %s, last_error = %s, updated_at = now() "
   182	                "WHERE label = %s",
   183	                (JobState.ZOMBIE.value, redact(reason, channel="jobs.last_error").text, label),
   184	            )
   185	
   186	    def mark_probe(
   187	        self,
   188	        label: str,
   189	        *,
   190	        alive: bool,
   191	        detail: str,
   192	        now: Optional[datetime] = None,
   193	    ) -> None:
   194	        """Stamp a resident whose heartbeat comes from a PROBE, not from
   195	        itself (`supervisor: launchd | pidfile`).
   196	
   197	        A probe says "the process exists". That is a weaker claim than a
   198	        wrapper's "I am running and past my gates", which is why
   199	        `heartbeat_source` is a column: the two must never be read as the
   200	        same evidence.
   201	        """
   202	        from cobalt.redact import redact
   203	
   204	        ts = now or clock_mod.now_utc()
   205	        safe = redact(detail, channel="jobs.last_error").text
   206	        with self._connect() as conn:
   207	            if alive:
   208	                conn.execute(
   209	                    "UPDATE cobalt_jobs SET state = %s, heartbeat_at = %s, last_error = NULL, "
   210	                    "updated_at = now() WHERE label = %s",
   211	                    (JobState.RUNNING.value, ts, label),
   212	                )
   213	            else:
   214	                conn.execute(
   215	                    "UPDATE cobalt_jobs SET state = %s, last_error = %s, updated_at = now() "
   216	                    "WHERE label = %s",
   217	                    (JobState.FAILED.value, safe, label),
   218	                )
   219	
   220	    # -- the kill switch (F17d) ---------------------------------------
   221	
   222	    def kill_switch(self) -> dict[str, Any]:
   223	        with self._connect() as conn:
   224	            cur = conn.execute("SELECT * FROM cobalt_kill_switch WHERE id = TRUE")
   225	            row = cur.fetchone()
   226	            if row is None:
   227	                return {"active": False}
   228	            return dict(zip([d.name for d in cur.description], row))
   229	
   230	    def set_kill_switch(
   231	        self, *, active: bool, phrase: Optional[str], by: str,
   232	        now: Optional[datetime] = None,
   233	    ) -> dict[str, Any]:
   234	        ts = now or clock_mod.now_utc()
   235	        with self._connect() as conn:
   236	            if active:
   237	                conn.execute(
   238	                    "UPDATE cobalt_kill_switch SET active = TRUE, phrase = %s, set_by = %s, "
   239	                    "set_at = %s, cleared_by = NULL, cleared_at = NULL WHERE id = TRUE",
   240	                    (phrase, by, ts),
   241	                )
   242	            else:
   243	                conn.execute(
   244	                    "UPDATE cobalt_kill_switch SET active = FALSE, cleared_by = %s, "
   245	                    "cleared_at = %s WHERE id = TRUE",
   246	                    (by, ts),
   247	                )
   248	        return self.kill_switch()
   249	
   250	    # -- what F18 reads -----------------------------------------------
   251	
   252	    def counts_by_state(self) -> dict[str, int]:
   253	        with self._connect() as conn:
   254	            cur = conn.execute("SELECT state, count(*) FROM cobalt_jobs GROUP BY 1")
   255	            return {r[0]: int(r[1]) for r in cur.fetchall()}
   256	
   257	    def last_result(self, label: str) -> Optional[dict[str, Any]]:
   258	        row = self.get(label)
   259	        return (row or {}).get("last_result")
   260	
   261	
   262	__all__ = ["JobStore", "JobStoreError"]

exec
/bin/zsh -lc "nl -ba src/cobalt/db_migrations/__init__.py; nl -ba src/cobalt/db_migrations/cli.py; rg --files src/cobalt/db_migrations; nl -ba ops/README.md | sed -n '145,235p'; nl -ba 'docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
     1	"""The two-layer data model's migrations (ADR-0008).
     2	
     3	`0001_schemas.sql`  — schemas, roles, grants, ownership, `"user".traders`,
     4	                      the `cobalt.trader_id` GUC convention.
     5	`0002_move_tables.sql` — every new-core table onto its side, plus
     6	                      `user_id` on the user side.
     7	`0002_move_tables.rollback.sql` — the reverse, catalog-only.
     8	
     9	These are the DATABASE-WIDE migrations and they are the only ones that
    10	live outside a feature module. A module's own DDL still lives in its own
    11	`migrations/` directory and is still executed by its store's
    12	`ensure_schema()`; those files create tables UNQUALIFIED and land them in
    13	whichever schema the factory pinned on the connection.
    14	
    15	Run them with `cobalt db migrate` (`--allow-prod` from ~/cobalt only,
    16	`--rollback` to reverse 0002). Nothing runs them implicitly: a store's
    17	`ensure_schema()` asserts the schemas exist and tells you to run the CLI.
    18	"""
    19	
    20	from pathlib import Path
    21	
    22	MIGRATIONS_DIR = Path(__file__).parent
    23	
    24	#: Applied in this order, every time, both idempotent.
    25	FORWARD = (
    26	    MIGRATIONS_DIR / "0001_schemas.sql",
    27	    MIGRATIONS_DIR / "0002_move_tables.sql",
    28	)
    29	
    30	#: `--rollback`. 0001 is deliberately NOT reversed — see the file header.
    31	REVERSE = (MIGRATIONS_DIR / "0002_move_tables.rollback.sql",)
    32	
    33	__all__ = ["FORWARD", "MIGRATIONS_DIR", "REVERSE"]
     1	"""`cobalt db migrate [--allow-prod] [--rollback]` — ADR-0008's harness.
     2	
     3	WHAT IT PRINTS IS THE POINT. A migration that moves twelve tables between
     4	schemas and adds a column to six of them is a migration whose claim
     5	("nothing was lost") has to be checkable by looking, not by trusting. So
     6	every run captures, per table, BEFORE and AFTER:
     7	
     8	  * where it lives (`public` / `system` / `"user"`),
     9	  * `count(*)`,
    10	  * a content digest: `md5(string_agg(row::text, '|' ORDER BY <pk>))`.
    11	
    12	THE DIGEST EXCLUDES `user_id`. The forward migration ADDS that column to
    13	the six user-side tables, so a digest over the whole row would differ
    14	before and after by construction and would prove nothing. Taking it over
    15	`to_jsonb(t) - 'user_id'` means the two digests are comparable and an
    16	inequality is a real finding: the rows themselves changed. `to_jsonb`
    17	serialises keys in a stable order, so the digest does not depend on
    18	column order either — which matters, because `SET SCHEMA` and `ADD
    19	COLUMN` both touch the catalog the naive `row::text` reads.
    20	
    21	ORDERED BY THE PRIMARY KEY, read from the catalog per table rather than
    22	hard-coded: `bars` is keyed `(ticker, interval, ts)`, `day_modes` by
    23	`trade_date`, `cobalt_jobs` by `label`, the rest by `id`.
    24	
    25	`--rollback` runs `0002_move_tables.rollback.sql` (catalog-only reverse)
    26	and prints the same proof table. Running `migrate`, then `--rollback`,
    27	then `migrate` again must land on the same digests — the suite asserts
    28	exactly that round-trip on `cobalt_dev`.
    29	
    30	`--allow-prod` reaches `cobalt_brain` without flipping the process into
    31	production mode (RULING 7's one-off-tooling seam). Without it the target
    32	is whatever `COBALT_ENV` resolves.
    33	"""
    34	
    35	from __future__ import annotations
    36	
    37	import argparse
    38	from typing import Optional
    39	
    40	from psycopg import sql
    41	
    42	from cobalt import db, env
    43	
    44	from . import FORWARD, REVERSE
    45	from .placement import MOVED_TABLES, SEEDED_TABLES
    46	
    47	#: The tenancy column the digest ignores — see the module docstring.
    48	TENANCY_COLUMN = "user_id"
    49	
    50	#: Where a new-core table may legitimately be found, in look-up order.
    51	SEARCHED_SCHEMAS = ("public", "user", "system")
    52	
    53	
    54	class MigrationError(RuntimeError):
    55	    """The migration could not be run or could not be proven."""
    56	
    57	
    58	def _schema_of(conn, table: str) -> Optional[str]:
    59	    row = conn.execute(
    60	        "SELECT schemaname FROM pg_tables "
    61	        "WHERE tablename = %s AND schemaname = ANY(%s) LIMIT 1",
    62	        (table, list(SEARCHED_SCHEMAS)),
    63	    ).fetchone()
    64	    return row[0] if row else None
    65	
    66	
    67	def _pk_columns(conn, schema: str, table: str) -> list[str]:
    68	    rows = conn.execute(
    69	        """
    70	        SELECT a.attname
    71	        FROM pg_index i
    72	        JOIN pg_attribute a
    73	          ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
    74	        WHERE i.indrelid = (quote_ident(%s) || '.' || quote_ident(%s))::regclass
    75	          AND i.indisprimary
    76	        ORDER BY array_position(i.indkey::int2[], a.attnum)
    77	        """,
    78	        (schema, table),
    79	    ).fetchall()
    80	    if not rows:
    81	        raise MigrationError(
    82	            f"{schema}.{table} has no primary key, so its rows cannot be put in a "
    83	            "deterministic order and no content digest can be taken. Every "
    84	            "new-core table has one; this is a real finding, not a tooling gap."
    85	        )
    86	    return [r[0] for r in rows]
    87	
    88	
    89	def _probe(conn, table: str) -> dict:
    90	    """(schema, rows, digest) for `table`, wherever it currently lives."""
    91	    schema = _schema_of(conn, table)
    92	    if schema is None:
    93	        return {"schema": None, "rows": None, "digest": None}
    94	    pk = _pk_columns(conn, schema, table)
    95	    query = sql.SQL(
    96	        "SELECT count(*), "
    97	        "md5(coalesce(string_agg((to_jsonb(t) - {tenancy})::text, '|' ORDER BY {order}), '')) "
    98	        "FROM {rel} AS t"
    99	    ).format(
   100	        tenancy=sql.Literal(TENANCY_COLUMN),
   101	        order=sql.SQL(", ").join(sql.Identifier("t", c) for c in pk),
   102	        rel=sql.Identifier(schema, table),
   103	    )
   104	    rows, digest = conn.execute(query).fetchone()
   105	    return {"schema": schema, "rows": int(rows), "digest": digest}
   106	
   107	
   108	def _probe_all(conn) -> dict[str, dict]:
   109	    tables = {**MOVED_TABLES, **SEEDED_TABLES}
   110	    return {t: _probe(conn, t) for t in sorted(tables)}
   111	
   112	
   113	def _print_proof(before: dict[str, dict], after: dict[str, dict]) -> int:
   114	    """Render the proof table. Returns the number of CHANGED digests."""
   115	    tables = {**MOVED_TABLES, **SEEDED_TABLES}
   116	    header = (
   117	        f"{'table':<20} {'side':<7} {'schema before -> after':<26} "
   118	        f"{'rows':<15} {'digest before -> after':<21} verdict"
   119	    )
   120	    print(header)
   121	    print("-" * len(header))
   122	    changed = 0
   123	    for name in sorted(tables):
   124	        b, a = before[name], after[name]
   125	        where = f"{b['schema'] or '-'} -> {a['schema'] or '-'}"
   126	        rows = f"{'-' if b['rows'] is None else b['rows']} -> " \
   127	               f"{'-' if a['rows'] is None else a['rows']}"
   128	        dig = f"{(b['digest'] or '-')[:8]} -> {(a['digest'] or '-')[:8]}"
   129	        if b["schema"] is None and a["schema"] is None:
   130	            verdict = "ABSENT"
   131	        elif b["digest"] == a["digest"] and b["rows"] == a["rows"]:
   132	            verdict = "OK"
   133	        elif b["schema"] is None:
   134	            verdict = "CREATED"
   135	        else:
   136	            verdict = "CHANGED"
   137	            changed += 1
   138	        print(
   139	            f"{name:<20} {tables[name].value:<7} {where:<26} {rows:<15} "
   140	            f"{dig:<21} {verdict}"
   141	        )
   142	    print("-" * len(header))
   143	    print(
   144	        f"{len(tables)} table(s) proven; digest = md5(string_agg((to_jsonb(row) - "
   145	        f"'{TENANCY_COLUMN}')::text, '|' ORDER BY pk)). "
   146	        + ("content UNCHANGED on every table."
   147	           if changed == 0
   148	           else f"{changed} table(s) CHANGED — investigate before proceeding.")
   149	    )
   150	    return changed
   151	
   152	
   153	def _apply(conn, paths) -> None:
   154	    """Run whole .sql files, one transaction for the lot.
   155	
   156	    Each file is handed to the server ENTIRE rather than split on ';':
   157	    these migrations are DO blocks, and a splitter would cut them at the
   158	    first semicolon inside the body. psycopg uses the simple query
   159	    protocol when there are no parameters, which accepts multiple
   160	    statements — and the migrations take no parameters by design.
   161	    """
   162	    for path in paths:
   163	        print(f"-- applying {path.name}")
   164	        conn.execute(path.read_text())
   165	
   166	
   167	def cmd_migrate(args: argparse.Namespace) -> None:
   168	    dbname = db.PROD_DB_NAME if args.allow_prod else env.resolve_db_name()
   169	    direction = "ROLLBACK" if args.rollback else "FORWARD"
   170	    paths = REVERSE if args.rollback else FORWARD
   171	
   172	    print(f"cobalt db migrate — {direction} on {dbname}")
   173	    conn = db.connect_migration(dbname, allow_prod=args.allow_prod)
   174	    conn.autocommit = False
   175	    try:
   176	        before = _probe_all(conn)
   177	        _apply(conn, paths)
   178	        after = _probe_all(conn)
   179	        conn.commit()
   180	    except BaseException:
   181	        conn.rollback()
   182	        raise
   183	    finally:
   184	        conn.close()
   185	
   186	    print()
   187	    changed = _print_proof(before, after)
   188	    if changed:
   189	        raise MigrationError(
   190	            f"{changed} table(s) changed content across the migration. The "
   191	            "migration is committed; the proof is not clean — compare against the "
   192	            "pg_dump taken before this run."
   193	        )
   194	
   195	
   196	def add_parser(sub) -> None:
   197	    group = sub.add_parser("db", help="Database migrations (ADR-0008 two-layer model)")
   198	    gsub = group.add_subparsers(dest="command", required=True)
   199	
   200	    migrate = gsub.add_parser(
   201	        "migrate",
   202	        help="Create the system/\"user\" schemas and move every new-core table.",
   203	    )
   204	    migrate.add_argument(
   205	        "--allow-prod",
   206	        action="store_true",
   207	        help="Target cobalt_brain (run from ~/cobalt only, outside market hours).",
   208	    )
   209	    migrate.add_argument(
   210	        "--rollback",
   211	        action="store_true",
   212	        help="Reverse 0002: every table back to public, user_id dropped.",
   213	    )
   214	    migrate.set_defaults(func=cmd_migrate)
   215	
   216	
   217	__all__ = ["MigrationError", "add_parser", "cmd_migrate"]
src/cobalt/db_migrations/placement.py
src/cobalt/db_migrations/cli.py
src/cobalt/db_migrations/0001_schemas.sql
src/cobalt/db_migrations/__init__.py
src/cobalt/db_migrations/0002_move_tables.rollback.sql
src/cobalt/db_migrations/0002_move_tables.sql
   145	it is reviewed in a diff; `~/.lmstudio/` is where the 09-04 note put it
   146	and the plist never agreed.)*
   147	
   148	## Install / reload
   149	
   150	```sh
   151	# first install
   152	cp ops/com.cobalt.<name>.plist ~/Library/LaunchAgents/
   153	launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.<name>.plist
   154	
   155	# after editing the plist or its wrapper script
   156	cp ops/com.cobalt.<name>.plist ~/Library/LaunchAgents/   # only if the plist itself changed
   157	launchctl kickstart -k gui/$(id -u)/com.cobalt.<name>
   158	
   159	# status / logs
   160	launchctl list | grep com.cobalt.<name>
   161	tail -f logs/<name>.log logs/<name>.err
   162	
   163	# stop + unload
   164	launchctl bootout gui/$(id -u)/com.cobalt.<name>
   165	```
   166	
   167	## Deploy checklist
   168	
   169	**THE LAW, ruled three times — 2026-09-04, 2026-09-08 (`aset.yaml`) and
   170	2026-09-09 (`tunables.yaml`): a config-shape change and the restart of
   171	EVERY resident that reads that file are ONE ACTION.** Not two steps, not
   172	a follow-up. A deploy plan that changes a config and does not name the
   173	processes it restarts is an incomplete plan.
   174	
   175	**Every deploy plan carries a `RESTARTS:` line, and it is produced by a
   176	command, not by memory:**
   177	
   178	```sh
   179	# for every config file the merge touches
   180	uv run cobalt jobs readers configs/cobalt/taxonomy/tunables.yaml
   181	#   -> RESTARTS: com.cobalt.aset
   182	
   183	launchctl kickstart -k gui/$(id -u)/com.cobalt.aset
   184	```
   185	
   186	`cobalt jobs readers` reads `reads:` in `configs/cobalt/jobs.yaml` —
   187	per-resident, derived from the code, one row per config file the process
   188	re-reads at runtime. **An unknown path exits 1**, deliberately: "no
   189	resident re-reads this" and "nobody has worked out who reads this" are
   190	different answers, and only one of them makes it safe to deploy without
   191	a restart. `uv run cobalt validate` prints the whole map and fails if a
   192	listed path has gone missing.
   193	
   194	### Why this is a law and not a habit
   195	
   196	On 2026-09-08 at ~19:00 the seat-usage deploy added a
   197	`TunableUnit.WINDOW` row to `configs/cobalt/taxonomy/tunables.yaml`. Its
   198	plan said *"nothing else is loaded or restarted"* — true of its own job,
   199	and wrong about the sheet. `com.cobalt.aset` had been running since
   200	17:50 and **re-reads `tunables.yaml` on every request**, so it read the
   201	new row through code that predated the enum value and raised
   202	`TaxonomyConfigError` on every render. From then until the kickstart at
   203	**07:06 on 09-09** — about thirteen hours, including the premarket — the
   204	page he trades beside served HTTP 200 with
   205	
   206	> ⚠ DAY MODE UNRESOLVED — cards are refused until this is fixed
   207	
   208	and every card write was refused. `sheet_http` was green throughout and
   209	was telling the truth: the server was up.
   210	
   211	Two things came out of it, and both are in place now: this checklist,
   212	and the `sheet daymode` probe (F18) that reads the banner instead of the
   213	status line, so the same failure is red within one heartbeat interval
   214	rather than at whatever hour somebody happens to look.
   215	
   216	### The order
   217	
   218	1. `uv run cobalt validate` — the config gate, on the branch, before merging.
   219	2. In the worktree, `git rebase main` first — after the nightly generated commit
   220	   (`com.cobalt.generated`, 23:37) every branch older than a day is behind `main`.
   221	   Then `git merge --ff-only <branch>` from `~/cobalt`. **Merge is deploy** (R4).
   222	   If the merge carries a NEW credential, its `.env` lines land BEFORE the merge:
   223	   between merge and `.env` a starting job fails loud (heartbeat, seat-usage).
   224	3. **Migrations**, if any, as their own step with their own rollback.
   225	4. **`RESTARTS:`** — kickstart every resident named by `cobalt jobs
   226	   readers` for every config file the merge touched.
   227	5. **Registry** — `uv run cobalt jobs register` if `jobs.yaml` changed;
   228	   `cp` + `launchctl bootstrap` for a new plist.
   229	6. **Force a beat** and read it:
   230	   `launchctl kickstart -k gui/$(id -u)/com.cobalt.heartbeat`.
   231	7. Deploys go **outside market hours** (NN#16) and outside 20:00-21:30 ET
   232	   (F1's market-reset window).
   233	8. **Vault delivery snapshots:** a report written on an unmerged branch is copied
   234	   to `docs/_inflight/` (git-ignored, visible in Obsidian at
   235	   `0 - Projects/Cobalt/_inflight/`) so Dejan can read it before the merge; delete
     1	# Heartbeat blackout — 2026-09-08 & 09-09, 20:00–21:00 ET
     2	
     3	*Read-only diagnosis. No fix applied, nothing committed. Hub: Opus 5. Worker: Codex `gpt-5.6-terra`, `-s read-only`.*
     4	
     5	## §0 Headline
     6	
     7	Both blackouts are **one cause, fully in the log**: every "missing" beat ran, and
     8	died at the F1 `market_reset` gate on its own daily-note write. `write_note_block()`
     9	is called unguarded at `runner.py:249`, and the heartbeat's own DB row is not stamped
    10	until `runner.py:291-292` — so the refusal kills the beat before it records itself,
    11	alerts, or DMs. **H1 SUPPORTED · H2 REFUTED · H3 REFUTED.** ESCALATE: 4.
    12	
    13	## The two windows, side by side
    14	
    15	| | 2026-09-08 | 2026-09-09 |
    16	|---|---|---|
    17	| Last beat before gap | 19:52:20 ET (`vault_writes` id 2103) | 19:59:01 ET (id 2216) |
    18	| Beats attempted in gap | 20:07:23, 20:22:26, 20:37:28, 20:52:31 | 20:14:04, 20:29:07, 20:44:10, 20:59:13 |
    19	| Each attempt's outcome | `SessionBlocked` → process exit non-zero | `SessionBlocked` → process exit non-zero |
    20	| First beat back | 21:07:31 ET, **RED — 1 job(s)** (id 2106) | 21:14:16 ET, **RED — 1 job(s)** (id 2219) |
    21	| Gap length | 75 min 13 s | 75 min 15 s |
    22	| Archiver 20:30 run | 20:30:05 → 20:53:26, 3,166,696 rows, exit 0, 23m20s | 20:30:05 → 20:53:25, 3,167,272 rows, exit 0, 23m19s |
    23	
    24	The gap is not approximately the block window — it **is** the block window, snapped to
    25	the 15-min phase: every scheduled tick whose clock fell inside 20:00–21:00 ET died,
    26	and the phase is unbroken across the gap (19:52→21:07, 19:59→21:14). launchd never
    27	missed a beat; the beat missed itself.
    28	
    29	## Verdicts
    30	
    31	| H | Verdict | Evidence |
    32	|---|---|---|
    33	| **H1** write-block collision | **SUPPORTED** | `system.session_blocks` ids 1–8, actor `vaultwrite:heartbeat:upsert_unit`, one row per missing tick, target = that day's daily note. Each is paired in `logs/heartbeat.err` with `FAILED: SessionBlocked: …` — the CLI's top-level fail-loud exit. 8 rows, 8 `FAILED` lines, whole-file totals, no other cause anywhere. |
    34	| **H2** job never launched | **REFUTED** | The job launched at all four ticks each night — the refusal rows carry its own wall clock (20:07:23, 20:22:26, …). `launchctl print gui/501/com.cobalt.heartbeat`: `run interval = 900 seconds`, `runs = 518`, `last exit code = 0`, no throttle field, `runatload`. `pmset -g log` shows `caffeinate PreventUserIdleSystemSleep` held through both windows and no sleep/wake transition. |
    35	| **H3** launched, hung or killed | **REFUTED** | Every attempt died **fast** and by name: `SessionBlocked`, ~3 s after launch, after all 12 probes had already run. The archiver completed cleanly both nights (exit 0, 0 failures, 23m). No hang, no SIGKILL, no timeout. |
    36	
    37	## The code path (item 1.6)
    38	
    39	`src/cobalt/heartbeat/runner.py:243-292` — the order is the defect:
    40	
    41	```python
    42	243  def run_beat(*, now=None, dry_run=False, probe=True) -> Beat:
    43	247      beat = take_beat(now=now, probe=probe)      # all 12 probes + job sweep — succeeded every time
    44	249      write = write_note_block(beat, dry_run=dry_run)   # ← raises here, unguarded
    45	250      if write is None:                                  # only handles "note does not exist"
    46	...
    47	291      store.mark_running(JOB_LABEL,  now=...)     # ← never reached
    48	292      store.mark_finished(JOB_LABEL, exit_code=0, result=result, now=...)
    49	```
    50	
    51	`write_note_block` → `runner.py:147` `writer.upsert_unit(...)` → `vaultwrite/writer.py:664`
    52	`self._session_gate("upsert_unit", path)` → `writer.py:411` `assert_writable(...)` →
    53	`session/guard.py:150` **raises `SessionBlocked`** (a `RuntimeError`; the ERROR line is `guard.py:146`).
    54	
    55	Nothing catches it. `write_note_block` guards only "the note does not exist"
    56	(`runner.py:136-142`); `cmd_beat` (`heartbeat/cli.py:27`) has no handler either. The
    57	exception unwinds to the CLI's fail-loud top level, which prints `FAILED: SessionBlocked: …`
    58	to stderr and exits non-zero.
    59	
    60	Consequences of dying at :249, all four of them:
    61	1. **No DB row** — `system.cobalt_jobs` is a single upsert row per label, so the heartbeat's
    62	   row simply stays at 19:52 and goes stale. There is no beat history to lose; there is no
    63	   beat history at all.
    64	2. **No alert** — `out_of_band()` (email) and `send_dm()` are at `runner.py:269-270`, after
    65	   the write. A beat that has something to say is silenced by the fact that it cannot write
    66	   the note.
    67	3. **No F17 wrapper to catch it** — the plist runs `uv run cobalt heartbeat beat` directly.
    68	   Unlike the archiver (`jobs.wrapper` logs `F17: … RUNNING` / `DONE`), the heartbeat
    69	   self-records inside `run_beat`, so a crash before :291 leaves no `failed` row — just silence.
    70	4. **Nothing degrades** — probes, sweep, and rendered beat were all in hand at :249 and were
    71	   thrown away with the exception.
    72	
    73	## Why it self-detects, and why that took 75 minutes
    74	
    75	The 21:07 / 21:14 beat is the first one whose clock is outside the block. Its own watchdog
    76	sweep reads its own stale `cobalt_jobs` row and reports:
    77	
    78	```
    79	RED  com.cobalt.heartbeat  done (MISSED) every 15 min; last finish 2026-09-08 19:52 ET,
    80	     measured from 2026-09-08 19:52 ET — more than two intervals (30 min) ago.
    81	```
    82	
    83	Correct, and it names the symptom without the cause. The cause was in `heartbeat.err` the
    84	whole time — Dejan's "not in the log" is `heartbeat.log` (stdout, the rendered beat), which
    85	by construction contains only beats that survived to be rendered.
    86	
    87	## The probe that watched it happen and called it green
    88	
    89	`probes.py:320-348` `vaultwrite_blocks` reported, in the very RED beat that noticed the gap:
    90	
    91	```
    92	OK   vault blocks   4 refused, 0 ungated repair run(s) in the counter window
    93	```
    94	
    95	Four refusals — the exact four dead beats — rated **OK by design**: *"NOT RED ON ITS OWN. A
    96	refusal is the guard WORKING"* (`probes.py:321-324`). True of every other actor; false when
    97	the refused writer is the heartbeat itself. `system.session_blocks` has **8 rows total,
    98	all 8 `vaultwrite:heartbeat:upsert_unit`** — to date, the only thing F1 has ever turned away
    99	is the heartbeat.
   100	
   101	## The control case: 2026-09-07 proves causation
   102	
   103	| Date | Trading day? | Heartbeat writes inside 20:00–21:00 |
   104	|---|---|---|
   105	| 2026-09-07 | **No — Labor Day** (`configs/cobalt/calendar/nyse-2026.yaml:45`) | **4** (20:02, 20:17, 20:32, 20:47) — no gap |
   106	| 2026-09-08 | Yes | 0 |
   107	| 2026-09-09 | Yes | 0 |
   108	
   109	On a market holiday the whole day is `overnight` (`clock.py:196-198`), no `market_reset`
   110	window exists, the gate never fires, and the beats went through — same code, same archiver
   111	run at 20:30 (also exit 0, 23m21s), same machine. This also dates the defect: the gate landed
   112	2026-09-04 19:03 (`e2acd20`), and **09-08 was the first trading-day 20:00–21:00 window with
   113	both the gate and the heartbeat live**. It is not a regression from 09-08's deploy; it is the
   114	first night the two met. It will recur tonight and every trading night until fixed.
   115	
   116	## ESCALATE
   117	
   118	- **Fix class (not applied):** *persistence ordering + vault-write degradation.* The beat must
   119	  persist itself (DB row) and run its alert channels **before**, or independently of, the vault
   120	  write; the `market_reset` refusal of the heartbeat's own status unit must be a caught,
   121	  degraded, reported condition — not an exception that ends the beat. Whether the correct shape
   122	  is (a) reorder + `try/except SessionBlocked` around `write_note_block`, (b) a repo-owned-style
   123	  carve-out for the heartbeat's status unit, or (c) writing the block at 21:00 as a catch-up, is
   124	  a **trading-logic-adjacent design call** — F1's window is a Charter rule and any carve-out in it
   125	  needs its own ruling. Not decided here.
   126	- **`log show` unavailable.** Terra's Unified Log queries returned `log: Cannot run while sandboxed`;
   127	  launchd's own spawn/throttle/kill messages are unread. Moot for these verdicts — the refusal rows
   128	  timestamp the launches directly — but it means no independent launchd-side confirmation exists,
   129	  and this tool will be unavailable to the next sandboxed forensics run too.
   130	- **Per-run exit codes are not retained.** `heartbeat.err` carries no per-run exit code or duration,
   131	  and `launchctl` keeps only the most recent (`last exit code = 0`). Eight non-zero exits left no
   132	  durable trace outside the log text. The heartbeat is the one job with no F17 wrapper.
   133	- **Second failure mode, unrelated to the gap:** `vaultwrite_blocks` cannot distinguish "F1 turned
   134	  away someone else" from "F1 killed the watcher". As written it will stay green through every
   135	  future recurrence of this exact outage.
   136	- **Also observed, not investigated:** an off-phase beat at 2026-09-08 19:22:14, 62 s after the
   137	  19:21:12 beat. Out of scope here; flagging it rather than dropping it.

exec
/bin/zsh -lc "nl -ba src/cobalt/jobs/wrapper.py | sed -n '70,215p'; nl -ba src/cobalt/jobs/cli.py | sed -n '55,165p'; nl -ba src/cobalt/jobs/store.py | sed -n '40,210p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
    70	            "default (F16)."
    71	        )
    72	    return int(row.value)
    73	
    74	
    75	class _Beater:
    76	    """Stamps `heartbeat_at` on a timer until the run ends."""
    77	
    78	    def __init__(self, store: JobStore, label: str, every_s: float):
    79	        self.store = store
    80	        self.label = label
    81	        self.every_s = max(1.0, every_s)
    82	        self._stop = threading.Event()
    83	        self._thread = threading.Thread(
    84	            target=self._loop, name=f"beat:{label}", daemon=True
    85	        )
    86	
    87	    def _loop(self) -> None:
    88	        while not self._stop.wait(self.every_s):
    89	            try:
    90	                self.store.beat(self.label)
    91	            except Exception as e:  # noqa: BLE001
    92	                # A missed stamp is not a reason to kill the job. It IS a
    93	                # reason to say so: the watchdog may conclude ZOMBIE from
    94	                # this, and an operator needs the other half of the story.
    95	                logger.error(
    96	                    "F17: heartbeat stamp FAILED for {} ({}: {}) — the job is still "
    97	                    "running; the watchdog may see a stale heartbeat.",
    98	                    self.label, type(e).__name__, e,
    99	                )
   100	
   101	    def __enter__(self) -> "_Beater":
   102	        self._thread.start()
   103	        return self
   104	
   105	    def __exit__(self, *exc) -> None:
   106	        self._stop.set()
   107	
   108	
   109	class JobRun:
   110	    """Handle a wrapped job can hang its result on."""
   111	
   112	    def __init__(self, spec: JobSpec):
   113	        self.spec = spec
   114	        self.label = spec.label
   115	        #: Whatever the run wants F18 to be able to report — the
   116	        #: archiver's `rows_written` is what makes "archiver freshness
   117	        #: (last run + rows written)" answerable.
   118	        self.result: Optional[dict[str, Any]] = None
   119	
   120	
   121	@contextmanager
   122	def job_run(
   123	    label: str,
   124	    *,
   125	    store: Optional[JobStore] = None,
   126	    register: bool = True,
   127	    allow_prod: bool = False,
   128	):
   129	    """Run a block as a registered job. See the module docstring."""
   130	    registry = load_job_registry()
   131	    spec = registry.spec(label)
   132	    store = store or JobStore()
   133	    store.ensure_schema(allow_prod=allow_prod)
   134	    if register:
   135	        store.register(spec, allow_prod=allow_prod)
   136	
   137	    if killswitch.is_active(store):
   138	        state = killswitch.read(store)
   139	        logger.error("F17: {} REFUSED TO START — {}", label, state.describe())
   140	        raise JobStopped(state.describe())
   141	
   142	    store.mark_running(label)
   143	    run = JobRun(spec)
   144	    every_s = spec.timeout_s / heartbeat_fraction()
   145	    logger.info(
   146	        "F17: {} RUNNING (timeout {}s, heartbeat every {:.0f}s)",
   147	        label, spec.timeout_s, every_s,
   148	    )
   149	    try:
   150	        with _Beater(store, label, every_s):
   151	            yield run
   152	    except BaseException as e:
   153	        store.mark_finished(
   154	            label,
   155	            exit_code=1,
   156	            error=f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=8)}",
   157	            result=run.result,
   158	        )
   159	        logger.error("F17: {} FAILED — {}: {}", label, type(e).__name__, e)
   160	        raise            # the wrapper reports; it never swallows
   161	    store.mark_finished(label, exit_code=0, result=run.result)
   162	    logger.info("F17: {} DONE", label)
   163	
   164	
   165	def should_keep_running(label: str, *, store: Optional[JobStore] = None) -> bool:
   166	    """A RESIDENT's own loop check. `False` means exit cleanly now.
   167	
   168	    Residents call this where they can stop without tearing out of a
   169	    write. Cobalt's residents today are supervised by launchd rather than
   170	    wrapped (see jobs.yaml), so this exists for the first new-core
   171	    resident — the S2 radar poller — and for anything the chief of staff
   172	    grows into.
   173	    """
   174	    if killswitch.is_active(store):
   175	        logger.error(
   176	            "F17: kill switch engaged — {} is exiting cleanly at its next safe point.",
   177	            label,
   178	        )
   179	        return False
   180	    return True
   181	
   182	
   183	__all__ = [
   184	    "HEARTBEAT_FRACTION_KEY",
   185	    "STOPPED_EXIT_CODE",
   186	    "JobRun",
   187	    "JobStopped",
   188	    "heartbeat_fraction",
   189	    "job_run",
   190	    "should_keep_running",
   191	]
    55	            f"{r['heartbeat_source']:<8} {finish:<20} "
    56	            f"{'-' if r['exit_code'] is None else r['exit_code']:<5} "
    57	            f"{r['expected_cadence'] or '(resident)'}"
    58	        )
    59	        if r["last_error"]:
    60	            print(f"{'':>28}   last_error: {r['last_error'][:160]}")
    61	
    62	
    63	def cmd_register(args: argparse.Namespace) -> None:
    64	    store = _store()
    65	    registry = load_job_registry()
    66	    labels = store.register_all(registry)
    67	    print(f"database: {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    68	    print(f"registered {len(labels)} job(s):")
    69	    for label in labels:
    70	        spec = registry.spec(label)
    71	        print(f"  {label:<28} {spec.kind!s:<9} supervisor={spec.supervisor!s:<8} "
    72	              f"timeout={spec.timeout_s}s  {spec.cadence or '(resident)'}")
    73	
    74	
    75	def cmd_readers(args: argparse.Namespace) -> None:
    76	    """`cobalt jobs readers <path>` — who must be restarted for this file.
    77	
    78	    THE COMMAND THAT PRODUCES A DEPLOY PLAN'S `RESTARTS:` LINE. The law
    79	    has been ruled three times (2026-09-04, 09-08 on aset.yaml, 09-09 on
    80	    tunables.yaml): a config-shape change and the restart of every
    81	    resident that reads that file are ONE ACTION. Re-deriving that list
    82	    from memory at deploy time is what failed on 09-08, when a plan that
    83	    said "nothing else is restarted" left the ASET sheet answering 200s
    84	    and refusing every card for thirteen hours.
    85	
    86	    EXIT 1 ON AN UNKNOWN PATH, and that is the useful half. "No resident
    87	    re-reads this" and "nobody has written down who reads this" are
    88	    different answers, and only one of them means it is safe to deploy
    89	    without a restart. A path no row mentions gets a non-zero exit and
    90	    the list of paths that ARE covered, so the operator knows they are
    91	    looking at a gap rather than an all-clear.
    92	    """
    93	    from pathlib import Path
    94	
    95	    registry = load_job_registry()
    96	    path = args.path
    97	    readers = registry.readers_of(path)
    98	
    99	    if not readers:
   100	        known = registry.read_paths
   101	        print(
   102	            f"UNKNOWN PATH: no job row lists {path!r} as re-read at runtime.\n"
   103	            "\n"
   104	            "That is NOT the same as 'nothing reads it'. `reads` is derived by hand\n"
   105	            "from the code, so an unlisted path means nobody has worked out its\n"
   106	            "readers yet — check before deploying a change to it, and add the row.\n"
   107	            "\n"
   108	            "Paths that ARE covered:\n  " + ("\n  ".join(known) or "(none)"),
   109	            file=sys.stderr,
   110	        )
   111	        sys.exit(1)
   112	
   113	    print(f"{path} is re-read at runtime by {len(readers)} resident(s):")
   114	    for spec in readers:
   115	        print(f"  {spec.label:<28} {spec.what.strip().splitlines()[0]}")
   116	    print("\nRESTARTS: " + " ".join(s.label for s in readers))
   117	    print("  launchctl kickstart -k gui/$(id -u)/<label>")
   118	
   119	
   120	def cmd_check(args: argparse.Namespace) -> None:
   121	    findings = sweep()
   122	    for f in findings:
   123	        print(f.line())
   124	    bad = [f for f in findings if not f.ok]
   125	    print(f"\n{len(findings)} job(s) checked, {len(bad)} RED.")
   126	    if bad:
   127	        sys.exit(1)
   128	
   129	
   130	def cmd_run(args: argparse.Namespace) -> None:
   131	    """Wrap an arbitrary command as `label`. Its exit code is ours."""
   132	    if not args.command:
   133	        raise SystemExit("nothing to run — pass the command after `--`")
   134	    try:
   135	        with job_run(args.label) as run:
   136	            proc = subprocess.run(args.command)
   137	            run.result = {"argv": args.command, "returncode": proc.returncode}
   138	            if proc.returncode != 0:
   139	                raise RuntimeError(
   140	                    f"{args.label}: `{' '.join(args.command)}` exited "
   141	                    f"{proc.returncode}"
   142	                )
   143	    except JobStopped as e:
   144	        # Exit 0: a deliberate stop is not a failure and must not paint
   145	        # F18 red for a state the operator caused on purpose.
   146	        print(f"NOT RUN — {e}")
   147	        return
   148	    print(f"{args.label}: exit 0")
   149	
   150	
   151	def cmd_stop(args: argparse.Namespace) -> None:
   152	    state = killswitch.engage(by=args.by, phrase=args.phrase)
   153	    print(state.describe())
   154	
   155	
   156	def cmd_resume(args: argparse.Namespace) -> None:
   157	    state = killswitch.clear(by=args.by)
   158	    print(state.describe())
   159	
   160	
   161	def add_parser(sub) -> None:
   162	    jobs = sub.add_parser("jobs", help="F17 task integrity (Charter §3 F17)")
   163	    jsub = jobs.add_subparsers(dest="command", required=True)
   164	
   165	    lst = jsub.add_parser("list", help="Every job row, as F18 reads it.")
    40	
    41	
    42	class JobStore:
    43	    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
    44	    #: The scheduler's own bookkeeping: one row per launchd label, plus
    45	    #: the kill switch. Engine state, identical on every install.
    46	    SIDE = Side.SYSTEM
    47	
    48	    def __init__(self, db_name: Optional[str] = None):
    49	        self.db_name = db_name or env.resolve_db_name()
    50	
    51	    def _connect(self, *, allow_prod: bool = False):
    52	        return db.connect(self.db_name, side=self.SIDE, allow_prod=allow_prod)
    53	
    54	    def ensure_schema(self, *, allow_prod: bool = False) -> None:
    55	        with self._connect(allow_prod=allow_prod) as conn:
    56	            db.assert_schemas_exist(conn)
    57	            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
    58	                lines = migration.read_text().splitlines()
    59	                sql = "\n".join(l for l in lines if not l.strip().startswith("--"))
    60	                for statement in sql.split(";"):
    61	                    statement = statement.strip()
    62	                    if statement:
    63	                        conn.execute(statement)
    64	
    65	    # -- registration -------------------------------------------------
    66	
    67	    def register(self, spec: JobSpec, *, allow_prod: bool = False) -> None:
    68	        """Upsert one row from its config spec. IDEMPOTENT, and it does
    69	        NOT touch runtime columns: re-registering after a config edit
    70	        must never erase the last run's exit code, which is the one thing
    71	        an operator looks at first."""
    72	        with self._connect(allow_prod=allow_prod) as conn:
    73	            conn.execute(
    74	                "INSERT INTO cobalt_jobs (label, kind, expected_cadence, timeout_s, "
    75	                "heartbeat_source) VALUES (%s, %s, %s, %s, %s) "
    76	                "ON CONFLICT (label) DO UPDATE SET kind = EXCLUDED.kind, "
    77	                "expected_cadence = EXCLUDED.expected_cadence, "
    78	                "timeout_s = EXCLUDED.timeout_s, "
    79	                "heartbeat_source = EXCLUDED.heartbeat_source, updated_at = now()",
    80	                (
    81	                    spec.label,
    82	                    spec.kind.value,
    83	                    spec.cadence,
    84	                    spec.timeout_s,
    85	                    spec.supervisor.value,
    86	                ),
    87	            )
    88	
    89	    def register_all(self, registry, *, allow_prod: bool = False) -> list[str]:
    90	        self.ensure_schema(allow_prod=allow_prod)
    91	        for spec in registry.jobs:
    92	            self.register(spec, allow_prod=allow_prod)
    93	        return [s.label for s in registry.jobs]
    94	
    95	    # -- reads --------------------------------------------------------
    96	
    97	    def get(self, label: str) -> Optional[dict[str, Any]]:
    98	        with self._connect() as conn:
    99	            cur = conn.execute("SELECT * FROM cobalt_jobs WHERE label = %s", (label,))
   100	            row = cur.fetchone()
   101	            if row is None:
   102	                return None
   103	            return dict(zip([d.name for d in cur.description], row))
   104	
   105	    def all(self) -> list[dict[str, Any]]:
   106	        with self._connect() as conn:
   107	            cur = conn.execute("SELECT * FROM cobalt_jobs ORDER BY kind DESC, label")
   108	            columns = [d.name for d in cur.description]
   109	            return [dict(zip(columns, r)) for r in cur.fetchall()]
   110	
   111	    # -- the run lifecycle (the wrapper's three calls) -----------------
   112	
   113	    def mark_running(self, label: str, *, now: Optional[datetime] = None) -> None:
   114	        ts = now or clock_mod.now_utc()
   115	        with self._connect() as conn:
   116	            cur = conn.execute(
   117	                "UPDATE cobalt_jobs SET state = %s, started_at = %s, heartbeat_at = %s, "
   118	                "finished_at = NULL, exit_code = NULL, last_error = NULL, "
   119	                "updated_at = now() WHERE label = %s",
   120	                (JobState.RUNNING.value, ts, ts, label),
   121	            )
   122	            if cur.rowcount != 1:
   123	                raise JobStoreError(
   124	                    f"no jobs row for {label!r} — register it first "
   125	                    "(`cobalt jobs register`). F17 refuses to run a job it cannot "
   126	                    "report on: an unregistered job that hangs is invisible."
   127	                )
   128	
   129	    def beat(self, label: str, *, now: Optional[datetime] = None) -> None:
   130	        """Stamp `heartbeat_at`. The only thing separating a long job
   131	        from a hung one."""
   132	        with self._connect() as conn:
   133	            conn.execute(
   134	                "UPDATE cobalt_jobs SET heartbeat_at = %s, updated_at = now() WHERE label = %s",
   135	                (now or clock_mod.now_utc(), label),
   136	            )
   137	
   138	    def mark_finished(
   139	        self,
   140	        label: str,
   141	        *,
   142	        exit_code: int,
   143	        error: Optional[str] = None,
   144	        result: Optional[dict[str, Any]] = None,
   145	        now: Optional[datetime] = None,
   146	    ) -> None:
   147	        """`done` on 0, `failed` on anything else. Failed is LOUD: F18
   148	        turns red on this column, and the error text goes with it."""
   149	        ts = now or clock_mod.now_utc()
   150	        state = JobState.DONE if exit_code == 0 else JobState.FAILED
   151	        # F19: a job's own error text is outbound the moment F18 puts it
   152	        # in a DM. Redacting at the point of STORAGE means a traceback
   153	        # carrying a DSN never becomes a row that later leaks.
   154	        safe_error = None
   155	        if error:
   156	            from cobalt.redact import redact
   157	
   158	            safe_error = redact(error, channel="jobs.last_error").text
   159	        with self._connect() as conn:
   160	            conn.execute(
   161	                "UPDATE cobalt_jobs SET state = %s, finished_at = %s, heartbeat_at = %s, "
   162	                "exit_code = %s, last_error = %s, last_result = %s, updated_at = now() "
   163	                "WHERE label = %s",
   164	                (
   165	                    state.value,
   166	                    ts,
   167	                    ts,
   168	                    exit_code,
   169	                    safe_error,
   170	                    json.dumps(result, default=str) if result is not None else None,
   171	                    label,
   172	                ),
   173	            )
   174	
   175	    def mark_zombie(self, label: str, *, reason: str) -> None:
   176	        """The watchdog's conclusion. Nothing else may write this state."""
   177	        from cobalt.redact import redact
   178	
   179	        with self._connect() as conn:
   180	            conn.execute(
   181	                "UPDATE cobalt_jobs SET state = %s, last_error = %s, updated_at = now() "
   182	                "WHERE label = %s",
   183	                (JobState.ZOMBIE.value, redact(reason, channel="jobs.last_error").text, label),
   184	            )
   185	
   186	    def mark_probe(
   187	        self,
   188	        label: str,
   189	        *,
   190	        alive: bool,
   191	        detail: str,
   192	        now: Optional[datetime] = None,
   193	    ) -> None:
   194	        """Stamp a resident whose heartbeat comes from a PROBE, not from
   195	        itself (`supervisor: launchd | pidfile`).
   196	
   197	        A probe says "the process exists". That is a weaker claim than a
   198	        wrapper's "I am running and past my gates", which is why
   199	        `heartbeat_source` is a column: the two must never be read as the
   200	        same evidence.
   201	        """
   202	        from cobalt.redact import redact
   203	
   204	        ts = now or clock_mod.now_utc()
   205	        safe = redact(detail, channel="jobs.last_error").text
   206	        with self._connect() as conn:
   207	            if alive:
   208	                conn.execute(
   209	                    "UPDATE cobalt_jobs SET state = %s, heartbeat_at = %s, last_error = NULL, "
   210	                    "updated_at = now() WHERE label = %s",

codex
The brief now specifies corrective alerts, durable vault outcomes, wrapper startup during a database outage, and migration digest handling. I’m checking whether the restart rule closes round 2’s unknown-path gap and whether finalization keeps corrective alerts independent of database writes.
exec
/bin/zsh -lc "nl -ba src/cobalt/db_migrations/__init__.py; nl -ba src/cobalt/db_migrations/cli.py | sed -n '20,113p'; nl -ba src/cobalt/db_migrations/placement.py | sed -n '1,180p'; nl -ba configs/cobalt/jobs.yaml | sed -n '1,260p'; nl -ba src/cobalt/jobs/config.py | sed -n '215,315p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
     1	"""The two-layer data model's migrations (ADR-0008).
     2	
     3	`0001_schemas.sql`  — schemas, roles, grants, ownership, `"user".traders`,
     4	                      the `cobalt.trader_id` GUC convention.
     5	`0002_move_tables.sql` — every new-core table onto its side, plus
     6	                      `user_id` on the user side.
     7	`0002_move_tables.rollback.sql` — the reverse, catalog-only.
     8	
     9	These are the DATABASE-WIDE migrations and they are the only ones that
    10	live outside a feature module. A module's own DDL still lives in its own
    11	`migrations/` directory and is still executed by its store's
    12	`ensure_schema()`; those files create tables UNQUALIFIED and land them in
    13	whichever schema the factory pinned on the connection.
    14	
    15	Run them with `cobalt db migrate` (`--allow-prod` from ~/cobalt only,
    16	`--rollback` to reverse 0002). Nothing runs them implicitly: a store's
    17	`ensure_schema()` asserts the schemas exist and tells you to run the CLI.
    18	"""
    19	
    20	from pathlib import Path
    21	
    22	MIGRATIONS_DIR = Path(__file__).parent
    23	
    24	#: Applied in this order, every time, both idempotent.
    25	FORWARD = (
    26	    MIGRATIONS_DIR / "0001_schemas.sql",
    27	    MIGRATIONS_DIR / "0002_move_tables.sql",
    28	)
    29	
    30	#: `--rollback`. 0001 is deliberately NOT reversed — see the file header.
    31	REVERSE = (MIGRATIONS_DIR / "0002_move_tables.rollback.sql",)
    32	
    33	__all__ = ["FORWARD", "MIGRATIONS_DIR", "REVERSE"]
    20	
    21	ORDERED BY THE PRIMARY KEY, read from the catalog per table rather than
    22	hard-coded: `bars` is keyed `(ticker, interval, ts)`, `day_modes` by
    23	`trade_date`, `cobalt_jobs` by `label`, the rest by `id`.
    24	
    25	`--rollback` runs `0002_move_tables.rollback.sql` (catalog-only reverse)
    26	and prints the same proof table. Running `migrate`, then `--rollback`,
    27	then `migrate` again must land on the same digests — the suite asserts
    28	exactly that round-trip on `cobalt_dev`.
    29	
    30	`--allow-prod` reaches `cobalt_brain` without flipping the process into
    31	production mode (RULING 7's one-off-tooling seam). Without it the target
    32	is whatever `COBALT_ENV` resolves.
    33	"""
    34	
    35	from __future__ import annotations
    36	
    37	import argparse
    38	from typing import Optional
    39	
    40	from psycopg import sql
    41	
    42	from cobalt import db, env
    43	
    44	from . import FORWARD, REVERSE
    45	from .placement import MOVED_TABLES, SEEDED_TABLES
    46	
    47	#: The tenancy column the digest ignores — see the module docstring.
    48	TENANCY_COLUMN = "user_id"
    49	
    50	#: Where a new-core table may legitimately be found, in look-up order.
    51	SEARCHED_SCHEMAS = ("public", "user", "system")
    52	
    53	
    54	class MigrationError(RuntimeError):
    55	    """The migration could not be run or could not be proven."""
    56	
    57	
    58	def _schema_of(conn, table: str) -> Optional[str]:
    59	    row = conn.execute(
    60	        "SELECT schemaname FROM pg_tables "
    61	        "WHERE tablename = %s AND schemaname = ANY(%s) LIMIT 1",
    62	        (table, list(SEARCHED_SCHEMAS)),
    63	    ).fetchone()
    64	    return row[0] if row else None
    65	
    66	
    67	def _pk_columns(conn, schema: str, table: str) -> list[str]:
    68	    rows = conn.execute(
    69	        """
    70	        SELECT a.attname
    71	        FROM pg_index i
    72	        JOIN pg_attribute a
    73	          ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
    74	        WHERE i.indrelid = (quote_ident(%s) || '.' || quote_ident(%s))::regclass
    75	          AND i.indisprimary
    76	        ORDER BY array_position(i.indkey::int2[], a.attnum)
    77	        """,
    78	        (schema, table),
    79	    ).fetchall()
    80	    if not rows:
    81	        raise MigrationError(
    82	            f"{schema}.{table} has no primary key, so its rows cannot be put in a "
    83	            "deterministic order and no content digest can be taken. Every "
    84	            "new-core table has one; this is a real finding, not a tooling gap."
    85	        )
    86	    return [r[0] for r in rows]
    87	
    88	
    89	def _probe(conn, table: str) -> dict:
    90	    """(schema, rows, digest) for `table`, wherever it currently lives."""
    91	    schema = _schema_of(conn, table)
    92	    if schema is None:
    93	        return {"schema": None, "rows": None, "digest": None}
    94	    pk = _pk_columns(conn, schema, table)
    95	    query = sql.SQL(
    96	        "SELECT count(*), "
    97	        "md5(coalesce(string_agg((to_jsonb(t) - {tenancy})::text, '|' ORDER BY {order}), '')) "
    98	        "FROM {rel} AS t"
    99	    ).format(
   100	        tenancy=sql.Literal(TENANCY_COLUMN),
   101	        order=sql.SQL(", ").join(sql.Identifier("t", c) for c in pk),
   102	        rel=sql.Identifier(schema, table),
   103	    )
   104	    rows, digest = conn.execute(query).fetchone()
   105	    return {"schema": schema, "rows": int(rows), "digest": digest}
   106	
   107	
   108	def _probe_all(conn) -> dict[str, dict]:
   109	    tables = {**MOVED_TABLES, **SEEDED_TABLES}
   110	    return {t: _probe(conn, t) for t in sorted(tables)}
   111	
   112	
   113	def _print_proof(before: dict[str, dict], after: dict[str, dict]) -> int:
     1	"""The placement map: which side every table is on (ADR-0008 D2).
     2	
     3	ONE MAP, THREE READERS. The suite's placement test compares it against
     4	what the database actually holds; the lint test compares every store's
     5	SQL against its own `SIDE`; and a test asserts this map and
     6	`0002_move_tables.sql` name the same tables on the same sides, so the
     7	Python copy and the SQL copy cannot drift apart in silence.
     8	
     9	FUTURE TABLES ARE DECLARED HERE BEFORE THEY EXIST. That is the point of
    10	the map: ADR-0008 D2 names the S2/S3 tables (`trade_defs`, `tunables`,
    11	`trader_settings`, `radar_pool`, `radar_membership`, the legs/fills and
    12	missed rows, the taxonomy anatomy instances) so that when one of them is
    13	created it lands on a side someone already ruled on. A table that exists
    14	in `"user"` or `system` and is NOT in this map fails the placement test;
    15	so does a table on the wrong side.
    16	
    17	`public` IS FROZEN. The 17 old-tree tables are listed and untouched
    18	(strangler rule). A NEW table landing in `public` fails the suite — that
    19	is the whole enforcement behind "every new table is declared on a side".
    20	"""
    21	
    22	from cobalt.db import Side
    23	
    24	#: The 12 tables `0002_move_tables.sql` moves out of `public`.
    25	#: `"user".traders` is not here: 0001 creates it directly on its side.
    26	MOVED_TABLES: dict[str, Side] = {
    27	    # --- user side -----------------------------------------------------
    28	    "aset_sizings": Side.USER,
    29	    "card_transitions": Side.USER,
    30	    "card_stop_edits": Side.USER,
    31	    "day_modes": Side.USER,
    32	    "vault_writes": Side.USER,
    33	    "vault_overrides": Side.USER,
    34	    # --- system side ---------------------------------------------------
    35	    "bars": Side.SYSTEM,
    36	    "cobalt_jobs": Side.SYSTEM,
    37	    "cobalt_kill_switch": Side.SYSTEM,
    38	    "cobalt_redactions": Side.SYSTEM,
    39	    "cobalt_email_sends": Side.SYSTEM,
    40	    "session_blocks": Side.SYSTEM,
    41	}
    42	
    43	#: Created by 0001 on its side, never moved.
    44	SEEDED_TABLES: dict[str, Side] = {
    45	    "traders": Side.USER,
    46	}
    47	
    48	#: Created by a FEATURE MODULE's own migration, directly on its side —
    49	#: `<module>/migrations/*.sql`, executed by that module's store, the way
    50	#: every other table in the new core is created. They were never in
    51	#: `public`, so `0002_move_tables.sql` does not name them and the migrate
    52	#: proof table does not carry them; the placement test does.
    53	MODULE_TABLES: dict[str, Side] = {
    54	    # taxonomy/migrations/0001_trade_defs.sql (ADR-0008 D3)
    55	    "trade_defs": Side.USER,
    56	    "tunables": Side.USER,
    57	    "setup_trade_matrix": Side.USER,   # a VIEW unnested from trade_defs.def
    58	    # settings/migrations/0001_trader_settings.sql (ADR-0008 D3.4)
    59	    "trader_settings": Side.USER,
    60	}
    61	
    62	#: Declared by ADR-0008 D2 before they are built, so the first migration
    63	#: that creates one has a ruled side to create it on. Nothing here exists
    64	#: yet; the placement test only checks tables that DO exist.
    65	DECLARED_TABLES: dict[str, Side] = {
    66	    # S2-P4 / S3 — named now so the placement test knows them on sight.
    67	    "legs": Side.USER,
    68	    "fills": Side.USER,
    69	    "missed": Side.USER,
    70	    "drc_rows": Side.USER,
    71	    "prediction_records": Side.USER,
    72	    # S2-P1 — the radar. System: the pool and its membership history are
    73	    # engine artefacts any trader's strategies plug into.
    74	    "radar_pool": Side.SYSTEM,
    75	    "radar_membership": Side.SYSTEM,
    76	    # S2-P2 — taxonomy anatomy instances (regime, range, gap, extension,
    77	    # leg, session clock). The anatomy IS the system.
    78	    "anatomy_instances": Side.SYSTEM,
    79	}
    80	
    81	#: Every table this codebase has ruled on.
    82	PLACEMENT: dict[str, Side] = {
    83	    **MOVED_TABLES,
    84	    **SEEDED_TABLES,
    85	    **MODULE_TABLES,
    86	    **DECLARED_TABLES,
    87	}
    88	
    89	#: The old tree's tables, frozen in `public` and never touched
    90	#: (strangler rule). They exist in `cobalt_brain`; `cobalt_dev` has none
    91	#: of them, so the test asserts containment, not equality.
    92	OLD_TREE_PUBLIC_TABLES: frozenset[str] = frozenset({
    93	    "memory_logs",
    94	    "graph_nodes",
    95	    "graph_edges",
    96	    "hitl_proposals",
    97	    "browser_fast_path",
    98	    "instruments",
    99	    "market_snapshots",
   100	    "daily_in_play",
   101	    "key_levels",
   102	    "news_events",
   103	    "news_mentions",
   104	    "order_fills",
   105	    "strategy_signals",
   106	    "system_alerts",
   107	    "themes",
   108	    "trades",
   109	    "trading_accounts",
   110	})
   111	
   112	
   113	def side_of(table: str) -> Side:
   114	    """The ruled side of `table`, or a loud failure naming this file."""
   115	    try:
   116	        return PLACEMENT[table]
   117	    except KeyError:
   118	        raise KeyError(
   119	            f"table {table!r} has no ruled side. Every new table is declared on "
   120	            "exactly one side in cobalt/db_migrations/placement.py (ADR-0008 D2) "
   121	            "before it is created."
   122	        ) from None
   123	
   124	
   125	def tables_on(side: Side) -> frozenset[str]:
   126	    """Every ruled table on `side`, declared-but-unbuilt ones included."""
   127	    return frozenset(t for t, s in PLACEMENT.items() if s is side)
   128	
   129	
   130	__all__ = [
   131	    "DECLARED_TABLES",
   132	    "MODULE_TABLES",
   133	    "MOVED_TABLES",
   134	    "OLD_TREE_PUBLIC_TABLES",
   135	    "PLACEMENT",
   136	    "SEEDED_TABLES",
   137	    "side_of",
   138	    "tables_on",
   139	]
     1	# F17 TASK INTEGRITY — the job registry (Charter §3 F17, L18).
     2	#
     3	# Schema: src/cobalt/jobs/config.py. Pydantic-validated on load; a bad
     4	# row CRASHES with its label. `cobalt validate` cross-checks this file
     5	# against ops/*.plist and fails on a job in one and not the other —
     6	# a registry that has drifted from launchd is a registry that reports
     7	# green for a job that no longer exists.
     8	#
     9	# ---------------------------------------------------------------------
    10	# WHAT A ROW MEANS
    11	# ---------------------------------------------------------------------
    12	# label     : the launchd label, exactly. It is the join key everywhere.
    13	# kind      : resident (runs continuously) | one-shot (runs and exits).
    14	# supervisor: WHO stamps `heartbeat_at`, and this is the honest part —
    15	#             `self`    Cobalt's own code, through the wrapper
    16	#                       (src/cobalt/jobs/wrapper.py). The process says it
    17	#                       is alive because it IS alive and running our code.
    18	#             `launchd` launchd holds a live PID for it. Cobalt does not
    19	#                       run inside it (Obsidian, the LM Studio server) or
    20	#                       does not want a heartbeat thread in it (the ASET
    21	#                       sheet). The WATCHDOG stamps from a real
    22	#                       `launchctl` probe, and the row says so, so nothing
    23	#                       pretends the process reported in itself.
    24	#             `pidfile` the process is not launchd's own child — see
    25	#                       com.cobalt.agent below.
    26	# enabled   : is this plist supposed to be LOADED in launchd right now?
    27	#             Defaults true, which is what every row has always meant.
    28	#             `false` is the declared case of a job that is built,
    29	#             registered and reviewable but NOT yet handed over — the
    30	#             sweep reports it and probes nothing, so a deliberate state
    31	#             never shows up as a standing red.
    32	# timeout_s : how long a run may take before a stale heartbeat means
    33	#             ZOMBIE. The wrapper stamps at least every timeout_s/3.
    34	# schedule  : mirrors the plist. launchd cannot read this file and this
    35	#             file cannot read launchd, so `cobalt validate` compares
    36	#             them and a drift is loud.
    37	jobs:
    38	  # ---------------- residents ----------------
    39	  - label: com.cobalt.aset
    40	    kind: resident
    41	    supervisor: launchd
    42	    # The ASET sheet (ops/start_aset.sh -> uvicorn). It is Cobalt's own
    43	    # code, but it is a request-driven server: a heartbeat thread inside
    44	    # it would report "the process exists", which is exactly what the
    45	    # launchd probe already reports, and F18 additionally probes the
    46	    # sheet's HTTP 200 — which is the thing that actually matters and
    47	    # that a thread could not tell us (S1-P2 watched this process serve
    48	    # 500s while perfectly alive).
    49	    timeout_s: 300
    50	    # WHAT THIS PROCESS RE-READS ON EVERY REQUEST — derived by measuring
    51	    # the request path (instrumented `open`/`read_text` over GET / and
    52	    # GET /api/health), not by reading config names off a shelf. Each
    53	    # entry cites its loader call in the 2026-09-09 ops report.
    54	    #
    55	    # It is the reason the field exists. On 09-08 a deploy added a
    56	    # `TunableUnit.WINDOW` row to tunables.yaml and said "nothing else is
    57	    # restarted"; this process re-read the new file through code that
    58	    # predated the enum value, and from ~19:00 to 07:06 the page he
    59	    # trades beside answered HTTP 200 and refused every card.
    60	    #
    61	    # NOT LISTED, and the omission is the point: `configs/dev/vault.yaml`
    62	    # IS re-read per request in dev (cobalt/vault.py:167) but NOT in
    63	    # production, where COBALT_VAULT_PATH is set in this job's own plist
    64	    # and the resolver returns before it reads the file. A row here that
    65	    # is only true in dev would send an operator to restart the sheet for
    66	    # a file production never opens.
    67	    reads:
    68	      - "configs/dev/aset.yaml"                    # aset/config.py:134 (load_config); the name says dev, but there is no configs/cobalt/aset.yaml — this IS the production sheet's config
    69	      - "configs/cobalt/taxonomy/tunables.yaml"    # taxonomy/loader.py:79 (load_tunables); the 09-09 R1 case
    70	    what: "the ASET semi-auto sheet on :5010 — the surface he trades beside"
    71	
    72	  - label: com.cobalt.mainframe
    73	    kind: resident
    74	    supervisor: launchd
    75	    timeout_s: 600
    76	    # EMPTY, derived: LM Studio is not Cobalt code and reads its own
    77	    # `~/.lmstudio/` config, which is not repo-relative. Nothing in
    78	    # configs/ reaches this process.
    79	    reads: []
    80	    what: "the LM Studio local-model server (ops/start_mainframe.sh), the L23 local lane"
    81	
    82	  - label: com.cobalt.obsidian
    83	    kind: resident
    84	    supervisor: launchd
    85	    timeout_s: 300
    86	    what: >
    87	      Obsidian as a supervised service (RULING 6). Not decoration: the
    88	      vault reaches his other devices only through a RUNNING Obsidian on
    89	      this Mac, and on 09-04 a correct 05:15 write was silently
    90	      overwritten because none was running.
    91	    # EMPTY, derived: Obsidian is a third-party app. It reads the vault's
    92	    # own .obsidian/ directory, never configs/.
    93	    reads: []
    94	
    95	  - label: com.cobalt.agent
    96	    kind: resident
    97	    supervisor: pidfile
    98	    pidfile: logs/cobalt.pid
    99	    timeout_s: 600
   100	    # WHAT com.cobalt.agent IS (S1-P3 answer to the prompt's question).
   101	    # It is the OLD TREE's agent: the plist runs `cobalt.sh start`, which
   102	    # pre-flight-checks LM Studio/Postgres/Mattermost and then
   103	    # `nohup uv run src/cobalt_agent/main.py &` — the Mattermost
   104	    # websocket listener, the scheduler, the Scribe, the memory layer.
   105	    #
   106	    # It is registered as `pidfile` and not `launchd` because of a real
   107	    # shape, not a preference: cobalt.sh spawns the agent detached
   108	    # (`nohup`, and the plist sets AbandonProcessGroup) and EXITS 0. So
   109	    # launchd sees a one-shot that completed successfully and holds no
   110	    # PID — `launchctl list` shows `- 0` for this label whether the agent
   111	    # is running or dead. The only truthful liveness signal is the PID
   112	    # file cobalt.sh writes.
   113	    #
   114	    # It gets a row because F18 must be able to say it is down; it gets
   115	    # no wrapper because the strangler rule (CLAUDE.md) says the old tree
   116	    # stays untouched and no new-core code is added to it.
   117	    # EMPTY, and it needs the caveat. The old tree loads `configs/*.yaml`
   118	    # ONCE into a singleton at first construction
   119	    # (cobalt_agent/config.py:410) and `Config.load()` returns the cached
   120	    # object thereafter — so it does not RE-READ anything, which is what
   121	    # this field records. It still has to be restarted when one of those
   122	    # files changes, because it is running the old values. That is the
   123	    # read-once class; it wants its own field (09-09 ESCALATE).
   124	    reads: []
   125	    what: "the OLD-TREE agent (cobalt.sh start -> cobalt_agent/main.py), detached; liveness from its PID file"
   126	
   127	  - label: com.cobalt.herdr
   128	    kind: resident
   129	    supervisor: launchd
   130	    # BUILT, NOT LOADED (2026-09-08). See ops/com.cobalt.herdr.plist and
   131	    # the "herdr handover" procedure in ops/README.md. The flag comes off
   132	    # at the Mac keyboard, as the LAST step of that procedure, because
   133	    # the server being registered is the one hosting the session that
   134	    # would register it — bootstrapping it from inside a herdr pane takes
   135	    # that pane down mid-command.
   136	    enabled: true
   137	    # `launchd`, not `self`: herdr is not Cobalt code and will never
   138	    # carry our wrapper. The watchdog probes launchctl and stamps on its
   139	    # behalf, and the row says so, so nothing reads "the process exists"
   140	    # as "the server is answering". The F18 probe `herdr` asks the
   141	    # second question separately — socket + agent list — for the same
   142	    # reason the ASET sheet gets an HTTP probe next to its PID probe.
   143	    timeout_s: 300
   144	    # EMPTY, derived: herdr is not Cobalt code. Its config is
   145	    # `~/.config/herdr/config.toml` (and `herdr server reload-config`
   146	    # re-reads it without a restart) — not repo-relative, so no deploy of
   147	    # ours can change it.
   148	    reads: []
   149	    what: "the herdr server — the terminal workspace hosting every agent seat"
   150	
   151	  # ---------------- one-shots ----------------
   152	  - label: com.cobalt.prefill-daily
   153	    kind: one-shot
   154	    supervisor: self
   155	    timeout_s: 600
   156	    schedule: {at: "05:15", weekdays: [1, 2, 3, 4, 5]}
   157	    what: "the morning daily-note prefill (uv run prefill daily)"
   158	
   159	  - label: com.cobalt.prefill-drc
   160	    kind: one-shot
   161	    supervisor: self
   162	    timeout_s: 600
   163	    schedule: {at: "15:40", weekdays: [1, 2, 3, 4, 5]}
   164	    what: "the evening DRC prefill (uv run prefill drc)"
   165	
   166	  - label: com.cobalt.archiver
   167	    kind: one-shot
   168	    supervisor: self
   169	    # The nightly full run took 23m04s and 23m11s on the last two nights.
   170	    # 90 minutes is not a target, it is the point past which a silent
   171	    # hang is more likely than a slow night.
   172	    timeout_s: 5400
   173	    schedule: {at: "20:30", weekdays: [1, 2, 3, 4, 5]}
   174	    what: "the Bar Archiver nightly full run (uv run archiver)"
   175	
   176	  - label: com.cobalt.cards-expire
   177	    kind: one-shot
   178	    supervisor: self
   179	    timeout_s: 300
   180	    schedule: {at: "16:05", weekdays: [1, 2, 3, 4, 5]}
   181	    what: "expire cards whose window closed (uv run cobalt cards expire)"
   182	
   183	  - label: com.cobalt.daymode-propose
   184	    kind: one-shot
   185	    supervisor: self
   186	    timeout_s: 300
   187	    schedule: {at: "09:00", weekdays: [1, 2, 3, 4, 5]}
   188	    what: "the 09:00 day-mode proposal (uv run cobalt daymode propose)"
   189	
   190	  - label: com.cobalt.backup
   191	    kind: one-shot
   192	    supervisor: self
   193	    # An hour. The first real snapshot took minutes, but the number that
   194	    # matters is the one a FULL re-read takes on a bad night — restic
   195	    # rescans every source file when its cache is cold, and the dump
   196	    # alone is 360 MB.
   197	    timeout_s: 3600
   198	    # EVERY day including weekends, and after the archiver's 20:30 (which
   199	    # takes ~23 min) so the snapshot contains that night's bars rather
   200	    # than racing them. A vault edit on a Saturday is exactly as
   201	    # unrecoverable as one on a Tuesday.
   202	    schedule: {at: "21:40", weekdays: [0, 1, 2, 3, 4, 5, 6]}
   203	    what: "the nightly restic snapshot — vault + a fresh cobalt_brain dump, to the SSD"
   204	
   205	  - label: com.cobalt.heartbeat
   206	    kind: one-shot
   207	    supervisor: self
   208	    timeout_s: 300
   209	    # EVERY interval, all week. The heartbeat is the thing that notices a
   210	    # weekend failure before Monday morning needs it.
   211	    schedule: {every_min_tunable: heartbeat.interval_min}
   212	    what: "the F18 heartbeat host — probes everything above and says so out loud"
   213	
   214	  - label: com.cobalt.seat-usage
   215	    kind: one-shot
   216	    supervisor: self
   217	    timeout_s: 300
   218	    # An INTERVAL inside a WINDOW, both from tunables rows (F16). launchd
   219	    # has no such shape natively, so the plist carries the window expanded
   220	    # into one StartCalendarInterval entry per firing and the suite
   221	    # compares the two — see Schedule.calendar_entries().
   222	    schedule:
   223	      every_min_tunable: seat_usage.interval_min
   224	      window_tunable: seat_usage.window
   225	      weekdays: [0, 1, 2, 3, 4, 5, 6]
   226	    what: "the hourly seat-usage report (uv run cobalt seat-usage run) — what the seats cost today"
   227	
   228	  - label: com.cobalt.generated
   229	    kind: one-shot
   230	    supervisor: self
   231	    timeout_s: 300
   232	    # 23:37 ET, EVERY DAY. After the last seat-usage run (23:00) and well
   233	    # after the archiver's 20:30 + the backup's 21:40, so the day's
   234	    # rewrites are all on disk before this looks. Not on the hour, and
   235	    # not on a round five: a scheduled `git add` should not share its
   236	    # minute with anything, and an odd minute is the cheapest way to say
   237	    # so. Weekends included — the seat-usage report is rewritten on a
   238	    # Saturday exactly as it is on a Tuesday.
   239	    schedule: {at: "23:37", weekdays: [0, 1, 2, 3, 4, 5, 6]}
   240	    what: >
   241	      commit the generated files a job rewrote today (uv run cobalt
   242	      generated commit). configs/cobalt/generated.yaml is the declared
   243	      list; the command refuses off `main`, mid-merge, or with anything
   244	      already staged, and it NEVER pushes. It exists because ~/cobalt IS
   245	      production and a permanently dirty working tree is one nobody
   246	      reads.
   247	
   248	# THE KILL PHRASE (F17d). Config, not a literal: `cobalt stop` and any
   249	# future DM listener compare against this exact string.
   250	kill_phrase: "COBALT STOP"
   251	resume_phrase: "COBALT RESUME"
   215	            last = closes.hour * 60 + closes.minute
   216	            while cursor <= last:
   217	                entries.append(
   218	                    {"Weekday": day, "Hour": cursor // 60, "Minute": cursor % 60}
   219	                )
   220	                cursor += minutes
   221	        return entries
   222	
   223	
   224	class JobSpec(BaseModel):
   225	    model_config = ConfigDict(extra="forbid")
   226	
   227	    label: str = Field(min_length=1)
   228	    kind: JobKind
   229	    supervisor: Supervisor
   230	    timeout_s: int = Field(gt=0)
   231	    what: str = Field(min_length=1)
   232	    schedule: Optional[Schedule] = None
   233	    pidfile: Optional[str] = None
   234	    #: Is this job's plist supposed to be LOADED in launchd right now?
   235	    #:
   236	    #: Default True, because that is what every job in this registry has
   237	    #: always meant. `enabled: false` is the narrow, declared case of a
   238	    #: job that is BUILT, registered and reviewable but deliberately not
   239	    #: yet handed over to launchd — `com.cobalt.herdr` is the first, and
   240	    #: it exists because the handover has to happen at the keyboard (the
   241	    #: server being registered is the one hosting the session that would
   242	    #: register it).
   243	    #:
   244	    #: THE FLAG SUPPRESSES THE PROBE, NOT THE ROW. A disabled job is
   245	    #: still in the registry, still has to have a plist in ops/, still
   246	    #: has its schedule cross-checked by the suite. What it does not get
   247	    #: is a red "NOT LOADED in launchd" every 15 minutes for a state
   248	    #: somebody chose on purpose — which is exactly the kind of standing
   249	    #: red that teaches a reader to scroll past the heartbeat.
   250	    #:
   251	    #: Flipping it to true is the LAST step of a handover, after the
   252	    #: bootstrap: true means "launchd should hold this, tell me if it
   253	    #: does not".
   254	    enabled: bool = True
   255	
   256	    #: Repo-relative config files this RESIDENT RE-READS AT RUNTIME.
   257	    #:
   258	    #: THE LAW THIS SERVES, ruled three times (2026-09-04, 2026-09-08 on
   259	    #: aset.yaml, 2026-09-09 on tunables.yaml): a config-shape change and
   260	    #: the restart of every resident that reads that file are ONE ACTION.
   261	    #: The 09-09 case is the one to remember — the 09-08 seat-usage deploy
   262	    #: added a `TunableUnit.WINDOW` row to tunables.yaml and its plan said
   263	    #: "nothing else is restarted". The ASET sheet re-reads that file on
   264	    #: every request, through code that predated the enum value, so from
   265	    #: roughly 19:00 to 07:06 the page he trades beside answered HTTP 200
   266	    #: and refused every card. The deploy was right about its own job and
   267	    #: wrong about everybody else's.
   268	    #:
   269	    #: EVERY ENTRY IS DERIVED FROM THE CODE, never guessed: a row here
   270	    #: claims that a specific loader call reads a specific file on a
   271	    #: request path, and the 2026-09-09 ops report cites file:line for
   272	    #: each one. A guessed row is worse than an empty list, because
   273	    #: `cobalt jobs readers` is trusted to be complete.
   274	    #:
   275	    #: ONE-SHOTS LEAVE IT EMPTY, and `cobalt validate` enforces that: a
   276	    #: one-shot re-reads everything every time it runs, by definition —
   277	    #: it starts, reads, exits. There is no stale process to restart, so
   278	    #: rows here would be noise diluting the ones that mean something.
   279	    #:
   280	    #: KNOWN GAP, deliberately not papered over: this is RE-READS, not
   281	    #: reads. A resident that loads a config ONCE AT STARTUP also needs a
   282	    #: restart when it changes, and `com.cobalt.agent` (the old tree) is
   283	    #: exactly that shape — it caches settings in a singleton at first
   284	    #: construction (`cobalt_agent/config.py:410`). That wants its own
   285	    #: field; see the 09-09 report's ESCALATE.
   286	    reads: list[str] = Field(default_factory=list)
   287	
   288	    @model_validator(mode="after")
   289	    def _shape_matches_kind(self) -> "JobSpec":
   290	        if self.kind is JobKind.ONE_SHOT and self.reads:
   291	            raise ValueError(
   292	                f"{self.label}: `reads` belongs to a RESIDENT. A one-shot re-reads "
   293	                "everything every time it runs — there is no stale process to "
   294	                "restart, so naming files here dilutes the rows that do mean "
   295	                "something."
   296	            )
   297	        bad = [p for p in self.reads if Path(p).is_absolute() or ".." in Path(p).parts]
   298	        if bad:
   299	            raise ValueError(
   300	                f"{self.label}: `reads` entries are REPO-RELATIVE with no `..`: {bad}"
   301	            )
   302	        if self.kind is JobKind.ONE_SHOT and self.schedule is None:
   303	            raise ValueError(
   304	                f"{self.label}: a one-shot needs a `schedule` — the MISSED probe "
   305	                "asks 'should this have run by now', and without a schedule there "
   306	                "is no answer, only silence."
   307	            )
   308	        if self.supervisor is Supervisor.PIDFILE and not self.pidfile:
   309	            raise ValueError(f"{self.label}: supervisor `pidfile` needs a `pidfile` path")
   310	        if self.supervisor is not Supervisor.PIDFILE and self.pidfile:
   311	            raise ValueError(
   312	                f"{self.label}: `pidfile` is set but the supervisor is "
   313	                f"{self.supervisor} — nothing would read it."
   314	            )
   315	        return self

exec
/bin/zsh -lc "rg -n 'load_job_registry|jobs\\.yaml|reads:' src/cobalt/aset configs/cobalt/jobs.yaml src/cobalt/jobs; rg -n 'class WriteResult|write_id|return WriteResult|unchanged' src/cobalt/vaultwrite/writer.py; nl -ba src/cobalt/heartbeat/probes.py | sed -n '35,85p;310,355p'; nl -ba src/cobalt/session/clock.py | sed -n '183,230p'; nl -ba src/cobalt/jobs/killswitch.py | sed -n '35,110p'; nl -ba ops/com.cobalt.heartbeat.plist | sed -n '10,60p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
configs/cobalt/jobs.yaml:67:    reads:
configs/cobalt/jobs.yaml:79:    reads: []
configs/cobalt/jobs.yaml:93:    reads: []
configs/cobalt/jobs.yaml:124:    reads: []
configs/cobalt/jobs.yaml:148:    reads: []
src/cobalt/jobs/cli.py:4:    cobalt jobs register                 upsert every row from jobs.yaml
src/cobalt/jobs/cli.py:24:from .config import load_job_registry
src/cobalt/jobs/cli.py:65:    registry = load_job_registry()
src/cobalt/jobs/cli.py:95:    registry = load_job_registry()
src/cobalt/jobs/cli.py:168:    reg = jsub.add_parser("register", help="Upsert every row from configs/cobalt/jobs.yaml.")
src/cobalt/jobs/cli.py:195:    stop.add_argument("--phrase", default=None, help="Defaults to jobs.yaml's kill_phrase.")
src/cobalt/jobs/entrypoint.py:49:        from .config import load_job_registry
src/cobalt/jobs/entrypoint.py:51:        yield JobRun(load_job_registry().spec(label))
src/cobalt/jobs/__init__.py:6:* `config.py`     — the registry, `configs/cobalt/jobs.yaml`, one row per
src/cobalt/jobs/__init__.py:21:from .config import JobConfigError, JobRegistry, JobSpec, load_job_registry
src/cobalt/jobs/__init__.py:43:    "load_job_registry",
src/cobalt/jobs/watchdog.py:42:from .config import JobRegistry, JobSpec, load_job_registry
src/cobalt/jobs/watchdog.py:304:    registry = registry or load_job_registry()
src/cobalt/jobs/watchdog.py:330:                    "configs/cobalt/jobs.yaml) — nothing is probed and nothing is "
src/cobalt/jobs/models.py:64:    #: its PID lives in a file. See com.cobalt.agent in jobs.yaml.
src/cobalt/jobs/config.py:1:"""F17 config: the job registry, `configs/cobalt/jobs.yaml`.
src/cobalt/jobs/config.py:22:CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "jobs.yaml"
src/cobalt/jobs/config.py:286:    reads: list[str] = Field(default_factory=list)
src/cobalt/jobs/config.py:290:        if self.kind is JobKind.ONE_SHOT and self.reads:
src/cobalt/jobs/config.py:378:                f"{', '.join(sorted(self.by_label))} (configs/cobalt/jobs.yaml)."
src/cobalt/jobs/config.py:382:def load_job_registry() -> JobRegistry:
src/cobalt/jobs/config.py:406:    "load_job_registry",
src/cobalt/jobs/wrapper.py:47:from .config import JobSpec, load_job_registry
src/cobalt/jobs/wrapper.py:130:    registry = load_job_registry()
src/cobalt/jobs/wrapper.py:170:    wrapped (see jobs.yaml), so this exists for the first new-core
src/cobalt/jobs/migrations/0001_cobalt_jobs.sql:22:-- configs/cobalt/jobs.yaml, ops/*.plist, `launchctl list`, and the F18
src/cobalt/jobs/migrations/0001_cobalt_jobs.sql:30:--   expected_cadence — rendered from the schedule in jobs.yaml, so the
src/cobalt/jobs/killswitch.py:34:from .config import load_job_registry
src/cobalt/jobs/killswitch.py:90:    registry = load_job_registry()
src/cobalt/jobs/killswitch.py:110:    core. The phrase is CONFIG (`configs/cobalt/jobs.yaml`), compared
src/cobalt/jobs/killswitch.py:114:    registry = load_job_registry()
src/cobalt/jobs/killswitch.py:119:    registry = load_job_registry()
246:class WriteResult:
248:    action: str  # created | updated | unchanged | skipped_exists | skipped | restored
253:    write_id: Optional[int] = None
276:        if self.write_id is not None:
277:            head += f" · write_id={self.write_id}"
326:# Actions that put (or would put) bytes on disk. "unchanged", "skipped"
335:    entry points rather than the ten `return WriteResult(...)` sites, so
522:        ) as write_id:
528:        return write_id
544:                write_id = self._persist_and_write(
553:            return (new_text, kwargs, write_id), snapshot
570:            return WriteResult(
589:            return WriteResult(
599:        write_id = self._persist_and_write(
612:        return WriteResult(
616:            write_id=write_id,
757:                state["unchanged"] = True
776:            return WriteResult(
783:            return WriteResult(
784:                path=path, action="unchanged", section=section, unit=unit_id,
790:        new_text, _kwargs, write_id = outcome
792:        return WriteResult(
794:            action="updated" if changed else "unchanged",
799:            write_id=write_id,
863:        for write_id, after in self.store.recent_afters(
868:            row = self.store.get_write(write_id)
872:                f"id {write_id}"
885:                write_id,
889:                text=human_body, missing=False, sync_revert_of=write_id, note=note
912:        Everything else L28 asks for still applies, unchanged: the same
976:            return WriteResult(
977:                path=path, action="unchanged", section=section_label, unit=region_id,
982:        new_text, _kwargs, write_id = outcome
984:        return WriteResult(
986:            action="updated" if changed else "unchanged",
991:            write_id=write_id,
1066:    def restore(self, write_id: int) -> WriteResult:
1094:          the original whole-section replace, unchanged. Rows written
1099:        row = store.get_write(write_id)
1101:            raise VaultWriteError(f"No vault_writes row with id {write_id}.")
1104:                f"vault_writes id {write_id} is a whole-file create (no section) — "
1109:                f"vault_writes id {write_id} created section {row['section']!r} "
1128:            why=f"restoring vault_writes id {write_id} is the rollback path — the "
1255:            return WriteResult(
1256:                path=path, action="unchanged", section=section_name, unit=row["unit"],
1258:                notes=[f"section {section_name!r} already matches vault_writes id {write_id}"],
1260:        new_text, _kwargs, new_write_id = outcome
1261:        return WriteResult(
1268:            write_id=new_write_id,
1271:            notes=[f"restored section {section_name!r} to vault_writes id {write_id} before-state"],
    35	    detail: str
    36	    #: True when the probe could not run. Still red — but an operator
    37	    #: needs to know they are looking at ignorance, not at a diagnosis.
    38	    unknown: bool = False
    39	
    40	    def line(self) -> str:
    41	        mark = "OK  " if self.ok else ("??  " if self.unknown else "RED ")
    42	        return f"{mark} {self.name:<24} {self.detail}"
    43	
    44	
    45	def _tunable(key: str):
    46	    from cobalt.taxonomy.loader import load_tunables
    47	
    48	    row = load_tunables().by_key.get(key)
    49	    if row is None:
    50	        raise RuntimeError(
    51	            f"tunable {key!r} is missing from tunables.yaml — the heartbeat reads "
    52	            "its thresholds from config and has no built-in defaults (F16)."
    53	        )
    54	    return row.value
    55	
    56	
    57	def probe_timeout_s() -> float:
    58	    return float(_tunable("heartbeat.probe_timeout_s"))
    59	
    60	
    61	# ---------------------------------------------------------------------
    62	
    63	
    64	def sheet_http(url: str = "http://127.0.0.1:5010/") -> Probe:
    65	    """The ASET sheet answers 200.
    66	
    67	    NOT the same question as "the process exists", and S1-P2 is why this
    68	    is a separate probe: reshaping `configs/cobalt/aset.yaml` took the
    69	    running sheet to HTTP 500 while the process stayed perfectly alive
    70	    and launchd stayed perfectly happy. The thing he trades beside is the
    71	    PAGE, not the PID.
    72	    """
    73	    try:
    74	        with urlrequest.urlopen(url, timeout=probe_timeout_s()) as resp:
    75	            code = resp.status
    76	        if code == 200:
    77	            return Probe("sheet HTTP", True, f"{url} -> 200")
    78	        return Probe("sheet HTTP", False, f"{url} -> {code} (expected 200)")
    79	    except Exception as e:  # noqa: BLE001
    80	        return Probe("sheet HTTP", False, f"{url} unreachable: {type(e).__name__}: {e}")
    81	
    82	
    83	#: How much of a config error's own message reaches the beat line. A
    84	#: `TaxonomyConfigError` runs to several hundred characters; the first
    85	#: 160 carry the name of the thing that broke, which is what a reader
   310	                     "holds NO snapshot yet")
   311	    hours = age.total_seconds() / 3600
   312	    detail = (f"newest snapshot {hours:.1f} h old across "
   313	              f"{', '.join(d.name for d in cfg.armed)}")
   314	    if age > max_age:
   315	        return Probe("backup", False,
   316	                     f"STALE — {detail} (limit {max_age.total_seconds()/3600:.0f} h)")
   317	    return Probe("backup", True, detail)
   318	
   319	
   320	def vaultwrite_blocks(now: Optional[datetime] = None) -> Probe:
   321	    """market_reset refusals + ungated migration runs since the last beat.
   322	
   323	    NOT RED ON ITS OWN. A refusal is the guard WORKING — F1 turning away
   324	    a write inside 20:00-21:00 is the system doing its job. The number is
   325	    reported because a spike means something is retrying blind, and
   326	    because the RULING on migration tooling (S1-P3, decided-with-veto)
   327	    says every ungated repair run inside the block increments this same
   328	    counter so it can never happen quietly.
   329	    """
   330	    from cobalt.session.store import SessionBlockStore
   331	
   332	    try:
   333	        store = SessionBlockStore()
   334	        counts = store.counts_over_window(now=now)
   335	    except Exception as e:  # noqa: BLE001
   336	        return Probe("vault blocks", False, f"counter unreadable: {type(e).__name__}: {e}",
   337	                     unknown=True)
   338	    refused = counts.get(SessionBlockStore.REFUSED, 0)
   339	    ungated = counts.get(SessionBlockStore.UNGATED_RUN, 0)
   340	    # BOTH numbers, always, and never summed into one. They share a
   341	    # counter because they are both "a write met the market_reset window"
   342	    # — but a refusal is the guard working and an ungated run is the
   343	    # carve-out being used, and reading five repairs as five refusals
   344	    # would send someone hunting a bug that is not there.
   345	    return Probe(
   346	        "vault blocks", True,
   347	        f"{refused} refused, {ungated} ungated repair run(s) in the counter window",
   348	    )
   349	
   350	
   351	def redactions(minutes: int, now: Optional[datetime] = None) -> Probe:
   352	    """F19 hits since the last beat.
   353	
   354	    Also not red on its own — the guard firing is the guard working. It
   355	    is on the block because a redaction count that suddenly climbs means
   183	            # purpose — but on a FULL day these two are the same instant
   184	            # by design, and a silent divergence would put an unnamed
   185	            # overnight sliver in the middle of the trading evening.
   186	            raise SessionError(
   187	                "session.market_reset_open "
   188	                f"({self._b['session.market_reset_open']:%H:%M}) must equal "
   189	                "session.aftermarket_close "
   190	                f"({self._b['session.aftermarket_close']:%H:%M}) — on a full "
   191	                "day market_reset begins the moment aftermarket ends"
   192	            )
   193	
   194	    # -- the day's shape ---------------------------------------------
   195	
   196	    def windows_for(self, day: date) -> list[Window]:
   197	        """The ordered [start, end) ET windows of `day`. Empty list = the
   198	        whole day is overnight (weekend or holiday)."""
   199	        if not self.calendar.is_trading_day(day):
   200	            return []
   201	
   202	        early = self.calendar.is_early_close(day)
   203	        rth_close = self._b[
   204	            "session.early_close.rth_close" if early else "session.rth_close"
   205	        ]
   206	        am_close = self._b[
   207	            "session.early_close.aftermarket_close" if early else "session.aftermarket_close"
   208	        ]
   209	        return [
   210	            Window(Session.PREMARKET, self._b["session.premarket_open"], self._b["session.rth_open"]),
   211	            Window(Session.RTH, self._b["session.rth_open"], rth_close),
   212	            Window(Session.AFTERMARKET, rth_close, am_close),
   213	            Window(
   214	                Session.MARKET_RESET,
   215	                self._b["session.market_reset_open"],
   216	                self._b["session.market_reset_close"],
   217	            ),
   218	        ]
   219	
   220	    # -- the two questions -------------------------------------------
   221	
   222	    def session(self, ts: datetime) -> Session:
   223	        """The session `ts` falls in. `ts` MUST be tz-aware."""
   224	        et = self.to_et(ts)
   225	        for window in self.windows_for(et.date()):
   226	            if window.start <= et.time() < window.end:
   227	                return window.session
   228	        return Session.OVERNIGHT
   229	
   230	    def next_boundary(self, ts: datetime) -> tuple[datetime, Session]:
    35	from .store import JobStore
    36	
    37	
    38	@dataclass(frozen=True)
    39	class KillState:
    40	    active: bool
    41	    phrase: Optional[str]
    42	    set_by: Optional[str]
    43	    set_at: Optional[object]
    44	
    45	    def describe(self) -> str:
    46	        if not self.active:
    47	            return "kill switch CLEAR — jobs run normally"
    48	        when = f" at {self.set_at:%Y-%m-%d %H:%M:%S %Z}" if self.set_at else ""
    49	        return (
    50	            f"KILL SWITCH ACTIVE — set by {self.set_by or 'unknown'}{when} "
    51	            f"(phrase: {self.phrase!r}). One-shots refuse to start; residents exit "
    52	            "cleanly at their next heartbeat. Clear it with `cobalt resume`."
    53	        )
    54	
    55	
    56	def read(store: Optional[JobStore] = None) -> KillState:
    57	    store = store or JobStore()
    58	    row = store.kill_switch()
    59	    return KillState(
    60	        active=bool(row.get("active")),
    61	        phrase=row.get("phrase"),
    62	        set_by=row.get("set_by"),
    63	        set_at=row.get("set_at"),
    64	    )
    65	
    66	
    67	def is_active(store: Optional[JobStore] = None) -> bool:
    68	    """Fail OPEN, deliberately, and loudly.
    69	
    70	    If the database cannot be reached the answer is "not stopped". The
    71	    alternative — a database blip silently stopping every scheduled job
    72	    on the host — is a far worse failure than one run happening after a
    73	    stop was requested, and it would look exactly like the kill switch
    74	    working correctly.
    75	    """
    76	    try:
    77	        return read(store).active
    78	    except Exception as e:  # noqa: BLE001
    79	        logger.error(
    80	            "F17: could not read the kill switch ({}: {}) — treating it as CLEAR. "
    81	            "A database blip must not silently stop every job on this host.",
    82	            type(e).__name__, e,
    83	        )
    84	        return False
    85	
    86	
    87	def engage(*, by: str, phrase: Optional[str] = None, store: Optional[JobStore] = None) -> KillState:
    88	    store = store or JobStore()
    89	    store.ensure_schema()
    90	    registry = load_job_registry()
    91	    store.set_kill_switch(active=True, phrase=phrase or registry.kill_phrase, by=by)
    92	    state = read(store)
    93	    logger.error(state.describe())      # ERROR: this is a loud, visible act
    94	    return state
    95	
    96	
    97	def clear(*, by: str, store: Optional[JobStore] = None) -> KillState:
    98	    store = store or JobStore()
    99	    store.ensure_schema()
   100	    store.set_kill_switch(active=False, phrase=None, by=by)
   101	    state = read(store)
   102	    logger.warning("F17: kill switch CLEARED by {} — jobs run normally again.", by)
   103	    return state
   104	
   105	
   106	def matches_kill_phrase(text: str) -> bool:
   107	    """Does an inbound message carry the kill phrase?
   108	
   109	    Exists for the Mattermost DM listener the moment one lands in the new
   110	    core. The phrase is CONFIG (`configs/cobalt/jobs.yaml`), compared
    10	        <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/cobalt/.local/bin</string>
    11	        <!-- RULING 7 / Charter §8.4: every plist carries COBALT_ENV. The
    12	             heartbeat reads the LIVE jobs table and writes the LIVE daily
    13	             note, so it declares production. Without this the store would
    14	             refuse to resolve a database at all rather than quietly
    15	             defaulting to dev. -->
    16	        <key>COBALT_ENV</key>
    17	        <string>production</string>
    18	        <!-- Output 1 is a Cobalt-owned block in TODAY'S daily note (L28
    19	             unit, in-place update). That has to be the real vault. -->
    20	        <key>COBALT_VAULT_PATH</key>
    21	        <string>/Users/cobalt/Vault/Think</string>
    22	    </dict>
    23	    <key>ProgramArguments</key>
    24	    <array>
    25	        <!-- ABSOLUTE PATH, deliberately: launchd posix_spawn()s
    26	             ProgramArguments[0] and does NOT search the job's own PATH
    27	             the way a shell does. A bare "uv" here produces exit 78
    28	             (EX_CONFIG) with empty stdout and stderr, which is exactly
    29	             how the 05:15 prefill failed silently on 2026-09-03. -->
    30	        <string>/Users/cobalt/.local/bin/uv</string>
    31	        <string>run</string>
    32	        <string>cobalt</string>
    33	        <string>heartbeat</string>
    34	        <string>beat</string>
    35	    </array>
    36	    <key>WorkingDirectory</key>
    37	    <string>/Users/cobalt/cobalt</string>
    38	    <key>AbandonProcessGroup</key>
    39	    <true/>
    40	    <!-- StartInterval, NOT StartCalendarInterval, and every day of the
    41	         week. The heartbeat is the thing that notices a Saturday failure
    42	         before Monday morning needs it, and every "red within one
    43	         interval" claim in Charter §3 F18 is measured against THIS
    44	         number.
    45	
    46	         900 s = 15 min = the `heartbeat.interval_min` tunable. launchd
    47	         cannot read a tunables row, so this is a mirror; `cobalt
    48	         validate` prints both and fails if they disagree, which is the
    49	         only thing standing between the schedule and the code that
    50	         believes it. -->
    51	    <key>StartInterval</key>
    52	    <integer>900</integer>
    53	    <!-- RunAtLoad: the first beat happens when the machine comes up,
    54	         rather than up to 15 minutes later. A reboot is precisely when
    55	         something is most likely to be down (09-04: the 15.7.9 reboot
    56	         left Obsidian dead and a whole day's writes unsynced). -->
    57	    <key>RunAtLoad</key>
    58	    <true/>
    59	    <key>StandardOutPath</key>
    60	    <string>/Users/cobalt/cobalt/logs/heartbeat.log</string>

exec
/bin/zsh -lc "rg --files | rg '0004|db_migrations|test_heartbeat|test_jobs|test_db'; nl -ba 'docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md'; nl -ba configs/cobalt/jobs.yaml | sed -n '49,73p'; git diff --stat main" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
src/cobalt/db_migrations/placement.py
src/cobalt/db_migrations/cli.py
src/cobalt/db_migrations/0001_schemas.sql
src/cobalt/db_migrations/__init__.py
src/cobalt/db_migrations/0002_move_tables.rollback.sql
src/cobalt/db_migrations/0002_move_tables.sql
src/cobalt/aset/migrations/0004_aset_sizings_session.sql
src/cobalt/vaultwrite/migrations/0004_vault_writes_sync_revert.sql
src/cobalt/vaultwrite/migrations/0004_vault_writes_sync_revert.rollback.sql
docs/10 - Decisions/ADR-0004-l28-one-vault-write-path.md
tests/cobalt/test_db_credentials.py
tests/cobalt/test_jobs_reads.py
tests/cobalt/test_heartbeat.py
tests/cobalt/test_jobs.py
docs/40 - DevDocs/cobalt/db_migrations/__init__.md
docs/40 - DevDocs/cobalt/db_migrations/placement.md
docs/40 - DevDocs/cobalt/db_migrations/cli.md
     1	=== BRIEF v3 (Sol) ===
     2	Worktree ~/cobalt-wt/heartbeat-mr, branch ops/heartbeat-market-reset. You cannot commit; leave the diff + report. No production paths (~/cobalt, ~/Vault, launchd) touched. Laws: fail loud; one path; fresh code. Inputs: the triage report heartbeat-blackout-2026-09-10.md (cause), _inflight/heartbeat-fix-astra.md, -r2.md and -r3.md (reviews). Every round-1/2 blocker maps to a numbered item below — cite the item per blocker in your report. Round 3 (-r3.md) is dissent: if it names a concrete file:line defect in this brief, fix it in the build and say so; otherwise record it as dissent, do not redesign.
     3	Cause: run_beat writes the daily-note unit unguarded at runner.py:249, upstream of alerts (:269-270) and the beat row (:291-292); F1's market_reset block (20:00–21:00 ET) raises SessionBlocked there and the whole beat dies — 4 beats/night, traceback only in logs/heartbeat.err. The heartbeat is the one job outside the F17 wrapper. probes.py:321 stays as is.
     4	Build:
     5	1. Stage order in run_beat: probes → compose → alerts (RED out-of-band; green DM under the existing green_summary_date dedup) → persist beat row → vault unit → FINALIZE. Every stage isolated: a failure is logged loud, recorded in the beat and never aborts later stages; alerts never depend on persistence. FINALIZE (r2 blocker 1): updates the persisted row with the vault result and, if the vault outcome is `failed`, sends a corrective RED alert out-of-band naming the reason — a beat can never end all-clear with a failed vault write.
     6	2. Vault step: session clock first (cobalt.session; boundary tests at 19:59/20:00/20:59/21:00 ET and a holiday — r2 risk). market_reset → no write attempt, outcome `deferred_market_reset`. Otherwise write; `written` ONLY when the writer returns a success result with a write id — a `None` return or any exception → `failed` with the reason (r2 risk). Persisted on the beat row as two nullable text columns: `vault_outcome` (`written | deferred_market_reset | failed`) and `vault_reason`. render.py reads them: `deferred_market_reset` leaves the beat's colour to the probes (never masks an unrelated RED — r2 risk); `failed` renders RED.
     7	3. Migration (r2 blocker 3): a new numbered file in db_migrations/ REGISTERED in the fixed list in db_migrations/__init__.py exactly as 0004 was, placement declared system side, rollback sql; the row digest in db_migrations/cli.py excludes the two new columns (or the digest scheme is versioned) — test proves populated-row digests are unchanged after the migration.
     8	4. F17 wrapper enrolment for com.cobalt.heartbeat: (i) wrapper writes ONLY its own fields, never beat detail or green_summary_date (r1 blocker 3); (ii) kill-switch exemption via a validated per-job JobSpec flag, default false, true only for the heartbeat; the beat reports the switch state; (iii) heartbeat-only rule (r2 blocker 2): wrapper bookkeeping (schema setup, registration, mark_running) is best-effort for this job — any failure there is logged loud and the beat subprocess STILL runs; its own DB probe then reports the outage out-of-band; (iv) the new plist in ops/ replaces the current invocation per ops/README, never side by side; NO `reads:` (one-shot).
     9	5. Tests: (a) market_reset → alerts, row with `deferred_market_reset`, ZERO write attempts, zero new session_blocks rows for actor `vaultwrite:heartbeat:*`; (b) vault exception or None outside the window → `failed`, RED, corrective RED alert sent, row present; (c) any stage's exception never suppresses later stages; (d) registry/plist parity + flag validation; (e) wrapped run leaves beat detail + green_summary_date intact; (f) wrapper bookkeeping failure → beat subprocess still runs; (g) boundary + holiday clock cases; (h) migration registered, rollback works, digests unchanged. Full suite green; `uv run cobalt validate` exit 0.
    10	6. Report docs/40 - DevDocs/reports/heartbeat-fix-2026-09-10.md: changes, which review item each answers, DISSENT section quoting anything from -r3.md not adopted with one line why, test results, and RESTARTS derived by RULE (r2 blocker 4): every plist under ops/ present in `git diff --stat main` + every resident whose `reads:` names a changed file — print the derivation, expected result `RESTARTS: com.cobalt.heartbeat (plist changed: bootout old, bootstrap new)`. LIVE block as named steps: (1) after ff-only merge, `cobalt db migrate --allow-prod` (two nullable columns; rollback sql named); (2) plist install per ops/README; (3) `cobalt jobs register` (rows only); (4) force one beat; proof = row shows `vault_outcome=written`, wrapper fields present, beat fields + green_summary_date intact, log shows the stage order incl. FINALIZE; no DM expected (dedup); (5) tonight: the FIRST beat after 20:00 (900 s interval, minute not guaranteed) shows `deferred_market_reset`, colour from probes, and the count of session_blocks rows for actor `vaultwrite:heartbeat:*` does not grow. Rollback: `git revert`, reinstall the previous plist, migration rollback sql. Print DONE as the last line.
    11	=== END BRIEF ===
    49	    timeout_s: 300
    50	    # WHAT THIS PROCESS RE-READS ON EVERY REQUEST — derived by measuring
    51	    # the request path (instrumented `open`/`read_text` over GET / and
    52	    # GET /api/health), not by reading config names off a shelf. Each
    53	    # entry cites its loader call in the 2026-09-09 ops report.
    54	    #
    55	    # It is the reason the field exists. On 09-08 a deploy added a
    56	    # `TunableUnit.WINDOW` row to tunables.yaml and said "nothing else is
    57	    # restarted"; this process re-read the new file through code that
    58	    # predated the enum value, and from ~19:00 to 07:06 the page he
    59	    # trades beside answered HTTP 200 and refused every card.
    60	    #
    61	    # NOT LISTED, and the omission is the point: `configs/dev/vault.yaml`
    62	    # IS re-read per request in dev (cobalt/vault.py:167) but NOT in
    63	    # production, where COBALT_VAULT_PATH is set in this job's own plist
    64	    # and the resolver returns before it reads the file. A row here that
    65	    # is only true in dev would send an operator to restart the sheet for
    66	    # a file production never opens.
    67	    reads:
    68	      - "configs/dev/aset.yaml"                    # aset/config.py:134 (load_config); the name says dev, but there is no configs/cobalt/aset.yaml — this IS the production sheet's config
    69	      - "configs/cobalt/taxonomy/tunables.yaml"    # taxonomy/loader.py:79 (load_tunables); the 09-09 R1 case
    70	    what: "the ASET semi-auto sheet on :5010 — the surface he trades beside"
    71	
    72	  - label: com.cobalt.mainframe
    73	    kind: resident

codex
Reviewed as a **build brief**: RESOLVED means the requirements address the finding; implementation remains pending.

**Round-1 blockers**

| Blocker | Status and evidence |
|---|---|
| Deployment and rollback | **RESOLVED.** Items 4/6 require replacing the invocation, bootout/bootstrap, registration as “rows only,” and restoring the previous plist. [brief:8](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:8>), [brief:10](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:10>). |
| Empty `reads` and restart derivation | **OPEN.** Item 4 correctly leaves heartbeat `reads` empty; item 6 still omits unknown-path handling. [brief:8](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:8>), [brief:10](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:10>), [ops/README.md:186](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:186). |
| F17 persistence ownership | **RESOLVED.** Items 4(i)/5(e) prohibit wrapper replacement of beat details and `green_summary_date`, with verification after completion. This addresses the current replacement at [store.py:162](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/store.py:162). [brief:8](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:8>), [brief:9](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:9>). |
| Durable degradation and notification | **RESOLVED.** Items 1/2/5(b) specify final persistence, explicit `vault_reason`, RED severity, and a corrective out-of-band alert for late vault failure. [brief:5](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:5>), [brief:6](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:6>), [brief:9](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:9>). |
| Missing triage report | **RESOLVED.** The report supplies eight attempted beats and corresponding refusal records; its failure ordering matches the code. [triage:18](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md:18>), [triage:33](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md:33>), [runner.py:249](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:249). |

**Round-2 blockers**

| Blocker | Status and evidence |
|---|---|
| Late-failure reporting and reason storage | **RESOLVED.** FINALIZE plus the two named columns closes both gaps. [brief:5](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:5>), [brief:6](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:6>). |
| Wrapper database failure before launch | **RESOLVED.** Items 4(iii)/5(f) require heartbeat to launch despite failed bookkeeping, addressing the pre-yield database operations. [brief:8](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:8>), [brief:9](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:9>), [wrapper.py:133](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:133). |
| Migration execution and digest proof | **RESOLVED.** Items 3/5(h) explicitly require registration, rollback testing, and populated-row digest preservation, addressing the fixed migration list and whole-row hashing. [brief:7](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:7>), [db_migrations/__init__.py:25](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:25), [db_migrations/cli.py:96](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:96). |
| Restart derivation | **OPEN.** Item 6 finds declared matches but does not distinguish an unknown changed configuration from one proven to have no resident readers. [brief:10](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:10>), [jobs/cli.py:99](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:99). |

**BLOCKERS**

- **One remaining: restart analysis silently drops unknown paths.** The new JobSpec flag entails changing `configs/cobalt/jobs.yaml`, which is absent from the registry’s populated `reads` list ([jobs.yaml:67](/Users/cobalt/cobalt-wt/heartbeat-mr/configs/cobalt/jobs.yaml:67)). Item 6’s matching rule therefore skips its reader analysis. Require `cobalt jobs readers` for every changed configuration and explicit investigation of unknown results before producing `RESTARTS`, as required by [ops/README.md:175](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:175). This does **not** establish that another resident needs restarting; it establishes that the required check remains missing.

**RISKS**

- FINALIZE contains both persistence and notification. Test **vault failure plus final database-update failure** together, proving the corrective alert still runs. Stage-level isolation alone could miss this internal coupling ([brief:5](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:5>)).
- “Exactly as 0004 was” is an incorrect migration precedent: the database-wide list contains only 0001/0002. Correct that reference and name the feature-specific rollback execution; the existing `--rollback` reverses table placement ([brief:7](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:7>), [db_migrations/__init__.py:31](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:31)).
- LIVE’s “no DM expected” assumes a healthy beat with today’s green summary already sent. A forced RED beat should still notify ([brief:10](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:10>), [runner.py:262](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:262)).

**VERDICT: RETHINK.** Close the unknown-path restart check; the other prior blockers are resolved at brief level. Static review only—no tests or production actions performed.
tokens used
71,421
Reviewed as a **build brief**: RESOLVED means the requirements address the finding; implementation remains pending.

**Round-1 blockers**

| Blocker | Status and evidence |
|---|---|
| Deployment and rollback | **RESOLVED.** Items 4/6 require replacing the invocation, bootout/bootstrap, registration as “rows only,” and restoring the previous plist. [brief:8](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:8>), [brief:10](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:10>). |
| Empty `reads` and restart derivation | **OPEN.** Item 4 correctly leaves heartbeat `reads` empty; item 6 still omits unknown-path handling. [brief:8](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:8>), [brief:10](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:10>), [ops/README.md:186](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:186). |
| F17 persistence ownership | **RESOLVED.** Items 4(i)/5(e) prohibit wrapper replacement of beat details and `green_summary_date`, with verification after completion. This addresses the current replacement at [store.py:162](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/store.py:162). [brief:8](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:8>), [brief:9](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:9>). |
| Durable degradation and notification | **RESOLVED.** Items 1/2/5(b) specify final persistence, explicit `vault_reason`, RED severity, and a corrective out-of-band alert for late vault failure. [brief:5](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:5>), [brief:6](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:6>), [brief:9](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:9>). |
| Missing triage report | **RESOLVED.** The report supplies eight attempted beats and corresponding refusal records; its failure ordering matches the code. [triage:18](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md:18>), [triage:33](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md:33>), [runner.py:249](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:249). |

**Round-2 blockers**

| Blocker | Status and evidence |
|---|---|
| Late-failure reporting and reason storage | **RESOLVED.** FINALIZE plus the two named columns closes both gaps. [brief:5](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:5>), [brief:6](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:6>). |
| Wrapper database failure before launch | **RESOLVED.** Items 4(iii)/5(f) require heartbeat to launch despite failed bookkeeping, addressing the pre-yield database operations. [brief:8](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:8>), [brief:9](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:9>), [wrapper.py:133](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:133). |
| Migration execution and digest proof | **RESOLVED.** Items 3/5(h) explicitly require registration, rollback testing, and populated-row digest preservation, addressing the fixed migration list and whole-row hashing. [brief:7](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:7>), [db_migrations/__init__.py:25](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:25), [db_migrations/cli.py:96](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:96). |
| Restart derivation | **OPEN.** Item 6 finds declared matches but does not distinguish an unknown changed configuration from one proven to have no resident readers. [brief:10](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:10>), [jobs/cli.py:99](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:99). |

**BLOCKERS**

- **One remaining: restart analysis silently drops unknown paths.** The new JobSpec flag entails changing `configs/cobalt/jobs.yaml`, which is absent from the registry’s populated `reads` list ([jobs.yaml:67](/Users/cobalt/cobalt-wt/heartbeat-mr/configs/cobalt/jobs.yaml:67)). Item 6’s matching rule therefore skips its reader analysis. Require `cobalt jobs readers` for every changed configuration and explicit investigation of unknown results before producing `RESTARTS`, as required by [ops/README.md:175](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:175). This does **not** establish that another resident needs restarting; it establishes that the required check remains missing.

**RISKS**

- FINALIZE contains both persistence and notification. Test **vault failure plus final database-update failure** together, proving the corrective alert still runs. Stage-level isolation alone could miss this internal coupling ([brief:5](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:5>)).
- “Exactly as 0004 was” is an incorrect migration precedent: the database-wide list contains only 0001/0002. Correct that reference and name the feature-specific rollback execution; the existing `--rollback` reverses table placement ([brief:7](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:7>), [db_migrations/__init__.py:31](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:31)).
- LIVE’s “no DM expected” assumes a healthy beat with today’s green summary already sent. A forced RED beat should still notify ([brief:10](</Users/cobalt/cobalt-wt/heartbeat-mr/docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md:10>), [runner.py:262](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:262)).

**VERDICT: RETHINK.** Close the unknown-path restart check; the other prior blockers are resolved at brief level. Static review only—no tests or production actions performed.
