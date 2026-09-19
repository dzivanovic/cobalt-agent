# `src/cobalt/archiver/cli.py`

New 2026-09-19 with the append-only redesign (chunk Q). Spec:
`docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §3 (V3-7),
§6, §8, §11, and spec O-4.

## What it does
`cobalt archiver …` — the operator's window onto the append-only
archiver. Registered by `src/cobalt/cli.py` as ONE new block at the end
of its subparser group (it reflows none of its neighbours; the
`archiver` script entry point in `pyproject.toml` is untouched and
still runs the nightly job).

| command | writes? | gated? |
|---|---|---|
| `progress` | no | no |
| `incidents` [`--ticker`] | no | no |
| `incidents resolve <id> --by --note` | the incident row only | no |
| `audit` [`--from YYYY-MM-DD`] | no | no |
| `shadow-report` [`--nights N`] | no (reads files) | no |
| `restate <ticker> [interval]` | **preview** | no |
| `restate … --apply --reason …` | **rewrites bars** | **quiet window + lock** |
| `backfill-missing <ticker> [interval]` | **preview** | no |
| `backfill-missing … --apply` | inserts only | **quiet window + lock** |

`READ_ONLY_COMMANDS` and `MUTATING_COMMANDS` are module constants, so a
test asserts the split rather than inferring it from the parser's
shape.

## Key functions/classes
- `add_parser(sub)` — the `archiver` group, added to `cobalt`'s CLI.
- `build_parser()` — the group alone, for tests and `--help`. Returns a
  `_Parser` whose `parse_args` runs `_validate_args`, because argparse
  cannot say "required WITH another flag" and a check that only ran in
  `main()` would let a caller build the namespace without it.
- `main(argv)` — catches `QuietRefused` and returns its exit code, 2.
- `_observer(settings)` — a zero-argument observation the quiet guard
  can RE-RUN, which is what makes the pre-commit re-check possible.
- `_pool_reader()` — the ONE read of `system.radar_pool` behind Q3.
  Read-only; the archiver writes nothing to the radar's tables (R8).

## Gotchas
- **`backfill-missing` can only DO NOTHING.** Its single write path is
  `BarStore.insert_new_bars` (`ON CONFLICT … DO NOTHING`), and a test
  asserts the name `upsert_bars` does not appear in its handler at all.
  A differing key is LEFT ALONE and stays a `restate` decision for a
  person; the preview says so in those words.
- **`restate --apply` is the only command in this build that may rewrite
  a stored bar** — and the reason `upsert_bars` still exists outside the
  poller and the `upsert` night. It needs `--reason`, and its audit
  trail lands on an incident row (spec O-4: where a repair's trail lives
  when no incident exists — this design opens and carries one).
- **There is no `--force`** (§8, L1, L37). The parser rejects it and a
  test asserts the string is absent from this module's CODE.
- **The pre-commit re-check is inside the caller's transaction.** Both
  `--apply` paths call `guard.check_before_commit()` as the LAST
  statement inside `store.target_transaction()`; raising there rolls the
  repair back. Putting it anywhere earlier would reintroduce exactly the
  window Astra's sequence exploits.
- **`audit` states its actual bounds** and says plainly that older
  vendor additions or corrections need a wider audit (§3 V3-7). The
  horizon IS the candidate range, and a report implying otherwise would
  claim coverage nobody measured.
- `shadow-report` reads the retained artifacts, not the database —
  which is the whole point: after tonight's overlay, last night's
  difference is gone from storage.
