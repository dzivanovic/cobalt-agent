# ops/ — LaunchAgents & wrapper scripts

Everything here is captured in git as the SOURCE for what's installed
to `~/Library/LaunchAgents/` — that install directory itself is outside
the repo and not tracked. When you add or change a plist, re-copy it
(see "Install / reload" below); the copy in `~/Library/LaunchAgents/`
does not auto-update from git.

## Inventory

**Eight plists below, seven of them loaded, as of 2026-09-08**
(`launchctl list | grep com.cobalt`). The exception is
`com.cobalt.herdr`, which is built and deliberately not bootstrapped —
see "herdr handover" further down.

This table is not the whole of `ops/`, and never was: `com.cobalt.backup`,
`cards-expire`, `daymode-propose`, `heartbeat` and `obsidian` have
plists and rows without a row here. **`configs/cobalt/jobs.yaml` is the
authoritative list** — thirteen labels, cross-checked against `ops/`
by `uv run cobalt validate` on every run of the gate. Read this table as
prose about the ones with a story attached, not as an inventory.

| Plist | Runs | Schedule | Wrapper | Installed |
|---|---|---|---|---|
| `com.cobalt.agent.plist` | `cobalt.sh start` (the Mattermost chief-of-staff agent) | RunAtLoad only, no KeepAlive | — | yes |
| `com.cobalt.mainframe.plist` | `~/.lmstudio/start_mainframe.sh` (local LLM) | RunAtLoad only | `~/.lmstudio/start_mainframe.sh` | yes |
| `com.cobalt.archiver.plist` | `/Users/cobalt/.local/bin/uv run archiver` (nightly bar archiver) | Mon-Fri 20:30 ET | — | yes (2026-09-03 — was not loaded before this) |
| `com.cobalt.prefill-daily.plist` | `/Users/cobalt/.local/bin/uv run prefill daily` | Mon-Fri 05:15 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
| `com.cobalt.prefill-drc.plist` | `/Users/cobalt/.local/bin/uv run prefill drc` | Mon-Fri 15:40 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
| `com.cobalt.aset.plist` | `ops/start_aset.sh` → `uv run python -m cobalt.aset` (ASET sizing widget, :5010) | RunAtLoad + KeepAlive (persistent) | `ops/start_aset.sh` | yes |
| `com.cobalt.herdr.plist` | `/opt/homebrew/bin/herdr server` (the terminal workspace every agent seat lives in) | RunAtLoad + KeepAlive on crash only | — | **no — built, not loaded** (see "herdr handover" below) |
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
`ProgramArguments` is `~/.lmstudio/start_mainframe.sh`, which uses `lms`
— the earlier note above conflated it with the archiver bug; left
uninvestigated further since it isn't broken).

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

## herdr handover — a keyboard procedure, not a job

**Status on 2026-09-08: BUILT, NOT LOADED** — unchanged by that
evening's `com.cobalt.seat-usage` deploy, which touched nothing here.
Before flipping the flag in step 8, settle the open ESCALATE in
`docs/00 - Project/BACKLOG.md` § Standing follow-ups: the probe this
turns on reads `herdr agent list`, which is the same list a reverted
SessionStart hook pointer silently corrupts.

**BUILT, NOT LOADED.** `ops/com.cobalt.herdr.plist`
exists, `configs/cobalt/jobs.yaml` has its row with `enabled: false`, and
the F18 `herdr` probe is green and silent because of that flag. The
server is running from a manual start (`/opt/homebrew/bin/herdr server`,
up since Sunday 11:00, herdr 0.8.2). Nothing below has been done.

### Why a session cannot do this for you

The server this job supervises is the one hosting the terminal that
would run the bootstrap. `launchctl bootstrap` on this label, with the
manual server already up, produces either a second server or a killed
first one — and either way the pane issuing the command dies mid-command
and cannot come back to check its own work. The procedure ends with a
human re-attaching, which is not a thing a job can do for itself. Run it
**at the Mac keyboard**, not over SSH and not from inside a herdr pane.

### What survives a restart, and what does not

Measured on 2026-09-06 (recorded in `PROJECT-LEDGER.md`): a server
restart **restored 1 of 2 panes**.

* **Survives** — the session (`default`), its workspace, tab and pane
  layout, and each pane's working directory. herdr re-creates the panes
  and re-runs their shells.
* **Does not survive** — the *conversation* inside an agent. The pane
  that did not come back was one running `claude --resume`: herdr
  restored the pane and the shell, but the agent process inside it was a
  resumed session, and nothing in herdr owns or replays that. The same
  is true of any harness with its own session state.
* **The standing rule, unchanged:** never rely on restore. State goes to
  the vault or to Postgres **before** a `/clear`, a restart or an update.

### The procedure

Do this outside market hours, with nothing mid-flight in any pane.

```sh
# 1. RECORD what is open, so restore has something to be checked against.
herdr session list
herdr workspace list
herdr tab list
herdr agent list          # this is the list the F18 probe will assert on
# Write the pane -> directory -> agent mapping down. It is the only copy.

# 2. LAND EVERYTHING. In every agent pane: finish or abandon the turn,
#    commit or stash, and put anything worth keeping into the vault or a
#    report file. Assume every conversation is lost.

# 3. STOP the manual server (exit 0 — KeepAlive is SuccessfulExit:false,
#    so nothing will fight you).
herdr server stop
pgrep -fl "herdr server" || echo "no server running"

# 4. INSTALL and bootstrap the job.
cp ops/com.cobalt.herdr.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.herdr.plist

# 5. VERIFY, before trusting anything to it.
launchctl list | grep com.cobalt.herdr        # expect a live PID, status 0
herdr status server                            # expect: running, protocol OK
herdr agent list                               # expect: JSON, result.agents
tail -20 ops/logs/herdr.err

# 6. RE-ATTACH (see the three ways below) and re-open the panes from
#    step 1's notes. Compare against what you wrote down.

# 7. RE-EXPOSE /remote-control on Claude1 — the herdr tab in ~/cobalt
#    that is the /rc seat. Start Claude Code there; recent versions
#    auto-start remote control, so confirm it rather than assume it, and
#    type /rc in that pane if it did not.

# 8. FLIP THE FLAG — the last step, and only once 1-7 are green.
#    configs/cobalt/jobs.yaml: com.cobalt.herdr -> enabled: true
uv run cobalt validate                         # the row leaves "NOT LOADED BY DESIGN"
uv run cobalt jobs register
uv run cobalt heartbeat show                   # the `herdr` line is now a real probe

# 9. GREEN BEAT. Wait one heartbeat interval (15 min) or force one:
launchctl kickstart -k gui/$(id -u)/com.cobalt.heartbeat
tail -40 logs/heartbeat.log
```

Step 8 is what turns the probe on. Before it, `herdr` on the beat reads
`enabled: false — NOT PROBED`; after it, a dead socket or a server that
will not answer `agent list` is red within one interval and names
`com.cobalt.herdr`.

### Re-attaching — the three ways

| From | Command | Notes |
|---|---|---|
| The Mac itself | `herdr` | Launches or attaches to the persistent session. `herdr session attach default` names it explicitly. |
| Fedora, over SSH | `herdr --remote cobalt@<mac-tailscale-name>` | The thin client. Text **and** image paste work, which is why it replaced VNC for Code work. `--remote-keybindings server` if the local map fights you. |
| The phone | `ssh cobalt@<mac-tailscale-name>` then `herdr` | Over Tailscale, same as any shell. There is no phone client; the phone is a terminal onto the Mac. |

The session's socket is `/Users/cobalt/.config/herdr/herdr.sock` and its
config is `/Users/cobalt/.config/herdr/config.toml` (`herdr server
reload-config` re-reads it without a restart — prefer that to a restart
for a config change). Server logs are in the same directory
(`herdr-server.log`); the launchd job's own stdout/stderr go to
`ops/logs/herdr.log` and `ops/logs/herdr.err`.

### Rolling it back

```sh
launchctl bootout gui/$(id -u)/com.cobalt.herdr
# set enabled: false in configs/cobalt/jobs.yaml, then:
uv run cobalt jobs register
/opt/homebrew/bin/herdr server &     # back to the manual start
```
