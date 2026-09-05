# `src/cobalt/daymode/config.py`

## What it does
Loads `configs/cobalt/daymode.yaml` (Pydantic, fail-loud) and resolves
the mode ladder against `configs/cobalt/aset.yaml`'s sheet order.

## The ladder is derived, never listed
```
modes (low -> high) = ["reduced"] + aset.yaml's sheet_modes.order
```
Today: `reduced < half < full`. Add a quarter sheet to `aset.yaml` and
it becomes `reduced < quarter < half < full` with no edit here and none
in `src/`.

## Key API
| Member | Answers |
|---|---|
| `modes` | the ladder, low to high |
| `lowest_enabled` / `highest_enabled` | stage 1's floor; the proposal's ceiling |
| `sheet_for(mode)` | which **key table** sizes this mode — `reduced` resolves through the pointer, every other mode *is* a sheet |
| `enabled_grades_for(mode)` | the keys permitted on this rung (reduced narrows to `[B]`) |
| `mode_for_hotkey_file(f)` | `full.htk`→full, `half.htk`→half, `reduced_day.htk`→reduced |

## What it refuses at load (config-as-code)
- a **dangling `reduced_sheet`** — refused, never defaulted to the
  lowest sheet: the premarket floor and the live rung both resolve
  through it, and guessing either is a risk decision no config error
  should be allowed to make;
- an `enabled_modes` entry not on the ladder;
- `reduced_enabled_grades` that would **widen** the account ladder — the
  rung narrows what the account permits, it can never permit a key the
  account does not;
- a hotkey file mapped to an unknown mode, or a duplicate filename.

`cobalt validate` builds this object, so a config that passes the gate
is one the runtime can boot on.
