# ops/ — LaunchAgents & wrapper scripts

Everything here is captured in git as the SOURCE for what's installed
to `~/Library/LaunchAgents/` — that install directory itself is outside
the repo and not tracked. When you add or change a plist, re-copy it
(see "Install / reload" below); the copy in `~/Library/LaunchAgents/`
does not auto-update from git.

## Inventory

All six installed and loaded as of 2026-09-03 (confirmed via
`launchctl print gui/$UID/<label>`).

| Plist | Runs | Schedule | Wrapper | Installed |
|---|---|---|---|---|
| `com.cobalt.agent.plist` | `cobalt.sh start` (the Mattermost chief-of-staff agent) | RunAtLoad only, no KeepAlive | — | yes |
| `com.cobalt.mainframe.plist` | `~/.lmstudio/start_mainframe.sh` (local LLM) | RunAtLoad only | `~/.lmstudio/start_mainframe.sh` | yes |
| `com.cobalt.archiver.plist` | `/Users/cobalt/.local/bin/uv run archiver` (nightly bar archiver) | Mon-Fri 20:30 ET | — | yes (2026-09-03 — was not loaded before this) |
| `com.cobalt.prefill-daily.plist` | `/Users/cobalt/.local/bin/uv run prefill daily` | Mon-Fri 05:15 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
| `com.cobalt.prefill-drc.plist` | `/Users/cobalt/.local/bin/uv run prefill drc` | Mon-Fri 15:40 ET | — | yes (reloaded 2026-09-03 with the absolute-path fix) |
| `com.cobalt.aset.plist` | `ops/start_aset.sh` → `uv run python -m cobalt.aset` (ASET sizing widget, :5010) | RunAtLoad + KeepAlive (persistent) | `ops/start_aset.sh` | yes |

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
