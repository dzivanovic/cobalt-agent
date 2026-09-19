# `src/cobalt/archiver/__init__.py`

## What it does
Package marker for the Bar Archiver. States the one hard rule: this
package never archives daily/weekly/monthly (Finviz serves 10y+ of
those on demand) and never touches the old tree's scheduler.

## Key functions/classes
None.

## Data flow in/out
None.

## Config it reads
None directly — see `config.py` for the package's actual config schema.

---

# The operator's page — the append-only archiver (2026-09-19)

Design: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md`.
Ruling behind the repair gate: `reports/cto-2026-09-19.md` §4 **R8**.

## The two modes

`archiver.write_mode` in `configs/cobalt/taxonomy/tunables.yaml`. **The
repo ships `upsert`.**

**`upsert` — what runs tonight.** The whole export through
`INSERT … ON CONFLICT DO UPDATE`: every in-window bar is refreshed,
about 3.34 M rows sent for about 390 k genuinely new ones. Exactly the
behaviour that has always run, byte for byte, plus three things and
nothing else:

1. a run-level advisory lock (so a manual `--backfill` DURING the
   nightly run now REFUSES instead of interleaving — the only
   operator-visible change before the switch);
2. the pre-write SHADOW COMPARE (reads only);
3. one `shadow` key on the job row and one artifact file per night.

**`append` — what the owner ruled for.** Per `(ticker, interval)` the
archiver knows its own watermark and inserts only bars that do not
exist. No stored row is ever rewritten by the nightly run. Switching is
**his ruling on the shadow numbers**, taken as a reviewed commit to that
config row — never a default that drifted (L7).

## What a shadow night writes

One JSON-lines file per night at `data/archiver-shadow/<YYYY-MM-DD>.jsonl`
(gitignored; retention `archiver.shadow_retention_nights`, default 30).
One line per target, every line labelled `pre-write`, each carrying the
four-way comparison over TWO scopes — the whole export (bootstrap) and
the last two sessions plus today (steady state) — with:

- `candidates`, `already_stored_equal`, `incoming_only` split into
  `new` / `late`, `stored_only`;
- `differing`: every key that differs, WHICH of O/H/L/C/V, and both
  values after normalisation to `NUMERIC(14,4)` / integer volume;
- `would_withhold`: whether `append` would have halted this target;
- the export's bounds, the fetch instant, and whether the radar poller
  could write this target at all (`poller_writable`: i1 only).

The aggregate lands on the job row under `shadow`.

## How to read `shadow-report`

```
cobalt archiver shadow-report --nights 5
```

A row per night (targets compared, how many WOULD have been withheld,
late and new counts), then the three lists that actually answer the
switch question:

- **PERSISTED** — a key that differed on an earlier night and still
  differs. A real, standing disagreement with the vendor.
- **VANISHED** — a key that differed and no longer does. It was healed
  by the very nightly overlay `append` would stop doing. These are the
  targets `append` would have withheld for nothing, and they are the
  cost of the switch.
- **APPEARED** — new disagreements.

A post-write audit cannot produce any of this: after the 20:30 overlay,
last night's difference is gone. That is why the artifact is retained
and why the comparison is pre-write.

## The quiet window, in plain words

Repairs that change stored bars — `restate --apply` and
`backfill-missing --apply` — run only when the radar is genuinely idle:
overnight, at least 35 minutes after the last poll cycle STARTED (30
minutes assumed for the cycle plus 5 minutes quiet), and at least 10
minutes before the next scanning session opens. All three are checked
again immediately before the commit, so a repair that runs into the
opening is rolled back rather than landing.

If any rule fails the command prints one line per failed rule and a
summary naming what it observed and the earliest time it would be
allowed, then exits 2 having written nothing. **Previews always run.**

There is no `--force`. Overriding the window is the owner's word,
recorded by the desk, and is a code or config change.

## The five known limits (spec §12, verbatim)

1. **Mixed prices after a vendor restatement (Astra, all three rounds).**
   After a split-like restatement the archiver withholds the target and
   the heartbeat goes non-green — but the unchanged poller keeps writing
   new-basis i1 bars beside old-basis history, and the formation replay
   (`radar/replay.py`, i1, last 14 days) reads them, until an operator
   runs `restate`. True of today's system too (inside the vendor window
   the nightly DO UPDATE heals it; under `append` nothing heals it
   without a person). Astra wants enforcement before activation; the
   design gives disclosure + incident + non-green heartbeat.
2. **Option A's closing-side protection is a bound, not an exclusion**
   (§8). B is Sunday's.
3. A full bootstrap comparison can withhold a target for an OLD
   difference outside the normal overlap; a withheld target's new bars
   age out of the vendor window (i5 ≈ 21 days) if nobody repairs it —
   the incident list and the heartbeat are the alarm.
4. Interior holes older than range (b) are found only by `audit --from`
   / `backfill-missing`.
5. The newest-timestamp check cannot detect interior or prefix
   truncation of an export.

Limits 1 and 2 are RECORDED DISSENTS (Gemini, Astra — spec §13) and go
to the owner WITH the switch ruling.

## The commands

| command | what it does |
|---|---|
| `cobalt archiver progress` | every target's watermark, oldest first |
| `cobalt archiver incidents [--ticker T]` | what a night refused to do, and why |
| `cobalt archiver incidents resolve <id> --by <who> --note <why>` | close one, on the record |
| `cobalt archiver audit [--from YYYY-MM-DD]` | coverage over the stored range |
| `cobalt archiver shadow-report [--nights N]` | the switch evidence |
| `cobalt archiver restate <ticker> [interval]` | preview the differences |
| `cobalt archiver restate … --apply --reason "…"` | rewrite them (quiet window) |
| `cobalt archiver backfill-missing <ticker> [interval]` | preview what is missing |
| `cobalt archiver backfill-missing … --apply` | insert it (quiet window; never overwrites) |

The heartbeat's archiver probe is **not green while any incident is
unresolved**. That is the alarm behind limit 3 — a dashboard that stayed
green through a fortnight of withholding would make `append` worse than
the overlay it replaces.
