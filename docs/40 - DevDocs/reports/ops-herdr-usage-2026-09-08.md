# ops/herdr-usage — 2026-09-08

Branch `ops/herdr-usage`, worktree `~/cobalt-wt/ops-herdr-usage`, one
commit, **READY FOR MERGE**. Nothing has been loaded, bootstrapped,
stopped or restarted. `~/cobalt` stayed on `main` throughout.

---

## LINE 0 — cleanup

`sprint-2/data-model` was merged into `main` (its tip `3f071e4` is an
ancestor of `f2e1720`), so the finished worktree came out and the branch
went with it.

```
git worktree remove ~/cobalt-wt/sprint-2-data-model
git branch -d sprint-2/data-model          # Deleted branch (was 3f071e4)
```

There was **no `origin/sprint-2/data-model`** to delete — `git branch -r`
lists only `origin/main` and `origin/HEAD`, so that branch was never
pushed. `~/cobalt` is clean on `main`, one worktree remains
(`~/cobalt-wt/ops-herdr-usage`).

---

## PART A — herdr as an ops-registered launchd job (BUILD ONLY)

### What landed

| Artifact | State |
|---|---|
| `ops/com.cobalt.herdr.plist` | written, `plutil -lint` OK, **not installed, not bootstrapped** |
| `configs/cobalt/jobs.yaml` row | `com.cobalt.herdr`, resident, `supervisor: launchd`, `timeout_s: 300`, **`enabled: false`** |
| `JobSpec.enabled` | new field, defaults `true`; the watchdog skips a disabled row before it asks launchctl anything |
| `heartbeat.probes.herdr` | socket accept + `agent list`, gated on the flag |
| `ops/README.md` → "herdr handover" | the keyboard procedure |
| `docs/40 - DevDocs/reports/codex-seat-test-2026-09-07.md` §10 | the hook-guard checklist line, above the Codex line |

### The plist, and the two decisions in it

`ProgramArguments` is `/opt/homebrew/bin/herdr server` — **no flags**,
and that is a reading, not an omission. The live process list on
2026-09-08 shows exactly:

```
cobalt  51236  /opt/homebrew/bin/herdr server        # up since Sun 11:00
cobalt  51235  herdr                                 # client
cobalt  26938  herdr                                 # client
```

herdr 0.8.2 takes no server arguments; its configuration is
`~/.config/herdr/config.toml`, which `herdr server reload-config`
re-reads. Adding a flag the manual server never had would have made the
handover a behaviour change as well as a supervision change.

**`KeepAlive` is `SuccessfulExit: false`, not `true`.** `herdr server
stop` exits 0 and is a deliberate human action; a bare `KeepAlive` would
bring the server straight back up every time he stopped it and would
make a herdr update — which stops the server — impossible to finish. A
crash is the case worth restarting and it is the only one.

`COBALT_ENV=production` is declared even though herdr never reads it, so
the suite's "every ops plist names its side" invariant stays a rule
rather than a habit, and so a shell opened in a herdr pane inherits
production rather than an unset value.

### Why `enabled: false` exists at all

The prompt's hard rule was "do not restart, stop or bootstrap the herdr
server tonight", and the reason generalises past tonight: **the server
this job supervises is the one hosting the terminal that would bootstrap
it.** `launchctl bootstrap` with the manual server up produces either a
second server or a killed first one, and either way the pane issuing the
command dies mid-command and cannot come back to check its own work.

That made a registry row a problem. F17's sweep asks `launchctl` about
every job **first**, and an unloaded label answers `NOT LOADED in
launchd` — a red every 15 minutes for a state somebody chose on purpose,
which is precisely how a heartbeat stops being read. So `enabled` is a
declared field rather than a special case:

* the sweep reports a disabled row as `disabled` / `ok=True` with
  `NOT LOADED BY DESIGN`, and probes nothing;
* the `herdr` probe returns green, names the flag, and points at the
  handover procedure — and a test asserts it does not touch the socket
  while disabled;
* `cobalt validate` prints a **`NOT LOADED BY DESIGN`** line naming every
  such row, so the state cannot be forgotten:

```
Jobs (F17): 13 registered — 5 resident, 8 one-shot. Kill phrase 'COBALT STOP'.
  NOT LOADED BY DESIGN (1): com.cobalt.herdr — the herdr server — the terminal workspace hosting every agent seat
  These are built and registered; their plists are not bootstrapped.
  registry <-> ops/: 13 label(s), exact match.
  registry <-> plists: schedules and COBALT_ENV agree on every job.
```

Everything else still applies to it: it must have a plist in `ops/`, its
plist must carry `COBALT_ENV`, and the registry/`ops/` parity test still
counts it.

### The probe asks two questions

`herdr` on the beat connects to `~/.config/herdr/herdr.sock` **and** runs
`herdr agent list`. The socket alone is not the test, for the same reason
the ASET sheet's PID is not the test: a socket file outlives the process
that made it, and a wedged server still holds one open. Red on either
half, and the message names `com.cobalt.herdr` with the kickstart line.

Proven against a **real AF_UNIX socket** in
`tests/cobalt/test_herdr_probe.py` — a live listener, a stale socket
file (bound then closed, which is what a killed server leaves behind),
and a socket that accepts but will not answer. A mocked `socket` module
would have proven the code calls a function; a real listener proves the
probe can tell "accepting" from "stale file", which is the distinction it
exists to make. The `agent list` parser is pinned to the payload the live
0.8.2 server returned today.

### Heartbeat, right now

```
OK   herdr                    com.cobalt.herdr is registered with `enabled: false` — NOT PROBED.
                              The plist is built and deliberately not loaded; the server is running
                              under a manual start. ops/README.md 'herdr handover' is the procedure,
                              and flipping that flag is its last step.
OK   com.cobalt.herdr         disabled  registered but NOT LOADED BY DESIGN (`enabled: false` in
                              configs/cobalt/jobs.yaml) — nothing is probed and nothing is claimed.
```

### The handover procedure

`ops/README.md` → **"herdr handover — a keyboard procedure, not a job"**.
Nine steps: record the panes → land everything → `herdr server stop` →
copy + bootstrap → verify (`launchctl list`, `herdr status server`,
`herdr agent list`, the err log) → re-attach and re-open → re-expose
`/remote-control` on Claude1 → **flip the flag** → force a beat.

It also records what a restart does and does not restore, from the
2026-09-06 measurement in `PROJECT-LEDGER.md` (**1 of 2 panes**): the
session, workspace, tabs, panes and working directories come back;
the *conversation* inside an agent does not — the pane that was lost was
running `claude --resume`, and nothing in herdr owns or replays a
harness's own session state. The standing rule is unchanged: never rely
on restore; state goes to the vault or Postgres before a `/clear`, a
restart or an update.

Re-attach, three ways: `herdr` at the Mac; `herdr --remote
cobalt@<mac>` from Fedora (text and image paste, which is why it
replaced VNC); `ssh` then `herdr` from the phone over Tailscale — there
is no phone client, the phone is a terminal onto the Mac.

### The seat checklist line

Added to `codex-seat-test-2026-09-07.md` §10, immediately **above** the
Codex line:

> **Re-verify the hook guard after every herdr bump** — a herdr update
> replaces the herdr-managed hook script and can rewrite the harness
> configs that point at it. Confirm `~/.claude/settings.json`'s
> `hooks.SessionStart` still points at
> `~/.claude/hooks/herdr-harness-guard.sh`, that the guard is still
> there and executable, and re-run the three-case scratch proof in
> `seats-followup-2026-09-08.md` §b. The failure mode is silent: the
> bump reverts the pointer, both hooks fire again, and every Grok
> session reports itself as `claude` in `herdr agent list` — **which is
> also the list the F18 `herdr` probe reads.**

That last clause is the new coupling this branch introduces, and it is
why the line belongs beside the Codex one rather than in a note
somewhere.

---

## PART B — the seat-usage report

### The ccusage gate result (L15, four gates)

| Gate | Answer | Evidence |
|---|---|---|
| Proven | yes | 59,123 npm downloads in the week to 2026-09-06 |
| Conformant | yes | read-only over harness logs; no Cobalt DB, no vault note, fixed-argv `subprocess.run`, no shell |
| Industry-standard | yes | MIT; **zero** declared runtime dependencies; one bin entry |
| Reviewed-clean | yes | `npm install -g --prefix ~/.npm-global ccusage@20.0.20` — 2 packages, outside the repo and the system prefix |

Installed at `/Users/cobalt/.npm-global/bin/ccusage`, version
**20.0.20**, pinned in `configs/cobalt/seat_usage.yaml` and re-checked
against `--version` on **every run** — a mismatch crashes rather than
warns. `@latest` appears nowhere, and a test asserts it never will.

```
$ uv run cobalt seat-usage gate
tool          ccusage
pinned        20.0.20
binary        /Users/cobalt/.npm-global/bin/ccusage
license       MIT
network       NONE at run time (--offline)
report        …/docs/40 - DevDocs/reports/seat-usage.md
installed     20.0.20  (matches the pin)
argv          …/ccusage daily --json --breakdown --since 20260908 --until 20260908 --by-agent --offline
```

**Two flags were added to the prompt's command, and both are load-bearing.**
`--offline` is the "no network at run time" gate. `--by-agent` adds the
observed-seat dimension the role-hint column needs; it changes no number,
it adds a fact. `--until` pins the run to one day so a clock skew cannot
widen it.

### The gate has a consequence, and it is the interesting part

`--offline` prices from ccusage's bundled table. Measured today, both
ways, back to back on identical token counts:

| model | online $ | offline $ | delta |
|---|---:|---:|---:|
| `claude-opus-5` | 137.4910 | 137.4910 | 0.0000 |
| `claude-sonnet-5` | 8.5494 | 8.5494 | 0.0000 |
| `grok-4.6-build` | 0.0289 | 0.0289 | 0.0000 |
| `mainframe` | 0.0000 | 0.0000 | 0.0000 |
| **`claude-fable-5-1`** | **17.3236** | **0.0000** | **−17.3236** |
| **`gpt-6-astra`** | **0.0431** | **0.0000** | **−0.0431** |
| TOTAL | 163.4360 | 146.0693 | −17.3667 |

The bundled table has **no rate** for two models that were used all day,
and prices them at exactly `$0.00`. Shipping that as written would have
put "$0.00" beside seventeen dollars of real usage — a plausible-empty
artifact, which is the one thing the fail-loud law forbids outright.

**The silent-zero guard.** A model with tokens, priced at `None` or
exactly `0.0`, that the config does not declare free, is reported as
**unpriced** — never as zero. The day total is labelled a **floor**
(`≥ $…`). A blockquote names the models, every hour, next to the number
they distort, and says the fix is a deliberate pin bump with a diff and
never a run-time network call.

`mainframe` gets its `$0.00` **and a footnote and no warning** — the
prompt's requirement — but by a general mechanism rather than a special
case: it is named in `zero_cost_models` with the reason (it is the local
Qwen3.8-27B on this Mac; its cost is electricity, not API spend), and
membership of that list is exactly what separates "free" from
"unpriced". That distinction cannot be inferred, so it is declared.

### The job

`com.cobalt.seat-usage`, one-shot, `supervisor: self`, `timeout_s: 300`,
**hourly 06:00–23:00 ET, every day including weekends** — a Saturday's
spend is as real as a Tuesday's.

launchd has no "every 60 minutes between 06:00 and 23:00": `StartInterval`
never stops and `StartCalendarInterval` is a list of moments. So the
schedule grew a shape — `Schedule.window_tunable` — and the window is
**expanded into 126 calendar entries** (18 hours × 7 days) by
`calendar_entries()`. `cobalt validate` and the test suite each compare
the plist's array against that list **entry for entry**, and validate
also refuses a plist carrying both a calendar array and a `StartInterval`
(launchd would honour both and the job would run outside its window).

`watchdog.is_missed()` learned the same window, and had to: an hourly
job that stops at 23:00 would otherwise be reported MISSED at 01:05
every single night, and inside the window the clock starts when the
window **opens** — measuring the 06:00 run against last night's 23:00
would report a miss every morning. Both cases are tested.

### The report file

`docs/40 - DevDocs/reports/seat-usage.md` — newest day on top, one
`cobalt:unit seat-usage:<YYYY-MM-DD>` per day, same id so the same hour's
table is replaced rather than appended.

```
<!-- cobalt:days -->
<!-- cobalt:section seat-usage:2026-09-08 -->
### 2026-09-08

weekly_pct_open:
weekly_pct_close:

<!-- cobalt:unit seat-usage:2026-09-08 -->
| model | role hint | cache read | cache write | output | API-equivalent $ | Δ since last run |
```

**One section per day is a mechanical decision, not a stylistic one.**
`upsert_unit` appends a new unit at the *end* of its section, and the
newest day has to be at the *top*; a per-day section can be **placed**,
so newest-on-top comes from the write path itself rather than from
re-sorting the file every hour. Nothing above or below the anchor is
touched.

**"API-equivalent $" is labelled as such**, in the file's own preamble:
the seats run on consumer plans (L29), so this is what the same tokens
would have cost at published API rates. A size, not an amount owed.

**Δ** is the change in that column since the previous run, read from the
job row's own `last_result` — no new table, the same call
`should_send_green` makes. An em dash means *no comparable figure*
(first run of the day, a new model, either side unpriced); never a zero,
because a zero claims the number held steady, which is a different
statement from not knowing. A snapshot from a different day is refused.

**Input tokens** are not a column — the prompt's column list is the
column list, and they are a rounding error beside cache reads — but they
are printed under the table rather than dropped.

### The human cells, and the bug this found

`weekly_pct_open:` / `weekly_pct_close:` sit **outside** the generated
unit and inside the day's section, seeded blank once and never written
again (clause 2a).

The first implementation had a real defect, found by deleting the report
file during testing: `upsert_region` merges three ways, and a **stale
audit baseline** — a day's row surviving in Postgres while its block left
the file — makes the merge read an empty span against a non-empty
baseline as *"the human deleted these lines"*, keep them deleted, and
report `unchanged`. The cells silently never came back.

Fixed at the root rather than papered over: the seed's audit id now
carries a hash of the section it is writing into
(`seat-usage-human:2026-09-08:f995ea3a`), so **every seed is a fresh id
with no baseline** and the merge always takes the clean-insert path. It
is deterministic, and it never appears in the note — a region is
marker-less, so the id lives only in `vault_writes`. Belt and braces, a
verification after the seed raises loudly if the cells still are not
there, with the one-line fix, which is his to make because they are his
cells.

Proven, in order: delete the file and run twice → cells seeded both
times, exit 0; fill a cell and run again → `already present — not touched
(clause 2a)`, the value survives every later table rewrite.

The presence check reads the **file**, not the database, so it holds on a
run that cannot reach Postgres.

### The L28 carve-out

The report is repo content by R3 — versioned, reviewed in a diff, no
human note in the folder — but `VaultWriter` refused every path inside
the repo working tree. Rather than write it with `open(..., "w")`, which
would regenerate over Dejan's own numbers once an hour, the writer grew
one narrow, code-declared tuple:

```python
REPO_OWNED_ROOTS: tuple[str, ...] = ("docs/40 - DevDocs/reports",)
```

A path inside it is accepted and skips **both** vault questions (it is
not in a vault, so it cannot be in the wrong one) **and** the F1
market_reset gate. That last one is deliberate and stated in the code:
F1 exists because 20:00–21:00 ET is when the day's notes are being reset
and a Cobalt write races a human one. A generated file in git has nobody
editing it at 20:30, reaches no device, and is reviewed in a diff —
refusing it would take the 20:00 and 21:00 runs out every night, fail
them, and paint F18 red for a guard doing something it was never asked
to do.

It is a fixed tuple in code, not an argument, so no caller can widen it,
and everything else inside the repo is refused exactly as before.

### Tunables (F16, with consumers)

| key | value | unit | consumers |
|---|---|---|---|
| `seat_usage.window` | `06:00-23:00` | `window` (new) | `Schedule.due_now/window_opened_at/calendar_entries`, `watchdog.is_missed`, `probes.seat_usage`, the plist's mirrored array |
| `seat_usage.interval_min` | `60` | `min` | `Schedule.interval_minutes/calendar_entries`, `watchdog.is_missed`, the plist |
| `seat_usage.max_age_min` | `120` | `min` | `probes.seat_usage` (asked only inside the window) |

`TunableUnit.WINDOW` is new. A window is an ET wall-clock **span**; it is
neither a `time` (one instant) nor a `label` (free text nothing parses),
and `jobs.config.parse_window` is its only reader — fail-loud on anything
that is not `HH:MM-HH:MM`, and on a window that wraps midnight.

`seat_usage.max_age_min` is two intervals, deliberately the same slack
the watchdog gives an interval job: one missed run is a hiccup nobody
needs to be told about; two in a row means the number he reads at the
close is wrong.

### The freshness probe

Green inside the window with a recent run; **red** when the last run is
older than `max_age_min` or exited non-zero; **green and silent outside
the window**, because at 03:00 the last run is four hours old and
everything is exactly as it should be. That is the same mistake the
archiver probe made against weekends and fixed on 2026-09-06 by asking
the schedule instead of guessing a number.

Unpriced models are **reported on the probe line but are not red** —
they are already loud in the report, hourly, next to the number they
distort, and a red beat for a condition fixed by a deliberate version
bump would be a permanent alert.

```
OK   seat usage   last run 2026-09-08 18:35 ET (0 min ago), exit 0;
                  UNPRICED in the report: claude-fable-5-1, gpt-6-astra
```

---

## Proofs

```
$ uv run pytest tests/cobalt tests/taxonomy -q
987 passed, 15 warnings in 20.52s          # 931 on main + 56 new

$ uv run cobalt validate ; echo $?
… registry <-> ops/: 13 label(s), exact match.
… registry <-> plists: schedules and COBALT_ENV agree on every job.
0

$ plutil -lint ops/com.cobalt.herdr.plist ops/com.cobalt.seat-usage.plist
OK / OK

$ uv run cobalt seat-usage run          # dev, cobalt_dev, three times
unit: [WRITE] updated  … unit=seat-usage:2026-09-08 · write_id=10940
human cells: already present — not touched (clause 2a)
```

126 plist calendar entries compared entry-for-entry against
`Schedule.calendar_entries()` — equal, by test and by `cobalt validate`.

**Old-tree suite is unchanged.** `pytest tests/ --ignore=tests/
test_finviz_extractor.py` gives **12 failed / 16 errors on this branch
and 12 failed / 16 errors on `main`** — identical, all pre-existing
old-tree breakage (`test_cortex.py`, `test_daemon.py` and friends).
`tests/test_finviz_extractor.py` fails to import on `main` too
(`FinvizStockData` no longer exists). Nothing here touched the old tree.

---

## Not done, and why

* **`com.cobalt.herdr` is not installed or loaded.** By instruction and
  by mechanism — see Part A. Its plist is not in
  `~/Library/LaunchAgents/`.
* **DevDocs for the *modified* files** (`jobs/config.md`,
  `jobs/watchdog.md`, `heartbeat/probes.md`, `vault.md`,
  `vaultwrite/writer.md`, `cli.md`) are not rewritten — that is sprint
  close, per CLAUDE.md. The five **new** `seatusage/*.py` files each got
  their page now, since they would otherwise have none, and `INDEX.md`
  carries the section.
* **The report file will make `git status` dirty in production**, once
  an hour inside the window. That is the existing pattern:
  `docs/30 - Design/archiver-runs.md` is tracked and rewritten nightly
  by the archiver, and its rows are committed with ordinary commits.
* **The two unpriced models are not fixed.** Fixing them means bumping
  the ccusage pin, which is a decision with a diff and a re-read of what
  the columns mean — not something this branch does on its own.

---

## ESCALATE

1. **Two seats are priced at nothing until the pin moves.**
   `claude-fable-5-1` and `gpt-6-astra` will read **unpriced** in the
   report every hour, and the day total will carry a `≥`. The report is
   correct and loud about it; it is also, today, about 11% short of the
   real API-equivalent figure. Bumping ccusage past 20.0.20 is the fix
   and it is Dejan's call — the alternative, letting the job fetch live
   pricing, breaks the four-gate law's no-network condition and is not
   on the table.

2. **The `herdr` probe reads the same list the hook guard protects.**
   `herdr agent list` is what the probe asserts on, and a herdr bump that
   reverts the `SessionStart` hook pointer makes every Grok session
   report itself as `claude` in that list. The checklist line is in, but
   the coupling is new and worth knowing before the handover.

3. **`ops/README.md`'s Inventory table still says "All six installed and
   loaded as of 2026-09-03".** It is now eight plists and that sentence
   is stale. I added the two new rows and a pointer to `cobalt validate`
   as the machine-readable answer, but did not rewrite the paragraph —
   out of scope for this branch, and worth a pass at sprint close.

---

## `git status --porcelain`

```
(clean)
```

## `git log --oneline main..HEAD`

```
4024939 ops: herdr as a launchd job (built, not loaded) + the seat-usage report
```

---

# READY FOR MERGE

`git merge --ff-only ops/herdr-usage` from `~/cobalt`.

**LIVE, after the merge, from `~/cobalt`** — the seat-usage job only.
Nothing else is loaded or restarted.

```sh
cp ops/com.cobalt.seat-usage.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.seat-usage.plist
launchctl list | grep com.cobalt.seat-usage

uv run cobalt jobs register
uv run cobalt seat-usage run                  # one run by hand
sed -n '20,40p' "docs/40 - DevDocs/reports/seat-usage.md"

# heartbeat green at the next beat (or force one):
launchctl kickstart -k gui/$(id -u)/com.cobalt.heartbeat
tail -40 logs/heartbeat.log | grep "seat usage"
```

The `herdr` handover is **not** part of this. It is
`ops/README.md` → "herdr handover", at the keyboard, whenever he is ready.
