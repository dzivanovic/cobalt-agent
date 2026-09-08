# agy/herdr detection-manifest mismatch — 2026-09-08

**Status:** reproduced, ready for Dejan to file upstream (with herdr and/or agy — herdr owns the
manifest, agy owns the actual UI text). Nothing opened on GitHub by this session.

## Versions

- agy (Antigravity CLI): `1.1.27`
- herdr: manifest `remote:~/.local/state/herdr/agent-detection/remote/agy.toml`, version
  `2026.06.24.1`

## The mismatch

herdr's `agy.toml` detection manifest has exactly one rule for a blocked/approval state:

```toml
[[rules]]
id = "permission_prompt"
state = "blocked"
priority = 300
region = "whole_recent"
visible_blocker = true
contains = ["requesting permission for:"]
any = [
  { contains = ["do you want to proceed?"] },
  { contains = ["tab amend", "edit command"] },
]
```

Real agy 1.1.27 never emits `"requesting permission for:"` anywhere in its UI. Its file-write
approval card reads:

```
Create file
────────────────────────────────────────────────────────────────────────────────────

/Users/cobalt/agy-test-p4/world.txt  +1
   1 +  world

Allow creation of this file?
> 1. Yes, allow creation
  2. No, deny creation

  ↑/↓ Navigate · tab Amend · f full diff
esc to cancel
```

`"Allow creation of this file?"` never matches `contains = ["requesting permission for:"]`
(nor either of the `any` alternatives), so the `permission_prompt` rule never fires. herdr falls
through to its idle fallback.

## Reproduction (live, this session)

1. Created a fresh herdr tab/pane (`w1:pF`) in a scratch directory (`~/agy-test-p4`, deleted at
   close — no repo/vault paths touched).
2. `herdr agent start agyp4b --kind agy --pane w1:pF` (interactive, no flags).
3. `herdr agent prompt agyp4b "create a file named world.txt in the current directory containing
   the word world"`.
4. agy rendered the "Allow creation of this file?" card above and sat there, genuinely waiting on
   human input.
5. At that exact moment: `herdr agent explain agyp4b` returned:
   ```
   agent: agy
   state: idle
   manifest: remote:/Users/cobalt/.local/state/herdr/agent-detection/remote/agy.toml 2026.06.24.1
   rule: none
   fallback_reason: default_known_agent_idle_fallback
   ```
   **herdr reports `idle` while agy is actually blocked on an approval it cannot proceed past
   without a human.** Any automation, script, or `herdr agent wait --until blocked` built on this
   state will never see the block.
6. Denied via the TUI (`Down`, `Enter` → "2. No, deny creation"). `world.txt` was not created.
   Cleaned up (`herdr tab close w1:tF`, `rm -rf ~/agy-test-p4`).

## Proposed manifest change

Add (or replace) a rule matching agy's actual card text, e.g.:

```toml
[[rules]]
id = "file_write_permission_prompt"
state = "blocked"
priority = 300
region = "whole_recent"
visible_blocker = true
any = [
  { contains = ["Allow creation of this file?"] },
  { contains = ["Allow overwriting this file?"] },
  { contains = ["Allow editing this file?"] },
]
```

The exact set of card variants (creation vs. overwrite vs. edit, and any command-execution
equivalent, e.g. `"Allow running this command?"`) was not exhaustively enumerated in this session
— only the file-creation card was reproduced. Whoever files this upstream should probe the other
approval types (command execution, multi-file patches) the same way before submitting, since the
same `"requesting permission for:"` assumption likely misses those too.

## Notes for whoever files this

- This is a **detection-manifest** bug in herdr's `agy.toml`, not a code bug in agy itself — agy's
  card text is presumably intentional UI copy, not something to "fix" on that side, unless the
  card text itself is expected to converge with other harnesses' wording.
- Not investigated in this session: where agy's own herdr integration hook is installed (it does
  fire — a scratch agy session reported `source: "herdr:antigravity_cli"` with a real session id —
  but its home-directory/config location was not located; `~/.agy` does not exist on this
  machine). That's a separate, smaller loose end, unrelated to this manifest mismatch.
