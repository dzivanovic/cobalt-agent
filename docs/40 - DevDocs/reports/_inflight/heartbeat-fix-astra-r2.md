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
session id: 01a08b5c-aa27-7fa3-818b-7231abc5a0cb
--------
user
Round 2. Review docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md against your round-1 review at _inflight/heartbeat-fix-astra.md, src/cobalt/heartbeat/ (runner.py, render.py, probes.py), src/cobalt/jobs/ (cli.py, config.py, wrapper.py, store.py), jobs.yaml, ops/README.md and the triage report. State for each round-1 blocker RESOLVED or OPEN with file:line evidence, then BLOCKERS (new or still open) / RISKS / VERDICT SHIP or RETHINK.
hook: SessionStart
hook: SessionStart Completed
codex
I’ll check the revised brief against the round-1 blockers, implementation, and triage report, then give a verdict with file and line evidence.
exec
/bin/zsh -lc "pwd; rg --files -g 'AGENTS.md' -g '*heartbeat*' -g '*triage*' -g 'jobs.yaml' -g 'README.md' -g 'runner.py' -g 'render.py' -g 'probes.py' -g 'cli.py' -g 'config.py' -g 'wrapper.py' -g 'store.py'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
/Users/cobalt/cobalt-wt/heartbeat-mr
src/cobalt_agent/interfaces/cli.py
src/cobalt_agent/config.py
src/cobalt/session/cli.py
src/cobalt/session/store.py
src/cobalt/seatusage/cli.py
src/cobalt/seatusage/config.py
src/cobalt/seatusage/runner.py
src/cobalt/db_migrations/cli.py
src/cobalt/aset/config.py
src/cobalt/aset/store.py
src/cobalt/backup/cli.py
src/cobalt/backup/config.py
src/cobalt/jobs/cli.py
src/cobalt/jobs/config.py
src/cobalt/jobs/wrapper.py
src/cobalt/jobs/store.py
src/cobalt/vaultwrite/store.py
src/cobalt/taxonomy/cli.py
src/cobalt/taxonomy/store.py
src/cobalt/cli.py
src/cobalt/heartbeat/probes.py
src/cobalt/heartbeat/cli.py
src/cobalt/heartbeat/render.py
src/cobalt/heartbeat/runner.py
src/cobalt/redact/config.py
src/cobalt/redact/store.py
src/cobalt/daymode/cli.py
src/cobalt/daymode/config.py
src/cobalt/daymode/store.py
src/cobalt/archiver/config.py
src/cobalt/archiver/runner.py
src/cobalt/archiver/store.py
src/cobalt/cards/cli.py
src/cobalt/cards/store.py
src/cobalt/prefill/cli.py
src/cobalt/prefill/config.py
src/cobalt/notify/cli.py
src/cobalt/notify/config.py
src/cobalt/notify/store.py
src/cobalt/settings/cli.py
src/cobalt/settings/store.py
src/cobalt/generated/cli.py
src/cobalt/generated/config.py
ops/pending/README.md
ops/README.md
ops/com.cobalt.heartbeat.plist
configs/cobalt/jobs.yaml
README.md
docs/20 - Assessment/README.md
tests/cobalt/test_heartbeat.py
docs/_archive/README.md
docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md
docs/40 - DevDocs/reports/mainframe-triage-2026-09-07.md
docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md
docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra.md
docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra-r2.md
docs/40 - DevDocs/cobalt/vaultwrite/README.md
docs/10 - Decisions/README.md
docs/00 - Project/README.md
docs/30 - Design/TRADE-RADAR-CARD-MOCK-v0_1/README.md
docs/30 - Design/README.md
docs/90 - References/trade-reporter/README.md
docs/90 - References/trade-reporter/utils/README.md

exec
/bin/zsh -lc "nl -ba 'docs/40 - DevDocs/reports/_inflight/heartbeat-fix-astra.md'; nl -ba 'docs/40 - DevDocs/reports/_inflight/heartbeat-fix-brief.md'" in /Users/cobalt/cobalt-wt/heartbeat-mr
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
     1	Worktree ~/cobalt-wt/heartbeat-mr, branch ops/heartbeat-market-reset. You cannot commit; leave the diff + report. No production paths (~/cobalt, ~/Vault, launchd) touched. Laws: fail loud; one path; fresh code. Inputs: docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md (cause), _inflight/heartbeat-fix-astra.md (round-1 review — every blocker there is addressed by a numbered item below; cite the item in your report).
     2	Cause: run_beat writes the daily-note unit unguarded at runner.py:249, upstream of alerts (:269-270) and the beat row (:291-292); F1's market_reset block (20:00–21:00 ET) raises SessionBlocked there and the whole beat dies — 4 beats/night, traceback only in logs/heartbeat.err. The heartbeat is the one job outside the F17 wrapper. probes.py:321 (vaultwrite_blocks) stays as is.
     3	Build:
     4	1. Stage order in run_beat: probes → compose beat → alerts (RED out-of-band; green DM under the existing green_summary_date dedup) → persist beat row → vault unit LAST. Every stage isolated: a stage failure is logged loud, recorded in the beat (stage name + reason) and never aborts the following stages. Alerts never depend on persistence succeeding (Astra risk 1).
     5	2. Vault step: consult the session clock (cobalt.session) first. market_reset → no write attempt, outcome `deferred_market_reset`. Otherwise write; any exception → outcome `failed` with the reason. Outcome is a PERSISTED column on the beat row: `vault_outcome` text nullable (`written | deferred_market_reset | failed`) — migration + placement declaration (system side) + rollback sql; render.py reads it: `deferred_market_reset` keeps GREEN, `failed` renders RED (Astra blocker 4). Human-readable reason goes in the existing notes/message field as well.
     6	3. F17 wrapper enrolment for com.cobalt.heartbeat with three invariants (Astra blocker 3): (i) the wrapper writes ONLY its own fields (argv, returncode, started/finished) and never overwrites beat detail or `green_summary_date` — partial update or separate columns, your choice, one path; (ii) kill-switch EXEMPTION: the heartbeat keeps running while the switch is on and the beat reports the switch state — implement as a validated per-job flag in the JobSpec, default false, true only for the heartbeat (Astra risk 2, ruled); (iii) the wrapper replaces the current invocation — new plist in ops/ per the existing install procedure in ops/README, never side by side. NO `reads:` — the heartbeat is one-shot and the schema rejects it (Astra blocker 2).
     7	4. Tests: (a) market_reset → alerts sent (stub), row persisted with `vault_outcome=deferred_market_reset`, ZERO write attempts, zero new session_blocks rows with actor `vaultwrite:heartbeat:*`; (b) SessionBlocked or any exception raised by the vault step outside the window → `vault_outcome=failed`, beat RED, alerts + row present; (c) ordering: an exception in any stage never suppresses the later stages; (d) registry/plist parity for the heartbeat + JobSpec flag validation; (e) after a wrapped run, beat detail and `green_summary_date` are unchanged by the wrapper. Full suite green (1092+); `uv run cobalt validate` exit 0.
     8	5. Report docs/40 - DevDocs/reports/heartbeat-fix-2026-09-10.md: what changed, why, which Astra item each change answers, test results, and `RESTARTS: com.cobalt.heartbeat (bootout old plist, bootstrap new)` (Astra blocker 1). LIVE block as named steps: (1) after ff-only merge, `cobalt db migrate --allow-prod` (one nullable column; rollback = the rollback sql); (2) plist install per ops/README (bootout old, bootstrap new); (3) `cobalt jobs register` (rows only); (4) force one beat; proof = beat row shows `vault_outcome=written`, wrapper fields present AND beat fields + `green_summary_date` intact, log shows the stage order; no DM expected (dedup) — the RED path is proven by suite stubs; (5) tonight: the FIRST beat after 20:00 (900 s interval, exact minute not guaranteed) lands `vault_outcome=deferred_market_reset`, GREEN, and the count of session_blocks rows with actor `vaultwrite:heartbeat:*` does not grow. Rollback: `git revert`, reinstall the previous plist, migration rollback sql. Print DONE as the last line.

exec
/bin/zsh -lc 'nl -ba src/cobalt/heartbeat/runner.py; nl -ba src/cobalt/heartbeat/render.py; nl -ba src/cobalt/heartbeat/probes.py' in /Users/cobalt/cobalt-wt/heartbeat-mr
exec
/bin/zsh -lc 'for p in /AGENTS.md /Users/AGENTS.md /Users/cobalt/AGENTS.md /Users/cobalt/cobalt-wt/AGENTS.md /Users/cobalt/cobalt-wt/heartbeat-mr/AGENTS.md; do if [ -f "$p" ]; then printf '"'%s\\n' \""'$p"; cat "$p"; fi; done; rg --files --hidden -g AGENTS.md -g '"'"'!'"\\.git' docs src ops configs" in /Users/cobalt/cobalt-wt/heartbeat-mr
 exited 1 in 0ms:
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
     1	"""F18's probes — one function per question, each answering honestly.
     2	
     3	Charter §3 F18: "services alive · archiver freshness · every ops plist
     4	loaded + last exit code · Obsidian running; red/green to daily note + DM;
     5	red also out-of-band."
     6	
     7	THE RULE EVERY PROBE HERE KEEPS. "The probe broke" and "the thing is
     8	down" are different facts, and collapsing them is how a red condition
     9	becomes invisible. A probe that cannot run returns UNKNOWN, and UNKNOWN
    10	is RED — because a heartbeat that says green when it did not look is
    11	worse than no heartbeat at all.
    12	"""
    13	
    14	from __future__ import annotations
    15	
    16	import json
    17	import os
    18	import socket
    19	import subprocess
    20	from dataclasses import dataclass
    21	from datetime import datetime, timedelta
    22	from pathlib import Path
    23	from typing import Optional
    24	from urllib import request as urlrequest
    25	
    26	from cobalt.session import clock as clock_mod
    27	
    28	
    29	@dataclass
    30	class Probe:
    31	    """One answered question."""
    32	
    33	    name: str
    34	    ok: bool
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
    86	#: needs at 06:09 — the whole text is on the page itself.
    87	DAYMODE_ERROR_CHARS = 160
    88	
    89	
    90	def sheet_daymode(url: str = "http://127.0.0.1:5010/api/health") -> Probe:
    91	    """The sheet is not just SERVING — it is WORKING.
    92	
    93	    THE THIRTEEN-HOUR GREEN. On 2026-09-09 the ASET sheet answered HTTP
    94	    200 from roughly 19:00 the previous evening until 07:06, while the
    95	    page carried "⚠ DAY MODE UNRESOLVED — cards are refused until this
    96	    is fixed". `sheet_http` was green the whole time and it was telling
    97	    the truth: the server was up. It was answering the wrong question.
    98	
    99	    The cause is worth keeping next to the probe, because it is the
   100	    shape of the failure this watches for. The 09-08 seat-usage deploy
   101	    added a `TunableUnit.WINDOW` row to `tunables.yaml`; the sheet
   102	    process re-reads that file per request through code that predated
   103	    the enum value, so every render raised `TaxonomyConfigError` — and
   104	    `_daymode_state()` catches everything and renders a banner, exactly
   105	    so the page paints rather than 500s. A page that refuses cards
   106	    politely looks identical, from the outside, to one that is working.
   107	
   108	    So this reads the banner. `/api/health` reports what
   109	    `_daymode_state()` resolved, and a false `ok` is red with the sheet's
   110	    own words.
   111	
   112	    NOT A REPLACEMENT FOR `sheet_http`, which stays exactly as it was.
   113	    Two questions: is it up, and is it usable. A dead server fails both,
   114	    and the first one's message is the one that says what to restart.
   115	    """
   116	    try:
   117	        with urlrequest.urlopen(url, timeout=probe_timeout_s()) as resp:
   118	            code = resp.status
   119	            payload = json.loads(resp.read().decode("utf-8"))
   120	    except Exception as e:  # noqa: BLE001
   121	        return Probe(
   122	            "sheet daymode", False,
   123	            f"{url} unreachable: {type(e).__name__}: {e}",
   124	            unknown=True,
   125	        )
   126	
   127	    if code != 200 or not isinstance(payload, dict) or "ok" not in payload:
   128	        return Probe(
   129	            "sheet daymode", False,
   130	            f"{url} -> {code}, payload {str(payload)[:120]!r} — the health endpoint "
   131	            "is not answering the shape this probe reads. UNKNOWN, which is red.",
   132	            unknown=True,
   133	        )
   134	
   135	    if payload.get("ok"):
   136	        return Probe(
   137	            "sheet daymode", True,
   138	            f"day mode {payload.get('mode')} · {payload.get('stage')} · "
   139	            f"{payload.get('sheet_mode')} sheet — cards are accepted",
   140	        )
   141	
   142	    reason = payload.get("error") or (
   143	        f"no day mode resolved (stage {payload.get('stage')})"
   144	    )
   145	    return Probe(
   146	        "sheet daymode", False,
   147	        "THE SHEET IS SERVING BUT REFUSING CARDS — "
   148	        + str(reason)[:DAYMODE_ERROR_CHARS],
   149	    )
   150	
   151	
   152	def database(db_name: Optional[str] = None) -> Probe:
   153	    """`cobalt_brain` (or whatever COBALT_ENV resolves) answers a query."""
   154	    from cobalt import db, env
   155	
   156	    name = db_name or env.resolve_db_name()
   157	    try:
   158	        # ADR-0008: the probe names no table, but a connection still has
   159	        # to declare a side. SYSTEM — the heartbeat is system-side, and a
   160	        # liveness probe must never be the thing that opens user data.
   161	        with db.connect(name, side=db.Side.SYSTEM) as conn:
   162	            row = conn.execute("SELECT 1").fetchone()
   163	        if row and row[0] == 1:
   164	            return Probe("database", True, f"{name} reachable")
   165	        return Probe("database", False, f"{name} answered {row!r} to SELECT 1")
   166	    except Exception as e:  # noqa: BLE001
   167	        return Probe("database", False, f"{name} unreachable: {type(e).__name__}: {e}")
   168	
   169	
   170	def obsidian() -> Probe:
   171	    """Obsidian is running — RULING 6, and not a cosmetic check.
   172	
   173	    The vault reaches his other devices only through a RUNNING Obsidian
   174	    on this Mac. On 2026-09-04 a correct 05:15 write was silently
   175	    overwritten by the trading PC's template because none was running
   176	    here. This reads the SAME `cobalt.obsidian.sync_status()` the vault
   177	    writer reads, so the two can never disagree about the wording.
   178	    """
   179	    from cobalt import obsidian as obsidian_mod
   180	
   181	    try:
   182	        running, message = obsidian_mod.sync_status()
   183	    except obsidian_mod.ObsidianProbeError as e:
   184	        return Probe("obsidian", False, f"PROBE FAILED — sync state UNKNOWN: {e}", unknown=True)
   185	    return Probe("obsidian", running, message)
   186	
   187	
   188	def mainframe(host: str = "127.0.0.1", port: int = 1234) -> Probe:
   189	    """The local model server accepts a connection (L23's local lane)."""
   190	    try:
   191	        with socket.create_connection((host, port), timeout=probe_timeout_s()):
   192	            return Probe("mainframe", True, f"{host}:{port} accepting connections")
   193	    except Exception as e:  # noqa: BLE001
   194	        return Probe("mainframe", False, f"{host}:{port} refused: {type(e).__name__}")
   195	
   196	
   197	def archiver_freshness(store=None, now: Optional[datetime] = None) -> Probe:
   198	    """Last run + rows written, checked against the archiver's own
   199	    Mon-Fri cadence via the same `is_missed` arithmetic F17's watchdog
   200	    uses — not a flat age window.
   201	
   202	    A flat `now - last_run > N hours` window cannot tell a genuine miss
   203	    from an ordinary Friday-to-Monday gap: whatever N is, it either
   204	    fires every weekend (too small) or hides a multi-day outage (too
   205	    big). 2026-09-06 is why this changed: the F17 wrapper was registered
   206	    at 22:19 ET Friday, AFTER that evening's 20:30 run had already
   207	    completed via the pre-wrapper code path, so the row's `finished_at`
   208	    stayed NULL forever with nothing wrong — and the old flat
   209	    `registered_at + heartbeat.archiver_max_age_min` grace expired
   210	    Saturday just after midnight, painting the whole weekend red for a
   211	    job that was never actually due again until Monday evening.
   212	    `is_missed` already gets this right, including the exact "cannot
   213	    miss a run it was not watching for" case above — reusing it here is
   214	    the one-path rule, not a nicety.
   215	
   216	    Rows written still matters once a run HAS completed — a nightly run
   217	    that exits 0 having written zero rows looks green in every state
   218	    column and is quietly not collecting the corpus every later feature
   219	    depends on. That check is cadence-independent and unchanged.
   220	    """
   221	    from cobalt.jobs.config import load_job_registry
   222	    from cobalt.jobs.store import JobStore
   223	    from cobalt.jobs.watchdog import MISSED_GRACE_KEY, is_missed
   224	    from cobalt.session.clock import session_clock
   225	
   226	    store = store or JobStore()
   227	    ts = now or clock_mod.now_utc()
   228	    row = store.get("com.cobalt.archiver")
   229	    if row is None:
   230	        return Probe("archiver", False, "no jobs row — not registered")
   231	
   232	    spec = load_job_registry().spec("com.cobalt.archiver")
   233	    now_et = session_clock().to_et(ts)
   234	    grace = timedelta(minutes=int(_tunable(MISSED_GRACE_KEY)))
   235	    missed, missed_detail = is_missed(spec, row, now_et=now_et, grace=grace)
   236	
   237	    finished = row["finished_at"]
   238	    if finished is None:
   239	        if missed:
   240	            return Probe("archiver", False, missed_detail)
   241	        return Probe(
   242	            "archiver", True,
   243	            f"no run OBSERVED yet — none due since registration "
   244	            f"({row['registered_at']:%Y-%m-%d %H:%M} UTC)",
   245	        )
   246	    age = ts - finished
   247	    result = row["last_result"] or {}
   248	    rows_written = result.get("rows_written")
   249	    detail = (
   250	        f"last run {finished:%Y-%m-%d %H:%M} UTC ({age.total_seconds() / 3600:.1f} h ago)"
   251	        f", rows written {rows_written if rows_written is not None else 'UNRECORDED'}"
   252	        f", exit {row['exit_code']}"
   253	    )
   254	    if missed:
   255	        return Probe("archiver", False, f"STALE — {detail} — {missed_detail}")
   256	    if row["exit_code"] not in (0, None):
   257	        return Probe("archiver", False, f"last run FAILED — {detail}")
   258	    if rows_written == 0:
   259	        return Probe(
   260	            "archiver", False,
   261	            f"ran and wrote NOTHING — {detail}. Exit 0 with zero rows is the "
   262	            "failure that looks green in every state column.",
   263	        )
   264	    return Probe("archiver", True, detail)
   265	
   266	
   267	def backup_freshness(now: Optional[datetime] = None) -> Probe:
   268	    """Age of the newest nightly snapshot, against
   269	    `heartbeat.backup_max_age_min` (26 h).
   270	
   271	    THE UNARMED CASE IS RED, AND SAYS SO. Both legs of the backup ruling
   272	    (external SSD, Backblaze B2) are off until their inputs exist, and
   273	    the honest report of that is "there is no backup", not `??` and not
   274	    a green tick. `unknown` is reserved for a probe that could not RUN;
   275	    a config that declares no destination ran fine and the answer is bad.
   276	    """
   277	    from cobalt.backup.config import BackupConfigError, load_backup_config
   278	    from cobalt.backup.restic import BackupError, latest_snapshot_age
   279	
   280	    ts = now or clock_mod.now_utc()
   281	    try:
   282	        cfg = load_backup_config()
   283	    except BackupConfigError as e:
   284	        return Probe("backup", False, f"config unreadable: {e}", unknown=True)
   285	
   286	    if not cfg.armed:
   287	        off = ", ".join(d.name for d in cfg.destinations)
   288	        return Probe(
   289	            "backup", False,
   290	            f"NO DESTINATION ARMED ({off} all off) — there is no backup. "
   291	            "configs/cobalt/backup.yaml says what each leg is missing.",
   292	        )
   293	
   294	    max_age = timedelta(minutes=int(_tunable("heartbeat.backup_max_age_min")))
   295	    try:
   296	        age = latest_snapshot_age(cfg)
   297	    except BackupError as e:
   298	        # BackupError's text is credential-free BY CONTRACT (see
   299	        # backup/restic.py), and it is the one carrying the actionable
   300	        # sentence — "/Volumes/COBALT-BACKUP is NOT MOUNTED". A beat that
   301	        # said only `BackupError` would send someone to read the log to
   302	        # learn they need to plug a disk in.
   303	        return Probe("backup", False, str(e).split(". ")[0], unknown=True)
   304	    except Exception as e:  # noqa: BLE001 — a repo we cannot reach is not a diagnosis
   305	        return Probe("backup", False, f"could not read the repository: {type(e).__name__}",
   306	                     unknown=True)
   307	    if age is None:
   308	        return Probe("backup", False,
   309	                     f"armed ({', '.join(d.name for d in cfg.armed)}) but the repository "
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
   356	    something started putting credentials into outbound text, and that is
   357	    worth seeing the day it starts rather than at the next audit.
   358	    """
   359	    from cobalt.redact.store import RedactionStore
   360	
   361	    try:
   362	        store = RedactionStore()
   363	        store.ensure_schema()
   364	        count = store.count_over_minutes(minutes, now=now)
   365	        by_pattern = store.by_pattern_since(
   366	            (now or clock_mod.now_utc()) - timedelta(minutes=minutes)
   367	        )
   368	    except Exception as e:  # noqa: BLE001
   369	        return Probe("redactions", False, f"counter unreadable: {type(e).__name__}: {e}",
   370	                     unknown=True)
   371	    if not count:
   372	        return Probe("redactions", True, "0 since the last beat")
   373	    kinds = ", ".join(f"{p} on {c} x{n}" for c, p, n in by_pattern[:5])
   374	    return Probe("redactions", True, f"{count} since the last beat ({kinds})")
   375	
   376	
   377	# ---------------------------------------------------------------------
   378	# herdr — the terminal workspace every agent seat lives in
   379	# ---------------------------------------------------------------------
   380	
   381	HERDR_LABEL = "com.cobalt.herdr"
   382	
   383	#: Where herdr puts its API socket. Not a tunable: F16 governs
   384	#: THRESHOLDS, and this is an address — a number you might tune versus a
   385	#: path that is either right or wrong. `herdr status server` prints it,
   386	#: and it has been this since 0.8.x.
   387	HERDR_SOCKET = Path("~/.config/herdr/herdr.sock")
   388	
   389	#: Absolute, for the same reason every plist's ProgramArguments is: a
   390	#: probe that resolved a binary off PATH would answer a different
   391	#: question under launchd than it answers in a shell.
   392	HERDR_BINARY = Path("/opt/homebrew/bin/herdr")
   393	
   394	#: Claude Code's settings file, and the harness-aware hook it must point
   395	#: at. Addresses, not thresholds — same reasoning as `HERDR_SOCKET`.
   396	CLAUDE_SETTINGS = Path("~/.claude/settings.json")
   397	HOOK_GUARD = Path("~/.claude/hooks/herdr-harness-guard.sh")
   398	
   399	
   400	class HookGuardDrift(RuntimeError):
   401	    """The SessionStart hook is not exactly the one guard entry."""
   402	
   403	
   404	def _check_hook_guard(
   405	    settings_path: Optional[Path] = None, guard_path: Optional[Path] = None
   406	) -> str:
   407	    """`hooks.SessionStart` is EXACTLY one entry pointing at the guard.
   408	
   409	    WHY THIS IS A HERDR QUESTION AND NOT A HOUSEKEEPING ONE. The `herdr`
   410	    probe's second question is `herdr agent list`, and that list is what
   411	    tells one seat from another. herdr's own Claude integration hardcodes
   412	    the agent name `herdr:claude` with no harness detection, so a Grok or
   413	    Codex session started under it reports itself as `claude`. The guard
   414	    script is what makes the report honest, and this probe reads the list
   415	    the guard protects — so the two belong in one answer.
   416	
   417	    IT IS NOT ENOUGH TO ASK WHETHER THE GUARD IS PRESENT. On 2026-09-09
   418	    at 08:33 `herdr integration install claude` (v8 -> v9) did NOT replace
   419	    the pointer, which a presence check would have called fine: it
   420	    APPENDED A SECOND SessionStart ENTRY aimed at herdr's own script, so
   421	    both would have fired and the last writer would have won. That is why
   422	    the assertion is EXACTLY ONE — an integration update is expected to
   423	    keep trying, and the count is the thing it changes.
   424	
   425	    Raises `HookGuardDrift` naming the drift; returns a one-line summary
   426	    when everything is as it should be.
   427	    """
   428	    settings = Path(settings_path or CLAUDE_SETTINGS).expanduser()
   429	    guard = Path(guard_path or HOOK_GUARD).expanduser()
   430	
   431	    if not settings.exists():
   432	        raise HookGuardDrift(f"{settings} does not exist — no SessionStart hook at all")
   433	    try:
   434	        data = json.loads(settings.read_text())
   435	    except Exception as e:  # noqa: BLE001
   436	        raise HookGuardDrift(
   437	            f"{settings} does not parse as JSON ({type(e).__name__}) — the hook "
   438	            "configuration is UNKNOWN, which is not the same as correct"
   439	        ) from None
   440	
   441	    entries = ((data.get("hooks") or {}).get("SessionStart")) or []
   442	    if not isinstance(entries, list):
   443	        raise HookGuardDrift(
   444	            f"hooks.SessionStart is a {type(entries).__name__}, not a list of entries"
   445	        )
   446	    if len(entries) != 1:
   447	        raise HookGuardDrift(
   448	            f"hooks.SessionStart has {len(entries)} entries, expected exactly 1 — "
   449	            "a herdr integration update appended/replaced the SessionStart hook. "
   450	            "Grok sessions will report as claude; restore the single guard entry "
   451	            f"({guard})"
   452	        )
   453	
   454	    hooks = entries[0].get("hooks") or []
   455	    commands = [h for h in hooks if isinstance(h, dict) and h.get("type") == "command"]
   456	    if len(commands) != 1:
   457	        raise HookGuardDrift(
   458	            f"the SessionStart entry carries {len(commands)} command hook(s), "
   459	            "expected exactly 1 — a herdr integration update appended/replaced the "
   460	            "SessionStart hook. Grok sessions will report as claude; restore the "
   461	            f"single guard entry ({guard})"
   462	        )
   463	
   464	    command = str(commands[0].get("command") or "")
   465	    if str(guard) not in command:
   466	        raise HookGuardDrift(
   467	            f"the SessionStart hook does not run {guard} — a herdr integration "
   468	            "update appended/replaced the SessionStart hook. Grok sessions will "
   469	            "report as claude; restore the single guard entry"
   470	        )
   471	    if not guard.exists():
   472	        raise HookGuardDrift(
   473	            f"the SessionStart hook points at {guard}, which DOES NOT EXIST — "
   474	            "every session starts with a failing hook and no harness detection. "
   475	            "Restore the guard script"
   476	        )
   477	    if not os.access(guard, os.X_OK):
   478	        raise HookGuardDrift(
   479	            f"{guard} exists but is NOT EXECUTABLE — the hook cannot run it, so "
   480	            "no harness detection happens. `chmod +x` it"
   481	        )
   482	    return f"hook guard: 1 SessionStart entry -> {guard.name}, executable"
   483	
   484	
   485	def _herdr_enabled() -> tuple[bool, str]:
   486	    """Is `com.cobalt.herdr` supposed to be up yet?
   487	
   488	    The registry row answers, and until the handover it says no. This is
   489	    read every beat rather than baked in, so flipping one flag in
   490	    `configs/cobalt/jobs.yaml` is the whole of the last handover step.
   491	    """
   492	    from cobalt.jobs.config import load_job_registry
   493	
   494	    spec = load_job_registry().by_label.get(HERDR_LABEL)
   495	    if spec is None:
   496	        return False, f"{HERDR_LABEL} is not in the job registry"
   497	    return spec.enabled, ""
   498	
   499	
   500	def _herdr_agent_list(binary: Path, timeout: float) -> list:
   501	    """`herdr agent list` -> the agents array. Raises on anything else."""
   502	    proc = subprocess.run(
   503	        [str(binary), "agent", "list"], capture_output=True, text=True, timeout=timeout
   504	    )
   505	    if proc.returncode != 0:
   506	        raise RuntimeError(
   507	            f"`herdr agent list` exited {proc.returncode}: "
   508	            f"{proc.stderr.strip()[:200] or '(no stderr)'}"
   509	        )
   510	    payload = json.loads(proc.stdout)
   511	    agents = (payload.get("result") or {}).get("agents")
   512	    if not isinstance(agents, list):
   513	        raise RuntimeError("`herdr agent list` returned no `result.agents` array")
   514	    return agents
   515	
   516	
   517	def herdr(
   518	    *,
   519	    socket_path: Optional[Path] = None,
   520	    binary: Optional[Path] = None,
   521	    list_agents=None,
   522	    settings_path: Optional[Path] = None,
   523	    guard_path: Optional[Path] = None,
   524	) -> Probe:
   525	    """The herdr server is up, answering, AND honestly labelled — three
   526	    questions, all asked.
   527	
   528	    THE SOCKET EXISTING IS NOT THE SERVER WORKING, which is the same
   529	    lesson the ASET sheet's HTTP probe carries: a stale socket file
   530	    outlives the process that made it, and a server that has wedged
   531	    still holds its socket open. So this connects to the socket (does it
   532	    accept?) and then asks it something real (`herdr agent list`, which
   533	    has to traverse the server's live pane state to answer). Either half
   534	    failing is red, and the message names the launchd label so a reader
   535	    knows what to bootstrap.
   536	
   537	    THE THIRD QUESTION, added 2026-09-09: is the SessionStart hook still
   538	    exactly the harness-aware guard? See `_check_hook_guard` — the short
   539	    version is that `agent list` is what this probe asserts on, and a
   540	    herdr integration update that appends a second hook makes every Grok
   541	    session report itself as `claude` IN THAT LIST. Asking the first two
   542	    questions of a list that has quietly stopped meaning what it says is
   543	    asking nothing.
   544	
   545	    WHEN THE ROW IS DISABLED IT IS GREEN AND SAYS WHY. `enabled: false`
   546	    is the declared state of a job that is built and deliberately not
   547	    loaded — see ops/README.md. A red every 15 minutes for a state
   548	    somebody chose on purpose is how a heartbeat stops being read. The
   549	    hook check is skipped there too: with no server under launchd there
   550	    is no `agent list` for a mislabelled seat to corrupt.
   551	    """
   552	    enabled, why = _herdr_enabled()
   553	    if not enabled:
   554	        return Probe(
   555	            "herdr", True,
   556	            (why or f"{HERDR_LABEL} is registered with `enabled: false`")
   557	            + " — NOT PROBED. The plist is built and deliberately not loaded; the "
   558	            "server is running under a manual start. ops/README.md 'herdr handover' "
   559	            "is the procedure, and flipping that flag is its last step.",
   560	        )
   561	
   562	    path = Path(socket_path or HERDR_SOCKET).expanduser()
   563	    timeout = probe_timeout_s()
   564	    if not path.exists():
   565	        return Probe(
   566	            "herdr", False,
   567	            f"no API socket at {path} — the server is not running. "
   568	            f"`launchctl kickstart -k gui/$(id -u)/{HERDR_LABEL}`",
   569	        )
   570	    try:
   571	        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
   572	            sock.settimeout(timeout)
   573	            sock.connect(str(path))
   574	    except OSError as e:
   575	        return Probe(
   576	            "herdr", False,
   577	            f"the socket at {path} exists but REFUSED a connection "
   578	            f"({type(e).__name__}) — a stale socket file outlives the process that "
   579	            f"made it. {HERDR_LABEL} needs a kickstart.",
   580	        )
   581	
   582	    caller = list_agents or _herdr_agent_list
   583	    try:
   584	        agents = caller(Path(binary or HERDR_BINARY), timeout)
   585	    except Exception as e:  # noqa: BLE001
   586	        return Probe(
   587	            "herdr", False,
   588	            f"socket accepted but the server did not answer `agent list` "
   589	            f"({type(e).__name__}: {e}) — {HERDR_LABEL} is up and not serving",
   590	        )
   591	    # THIRD QUESTION. Asked last, because a drifted hook is a fact about
   592	    # what the answer above MEANS, and the two answers above are worth
   593	    # having either way.
   594	    try:
   595	        guard_line = _check_hook_guard(settings_path, guard_path)
   596	    except HookGuardDrift as e:
   597	        return Probe(
   598	            "herdr", False,
   599	            f"socket and `agent list` are fine, but the SEAT LABELS ARE NOT "
   600	            f"TRUSTWORTHY: {e}",
   601	        )
   602	
   603	    seats = ", ".join(sorted({str(a.get("agent")) for a in agents if a.get("agent")}))
   604	    return Probe(
   605	        "herdr", True,
   606	        f"socket accepting at {path}; {len(agents)} pane(s)"
   607	        + (f", seats: {seats}" if seats else "")
   608	        + f"; {guard_line}",
   609	    )
   610	
   611	
   612	# ---------------------------------------------------------------------
   613	# seat-usage report freshness
   614	# ---------------------------------------------------------------------
   615	
   616	
   617	def seat_usage(store=None, now: Optional[datetime] = None) -> Probe:
   618	    """Has the seat-usage report been refreshed recently ENOUGH, and is
   619	    it even due right now?
   620	
   621	    ASKED ONLY INSIDE THE WINDOW. The job runs hourly between 06:00 and
   622	    23:00 ET; at 03:00 the last run is four hours old and everything is
   623	    exactly as it should be. A flat age check would be red all night for
   624	    a schedule working as written — the same mistake the archiver's
   625	    freshness probe made against weekends, and fixed on 2026-09-06 by
   626	    asking the schedule instead of guessing a number.
   627	
   628	    Inside the window, the limit is `seat_usage.max_age_min` (two
   629	    intervals): one missed run is a hiccup nobody needs to be told
   630	    about, two in a row means the number Dejan reads at the close is
   631	    wrong.
   632	    """
   633	    from cobalt.jobs.config import load_job_registry
   634	    from cobalt.jobs.store import JobStore
   635	    from cobalt.session.clock import session_clock
   636	    from cobalt.seatusage.runner import JOB_LABEL
   637	
   638	    ts = now or clock_mod.now_utc()
   639	    now_et = session_clock().to_et(ts)
   640	    spec = load_job_registry().by_label.get(JOB_LABEL)
   641	    if spec is None or spec.schedule is None:
   642	        return Probe("seat usage", False, f"{JOB_LABEL} is not in the job registry")
   643	    if not spec.enabled:
   644	        return Probe(
   645	            "seat usage", True,
   646	            f"{JOB_LABEL} is registered with `enabled: false` — NOT PROBED",
   647	        )
   648	    cadence = spec.cadence or "(no cadence)"
   649	    if not spec.schedule.due_now(now_et):
   650	        return Probe(
   651	            "seat usage", True,
   652	            f"outside its window — not due ({cadence}). The report holds "
   653	            "yesterday's last run until the window opens again.",
   654	        )
   655	
   656	    store = store or JobStore()
   657	    try:
   658	        row = store.get(JOB_LABEL)
   659	    except Exception as e:  # noqa: BLE001
   660	        return Probe("seat usage", False,
   661	                     f"jobs row unreadable: {type(e).__name__}: {e}", unknown=True)
   662	    if row is None:
   663	        return Probe("seat usage", False, f"no jobs row for {JOB_LABEL} — not registered")
   664	
   665	    limit = timedelta(minutes=int(_tunable("seat_usage.max_age_min")))
   666	    finished = row["finished_at"]
   667	    if finished is None:
   668	        opened = spec.schedule.window_opened_at(now_et)
   669	        reference = max(
   670	            [d for d in (opened, session_clock().to_et(row["registered_at"])) if d]
   671	        )
   672	        if now_et - reference <= limit:
   673	            return Probe(
   674	                "seat usage", True,
   675	                f"no run OBSERVED yet — none due since {reference:%Y-%m-%d %H:%M} ET "
   676	                f"({cadence})",
   677	            )
   678	        return Probe(
   679	            "seat usage", False,
   680	            f"NEVER RUN inside its window — nothing since "
   681	            f"{reference:%Y-%m-%d %H:%M} ET ({cadence})",
   682	        )
   683	
   684	    age = ts - finished
   685	    result = row["last_result"] or {}
   686	    unpriced = result.get("unpriced") or []
   687	    detail = (
   688	        f"last run {session_clock().to_et(finished):%Y-%m-%d %H:%M} ET "
   689	        f"({age.total_seconds() / 60:.0f} min ago), exit {row['exit_code']}"
   690	    )
   691	    if unpriced:
   692	        # NOT RED. An unpriced model is loud in the report itself, every
   693	        # hour, where the number it distorts is. Repeating it as a red
   694	        # beat would put a permanent alert on a condition that is fixed
   695	        # by a deliberate version bump, not by anything at 03:00.
   696	        detail += f"; UNPRICED in the report: {', '.join(unpriced)}"
   697	    if row["exit_code"] not in (0, None):
   698	        return Probe("seat usage", False, f"last run FAILED — {detail}")
   699	    if age > limit:
   700	        return Probe(
   701	            "seat usage", False,
   702	            f"STALE — {detail}, limit {limit.total_seconds() / 60:.0f} min "
   703	            f"({cadence}). The report is no longer today's.",
   704	        )
   705	    return Probe("seat usage", True, detail)
   706	
   707	
   708	def email() -> Probe:
   709	    """The out-of-band alert channel is armed — token present + last send.
   710	
   711	    THE ONE PROBE THAT WATCHES THE ALERT PATH ITSELF. Every other probe
   712	    here answers "is a monitored thing up?"; this one answers "could we
   713	    still tell him if it were not?". An email channel that quietly lost
   714	    its refresh token would take every red with it and leave the beat
   715	    looking exactly as green as before — which is the failure this row
   716	    exists to make impossible.
   717	
   718	    It NEVER SENDS. A probe that mailed a test every 15 minutes would put
   719	    96 messages a day in the inbox and train its reader to filter the
   720	    channel, defeating the thing it was checking. Presence of the
   721	    credential is read from the vault (names only, no values, no
   722	    network); the last real send is read from `cobalt_email_sends`,
   723	    written by whoever actually sent one.
   724	
   725	    A FAILED LAST SEND IS RED, and stays red until a later send succeeds.
   726	    "It worked in July" is not an answer about an alert path.
   727	    """
   728	    from cobalt.notify.email import channel_status
   729	    from cobalt.notify.store import EmailSendStore
   730	
   731	    try:
   732	        armed, detail = channel_status()
   733	    except Exception as e:  # noqa: BLE001
   734	        return Probe("email", False, f"PROBE FAILED — channel state UNKNOWN: {e}", unknown=True)
   735	    if not armed:
   736	        return Probe("email", False, detail)
   737	
   738	    try:
   739	        last = EmailSendStore().last()
   740	    except Exception as e:  # noqa: BLE001
   741	        # The credential IS there; only the history is unreadable. That
   742	        # is ignorance about half the question, not a dead channel — and
   743	        # `unknown` is what says so.
   744	        return Probe("email", False, f"{detail}; last send UNKNOWN ({type(e).__name__})",
   745	                     unknown=True)
   746	
   747	    if last is None:
   748	        # Never sent is not "broken", but it is not proven either, and
   749	        # F18's whole claim is that this path works. `cobalt notify
   750	        # email-test` is one command.
   751	        return Probe("email", False,
   752	                     f"{detail}, but NO SEND HAS EVER BEEN MADE from this host — the "
   753	                     "out-of-band path is unproven. Run `cobalt notify email-test`.")
   754	    when = f"{last['ts']:%Y-%m-%d %H:%M} UTC"
   755	    if not last["ok"]:
   756	        return Probe("email", False,
   757	                     f"{detail}; LAST SEND FAILED at {when} ({last['caller']}) — "
   758	                     f"{last['detail']}")
   759	    return Probe("email", True, f"{detail}; last send OK {when} ({last['caller']})")
   760	
   761	
   762	__all__ = [
   763	    "Probe",
   764	    "archiver_freshness",
   765	    "database",
   766	    "email",
   767	    "herdr",
   768	    "mainframe",
   769	    "obsidian",
   770	    "probe_timeout_s",
   771	    "redactions",
   772	    "seat_usage",
   773	    "sheet_http",
   774	    "vaultwrite_blocks",
   775	]

exec
/bin/zsh -lc "nl -ba src/cobalt/heartbeat/runner.py | sed -n '240,330p'; nl -ba src/cobalt/heartbeat/render.py; nl -ba src/cobalt/heartbeat/probes.py | sed -n '285,365p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
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
   285	
   286	    if not cfg.armed:
   287	        off = ", ".join(d.name for d in cfg.destinations)
   288	        return Probe(
   289	            "backup", False,
   290	            f"NO DESTINATION ARMED ({off} all off) — there is no backup. "
   291	            "configs/cobalt/backup.yaml says what each leg is missing.",
   292	        )
   293	
   294	    max_age = timedelta(minutes=int(_tunable("heartbeat.backup_max_age_min")))
   295	    try:
   296	        age = latest_snapshot_age(cfg)
   297	    except BackupError as e:
   298	        # BackupError's text is credential-free BY CONTRACT (see
   299	        # backup/restic.py), and it is the one carrying the actionable
   300	        # sentence — "/Volumes/COBALT-BACKUP is NOT MOUNTED". A beat that
   301	        # said only `BackupError` would send someone to read the log to
   302	        # learn they need to plug a disk in.
   303	        return Probe("backup", False, str(e).split(". ")[0], unknown=True)
   304	    except Exception as e:  # noqa: BLE001 — a repo we cannot reach is not a diagnosis
   305	        return Probe("backup", False, f"could not read the repository: {type(e).__name__}",
   306	                     unknown=True)
   307	    if age is None:
   308	        return Probe("backup", False,
   309	                     f"armed ({', '.join(d.name for d in cfg.armed)}) but the repository "
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
   356	    something started putting credentials into outbound text, and that is
   357	    worth seeing the day it starts rather than at the next audit.
   358	    """
   359	    from cobalt.redact.store import RedactionStore
   360	
   361	    try:
   362	        store = RedactionStore()
   363	        store.ensure_schema()
   364	        count = store.count_over_minutes(minutes, now=now)
   365	        by_pattern = store.by_pattern_since(

exec
/bin/zsh -lc "nl -ba src/cobalt/jobs/cli.py | sed -n '1,180p'; nl -ba src/cobalt/jobs/wrapper.py; nl -ba src/cobalt/jobs/store.py | sed -n '1,240p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
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

exec
/bin/zsh -lc "nl -ba src/cobalt/jobs/config.py | sed -n '200,355p'; nl -ba configs/cobalt/jobs.yaml | sed -n '175,240p'; nl -ba ops/README.md; nl -ba 'docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md'; git status --short" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
   200	
   201	        launchd has no "every N minutes between 06:00 and 23:00": it has
   202	        `StartInterval` (which never stops) and `StartCalendarInterval`
   203	        (which is a list of moments). A window is therefore EXPANDED into
   204	        moments here, and the test suite compares this list against the
   205	        plist's own array so the two can never drift.
   206	        """
   207	        minutes = self.interval_minutes()
   208	        span = self.window()
   209	        if minutes is None or span is None:
   210	            return []
   211	        opens, closes = span
   212	        entries: list[dict[str, int]] = []
   213	        for day in sorted(self.weekdays):
   214	            cursor = opens.hour * 60 + opens.minute
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
   316	
   317	    @property
   318	    def cadence(self) -> Optional[str]:
   319	        return self.schedule.describe() if self.schedule else None
   320	
   321	    @property
   322	    def pidfile_path(self) -> Optional[Path]:
   323	        return (REPO_ROOT / self.pidfile) if self.pidfile else None
   324	
   325	    @property
   326	    def plist_path(self) -> Path:
   327	        return OPS_DIR / f"{self.label}.plist"
   328	
   329	
   330	class JobRegistry(BaseModel):
   331	    model_config = ConfigDict(extra="forbid")
   332	
   333	    jobs: list[JobSpec] = Field(min_length=1)
   334	    kill_phrase: str = Field(min_length=1)
   335	    resume_phrase: str = Field(min_length=1)
   336	
   337	    @model_validator(mode="after")
   338	    def _unique_labels(self) -> "JobRegistry":
   339	        labels = [j.label for j in self.jobs]
   340	        dupes = sorted({l for l in labels if labels.count(l) > 1})
   341	        if dupes:
   342	            raise ValueError(f"duplicate job label(s): {dupes}")
   343	        if self.kill_phrase.strip().upper() == self.resume_phrase.strip().upper():
   344	            raise ValueError("kill_phrase and resume_phrase must differ")
   345	        return self
   346	
   347	    @property
   348	    def by_label(self) -> dict[str, JobSpec]:
   349	        return {j.label: j for j in self.jobs}
   350	
   351	    def readers_of(self, path: str) -> list[JobSpec]:
   352	        """Every RESIDENT that re-reads `path` at runtime — the jobs a
   353	        change to that file must restart, in one action with the change.
   354	
   355	        Normalised through `Path` so `./configs/cobalt/x.yaml` and
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
     1	# ops/ — LaunchAgents & wrapper scripts
     2	
     3	Everything here is captured in git as the SOURCE for what's installed
     4	to `~/Library/LaunchAgents/` — that install directory itself is outside
     5	the repo and not tracked. When you add or change a plist, re-copy it
     6	(see "Install / reload" below); the copy in `~/Library/LaunchAgents/`
     7	does not auto-update from git.
     8	
     9	## Inventory
    10	
    11	**Nine plists below, all of them loaded, as of 2026-09-09**
    12	(`launchctl list | grep com.cobalt`). `com.cobalt.herdr` was the one
    13	exception until the handover on 2026-09-08 at 19:21 ET; it is live now —
    14	see "herdr under launchd (0.9.0)" further down. `com.cobalt.generated`
    15	is new on 2026-09-09.
    16	
    17	This table is not the whole of `ops/`, and never was: `com.cobalt.backup`,
    18	`cards-expire`, `daymode-propose`, `heartbeat` and `obsidian` have
    19	plists and rows without a row here. **`configs/cobalt/jobs.yaml` is the
    20	authoritative list** — fourteen labels, cross-checked against `ops/`
    21	by `uv run cobalt validate` on every run of the gate. Read this table as
    22	prose about the ones with a story attached, not as an inventory.
    23	
    24	| Plist | Runs | Schedule | Wrapper | Installed |
    25	|---|---|---|---|---|
    26	| `com.cobalt.agent.plist` | `cobalt.sh start` (the Mattermost chief-of-staff agent) | RunAtLoad only, no KeepAlive | — | yes |
    27	| `com.cobalt.mainframe.plist` | `ops/start_mainframe.sh` (local LLM — the L23 local lane) | RunAtLoad only | `ops/start_mainframe.sh` | yes |
    28	| `com.cobalt.archiver.plist` | `/Users/cobalt/.local/bin/uv run archiver` (nightly bar archiver) | Mon-Fri 20:30 ET | — | yes (2026-09-03 — was not loaded before this) |
    29	| `com.cobalt.prefill-daily.plist` | `/Users/cobalt/.local/bin/uv run prefill daily` | Mon-Fri 05:15 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
    30	| `com.cobalt.prefill-drc.plist` | `/Users/cobalt/.local/bin/uv run prefill drc` | Mon-Fri 15:40 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
    31	| `com.cobalt.aset.plist` | `ops/start_aset.sh` → `uv run python -m cobalt.aset` (ASET sizing widget, :5010) | RunAtLoad + KeepAlive (persistent) | `ops/start_aset.sh` | yes |
    32	| `com.cobalt.herdr.plist` | `/opt/homebrew/bin/herdr server` (the terminal workspace every agent seat lives in) | RunAtLoad + KeepAlive on crash only | — | **yes (2026-09-08 19:21 — the handover)** |
    33	| `com.cobalt.generated.plist` | `/Users/cobalt/.local/bin/uv run cobalt generated commit` (commits the files a job rewrote today) | daily 23:37 ET | F17 wrapper | new 2026-09-09 |
    34	| `com.cobalt.seat-usage.plist` | `/Users/cobalt/.local/bin/uv run cobalt seat-usage run` (the hourly seat-usage report) | hourly 06:00-23:00 ET, every day | F17 wrapper (`cobalt seat-usage run`) | yes (2026-09-08) |
    35	
    36	The table above says which plists are *supposed* to be loaded.
    37	`configs/cobalt/jobs.yaml` is the machine-readable version of the same
    38	claim, and `uv run cobalt validate` compares the two: it fails on a job
    39	in one and not the other, and prints a `NOT LOADED BY DESIGN` line for
    40	every row carrying `enabled: false`.
    41	
    42	## com.cobalt.aset — persistence fix (2026-08-31)
    43	
    44	**Incident:** the ASET widget had no LaunchAgent at all — it was only
    45	ever started by hand (`uv run python -m cobalt.aset`, bare `nohup`, no
    46	supervision) and died silently at the Aug 29 10:35 reboot. Nobody
    47	noticed until the trading PC got connection-refused on `:5010`. It was
    48	restarted by hand at least twice since (2026-08-31 sessions) with no
    49	persistence fix until now.
    50	
    51	**Fix:** `com.cobalt.aset.plist` + `ops/start_aset.sh`.
    52	- `RunAtLoad: true` — starts on login/boot.
    53	- `KeepAlive: true` — unconditional restart on any exit (crash, kill,
    54	  even a clean 0 exit) — this is meant to be a persistent widget, not a
    55	  scheduled batch job like the archiver/prefill jobs above.
    56	- **Secret-free plist:** `COBALT_MASTER_KEY` is sourced inside
    57	  `ops/start_aset.sh` from `~/.cobalt_key` (the same key file
    58	  `cobalt.sh start` uses) — never written into the plist's
    59	  `EnvironmentVariables`. Without it, the sheet's pages still serve,
    60	  but `/api/prefill` (Finviz last-price fetch) fails every call because
    61	  VaultManager can't unlock.
    62	- **Logs with rotation:** `logs/aset.log` / `logs/aset.err`
    63	  (gitignored). Rotation is **best-effort, on-restart only**: launchd
    64	  binds stdout/stderr to those paths once at process spawn with no
    65	  SIGHUP/reopen support, and per this session's scope `ops/start_aset.sh`
    66	  does not touch `src/cobalt/aset`'s own Python — so true live rotation
    67	  would need either app-level logging changes (out of scope here) or a
    68	  root-owned `newsyslog.d` entry (not installed — avoided sudo). The
    69	  wrapper instead rotates each log to a timestamped `.YYYYMMDDHHMMSS`
    70	  suffix on every (re)start if it's grown past 5MB, keeping the 5 most
    71	  recent rotated files. For a KeepAlive service that's expected to stay
    72	  up for days/weeks at a stretch, this bounds worst-case growth but
    73	  does not guarantee any particular rotation cadence — if `aset.log`
    74	  grows unbounded between restarts, check it by hand.
    75	
    76	## NN#16 dev/prod vault split (2026-08-31)
    77	
    78	`configs/dev/vault.yaml`'s committed default no longer points at the
    79	real vault — it now points at `~/dev-vault-cobalt` (a skeleton copy:
    80	templates + Rules.md, no personal notes — see `docs/40 - DevDocs/cobalt/
    81	vault.md`). Every PRODUCTION consumer of `cobalt.vault.resolve_vault_path()`
    82	must therefore set `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`
    83	explicitly in its own environment, or it silently starts writing into
    84	the dev vault instead. All three plists that touch the vault do this:
    85	`com.cobalt.aset.plist` (via `ops/start_aset.sh`, so the plist itself
    86	stays free of it too) and both `com.cobalt.prefill-*.plist` (directly
    87	in `EnvironmentVariables`, since they have no wrapper script).
    88	
    89	**Action required (not done by this change):** `com.cobalt.aset` is
    90	already installed and running — its CURRENT process started before
    91	this fix and does not have `COBALT_VAULT_PATH` set. It needs
    92	`launchctl kickstart -k gui/$(id -u)/com.cobalt.aset` to pick it up;
    93	until then any card it saves would resolve the vault via the new dev
    94	default and land in `~/dev-vault-cobalt`, not the real vault. Not run
    95	automatically here — restarting a live production process during
    96	market hours needs a human go-ahead, not an agent's own judgment call.
    97	The two prefill plists are still not installed at all, so they carry
    98	no such risk yet.
    99	
   100	## uv path in ProgramArguments — FIXED 2026-09-03 (was the 09-03 prefill-silence root cause)
   101	
   102	**Rule: every `ops/*.plist` that invokes a binary directly in
   103	`ProgramArguments` (not through a wrapper script's own shebang) must use
   104	an ABSOLUTE path to that binary.** `uv` on this machine is a standalone
   105	install at `~/.local/bin/uv` (confirmed: `which uv` →
   106	`/Users/cobalt/.local/bin/uv`; `/opt/homebrew/bin/uv` → no such file;
   107	`brew list uv` → no such keg).
   108	
   109	Two different-looking bugs, same rule, found/fixed together:
   110	- `com.cobalt.archiver.plist` hardcoded the WRONG absolute path
   111	  (`/opt/homebrew/bin/uv`, doesn't exist here) — and was also simply not
   112	  loaded at all (`launchctl print` found no service). Its job had
   113	  therefore never run since 08-27 (`docs/30 - Design/archiver-runs.md`
   114	  has no nightly rows 08-28 onward) despite the Ledger's 08-29/31 claim
   115	  it was "verified running unattended" — that check evidently only
   116	  confirmed the plist file existed/looked right, not that launchd had
   117	  it loaded.
   118	- `com.cobalt.prefill-daily.plist` / `com.cobalt.prefill-drc.plist` used
   119	  a BARE `uv` (the 08-31 fix for the above bug, modeled on
   120	  `ops/start_aset.sh`'s pattern — see BACKLOG.md's 08-31 slice-2 entry).
   121	  This looked right but is itself wrong for a plist with no wrapper
   122	  script: `start_aset.sh`'s bare `uv` works because bash's own shebang
   123	  does a real PATH search before `exec`ing it; a bare name directly in
   124	  `ProgramArguments[0]` has no shell in front of it, and launchd's
   125	  posix_spawn does not reliably search the job's own
   126	  `EnvironmentVariables.PATH` the way a shell does. Confirmed by an
   127	  isolated diagnostic LaunchAgent: bare `uv` → `last exit code = 78:
   128	  EX_CONFIG`, empty stdout+stderr; absolute path → exit 0. This is
   129	  exactly what happened when `com.cobalt.prefill-daily` fired for real
   130	  at 05:15 on 09-03 (and `com.cobalt.prefill-drc` the evening before) —
   131	  loaded, fired, failed instantly, zero output, no alert. Full
   132	  root-cause writeup: `docs/00 - Project/BACKLOG.md`'s INCIDENT LOG,
   133	  2026-09-03 entry.
   134	
   135	**Fix (this session):** all three now use the absolute
   136	`/Users/cobalt/.local/bin/uv` in `ProgramArguments`; all three
   137	installed/reloaded and confirmed exit 0 on a manual `kickstart`.
   138	`com.cobalt.mainframe.plist` does not actually invoke `uv` at all (its
   139	`ProgramArguments` is `/Users/cobalt/cobalt/ops/start_mainframe.sh`,
   140	which uses `lms` — the earlier note above conflated it with the archiver
   141	bug; left uninvestigated further since it isn't broken).
   142	
   143	*(Path corrected 2026-09-09: this paragraph and the Inventory row both
   144	said `~/.lmstudio/start_mainframe.sh`. The wrapper is in the repo, where
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
   236	   the copy when the report lands in `40 - DevDocs/reports/` at merge.
   237	
   238	## herdr under launchd (0.9.0)
   239	
   240	**STATUS: LIVE since 2026-09-08 19:21 ET.** `com.cobalt.herdr` is
   241	bootstrapped, `configs/cobalt/jobs.yaml` carries `enabled: true`, and the
   242	F18 `herdr` probe is a real probe. On 2026-09-09 the server is **pid
   243	72998, run 3, herdr 0.9.0**, on the Mac and on Fedora.
   244	
   245	**launchd owns the server.** That is the whole change, and everything
   246	below follows from it.
   247	
   248	```sh
   249	launchctl list | grep com.cobalt.herdr            # the truth about who is running
   250	launchctl kickstart -k gui/$(id -u)/com.cobalt.herdr   # restart
   251	herdr server stop                                  # a DELIBERATE stop; nothing fights you
   252	```
   253	
   254	`KeepAlive` is `SuccessfulExit: false`, not `true`, and that is why
   255	`herdr server stop` works: a clean exit is a human decision and launchd
   256	leaves it alone. **A crash is the only case it restarts**, which is the
   257	only case worth restarting.
   258	
   259	### Attaching — the rules, not just the commands
   260	
   261	| From | Command | The rule |
   262	|---|---|---|
   263	| The Mac | `herdr` | Attaches to the persistent session. `herdr session attach default` names it explicitly. |
   264	| Fedora | `herdr --remote cobalt@cobalt` | **Only from a 0.9.0 client**, and **answer No to any replace prompt.** |
   265	| The phone | `ssh cobalt@cobalt` then `herdr` | **NEVER `--remote`.** There is no phone client; the phone is a terminal onto the Mac. |
   266	
   267	**WHY `--remote` HAS A RULE ATTACHED.** On the morning of 2026-09-09 the
   268	server was replaced twice — 06:03 and 07:26, both from Fedora, the second
   269	27 seconds after launchd had started it. A `herdr --remote` from a
   270	**0.8.2** client replaces the running server. 0.8.2 does prompt, and
   271	Dejan answered Yes without reading it, so this was partly procedure and
   272	not only version — which is why the rule is written as a rule and not as
   273	"upgrade and forget".
   274	
   275	**The fix was forward, not back.** Mac and Fedora went 0.8.2 → 0.9.0
   276	("client updates leave compatible servers untouched … replacing a remote
   277	server asks, default **No**"), and the server was restarted under launchd
   278	**from the Mac keyboard in Terminal.app — not from a herdr pane** — at
   279	08:17. Result: pid 72998, `endpoint_compatible yes`, heartbeat GREEN at
   280	08:19:57 (13 jobs / 11 probes).
   281	
   282	**The phone is still 0.8.2 and must not `--remote`.** `ssh` then `herdr`
   283	costs nothing and cannot replace anything.
   284	
   285	### Acceptance, 2026-09-09
   286	
   287	Dejan attached from Fedora over `--remote` on 0.9.0. **The client
   288	prompted before replacing; he answered No; `launchctl list | grep
   289	com.cobalt.herdr` still showed pid 72998 after four attaches.** The
   290	version fix and the procedure both hold. Recorded as PASSED.
   291	
   292	### What a restart brings back, and what it does not
   293	
   294	0.9.0's native agent restore is better than 0.8.2's, measured on the
   295	08:17 restart:
   296	
   297	* **Restored** — the session, workspace, tabs, panes and working
   298	  directories, **and** `claude`, `grok` and `qwen` were relaunched in
   299	  their panes with their sessions. The Claude1 conversation continued
   300	  without `claude --resume`.
   301	* **Not restored** — panes that were **empty shells**. Codex1 and
   302	  Gemini1 held no agent before the restart, so there was nothing for
   303	  restore to name; they were relaunched by hand.
   304	* **The standing rule is unchanged, and 0.9.0 does not soften it: never
   305	  rely on restore.** State goes to the vault or to Postgres **before** a
   306	  `/clear`, a restart or an update. An agent that reports a session
   307	  reference can be brought back; a conversation nobody wrote down cannot.
   308	
   309	### Integration updates append hooks — the probe watches for it
   310	
   311	`herdr integration install claude` rewrites Claude Code's hook config,
   312	and on **2026-09-09 at 08:33** the v8 → v9 update did **not** replace the
   313	guard pointer — it **APPENDED A SECOND `SessionStart` ENTRY** aimed at
   314	herdr's own script, so both would have fired. The duplicate was removed
   315	by hand and `~/.claude/settings.json` restored byte-identical to the
   316	pre-install backup (`~/.claude/settings.json.pre-herdr-v9`).
   317	
   318	This matters to this job, not just to the seats: v9 still hardcodes the
   319	agent name `herdr:claude` with **no harness detection**, so without
   320	`~/.claude/hooks/herdr-harness-guard.sh` every Grok session reports
   321	itself as `claude` in `herdr agent list` — **and that is the list the F18
   322	`herdr` probe asserts on**.
   323	
   324	Since 2026-09-09 **the probe checks the pointer as its third question**:
   325	`hooks.SessionStart` must be **exactly one entry with exactly one command
   326	hook** running the guard, and the guard must exist and be executable.
   327	Anything else is red, naming the drift. Counting is the check because a
   328	presence check would have called the 08:33 state fine.
   329	
   330	After any `brew upgrade herdr` or `herdr integration install`, force a
   331	beat rather than eyeballing the file:
   332	
   333	```sh
   334	launchctl kickstart -k gui/$(id -u)/com.cobalt.heartbeat
   335	tail -40 logs/heartbeat.log | grep herdr
   336	```
   337	
   338	### Where things live
   339	
   340	The socket is `/Users/cobalt/.config/herdr/herdr.sock` and the config
   341	`/Users/cobalt/.config/herdr/config.toml` — `herdr server reload-config`
   342	re-reads it without a restart, which is preferable to a restart for a
   343	config change. Server logs sit in the same directory
   344	(`herdr-server.log`); the launchd job's own stdout/stderr go to
   345	`ops/logs/herdr.log` and `ops/logs/herdr.err`.
   346	
   347	Nothing in `configs/` reaches this process, which is why its registry row
   348	carries `reads: []` — no deploy of ours can require restarting it.
   349	
   350	### Rolling it back
   351	
   352	Rolling back means **handing the server back to a manual start**, which
   353	is a downgrade from where it is now — do it only if launchd supervision
   354	is itself the problem.
   355	
   356	```sh
   357	launchctl bootout gui/$(id -u)/com.cobalt.herdr    # this STOPS the server; every pane goes
   358	# set `enabled: false` on com.cobalt.herdr in configs/cobalt/jobs.yaml, then:
   359	uv run cobalt jobs register                        # the probe goes quiet and says why
   360	/opt/homebrew/bin/herdr server &                   # back to the manual start
   361	```
   362	
   363	The order matters: `bootout` takes the terminal workspace down with it,
   364	so **run it from Terminal.app, not from a herdr pane** — the same reason
   365	the original handover had to happen at the keyboard. Land everything
   366	first; assume every conversation is lost.
   367	
   368	## Email OAuth token clock (F18 / S1-P4)
   369	
   370	The Google project behind `gmail.send` is still in **Testing** status, so a refresh token
   371	expires **7 days after consent**. Dejan retries **Publish** (from another browser); if it
   372	fails again, a fresh `uv run cobalt notify email-auth` consent resets the 7-day clock —
   373	repeat every **≤6 days** until Publish lands. After each consent: send a test alert and read
   374	the token date back (`cobalt notify` status / the heartbeat `email` probe line) — proof, not
   375	assumption. Ruled 09-09 (chat second opinion, item 10).
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
?? "docs/40 - DevDocs/reports/_inflight/"
?? "docs/40 - DevDocs/reports/heartbeat-blackout-2026-09-10.md"

exec
/bin/zsh -lc "nl -ba src/cobalt/jobs/wrapper.py | sed -n '85,210p'; nl -ba src/cobalt/jobs/store.py | sed -n '20,205p'; nl -ba src/cobalt/jobs/cli.py | sed -n '130,155p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
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

codex
The brief now specifies result preservation, empty `reads`, and plist replacement, and the triage report is present. Two gaps remain: alert selection happens before a vault failure can turn the beat RED, and F17’s database-dependent startup can prevent the beat from reaching its isolated stages.
exec
/bin/zsh -lc "nl -ba src/cobalt/jobs/config.py | sed -n '223,325p'; nl -ba configs/cobalt/jobs.yaml | sed -n '1,105p'; nl -ba configs/cobalt/jobs.yaml | sed -n '195,230p'; nl -ba ops/README.md | sed -n '1,38p'; nl -ba ops/README.md | sed -n '140,202p'; nl -ba ops/com.cobalt.heartbeat.plist | sed -n '1,82p'; rg -n 'jobs.yaml|load_job_registry|vault_outcome|notes|message' src/cobalt/jobs/migrations src/cobalt/aset src/cobalt/db_migrations configs/cobalt/db*" in /Users/cobalt/cobalt-wt/heartbeat-mr
 exited 1 in 0ms:
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
   316	
   317	    @property
   318	    def cadence(self) -> Optional[str]:
   319	        return self.schedule.describe() if self.schedule else None
   320	
   321	    @property
   322	    def pidfile_path(self) -> Optional[Path]:
   323	        return (REPO_ROOT / self.pidfile) if self.pidfile else None
   324	
   325	    @property
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
     1	# ops/ — LaunchAgents & wrapper scripts
     2	
     3	Everything here is captured in git as the SOURCE for what's installed
     4	to `~/Library/LaunchAgents/` — that install directory itself is outside
     5	the repo and not tracked. When you add or change a plist, re-copy it
     6	(see "Install / reload" below); the copy in `~/Library/LaunchAgents/`
     7	does not auto-update from git.
     8	
     9	## Inventory
    10	
    11	**Nine plists below, all of them loaded, as of 2026-09-09**
    12	(`launchctl list | grep com.cobalt`). `com.cobalt.herdr` was the one
    13	exception until the handover on 2026-09-08 at 19:21 ET; it is live now —
    14	see "herdr under launchd (0.9.0)" further down. `com.cobalt.generated`
    15	is new on 2026-09-09.
    16	
    17	This table is not the whole of `ops/`, and never was: `com.cobalt.backup`,
    18	`cards-expire`, `daymode-propose`, `heartbeat` and `obsidian` have
    19	plists and rows without a row here. **`configs/cobalt/jobs.yaml` is the
    20	authoritative list** — fourteen labels, cross-checked against `ops/`
    21	by `uv run cobalt validate` on every run of the gate. Read this table as
    22	prose about the ones with a story attached, not as an inventory.
    23	
    24	| Plist | Runs | Schedule | Wrapper | Installed |
    25	|---|---|---|---|---|
    26	| `com.cobalt.agent.plist` | `cobalt.sh start` (the Mattermost chief-of-staff agent) | RunAtLoad only, no KeepAlive | — | yes |
    27	| `com.cobalt.mainframe.plist` | `ops/start_mainframe.sh` (local LLM — the L23 local lane) | RunAtLoad only | `ops/start_mainframe.sh` | yes |
    28	| `com.cobalt.archiver.plist` | `/Users/cobalt/.local/bin/uv run archiver` (nightly bar archiver) | Mon-Fri 20:30 ET | — | yes (2026-09-03 — was not loaded before this) |
    29	| `com.cobalt.prefill-daily.plist` | `/Users/cobalt/.local/bin/uv run prefill daily` | Mon-Fri 05:15 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
    30	| `com.cobalt.prefill-drc.plist` | `/Users/cobalt/.local/bin/uv run prefill drc` | Mon-Fri 15:40 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
    31	| `com.cobalt.aset.plist` | `ops/start_aset.sh` → `uv run python -m cobalt.aset` (ASET sizing widget, :5010) | RunAtLoad + KeepAlive (persistent) | `ops/start_aset.sh` | yes |
    32	| `com.cobalt.herdr.plist` | `/opt/homebrew/bin/herdr server` (the terminal workspace every agent seat lives in) | RunAtLoad + KeepAlive on crash only | — | **yes (2026-09-08 19:21 — the handover)** |
    33	| `com.cobalt.generated.plist` | `/Users/cobalt/.local/bin/uv run cobalt generated commit` (commits the files a job rewrote today) | daily 23:37 ET | F17 wrapper | new 2026-09-09 |
    34	| `com.cobalt.seat-usage.plist` | `/Users/cobalt/.local/bin/uv run cobalt seat-usage run` (the hourly seat-usage report) | hourly 06:00-23:00 ET, every day | F17 wrapper (`cobalt seat-usage run`) | yes (2026-09-08) |
    35	
    36	The table above says which plists are *supposed* to be loaded.
    37	`configs/cobalt/jobs.yaml` is the machine-readable version of the same
    38	claim, and `uv run cobalt validate` compares the two: it fails on a job
   140	which uses `lms` — the earlier note above conflated it with the archiver
   141	bug; left uninvestigated further since it isn't broken).
   142	
   143	*(Path corrected 2026-09-09: this paragraph and the Inventory row both
   144	said `~/.lmstudio/start_mainframe.sh`. The wrapper is in the repo, where
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
     1	<?xml version="1.0" encoding="UTF-8"?>
     2	<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
     3	<plist version="1.0">
     4	<dict>
     5	    <key>Label</key>
     6	    <string>com.cobalt.heartbeat</string>
     7	    <key>EnvironmentVariables</key>
     8	    <dict>
     9	        <key>PATH</key>
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
    61	    <key>StandardErrorPath</key>
    62	    <string>/Users/cobalt/cobalt/logs/heartbeat.err</string>
    63	</dict>
    64	</plist>
zsh:1: no matches found: configs/cobalt/db*

exec
/bin/zsh -lc "rg --files src/cobalt/jobs/migrations src/cobalt/db_migrations configs | rg 'migration|placement'; rg -n 'load_job_registry|cobalt.jobs' src/cobalt/aset src/cobalt_agent; nl -ba src/cobalt/jobs/migrations/001_jobs.sql; nl -ba src/cobalt/jobs/killswitch.py | sed -n '50,110p'; nl -ba src/cobalt/jobs/watchdog.py | sed -n '90,205p'; nl -ba src/cobalt/db_migrations/cli.py | sed -n '1,135p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
 succeeded in 0ms:
src/cobalt/db_migrations/placement.py
src/cobalt/db_migrations/cli.py
src/cobalt/db_migrations/0001_schemas.sql
src/cobalt/db_migrations/__init__.py
src/cobalt/db_migrations/0002_move_tables.rollback.sql
src/cobalt/db_migrations/0002_move_tables.sql
src/cobalt/jobs/migrations/0001_cobalt_jobs.sql
nl: src/cobalt/jobs/migrations/001_jobs.sql: No such file or directory
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
    90	      fire again. Charter §3 F18's acceptance test is exactly this
    91	      ("unload a plist -> red within one interval").
    92	    * `loaded=True, pid=None` — registered with launchd, not currently
    93	      running. Correct and healthy for a one-shot between runs; a
    94	      FAILURE for a resident.
    95	    * `last_exit` — launchd's own record of how the last run ended,
    96	      which is the other half of what the Charter asks for ("every ops
    97	      plist loaded + last exit code").
    98	    """
    99	
   100	    label: str
   101	    loaded: bool
   102	    pid: Optional[int]
   103	    last_exit: Optional[int]
   104	    detail: str
   105	
   106	
   107	def launchctl_status(label: str, *, timeout: float = 5.0) -> LaunchdStatus:
   108	    """Ask launchd about one label. Fail-loud: a `launchctl` that cannot
   109	    be run RAISES rather than reporting "not loaded" — "the probe is
   110	    broken" and "the job is gone" are different facts, and collapsing
   111	    them is how a red condition becomes invisible (the same rule
   112	    `cobalt.obsidian` keeps)."""
   113	    binary = shutil.which("launchctl") or "/bin/launchctl"
   114	    if not os.path.exists(binary):
   115	        raise RuntimeError("launchctl not found — cannot probe launchd jobs.")
   116	    proc = subprocess.run(
   117	        [binary, "list"], capture_output=True, text=True, timeout=timeout
   118	    )
   119	    if proc.returncode != 0:
   120	        raise RuntimeError(
   121	            f"`launchctl list` exited {proc.returncode}: "
   122	            f"{proc.stderr.strip() or '(no stderr)'}"
   123	        )
   124	    for line in proc.stdout.splitlines():
   125	        parts = line.split("\t")
   126	        if len(parts) == 3 and parts[2].strip() == label:
   127	            pid_raw, status_raw = parts[0].strip(), parts[1].strip()
   128	            pid = int(pid_raw) if pid_raw.lstrip("-").isdigit() and pid_raw != "-" else None
   129	            try:
   130	                last_exit = int(status_raw)
   131	            except ValueError:
   132	                last_exit = None
   133	            detail = (
   134	                f"loaded, pid {pid}" if pid is not None
   135	                else f"loaded, not running (last exit {status_raw})"
   136	            )
   137	            return LaunchdStatus(label, True, pid, last_exit, detail)
   138	    return LaunchdStatus(
   139	        label, False, None, None,
   140	        "NOT LOADED in launchd — `launchctl list` does not know this label, so it "
   141	        "will never fire again. Reload it: "
   142	        f"launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/{label}.plist",
   143	    )
   144	
   145	
   146	def launchctl_pid(label: str, *, timeout: float = 5.0) -> tuple[Optional[int], str]:
   147	    """(pid, detail). Kept as the narrow question residents ask."""
   148	    status = launchctl_status(label, timeout=timeout)
   149	    if status.pid is not None:
   150	        return status.pid, f"launchd pid {status.pid}"
   151	    return None, status.detail
   152	
   153	
   154	def pidfile_alive(spec: JobSpec) -> tuple[bool, str]:
   155	    """(alive, detail) for a detached resident tracked by a PID file."""
   156	    path = spec.pidfile_path
   157	    if path is None or not path.exists():
   158	        return False, f"no pid file at {path} — the process was never started, or it cleaned up"
   159	    raw = path.read_text().strip()
   160	    if not raw.isdigit():
   161	        return False, f"pid file {path} does not contain a pid ({raw[:40]!r})"
   162	    pid = int(raw)
   163	    try:
   164	        os.kill(pid, 0)          # signal 0: existence check, changes nothing
   165	    except ProcessLookupError:
   166	        return False, f"pid {pid} from {path} is GONE — stale pid file, process is dead"
   167	    except PermissionError:
   168	        return True, f"pid {pid} exists (owned by another user)"
   169	    return True, f"pid {pid} alive (from {path})"
   170	
   171	
   172	# ---------------------------------------------------------------------
   173	# schedule arithmetic — "should this have run by now?"
   174	# ---------------------------------------------------------------------
   175	
   176	
   177	def last_due(spec: JobSpec, now_et: datetime) -> Optional[datetime]:
   178	    """The most recent CALENDAR moment this one-shot was scheduled to
   179	    fire, at or before `now_et`. `None` for an interval job (which has no
   180	    calendar moments — see `is_missed`) and for a resident.
   181	
   182	    Weekday numbering is launchd's (1 = Monday), matching the plists this
   183	    mirrors.
   184	    """
   185	    schedule = spec.schedule
   186	    if schedule is None or schedule.interval_minutes() is not None:
   187	        return None
   188	
   189	    hh, _, mm = schedule.at.partition(":")
   190	    hour, minute = int(hh), int(mm)
   191	    # launchd: Sunday is 0 and 7; python's isoweekday() is Mon=1..Sun=7.
   192	    wanted = {0 if d == 7 else d for d in schedule.weekdays}
   193	    probe: date = now_et.date()
   194	    for _ in range(14):
   195	        iso = probe.isoweekday()
   196	        launchd_day = 0 if iso == 7 else iso
   197	        if launchd_day in wanted:
   198	            due = datetime(
   199	                probe.year, probe.month, probe.day, hour, minute, tzinfo=ET
   200	            )
   201	            if due <= now_et:
   202	                return due
   203	        probe -= timedelta(days=1)
   204	    return None
   205	
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

exec
/bin/zsh -lc "nl -ba src/cobalt/db_migrations/__init__.py; nl -ba src/cobalt/db_migrations/cli.py | sed -n '148,230p'; nl -ba src/cobalt/jobs/migrations/0001_cobalt_jobs.sql; rg -n 'def upsert_unit|class WriteResult|return WriteResult|changed|dry_run' src/cobalt/vaultwrite/writer.py | head -45; nl -ba src/cobalt/session/clock.py | sed -n '179,222p'" in /Users/cobalt/cobalt-wt/heartbeat-mr
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
     1	-- 0001: cobalt_jobs — F17's persisted row per scheduled job (Charter §3, L18).
     2	--
     3	-- WHY THE `cobalt_` PREFIX, when no other new-core table has one.
     4	-- `cobalt_brain` is the SAME Postgres database Mattermost uses: 129
     5	-- tables, of which 103 were Mattermost's (they moved to their own
     6	-- database on 2026-09-04, ADR-0006) — and one of them was called
     7	-- `jobs`, with 164,320 rows of `expiry_notify` / `delete_expired_posts`
     8	-- work items in it. `CREATE TABLE IF NOT EXISTS jobs` therefore did
     9	-- NOTHING, silently, and the first query failed with `column "label"
    10	-- does not exist` (found 2026-09-04 by the first production dry run —
    11	-- the fail-loud discipline is what surfaced it in seconds rather than
    12	-- in a week of green heartbeats reporting on Mattermost's table).
    13	--
    14	-- `jobs` and `kill_switch` are generic enough that a collision was
    15	-- always going to happen; the existing new-core tables (aset_sizings,
    16	-- vault_writes, card_transitions, day_modes, bars) are specific enough
    17	-- that none has one, and they are NOT renamed here — they hold live
    18	-- trading record and a rename is a migration, not a naming preference.
    19	-- New tables from this prompt take the prefix.
    20	--
    21	-- ONE ROW PER LAUNCHD LABEL, and the label is the join key everywhere:
    22	-- configs/cobalt/jobs.yaml, ops/*.plist, `launchctl list`, and the F18
    23	-- heartbeat all name the same string.
    24	--
    25	-- WHY THE COLUMNS ARE THESE COLUMNS:
    26	--   state/started_at/finished_at/exit_code/last_error  — what happened.
    27	--   heartbeat_at  — the ONLY thing that distinguishes a long job from a
    28	--                   hung one. Without it `running` means "started and did
    29	--                   not finish", which is true of both.
    30	--   expected_cadence — rendered from the schedule in jobs.yaml, so the
    31	--                   MISSED probe reads one place and an operator reading
    32	--                   this table sees when the job should have run.
    33	--   heartbeat_source — `self` | `launchd` | `pidfile`. Cobalt cannot run
    34	--                   a heartbeat thread inside Obsidian or LM Studio, so
    35	--                   the watchdog stamps for them from a real probe. The
    36	--                   column exists so that is VISIBLE rather than implied:
    37	--                   a probe saying "the process exists" and a process
    38	--                   saying "I am working" are different claims.
    39	--   last_result   — the run's own numbers, JSON. The archiver's rows
    40	--                   written land here, which is what makes F18's
    41	--                   "archiver freshness (last run + rows written)"
    42	--                   answerable without a second table.
    43	CREATE TABLE IF NOT EXISTS cobalt_jobs (
    44	    label TEXT PRIMARY KEY,
    45	    kind TEXT NOT NULL CHECK (kind IN ('resident', 'one-shot')),
    46	    expected_cadence TEXT,
    47	    timeout_s INTEGER NOT NULL CHECK (timeout_s > 0),
    48	    state TEXT NOT NULL DEFAULT 'pending'
    49	        CHECK (state IN ('pending', 'running', 'done', 'failed', 'zombie')),
    50	    heartbeat_source TEXT NOT NULL DEFAULT 'self'
    51	        CHECK (heartbeat_source IN ('self', 'launchd', 'pidfile')),
    52	    started_at TIMESTAMPTZ,
    53	    heartbeat_at TIMESTAMPTZ,
    54	    finished_at TIMESTAMPTZ,
    55	    exit_code INTEGER,
    56	    last_error TEXT,
    57	    last_result JSONB,
    58	    registered_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    59	    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
    60	);
    61	
    62	-- The kill switch (F17d). ONE row, id = TRUE, so there is exactly one
    63	-- answer to "is Cobalt stopped" and no way to have two.
    64	CREATE TABLE IF NOT EXISTS cobalt_kill_switch (
    65	    id BOOLEAN PRIMARY KEY DEFAULT TRUE CHECK (id),
    66	    active BOOLEAN NOT NULL DEFAULT FALSE,
    67	    phrase TEXT,
    68	    set_by TEXT,
    69	    set_at TIMESTAMPTZ,
    70	    cleared_by TEXT,
    71	    cleared_at TIMESTAMPTZ
    72	);
    73	
    74	INSERT INTO cobalt_kill_switch (id, active) VALUES (TRUE, FALSE) ON CONFLICT (id) DO NOTHING;
25:   same directory) behind an mtime+hash guard: if the file changed since
124:    """The note changed between the read this edit was computed from and
246:class WriteResult:
248:    action: str  # created | updated | unchanged | skipped_exists | skipped | restored
252:    dry_run: bool = False
266:    def changed(self) -> bool:
271:        head = f"[{'DRY-RUN' if self.dry_run else 'WRITE'}] {self.action}: {self.path}"
290:        parts.append(self.diff if self.diff else "  (no diff — nothing changed)")
326:# Actions that put (or would put) bytes on disk. "unchanged", "skipped"
335:    entry points rather than the ten `return WriteResult(...)` sites, so
357:        dry_run: bool = False,
364:        self.dry_run = dry_run
398:        if self.dry_run:
447:        if self._purged or self.store is None or self.dry_run:
466:                f"ABORT: {path} changed on disk between this run's read and its "
541:            if self.dry_run:
570:            return WriteResult(
573:                dry_run=self.dry_run,
588:        if self.dry_run:
589:            return WriteResult(
593:                dry_run=True,
612:        return WriteResult(
644:    def upsert_unit(
757:                state["unchanged"] = True
776:            return WriteResult(
778:                dry_run=self.dry_run, hash_before=snapshot.sha256,
783:            return WriteResult(
784:                path=path, action="unchanged", section=section, unit=unit_id,
785:                dry_run=self.dry_run, hash_before=snapshot.sha256,
791:        changed = new_text != (snapshot.text or "")
792:        return WriteResult(
794:            action="updated" if changed else "unchanged",
798:            dry_run=self.dry_run,
912:        Everything else L28 asks for still applies, unchanged: the same
976:            return WriteResult(
977:                path=path, action="unchanged", section=section_label, unit=region_id,
978:                dry_run=self.dry_run, hash_before=snapshot.sha256, hash_after=snapshot.sha256,
983:        changed = new_text != (snapshot.text or "")
984:        return WriteResult(
986:            action="updated" if changed else "unchanged",
990:            dry_run=self.dry_run,
1055:                f"written — {row['note']} has changed since. Restoring would "
1094:          the original whole-section replace, unchanged. Rows written
1255:            return WriteResult(
1256:                path=path, action="unchanged", section=section_name, unit=row["unit"],
   179	                    + ", ".join(f"{k}={self._b[k]:%H:%M}" for k in keys)
   180	                )
   181	        if self._b["session.market_reset_open"] != self._b["session.aftermarket_close"]:
   182	            # Not fatal — an early close already opens such a gap on
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

codex
Reviewed as a **build brief**: RESOLVED means the revised requirements address the finding; implementation is still pending.

**Round-1 blockers**

1. **RESOLVED — deployment and rollback.** Items 3 and 5 require replacing the invocation, bootout/bootstrap, registry updates explicitly described as “rows only,” and restoration of the previous plist. This addresses the registration/install confusion. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:8](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:8), [cli.py:63](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:63), [ops/README.md:3](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:3). The new migration procedure has a separate blocker below.

2. **OPEN — empty `reads` fixed; restart derivation missing.** Item 3 correctly prohibits heartbeat `reads`, matching its one-shot declaration and validation. But item 5 hard-codes heartbeat’s reload without requiring reader analysis for every changed configuration or resolving unknown paths. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:8](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:8), [jobs.yaml:206](/Users/cobalt/cobalt-wt/heartbeat-mr/configs/cobalt/jobs.yaml:206), [config.py:290](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/config.py:290), [ops/README.md:175](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:175).

3. **RESOLVED — result ownership.** Item 3 explicitly protects beat details and `green_summary_date`; item 4(e) requires verification after wrapper completion. Those requirements directly address subprocess result replacement. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:7](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:7), [cli.py:137](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:137), [store.py:162](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/store.py:162).

4. **OPEN — durable degradation specified, late-failure notification unresolved.** Item 2 requires persisted outcomes and RED on failure, but item 1 selects alerts before the vault operation. An otherwise-green beat can send an all-clear—or nothing—then fail its vault write without sending a RED alert. Item 4(b)’s “alerts + row present” does not require an alert reporting that failure. Evidence: [brief:4](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:4), [brief:5](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:5), [brief:7](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:7), [runner.py:262](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:262).

5. **RESOLVED — triage report supplied.** The input named at brief line 1 now exists. It documents four attempts each night, eight refusal records, and the unguarded write preceding alerts and persistence. Evidence: [triage:18](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/heartbeat-blackout-2026-09-10.md:18), [triage:33](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/heartbeat-blackout-2026-09-10.md:33), [runner.py:249](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:249). Incident evidence was reviewed from the report; production logs were not rechecked.

**BLOCKERS**

- **Still open: restart derivation and late-failure reporting**, above. Specify a post-vault finalization step that persists the final outcome, severity, and reason, and sends corrective RED notifications when needed. There is no existing persisted `notes/message` column: `Beat.notes` is in memory, and current result serialization omits it ([render.py:32](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/render.py:32), [runner.py:279](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:279)). Name its storage location explicitly.
- **New: F17 can prevent database-outage alerts before `run_beat` starts.** The wrapper performs schema setup, registration, and `mark_running` before yielding to the subprocess ([wrapper.py:133](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:133), [wrapper.py:142](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:142)). Isolating stages inside `run_beat` cannot catch these failures. Define heartbeat-specific behavior and test the wrapped entry point with database access failing before launch.
- **New: the migration command does not execute the proposed feature migration.** `cobalt db migrate` runs a fixed two-file list; feature migrations run through their stores ([db_migrations/__init__.py:9](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:9), [db_migrations/__init__.py:25](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:25)). Specify the actual forward/rollback execution path. Simply extending that list also needs proof handling: its digest excludes only `user_id`, so adding `vault_outcome` changes populated-row digests and produces an error **after commit** ([cli.py:96](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:96), [cli.py:187](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:187)).

**RISKS**

- Define missing-note behavior: `write_note_block` returns `None` without raising, so exception handling alone cannot justify `written` ([runner.py:137](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:137)).
- Add session-boundary and holiday coverage; market reset is calendar-dependent ([clock.py:196](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/session/clock.py:196)).
- LIVE acceptance should require GREEN **when other checks are healthy**. Deferral must preserve unrelated RED findings; refusal counts remain informational by design ([render.py:43](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/render.py:43), [probes.py:323](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/probes.py:323)).

**VERDICT: RETHINK.** Close the notification, wrapper-startup, migration, and restart-analysis gaps before build. This was a static review; no tests or production actions were run.
tokens used
54,827
Reviewed as a **build brief**: RESOLVED means the revised requirements address the finding; implementation is still pending.

**Round-1 blockers**

1. **RESOLVED — deployment and rollback.** Items 3 and 5 require replacing the invocation, bootout/bootstrap, registry updates explicitly described as “rows only,” and restoration of the previous plist. This addresses the registration/install confusion. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:8](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:8), [cli.py:63](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:63), [ops/README.md:3](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:3). The new migration procedure has a separate blocker below.

2. **OPEN — empty `reads` fixed; restart derivation missing.** Item 3 correctly prohibits heartbeat `reads`, matching its one-shot declaration and validation. But item 5 hard-codes heartbeat’s reload without requiring reader analysis for every changed configuration or resolving unknown paths. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:8](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:8), [jobs.yaml:206](/Users/cobalt/cobalt-wt/heartbeat-mr/configs/cobalt/jobs.yaml:206), [config.py:290](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/config.py:290), [ops/README.md:175](/Users/cobalt/cobalt-wt/heartbeat-mr/ops/README.md:175).

3. **RESOLVED — result ownership.** Item 3 explicitly protects beat details and `green_summary_date`; item 4(e) requires verification after wrapper completion. Those requirements directly address subprocess result replacement. Evidence: [brief:6](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:6), [brief:7](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:7), [cli.py:137](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/cli.py:137), [store.py:162](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/store.py:162).

4. **OPEN — durable degradation specified, late-failure notification unresolved.** Item 2 requires persisted outcomes and RED on failure, but item 1 selects alerts before the vault operation. An otherwise-green beat can send an all-clear—or nothing—then fail its vault write without sending a RED alert. Item 4(b)’s “alerts + row present” does not require an alert reporting that failure. Evidence: [brief:4](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:4), [brief:5](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:5), [brief:7](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/_inflight/heartbeat-fix-brief.md:7), [runner.py:262](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:262).

5. **RESOLVED — triage report supplied.** The input named at brief line 1 now exists. It documents four attempts each night, eight refusal records, and the unguarded write preceding alerts and persistence. Evidence: [triage:18](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/heartbeat-blackout-2026-09-10.md:18), [triage:33](/Users/cobalt/cobalt-wt/heartbeat-mr/docs/40%20-%20DevDocs/reports/heartbeat-blackout-2026-09-10.md:33), [runner.py:249](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:249). Incident evidence was reviewed from the report; production logs were not rechecked.

**BLOCKERS**

- **Still open: restart derivation and late-failure reporting**, above. Specify a post-vault finalization step that persists the final outcome, severity, and reason, and sends corrective RED notifications when needed. There is no existing persisted `notes/message` column: `Beat.notes` is in memory, and current result serialization omits it ([render.py:32](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/render.py:32), [runner.py:279](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:279)). Name its storage location explicitly.
- **New: F17 can prevent database-outage alerts before `run_beat` starts.** The wrapper performs schema setup, registration, and `mark_running` before yielding to the subprocess ([wrapper.py:133](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:133), [wrapper.py:142](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/jobs/wrapper.py:142)). Isolating stages inside `run_beat` cannot catch these failures. Define heartbeat-specific behavior and test the wrapped entry point with database access failing before launch.
- **New: the migration command does not execute the proposed feature migration.** `cobalt db migrate` runs a fixed two-file list; feature migrations run through their stores ([db_migrations/__init__.py:9](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:9), [db_migrations/__init__.py:25](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/__init__.py:25)). Specify the actual forward/rollback execution path. Simply extending that list also needs proof handling: its digest excludes only `user_id`, so adding `vault_outcome` changes populated-row digests and produces an error **after commit** ([cli.py:96](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:96), [cli.py:187](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/db_migrations/cli.py:187)).

**RISKS**

- Define missing-note behavior: `write_note_block` returns `None` without raising, so exception handling alone cannot justify `written` ([runner.py:137](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/runner.py:137)).
- Add session-boundary and holiday coverage; market reset is calendar-dependent ([clock.py:196](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/session/clock.py:196)).
- LIVE acceptance should require GREEN **when other checks are healthy**. Deferral must preserve unrelated RED findings; refusal counts remain informational by design ([render.py:43](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/render.py:43), [probes.py:323](/Users/cobalt/cobalt-wt/heartbeat-mr/src/cobalt/heartbeat/probes.py:323)).

**VERDICT: RETHINK.** Close the notification, wrapper-startup, migration, and restart-analysis gaps before build. This was a static review; no tests or production actions were run.
