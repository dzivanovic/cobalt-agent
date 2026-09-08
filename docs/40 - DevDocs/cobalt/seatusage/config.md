# `src/cobalt/seatusage/config.py`

## What it does
Loads `configs/cobalt/seat_usage.yaml` into `SeatUsageConfig`. Pydantic,
`extra="forbid"`, crashes on a bad file. No defaults for anything a
number depends on — a report that priced a day from a fallback would be
a report nobody could audit.

## What lives here, and what deliberately does not
Here: the tool pin, the report path, the role-hint map, the free-model
list, the silent-zero switch.

**Not here: the cadence and the window.** Those are thresholds and F16
puts thresholds in `tunables.yaml` — `seat_usage.interval_min`,
`seat_usage.window`, `seat_usage.max_age_min`, each with its consumers
listed on the row.

## `ToolSpec` — the four-gate law (L15) written down
`name`, `version`, `binary`, `license`, `offline`. `version` is an exact
pin, never `latest`, and `ccusage.assert_pinned()` compares it against
what the installed binary reports on **every run**. A silent bump is the
failure the pin exists for: the numbers keep coming and the shape of
them changes.

`offline: true` is the "no network at run time" gate. It has a
consequence — see `ccusage.md`'s silent-zero section — which is handled
rather than hidden.

## `roles` is a hint map, and the column says so
ccusage can see which **seat** ran a model. It cannot see which **role**
that seat was holding. `role_hint()` returns `None` for an unmapped
model and the renderer prints an em dash: a wrong role beside a real
dollar figure is worse than no role at all.

## `zero_cost_models`
Model → why its `$0` is the true number. Today: `mainframe`, the local
lane. Membership is what separates "free" from "unpriced", and it is
declared by hand because that distinction cannot be inferred.
