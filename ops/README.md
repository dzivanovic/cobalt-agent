# ops/ — LaunchAgents & wrapper scripts

Everything here is captured in git as the SOURCE for what's installed
to `~/Library/LaunchAgents/` — that install directory itself is outside
the repo and not tracked. When you add or change a plist, re-copy it
(see "Install / reload" below); the copy in `~/Library/LaunchAgents/`
does not auto-update from git.

## Inventory

| Plist | Runs | Schedule | Wrapper |
|---|---|---|---|
| `com.cobalt.agent.plist` | `cobalt.sh start` (the Mattermost chief-of-staff agent) | RunAtLoad only, no KeepAlive | — |
| `com.cobalt.mainframe.plist` | `~/.lmstudio/start_mainframe.sh` (local LLM) | RunAtLoad only | `~/.lmstudio/start_mainframe.sh` |
| `com.cobalt.archiver.plist` | `uv run archiver` (nightly bar archiver) | Mon-Fri 20:30 ET | — |
| `com.cobalt.prefill-daily.plist` | `uv run prefill daily` | Mon-Fri 05:15 ET | — |
| `com.cobalt.prefill-drc.plist` | `uv run prefill drc` | Mon-Fri 15:40 ET | — |
| `com.cobalt.aset.plist` | `ops/start_aset.sh` → `uv run python -m cobalt.aset` (ASET sizing widget, :5010) | RunAtLoad + KeepAlive (persistent) | `ops/start_aset.sh` |

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

## uv path discrepancy (found while installing this plist — not fixed here)

`com.cobalt.archiver.plist` and `com.cobalt.mainframe.plist` hardcode
`/opt/homebrew/bin/uv` in `ProgramArguments`. **That path does not exist
on this machine** — `uv` is a standalone install at `~/.local/bin/uv`
(confirmed: `which uv` → `/Users/cobalt/.local/bin/uv`; `/opt/homebrew/bin/uv`
→ no such file; `brew list uv` → no such keg). `ops/com.cobalt.aset.plist`
avoids this by resolving `uv` via `PATH` inside `ops/start_aset.sh`
(the `EnvironmentVariables.PATH` in every plist here already includes
`~/.local/bin`) instead of hardcoding a binary path.

**This means `com.cobalt.archiver.plist`'s launchd job has likely been
failing silently since whenever `/opt/homebrew/bin/uv` stopped
existing** — `docs/30 - Design/archiver-runs.md` has exactly two rows,
both dated 2026-08-27, with no nightly rows for 08-28 through 08-31
despite the Mon-Fri 20:30 schedule and the Ledger's 08-29/31 claim that
the archiver was "verified running unattended." That verification was
evidently done by a different check (e.g. `launchctl list` showing a
label/PID) that doesn't catch an immediate exec failure. **Not fixed
here** — out of scope for the ASET persistence task; flagged in the
session recap for a real fix (same one-line `ProgramArguments` path
swap, or route through a wrapper the way `aset`/`mainframe` do).

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
