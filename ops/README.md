# ops/ — LaunchAgents & wrapper scripts

Everything here is captured in git as the SOURCE for what's installed
to `~/Library/LaunchAgents/` — that install directory itself is outside
the repo and not tracked. When you add or change a plist, re-copy it
(see "Install / reload" below); the copy in `~/Library/LaunchAgents/`
does not auto-update from git.

## Inventory

**Nine plists below, all of them loaded, as of 2026-09-09**
(`launchctl list | grep com.cobalt`). `com.cobalt.herdr` was the one
exception until the handover on 2026-09-08 at 19:21 ET; it is live now —
see "herdr under launchd (0.9.0)" further down. `com.cobalt.generated`
is new on 2026-09-09.

This table is not the whole of `ops/`, and never was: `com.cobalt.backup`,
`cards-expire`, `daymode-propose`, `heartbeat` and `obsidian` have
plists and rows without a row here. **`configs/cobalt/jobs.yaml` is the
authoritative list** — fourteen labels, cross-checked against `ops/`
by `uv run cobalt validate` on every run of the gate. Read this table as
prose about the ones with a story attached, not as an inventory.

| Plist | Runs | Schedule | Wrapper | Installed |
|---|---|---|---|---|
| `com.cobalt.agent.plist` | `cobalt.sh start` (the Mattermost chief-of-staff agent) | RunAtLoad only, no KeepAlive | — | yes |
| `com.cobalt.mainframe.plist` | `ops/start_mainframe.sh` (local LLM — the L23 local lane) | RunAtLoad only | `ops/start_mainframe.sh` | yes |
| `com.cobalt.archiver.plist` | `/Users/cobalt/.local/bin/uv run archiver` (nightly bar archiver) | Mon-Fri 20:30 ET | — | yes (2026-09-03 — was not loaded before this) |
| `com.cobalt.prefill-daily.plist` | `/Users/cobalt/.local/bin/uv run prefill daily` | Mon-Fri 05:15 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
| `com.cobalt.prefill-drc.plist` | `/Users/cobalt/.local/bin/uv run prefill drc` | Mon-Fri 15:40 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
| `com.cobalt.aset.plist` | `ops/start_aset.sh` → `uv run python -m cobalt.aset` (ASET sizing widget, :5010) | RunAtLoad + KeepAlive (persistent) | `ops/start_aset.sh` | yes |
| `com.cobalt.herdr.plist` | `/opt/homebrew/bin/herdr server` (the terminal workspace every agent seat lives in) | RunAtLoad + KeepAlive on crash only | — | **yes (2026-09-08 19:21 — the handover)** |
| `com.cobalt.generated.plist` | `/Users/cobalt/.local/bin/uv run cobalt generated commit` (commits the files a job rewrote today) | daily 23:37 ET | F17 wrapper | new 2026-09-09 |
| `com.cobalt.seat-usage.plist` | `/Users/cobalt/.local/bin/uv run cobalt seat-usage run` (the hourly seat-usage report) | hourly 06:00-23:00 ET, every day | F17 wrapper (`cobalt seat-usage run`) | yes (2026-09-08) |

The table above says which plists are *supposed* to be loaded.
`configs/cobalt/jobs.yaml` is the machine-readable version of the same
claim, and `uv run cobalt validate` compares the two: it fails on a job
in one and not the other, and prints a `NOT LOADED BY DESIGN` line for
every row carrying `enabled: false`.

## com.cobalt.aset — persistence fix (2026-08-31)

**Incident:** the ASET widget had no LaunchAgent at all — it was only
ever started by hand (`uv run python -m cobalt.aset`, bare `nohup`, no
supervision) and died silently at the Aug 29 10:35 reboot. Nobody
noticed until the trading PC got connection-refused on `:5010`. It was
restarted by hand at least twice since (2026-08-31 sessions) with no
persistence fix until now.

**Fix:** `com.cobalt.aset.plist` + `ops/start_aset.sh`.
- `RunAtLoad: true` — starts on login/boot.
- `KeepAlive: true` — unconditional restart on any exit (crash, kill,
  even a clean 0 exit) — this is meant to be a persistent widget, not a
  scheduled batch job like the archiver/prefill jobs above.
- **Secret-free plist:** `COBALT_MASTER_KEY` is sourced inside
  `ops/start_aset.sh` from `~/.cobalt_key` (the same key file
  `cobalt.sh start` uses) — never written into the plist's
  `EnvironmentVariables`. Without it, the sheet's pages still serve,
  but `/api/prefill` (Finviz last-price fetch) fails every call because
  VaultManager can't unlock.
- **Logs with rotation:** `logs/aset.log` / `logs/aset.err`
  (gitignored). Rotation is **best-effort, on-restart only**: launchd
  binds stdout/stderr to those paths once at process spawn with no
  SIGHUP/reopen support, and per this session's scope `ops/start_aset.sh`
  does not touch `src/cobalt/aset`'s own Python — so true live rotation
  would need either app-level logging changes (out of scope here) or a
  root-owned `newsyslog.d` entry (not installed — avoided sudo). The
  wrapper instead rotates each log to a timestamped `.YYYYMMDDHHMMSS`
  suffix on every (re)start if it's grown past 5MB, keeping the 5 most
  recent rotated files. For a KeepAlive service that's expected to stay
  up for days/weeks at a stretch, this bounds worst-case growth but
  does not guarantee any particular rotation cadence — if `aset.log`
  grows unbounded between restarts, check it by hand.

## NN#16 dev/prod vault split (2026-08-31)

`configs/dev/vault.yaml`'s committed default no longer points at the
real vault — it now points at `~/dev-vault-cobalt` (a skeleton copy:
templates + Rules.md, no personal notes — see `docs/40 - DevDocs/cobalt/
vault.md`). Every PRODUCTION consumer of `cobalt.vault.resolve_vault_path()`
must therefore set `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`
explicitly in its own environment, or it silently starts writing into
the dev vault instead. All three plists that touch the vault do this:
`com.cobalt.aset.plist` (via `ops/start_aset.sh`, so the plist itself
stays free of it too) and both `com.cobalt.prefill-*.plist` (directly
in `EnvironmentVariables`, since they have no wrapper script).

**Action required (not done by this change):** `com.cobalt.aset` is
already installed and running — its CURRENT process started before
this fix and does not have `COBALT_VAULT_PATH` set. It needs
`launchctl kickstart -k gui/$(id -u)/com.cobalt.aset` to pick it up;
until then any card it saves would resolve the vault via the new dev
default and land in `~/dev-vault-cobalt`, not the real vault. Not run
automatically here — restarting a live production process during
market hours needs a human go-ahead, not an agent's own judgment call.
The two prefill plists are still not installed at all, so they carry
no such risk yet.

## uv path in ProgramArguments — FIXED 2026-09-03 (was the 09-03 prefill-silence root cause)

**Rule: every `ops/*.plist` that invokes a binary directly in
`ProgramArguments` (not through a wrapper script's own shebang) must use
an ABSOLUTE path to that binary.** `uv` on this machine is a standalone
install at `~/.local/bin/uv` (confirmed: `which uv` →
`/Users/cobalt/.local/bin/uv`; `/opt/homebrew/bin/uv` → no such file;
`brew list uv` → no such keg).

Two different-looking bugs, same rule, found/fixed together:
- `com.cobalt.archiver.plist` hardcoded the WRONG absolute path
  (`/opt/homebrew/bin/uv`, doesn't exist here) — and was also simply not
  loaded at all (`launchctl print` found no service). Its job had
  therefore never run since 08-27 (`docs/30 - Design/archiver-runs.md`
  has no nightly rows 08-28 onward) despite the Ledger's 08-29/31 claim
  it was "verified running unattended" — that check evidently only
  confirmed the plist file existed/looked right, not that launchd had
  it loaded.
- `com.cobalt.prefill-daily.plist` / `com.cobalt.prefill-drc.plist` used
  a BARE `uv` (the 08-31 fix for the above bug, modeled on
  `ops/start_aset.sh`'s pattern — see BACKLOG.md's 08-31 slice-2 entry).
  This looked right but is itself wrong for a plist with no wrapper
  script: `start_aset.sh`'s bare `uv` works because bash's own shebang
  does a real PATH search before `exec`ing it; a bare name directly in
  `ProgramArguments[0]` has no shell in front of it, and launchd's
  posix_spawn does not reliably search the job's own
  `EnvironmentVariables.PATH` the way a shell does. Confirmed by an
  isolated diagnostic LaunchAgent: bare `uv` → `last exit code = 78:
  EX_CONFIG`, empty stdout+stderr; absolute path → exit 0. This is
  exactly what happened when `com.cobalt.prefill-daily` fired for real
  at 05:15 on 09-03 (and `com.cobalt.prefill-drc` the evening before) —
  loaded, fired, failed instantly, zero output, no alert. Full
  root-cause writeup: `docs/00 - Project/BACKLOG.md`'s INCIDENT LOG,
  2026-09-03 entry.

**Fix (this session):** all three now use the absolute
`/Users/cobalt/.local/bin/uv` in `ProgramArguments`; all three
installed/reloaded and confirmed exit 0 on a manual `kickstart`.
`com.cobalt.mainframe.plist` does not actually invoke `uv` at all (its
`ProgramArguments` is `/Users/cobalt/cobalt/ops/start_mainframe.sh`,
which uses `lms` — the earlier note above conflated it with the archiver
bug; left uninvestigated further since it isn't broken).

*(Path corrected 2026-09-09: this paragraph and the Inventory row both
said `~/.lmstudio/start_mainframe.sh`. The wrapper is in the repo, where
it is reviewed in a diff; `~/.lmstudio/` is where the 09-04 note put it
and the plist never agreed.)*

## Install / reload

```sh
# first install
cp ops/com.cobalt.<name>.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.<name>.plist

# after editing the plist or its wrapper script
cp ops/com.cobalt.<name>.plist ~/Library/LaunchAgents/   # only if the plist itself changed
launchctl kickstart -k gui/$(id -u)/com.cobalt.<name>

# status / logs
launchctl list | grep com.cobalt.<name>
tail -f logs/<name>.log logs/<name>.err

# stop + unload
launchctl bootout gui/$(id -u)/com.cobalt.<name>
```

## Deploy checklist

**THE LAW, ruled three times — 2026-09-04, 2026-09-08 (`aset.yaml`) and
2026-09-09 (`tunables.yaml`): a config-shape change and the restart of
EVERY resident that reads that file are ONE ACTION.** Not two steps, not
a follow-up. A deploy plan that changes a config and does not name the
processes it restarts is an incomplete plan.

**Every deploy plan carries a `RESTARTS:` line, and it is produced by a
command, not by memory:**

```sh
# for every config file the merge touches
uv run cobalt jobs readers configs/cobalt/taxonomy/tunables.yaml
#   -> RESTARTS: com.cobalt.aset

launchctl kickstart -k gui/$(id -u)/com.cobalt.aset
```

`cobalt jobs readers` reads `reads:` in `configs/cobalt/jobs.yaml` —
per-resident, derived from the code, one row per config file the process
re-reads at runtime. **An unknown path exits 1**, deliberately: "no
resident re-reads this" and "nobody has worked out who reads this" are
different answers, and only one of them makes it safe to deploy without
a restart. `uv run cobalt validate` prints the whole map and fails if a
listed path has gone missing.

### Why this is a law and not a habit

On 2026-09-08 at ~19:00 the seat-usage deploy added a
`TunableUnit.WINDOW` row to `configs/cobalt/taxonomy/tunables.yaml`. Its
plan said *"nothing else is loaded or restarted"* — true of its own job,
and wrong about the sheet. `com.cobalt.aset` had been running since
17:50 and **re-reads `tunables.yaml` on every request**, so it read the
new row through code that predated the enum value and raised
`TaxonomyConfigError` on every render. From then until the kickstart at
**07:06 on 09-09** — about thirteen hours, including the premarket — the
page he trades beside served HTTP 200 with

> ⚠ DAY MODE UNRESOLVED — cards are refused until this is fixed

and every card write was refused. `sheet_http` was green throughout and
was telling the truth: the server was up.

Two things came out of it, and both are in place now: this checklist,
and the `sheet daymode` probe (F18) that reads the banner instead of the
status line, so the same failure is red within one heartbeat interval
rather than at whatever hour somebody happens to look.

### The order

1. `uv run cobalt validate` — the config gate, on the branch, before merging.
2. `git merge --ff-only <branch>` from `~/cobalt`. **Merge is deploy** (R4).
3. **Migrations**, if any, as their own step with their own rollback.
4. **`RESTARTS:`** — kickstart every resident named by `cobalt jobs
   readers` for every config file the merge touched.
5. **Registry** — `uv run cobalt jobs register` if `jobs.yaml` changed;
   `cp` + `launchctl bootstrap` for a new plist.
6. **Force a beat** and read it:
   `launchctl kickstart -k gui/$(id -u)/com.cobalt.heartbeat`.
7. Deploys go **outside market hours** (NN#16) and outside 20:00-21:30 ET
   (F1's market-reset window).

## herdr under launchd (0.9.0)

**STATUS: LIVE since 2026-09-08 19:21 ET.** `com.cobalt.herdr` is
bootstrapped, `configs/cobalt/jobs.yaml` carries `enabled: true`, and the
F18 `herdr` probe is a real probe. On 2026-09-09 the server is **pid
72998, run 3, herdr 0.9.0**, on the Mac and on Fedora.

**launchd owns the server.** That is the whole change, and everything
below follows from it.

```sh
launchctl list | grep com.cobalt.herdr            # the truth about who is running
launchctl kickstart -k gui/$(id -u)/com.cobalt.herdr   # restart
herdr server stop                                  # a DELIBERATE stop; nothing fights you
```

`KeepAlive` is `SuccessfulExit: false`, not `true`, and that is why
`herdr server stop` works: a clean exit is a human decision and launchd
leaves it alone. **A crash is the only case it restarts**, which is the
only case worth restarting.

### Attaching — the rules, not just the commands

| From | Command | The rule |
|---|---|---|
| The Mac | `herdr` | Attaches to the persistent session. `herdr session attach default` names it explicitly. |
| Fedora | `herdr --remote cobalt@cobalt` | **Only from a 0.9.0 client**, and **answer No to any replace prompt.** |
| The phone | `ssh cobalt@cobalt` then `herdr` | **NEVER `--remote`.** There is no phone client; the phone is a terminal onto the Mac. |

**WHY `--remote` HAS A RULE ATTACHED.** On the morning of 2026-09-09 the
server was replaced twice — 06:03 and 07:26, both from Fedora, the second
27 seconds after launchd had started it. A `herdr --remote` from a
**0.8.2** client replaces the running server. 0.8.2 does prompt, and
Dejan answered Yes without reading it, so this was partly procedure and
not only version — which is why the rule is written as a rule and not as
"upgrade and forget".

**The fix was forward, not back.** Mac and Fedora went 0.8.2 → 0.9.0
("client updates leave compatible servers untouched … replacing a remote
server asks, default **No**"), and the server was restarted under launchd
**from the Mac keyboard in Terminal.app — not from a herdr pane** — at
08:17. Result: pid 72998, `endpoint_compatible yes`, heartbeat GREEN at
08:19:57 (13 jobs / 11 probes).

**The phone is still 0.8.2 and must not `--remote`.** `ssh` then `herdr`
costs nothing and cannot replace anything.

### Acceptance, 2026-09-09

Dejan attached from Fedora over `--remote` on 0.9.0. **The client
prompted before replacing; he answered No; `launchctl list | grep
com.cobalt.herdr` still showed pid 72998 after four attaches.** The
version fix and the procedure both hold. Recorded as PASSED.

### What a restart brings back, and what it does not

0.9.0's native agent restore is better than 0.8.2's, measured on the
08:17 restart:

* **Restored** — the session, workspace, tabs, panes and working
  directories, **and** `claude`, `grok` and `qwen` were relaunched in
  their panes with their sessions. The Claude1 conversation continued
  without `claude --resume`.
* **Not restored** — panes that were **empty shells**. Codex1 and
  Gemini1 held no agent before the restart, so there was nothing for
  restore to name; they were relaunched by hand.
* **The standing rule is unchanged, and 0.9.0 does not soften it: never
  rely on restore.** State goes to the vault or to Postgres **before** a
  `/clear`, a restart or an update. An agent that reports a session
  reference can be brought back; a conversation nobody wrote down cannot.

### Integration updates append hooks — the probe watches for it

`herdr integration install claude` rewrites Claude Code's hook config,
and on **2026-09-09 at 08:33** the v8 → v9 update did **not** replace the
guard pointer — it **APPENDED A SECOND `SessionStart` ENTRY** aimed at
herdr's own script, so both would have fired. The duplicate was removed
by hand and `~/.claude/settings.json` restored byte-identical to the
pre-install backup (`~/.claude/settings.json.pre-herdr-v9`).

This matters to this job, not just to the seats: v9 still hardcodes the
agent name `herdr:claude` with **no harness detection**, so without
`~/.claude/hooks/herdr-harness-guard.sh` every Grok session reports
itself as `claude` in `herdr agent list` — **and that is the list the F18
`herdr` probe asserts on**.

Since 2026-09-09 **the probe checks the pointer as its third question**:
`hooks.SessionStart` must be **exactly one entry with exactly one command
hook** running the guard, and the guard must exist and be executable.
Anything else is red, naming the drift. Counting is the check because a
presence check would have called the 08:33 state fine.

After any `brew upgrade herdr` or `herdr integration install`, force a
beat rather than eyeballing the file:

```sh
launchctl kickstart -k gui/$(id -u)/com.cobalt.heartbeat
tail -40 logs/heartbeat.log | grep herdr
```

### Where things live

The socket is `/Users/cobalt/.config/herdr/herdr.sock` and the config
`/Users/cobalt/.config/herdr/config.toml` — `herdr server reload-config`
re-reads it without a restart, which is preferable to a restart for a
config change. Server logs sit in the same directory
(`herdr-server.log`); the launchd job's own stdout/stderr go to
`ops/logs/herdr.log` and `ops/logs/herdr.err`.

Nothing in `configs/` reaches this process, which is why its registry row
carries `reads: []` — no deploy of ours can require restarting it.

### Rolling it back

Rolling back means **handing the server back to a manual start**, which
is a downgrade from where it is now — do it only if launchd supervision
is itself the problem.

```sh
launchctl bootout gui/$(id -u)/com.cobalt.herdr    # this STOPS the server; every pane goes
# set `enabled: false` on com.cobalt.herdr in configs/cobalt/jobs.yaml, then:
uv run cobalt jobs register                        # the probe goes quiet and says why
/opt/homebrew/bin/herdr server &                   # back to the manual start
```

The order matters: `bootout` takes the terminal workspace down with it,
so **run it from Terminal.app, not from a herdr pane** — the same reason
the original handover had to happen at the keyboard. Land everything
first; assume every conversation is lost.
